from app.database.models import db, Conversion
from app.api.utils import get_exchange_rate

def convert_currency(amount, currency_from, currency_to):
    rate = get_exchange_rate(currency_from, currency_to)
    converted_amount = amount * rate
    new_conversion = Conversion(amount=amount, currency_from=currency_from, currency_to=currency_to, rate=rate)
    db.session.add(new_conversion)
    db.session.commit()
    return {'converted_amount': converted_amount}
