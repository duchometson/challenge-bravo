from server.server import *
from models.currencymodel import currency

class CurrencySchema(server.database.ma.Schema)
    class Meta:
        fields = ("name","value","last_update","access_count")
        model = Currency

currency_schema = CurrencySchema()