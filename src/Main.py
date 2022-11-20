from lib.ShopLib import ShopLib
from lib.Invest import Invest


shopLib = ShopLib()
invest = Invest(shopLib)

models = {"shop": {"attribute": ["name", "online"], "add": shopLib.add_shop, "delete": shopLib.delete_shop, "invest": "", "update": {"aatribute": ["name"], "update": shopLib.update_shop}, "print": shopLib.get_shop}, "budget": {"attribute": ["shop_id", "month", "month_budget", "amount_spent"], "add": shopLib.add_shop_budget, "print": shopLib.get_shop_budget} } 

def insert():
    # models = {"shop": shopLib.add_shop, "budget": shopLib.add_shop_budget}
    while(True):
        print("Please choose below entity and Q for quite")
        print(*list(models.keys()), sep=" ")
        _input = input()
        if _input == "Q":
            break
        elif _input in models.keys():
            model = models[_input]
            param = {}
            for attr in model["attribute"]:
                val = input("Please enter {} for {}:".format(attr, _input))
                param[attr] = val
            model["add"](**param)
        else:
            print("unknown input")

def _print():
    while(True):
        print("Please choose below entity and Q for quite")
        print(*list(models.keys()), sep=" ")
        _input = input()
        if _input == "Q":
            break
        elif _input in models.keys():
            model = models[_input]
            _id = input("Enter id of {}".format(_input))
            model["print"](_id)
        else:
            print("unknown input")

def _print_bulk():
    pass

def update():
    pass

def delete():
    pass

def _invest():
    shop_id = input("Please enter your shop id: ")
    cost = input("please enter advertisement cost: ")
    year = "2020"
    month = "06"
    invest.advertise(shop_id, float(cost), month, year)




if __name__ == "__main__":
    print("Please select the mode and Q for quite mode")
    while(True):
        print("I for invest, D for Delete, P for print, A for add, U for Update, Q for quite")
        _input = input()
        if _input == "I":
            _invest()
        elif _input == "D":
            pass
        elif _input == "P":
            pass
        elif _input == "A":
            insert()
        elif _input == "U":
            insert()
        elif _input == "Q":
            break
        else:
            print("unknown input: " + _input)
