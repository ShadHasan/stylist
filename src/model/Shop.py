from lib.utils.MysqlClient import *

class Shop(db.Entity):

    _id = PrimaryKey(int, auto=True)
    name = Required(str)
    online = Required(bool)
    budgets = Set("Budget")
