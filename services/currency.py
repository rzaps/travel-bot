import aiohttp


# код для получения курса валют
async def get_currency():
    url = "https://v6.exchangerate-api.com/v6/09edf8b2bb246e1f801cbfba/latest/USD"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return "Произошла ошибка при получении курса валют"
                data = await response.json()
                usd_to_rub = data["conversion_rates"]["RUB"]
                eur_to_usd = data["conversion_rates"]["EUR"]
                eur_to_rub = eur_to_usd * usd_to_rub
                return f"💵 1 USD = {usd_to_rub:.2f} RUB\n💶 1 EUR = {eur_to_rub:.2f} RUB"
    except Exception:
        return "Произошла ошибка при получении курса валют"