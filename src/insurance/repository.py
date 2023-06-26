from src.insurance.model import Rate

class InseureRepository():

    async def load_prices(data: dict):
        # insert data to db
        for key, value in data.items():
            data = key
            print("====================================")
            print(key, value)
            print("||||||||||||||||||||||||||||||||||||")
            for i in value:
                cargo_type = i['cargo_type']
                rate = float(i['rate'].replace(',', '.'))
                print(data, cargo_type, rate)
                # insert data to db
                await Rate.create(date=data, cargo_type=cargo_type, rate=rate)

    async def get_price(date_i: str, cargo_type_i: str, price: float):
        # get price from db where date <= date_i and cargo_type = cargo_type_i
        rate = await Rate.filter(date__lte=date_i, cargo_type=cargo_type_i).order_by('-date').first()
        if rate is None:
            raise ValueError("No data found")
        price = price * rate.rate
        return price

