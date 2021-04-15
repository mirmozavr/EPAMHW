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
import json
import re
from typing import Iterator

import aiohttp
from bs4 import BeautifulSoup

INF = float("INF")
NEG_INF = -float("INF")
company_dummy = {
    "name": "Dummy",
    "code": "DUMMY",
    "price": NEG_INF,
    "P/E": INF,
    "growth": NEG_INF,
    "potential profit": NEG_INF,
}
highest_price = [company_dummy] * 10
lowest_pe = [company_dummy] * 10
highest_growth = [company_dummy] * 10
highest_potential_profit = [company_dummy] * 10


async def get_sp_500_info() -> None:
    base_url = "https://markets.businessinsider.com/index/components/s&p_500"
    base_company_url = "https://markets.businessinsider.com"
    async with aiohttp.ClientSession() as session:

        usd = await get_usd_currency_from_cbr(session)

        for page in range(1, 12):
            async with session.get(base_url, params=[("p", page)]) as resp:

                html = await resp.text()
                soup = BeautifulSoup(html, features="html.parser")

                for company in get_all_stocks_from_page(soup):
                    growth = float(
                        list(list(company.parent.next_siblings)[-4].children)[
                            -2
                        ].string.rstrip("%")
                    )
                    company_info = {
                        "name": company["title"],
                        "code": None,
                        "price": None,
                        "P/E": None,
                        "growth": growth,
                        "potential profit": None,
                    }

                    url = base_company_url + company["href"]

                    (
                        company_info["code"],
                        company_info["price"],
                        company_info["P/E"],
                        company_info["potential profit"],
                    ) = await get_company_info(url, session, usd)

                    evaluate_top10(company_info)
    write_into_files()


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


async def get_company_info(
    url: str, session: aiohttp.ClientSession, usd: float
) -> tuple:
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

        return code, current_value, p_e, potential_profit


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
    evaluate_top10_price(company)
    evaluate_top10_pe(company)
    evaluate_top10_growth(company)
    evaluate_top10_potential_profit(company)


def evaluate_top10_price(company: dict) -> None:
    for i in range(10):
        if company["price"] and company["price"] > highest_price[i]["price"]:
            highest_price.insert(i, company)
            highest_price.pop()
            break


def evaluate_top10_pe(company: dict) -> None:
    for i in range(10):
        if company["P/E"] and company["P/E"] < lowest_pe[i]["P/E"]:
            lowest_pe.insert(i, company)
            lowest_pe.pop()
            break


def evaluate_top10_growth(company: dict) -> None:
    for i in range(10):
        if company["growth"] and company["growth"] > highest_growth[i]["growth"]:
            highest_growth.insert(i, company)
            highest_growth.pop()
            break


def evaluate_top10_potential_profit(company: dict) -> None:
    for i in range(10):
        if (
            company["potential profit"]
            and company["potential profit"]
            > highest_potential_profit[i]["potential profit"]
        ):
            highest_potential_profit.insert(i, company)
            highest_potential_profit.pop()
            break


def write_into_files() -> None:
    with open("highest_price.json", "w") as file:
        file.write(json.dumps(highest_price))
    with open("lowest_pe.json", "w") as file:
        file.write(json.dumps(lowest_pe))
    with open("highest_growth.json", "w") as file:
        file.write(json.dumps(highest_growth))
    with open("highest_potential_profit.json", "w") as file:
        file.write(json.dumps(highest_potential_profit))


loop = asyncio.get_event_loop()
loop.run_until_complete(get_sp_500_info())
