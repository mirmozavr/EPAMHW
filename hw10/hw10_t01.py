"""
Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта.

https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

    Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта центробанка РФ)
    Код компании (справа от названия компании на странице компании)
    P/E компании (информация находится справа от графика на странице компании)
    Годовой рост/падение компании в процентах (основная таблица)
    Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High (справа от графика на странице компании)

Сохранить итоговую информацию в 4 JSON файла:

    Топ 10 компаний с самими дорогими акциями в рублях.
    Топ 10 компаний с самым низким показателем P/E.
    Топ 10 компаний, которые показали самый высокий рост за последний год
    Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.
    Пример формата:

[
{
    "code": "MMM",
    "name": "3M CO.",
    "price" | "P/E" | "growth" | "potential profit" : value,
},
...
]
"""
import asyncio
import datetime as dt
import heapq
import json
import re
from typing import Iterator

import aiohttp
from bs4 import BeautifulSoup

NEG_INF = -float("INF")

highest_price = [(NEG_INF, "", {})] * 10
lowest_pe = [(NEG_INF, "", {})] * 10
highest_growth = [(NEG_INF, "", {})] * 10
highest_potential_profit = [(NEG_INF, "", {})] * 10


async def get_sp_500_info() -> None:
    base_url = "https://markets.businessinsider.com/index/components/s&p_500"
    base_company_url = "https://markets.businessinsider.com"
    async with aiohttp.ClientSession() as session:

        usd = await get_usd_currency_from_cbr(session)

        for page in range(1, 2):
            async with session.get(base_url, params=[("p", page)]) as resp:

                html = await resp.text()
                soup = BeautifulSoup(html, features="html.parser")

                for company in get_all_stocks_from_page(soup):
                    name = company["title"]
                    growth = float(
                        list(list(company.parent.next_siblings)[-4].children)[
                            -2
                        ].string.rstrip("%")
                    )

                    company_url = base_company_url + company["href"]
                    asyncio.create_task(
                        get_company_info(company_url, usd, name, growth)
                    )
                    await asyncio.sleep(0.1)  #
    write_into_json_files()


async def get_usd_currency_from_cbr(session: aiohttp.ClientSession) -> float:
    today_date = dt.datetime.strftime(dt.datetime.today(), "%d/%m/%Y")
    yesterday_date = dt.datetime.strftime(
        dt.datetime.today() - dt.timedelta(days=1), "%d/%m/%Y"
    )
    usd_params = {
        "date_req1": yesterday_date,
        "date_req2": today_date,
        "VAL_NM_RQ": "R01235",
    }
    async with session.get(
        "http://www.cbr.ru/scripts/XML_dynamic.asp", params=usd_params
    ) as resp:
        html = await resp.text()
        soup = BeautifulSoup(html, features="html.parser")
        return float(soup.find_all("value")[-1].string.replace(",", "."))


def get_all_stocks_from_page(soup: BeautifulSoup) -> Iterator:
    return soup.find_all("a", span="", href=re.compile("stock$"), attrs={"title": True})


async def get_company_info(url: str, usd: float, name: str, growth: float) -> tuple:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            html = await resp.text()
            soup = BeautifulSoup(html, features="html.parser")

            current_value = float(
                soup.find(
                    "span", attrs={"class": "price-section__current-value"}
                ).string.replace(",", "")
            )

            code = list(
                soup.find("span", attrs={"class": "price-section__category"}).strings
            )[-2].strip(", ")

            p_e = get_parameter_from_company_page(soup, "P/E Ratio")

            year_low = get_parameter_from_company_page(soup, "52 Week Low")
            year_high = get_parameter_from_company_page(soup, "52 Week High")
            if all((year_low, year_high)):
                potential_profit = round((year_high - year_low) * usd, 2)
            else:
                potential_profit = None
            company_info = {
                "name": name,
                "code": code,
                "price": current_value,
                "P/E": p_e,
                "growth": growth,
                "potential_profit": potential_profit,
            }
            evaluate_top10(company_info)


def get_parameter_from_company_page(soup: BeautifulSoup, string: str) -> float:
    try:
        return float(
            list(
                soup.find(
                    "div",
                    attrs={"class": "snapshot__header"},
                    string=string,
                ).parent.stripped_strings
            )[0].replace(",", "")
        )
    except AttributeError:
        pass


def evaluate_top10(company: dict) -> None:
    if company["price"]:
        heapq.heappushpop(highest_price, (company["price"], company["code"], company))
    if company["P/E"]:
        heapq.heappushpop(lowest_pe, (-company["P/E"], company["code"], company))
    if company["growth"]:
        heapq.heappushpop(highest_growth, (company["growth"], company["code"], company))
    if company["potential_profit"]:
        heapq.heappushpop(
            highest_potential_profit,
            (company["potential_profit"], company["code"], company),
        )


def write_into_json_files() -> None:
    write_into_json("highest_price.json", highest_price, "price")
    write_into_json("lowest_pe.json", lowest_pe, "P/E", reverse=False)
    write_into_json("highest_growth.json", highest_growth, "growth")
    write_into_json(
        "highest_potential_profit.json", highest_potential_profit, "potential_profit"
    )


def write_into_json(
    file_name: str, data: list, sort_by: str, reverse: bool = True
) -> None:
    with open(file_name, "w") as file:
        json.dump(
            sorted(
                (item[2] for item in data),
                key=lambda info: info[sort_by],
                reverse=reverse,
            ),
            file,
            indent=0,
        )


loop = asyncio.get_event_loop()
loop.run_until_complete(get_sp_500_info())
