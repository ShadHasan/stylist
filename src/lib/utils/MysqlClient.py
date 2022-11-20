# from pymysql import mysql_module
from pony.orm import *

db = Database()
db.bind(provider="mysql", host="localhost", user="shad", passwd="pajisingh", db="sampledb")
# db.drop_all_tables()
# db.generate_mapping(create_tables=True)

'''
class TestTable(db.Entity):
    name = Required(str)
    x2 = Required(str)

if __name__ == "__main__":
    # db.bind(provider="mysql", host="localhost", user="shad", passwd="pajisingh", db="sampledb")
    # db.generate_mapping(create_tables=True)
    # p1 = TestTable(name="first", x2="something") ## won't work without db_session wrapper
    with db_session:  ## Non interactive application db_session wrap the code around
        p1 = TestTable(name="first", x2="something")

    #  commit()  ## This applicable for python interactive session, not applicable for non interactive session
'''
