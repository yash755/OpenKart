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



                sql = "SELECT * FROM oc21_product WHERE date_modified < %s"

                # sql = "SELECT * FROM oc21_product WHERE product_id = %s LIMIT 1"

                adr = date.today() - timedelta(days = 1)
                print (adr)

                # adr = 375

                cursor.execute(sql,adr)
                connection1.commit()


                for row in cursor:
                    try:
                        data = row
                        print (data)
                        prod_id = data['product_id']

                        price = float(data['price'])


                        print (price)




                        price  = price + 0.15*price

                        price = float("{:.2f}".format(price))

                        print (price)

                        today = date.today()

                        with connection1.cursor() as cursor2:


                            sql = "UPDATE oc21_product SET price = %s, date_modified = %s WHERE product_id = %s"
                            val = (price,today, prod_id)

                            cursor2.execute(sql, val)

                            print(cursor2.rowcount)


                    except Exception as e:
                        print ("Error")

                connection1.commit()

        except Exception as e:
            print ("Error")

    except pymysql.Error as e:
        print ("ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1]))
        print ("Loop1")
        time.sleep(2)
        print("Was a nice sleep, now let me continue...")



if __name__ == '__main__':
    get_list()