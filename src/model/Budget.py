from lib.utils.MysqlClient import *
from model.Shop import Shop


class Budget(db.Entity):

    _id = Required(Shop)
    month = Required(str)
    month_budget = Required(float)
    amount_spent = Required(float)
