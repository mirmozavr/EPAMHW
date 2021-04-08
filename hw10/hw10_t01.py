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

from bs4 import BeautifulSoup as BS
from bs4 import SoupStrainer
from urllib import request
import aiohttp
import re
import aiohttp
import asyncio
import datetime as dt


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
        soup = BS(html)
        USD = float(soup.find("value").string.replace(",", "."))
        print("Dollar", USD)
        return USD


async def get_company_info(url, session, USD):
    async with session.get(
        url
    ) as resp:
        print("Status:", resp.status)
        print("Content-type:", resp.headers["content-type"])
        print(resp.url)
        html = await resp.text()
        soup = BS(html)
        label = str(soup.find("span", attrs={"class": "price-section__label"}).string)
        current_value = float(
            soup.find("span", attrs={"class": "price-section__current-value"}).string
        )
        code = list(
            soup.find("span", attrs={"class": "price-section__category"}).strings
        )[-2].strip(", ")
        p_e = float(
            list(
                soup.find(
                    "div", attrs={"class": "snapshot__header"}, string="P/E Ratio"
                ).parent.stripped_strings
            )[0]
        )
        year_low = float(
            list(
                soup.find(
                    "div", attrs={"class": "snapshot__header"}, string="52 Week Low"
                ).parent.stripped_strings
            )[0]
        )
        year_high = float(
            list(
                soup.find(
                    "div", attrs={"class": "snapshot__header"}, string="52 Week High"
                ).parent.stripped_strings
            )[0]
        )
        potential_profit = round((year_high - year_low) * USD,2)
        print(potential_profit)

        return code, current_value, p_e, potential_profit


async def get_top_500_info():
    base_url = "https://markets.businessinsider.com/index/components/s&p_500"
    base_company_url = "https://markets.businessinsider.com"
    top_500_info = []
    async with aiohttp.ClientSession() as session:

        USD = await get_usd_currency_from_cbr(session)

        for page in range(1, 2):  # extend to 12!!!
            async with session.get(base_url, params=[("p", page)]) as resp:
                only_a_tags = SoupStrainer("a")

                print("Status:", resp.status)
                print(resp.url)
                html = await resp.text()

                soup = BS(html, parse_only=only_a_tags)

                stocks = soup.find_all(
                    "a", span="", href=re.compile("stock$"), attrs={"title": True}
                )
                print(len(stocks), "len stocks")

                company_info = {
                    "name": None,
                    "code": None,
                    "price": None,
                    "P/E": None,
                    "growth": None,
                    "potential profit": None,
                }
                for item in stocks:
                    print(item["href"], item["title"])

                    company_info["name"] = item["title"]

                    URL = base_company_url + item["href"]

                    (
                        company_info["code"],
                        company_info["price"],
                        company_info["P/E"],
                        company_info["potential profit"],
                    ) = (await get_company_info(URL, session, USD))

                    print(company_info)
                    top_500_info.append(company_info)


loop = asyncio.get_event_loop()
loop.run_until_complete(get_top_500_info())
