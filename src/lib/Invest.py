from datetime import datetime

def notify(message):
    print("Message: {}".format(message))


class Invest:

    def __init__(self, shopLib):
        self.shopLib = shopLib
    
    def advertise(self, shop_id, cost, month=None, year=None):
        # fetch shop if online True proceed else notify Budget reached
        # fetch budget
        # calculate advertisement cost if affordable
        # calculate budget crossed limit, raise notification if more than 50%
        # if budget crossed more than 100% set online status for shop and update
        # update budget table
        # update shop table
        shop = self.shopLib.get_shop(shop_id)
        if month is None:
            month = "{}-{}-01".format(datetime.now().year, datetime.now().month)
        else:
            month = "{}-{}-01".format(year, month)
        if shop.online:
            budget = self.shopLib.get_shop_budget(shop_id=shop_id, month=month)
            mb = budget.month_budget
            aspnt = budget.amount_spent
            plan_spent = aspnt + cost
            if aspnt >= (mb/2) and aspnt < mb:
                notify("Budget utilised 50%, amount apent {}".format(aspnt))
            elif aspnt >= mb:
                notify("Budget overreached, amount spent {}".format(aspnt))
                self.shopLib.update_shop(_id=shop_id, key="online", value="0")
            if plan_spent <= mb:
                notify("Spending advertisement cost: {}".format(cost))
                self.shopLib.update_shop_budget(shop_id=shop_id, month=month, key="amount_spent", value=plan_spent)
            else:
                notify("Cannot afford adventisement, out of budget {}, cost: {}, already spent: {}".format(mb, cost, aspnt))
        else:
            notify("Advertisement for shop: {} is offline contact admin".format(shop.name))
        

    def update_budget(self, shop_id, month, budget):
        # fetch buget by shop_id, month
        # if budget < amount_spent update budget, quite
        # if budget > amount_spent update budget and set shop online, quite
        pass
