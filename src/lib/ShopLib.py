from lib.utils.MysqlClient import *
from model.Shop import Shop
from model.Budget import Budget


db.generate_mapping(create_tables=True)
class ShopLib:

    def add_shop(self, name, online="0"):
        # db.generate_mapping(create_tables=True)
        with db_session:
            Shop(name=name, online=bool(online))

    def delete_shop(self, _id):
        try:
            with db_session:
                Shop[_id].delete()
        except Exception as e:
            print("Error occured: " + str(e))
    
    def get_shop(self, _id):
        shop = None
        with db_session:
            shop = Shop[_id]
        return shop

    def update_shop(self, _id, key, value):
        with db_session:
            shop = Shop[_id]
            setattr(shop, key, value)

    def add_shop_budget(self,shop_id, month, month_budget, amount_spent):
        # db.generate_mapping(create_tables=True)
        with db_session:
            shop = Shop[shop_id]
            Budget(_id=shop, month=month, month_budget=month_budget, amount_spent=amount_spent)
        
    def get_shop_budget(self, shop_id, month):
        budgets = None
        with db_session:
            if month is None:
                budgets = Budget.get(_id=shop_id)
            else:
                budgets = Budget.get(_id=shop_id, month=month)
        return budgets

    def update_shop_budget(self, shop_id, month, key, value):
        with db_session:
            budget = Budget.get(_id=shop_id, month=month)
            setattr(budget, key, value)

        
        
