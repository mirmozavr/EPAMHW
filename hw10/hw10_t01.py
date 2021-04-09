"""
Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта:
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
import re
import aiohttp
from bs4 import BeautifulSoup as BS

sp_500_info = []


async def get_usd_currency_from_cbr(session):
    today_date = dt.datetime.strftime(dt.datetime.today(), "%d/%m/%Y")
    usd_params = {
        "date_req1": today_date,
        "date_req2": today_date,
        "VAL_NM_RQ": "R01235",
    }
    async with session.get(
        "http://www.cbr.ru/scripts/XML_dynamic.asp", params=usd_params
    ) as resp:
        html = await resp.text()
        soup = BS(html, features="html.parser")
        USD = float(soup.find("value").string.replace(",", "."))
        print("Dollar", USD)
        return USD


async def get_company_info(url, session, USD):
    async with session.get(url) as resp:
        # print("Status:", resp.status)
        # print("Content-type:", resp.headers["content-type"])
        # print(resp.url)
        html = await resp.text()
        soup = BS(html, features="html.parser")
        label = str(soup.find("span", attrs={"class": "price-section__label"}).string)
        current_value = float(
            soup.find(
                "span", attrs={"class": "price-section__current-value"}
            ).string.replace(",", "")
        )
        code = list(
            soup.find("span", attrs={"class": "price-section__category"}).strings
        )[-2].strip(", ")
        try:
            p_e = float(
                list(
                    soup.find(
                        "div", attrs={"class": "snapshot__header"}, string="P/E Ratio"
                    ).parent.stripped_strings
                )[0].replace(",", "")
            )
        except AttributeError:
            p_e = None

        try:
            year_low = float(
                list(
                    soup.find(
                        "div", attrs={"class": "snapshot__header"}, string="52 Week Low"
                    ).parent.stripped_strings
                )[0].replace(",", "")
            )
            year_high = float(
                list(
                    soup.find(
                        "div",
                        attrs={"class": "snapshot__header"},
                        string="52 Week High",
                    ).parent.stripped_strings
                )[0].replace(",", "")
            )
            potential_profit = round((year_high - year_low) * USD, 2)
        except AttributeError:
            potential_profit = None

        return code, current_value, p_e, potential_profit


async def get_sp_500_info():
    global sp_500_info
    base_url = "https://markets.businessinsider.com/index/components/s&p_500"
    base_company_url = "https://markets.businessinsider.com"
    async with aiohttp.ClientSession() as session:

        usd = await get_usd_currency_from_cbr(session)

        for page in range(1, 2):  # extend to 12!!!
            async with session.get(base_url, params=[("p", page)]) as resp:

                # print("Status:", resp.status)
                # print(resp.url)
                html = await resp.text()

                soup = BS(html, features="html.parser")

                stocks = soup.find_all(
                    "a", span="", href=re.compile("stock$"), attrs={"title": True}
                )
                print(len(stocks), "len stocks")

                for company in stocks:
                    company_info = {
                        "name": None,
                        "code": None,
                        "price": None,
                        "P/E": None,
                        "growth": None,
                        "potential profit": None,
                    }
                    # print(item["href"], item["title"])
                    growth = float(
                        list(list(company.parent.next_siblings)[-4].children)[
                            -2
                        ].string.rstrip("%")
                    )

                    company_info["name"] = company["title"]
                    company_info["growth"] = growth

                    url = base_company_url + company["href"]

                    (
                        company_info["code"],
                        company_info["price"],
                        company_info["P/E"],
                        company_info["potential profit"],
                    ) = await get_company_info(url, session, usd)

                    print(company_info)
                    sp_500_info.append(company_info)


loop = asyncio.get_event_loop()
loop.run_until_complete(get_sp_500_info())
print("500 len", len(sp_500_info))
for info in sp_500_info:
    print(info)
