import pymysql.cursors
import time
from datetime import date
from datetime import timedelta


def get_list():
    try:
        connection1 = pymysql.connect(host="security-supply.com",
                                      user="security_ocar590",
                                      passwd="27c@44pS]k",
                                      db="security_ocar590",
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection1.cursor() as cursor:
                cursor.execute("SELECT * FROM oc21_product LIMIT 1")
                connection1.commit()


                for row in cursor:
                    try:
                        data = row
                        print (data)
                        prod_id = data['product_id']

                        price = float(data['price'])
                        print (price)


                        price  = price + 0.15*price
                        print (price)

                        with connection1.cursor() as cursor2:

                            sql = "UPDATE oc21_product SET price = %s WHERE product_id = %s"
                            val = (price, prod_id)

                            cursor2.execute(sql, val)

                            cursor2.commit()

                            print (cursor2.lastrowid)


                    except Exception as e:
                        print ("Error")

        except Exception as e:
            print ("Error")

    except pymysql.Error as e:
        print ("ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1]))
        print ("Loop1")
        time.sleep(2)
        print("Was a nice sleep, now let me continue...")



if __name__ == '__main__':
    get_list()