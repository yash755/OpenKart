import pymysql.cursors
import time
from datetime import date
from datetime import timedelta


def get_list():
    try:
        connection = pymysql.connect(host="dock14.com",
                                     user="dockonef_jashg",
                                     passwd="1uWSEW#pcZcJ",
                                     db="dockonef_scrape",
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM adi_category GROUP BY subcategory")
                # cursor.execute("SELECT * FROM adi WHERE subcategory IS NOT NULL LIMIT 10")
                connection.commit()


                for row in cursor:
                    try:
                        data = row

                        subcategory = data['subcategory']
                        category = data['category']

                        print (subcategory + '\n\n')

                        with connection.cursor() as cursor1:
                            sql = "SELECT * FROM adi WHERE subcategory  = %s  IS NOT NULL  AND  variant_price != 'Sign In forDealer Pricing' LIMIT 1000"
                            adr = subcategory

                            cursor1.execute(sql, adr)
                            connection.commit()

                            for row in cursor1:
                                try:
                                    data = row
                                    adi_id = data['id']
                                    handle = data['handle']
                                    title = data['title']
                                    html = data['html']
                                    vendor = data['vendor']

                                    variant_price = data['variant_price']
                                    variant_barcode = data['variant_barcode']

                                    type = data['type']

                                    vendor_id = ''

                                    print (title)

                                    try:
                                        connection1 = pymysql.connect(host="security-supply.com",
                                                                      user="security_ocar590",
                                                                      passwd="27c@44pS]k",
                                                                      db="security_ocar590",
                                                                      charset='utf8mb4',
                                                                      cursorclass=pymysql.cursors.DictCursor)

                                        try:

                                            with connection1.cursor() as cursor2:
                                                sql = "SELECT * FROM oc21_product_description WHERE name = %s"
                                                adr = title

                                                cursor2.execute(sql, adr)
                                                connection1.commit()


                                                if cursor2.rowcount == 0:
                                                    print (vendor)

                                                    with connection1.cursor() as cursor3:

                                                        sql = "SELECT * FROM oc21_manufacturer WHERE name = %s"
                                                        adr = vendor

                                                        cursor3.execute(sql, adr)
                                                        connection1.commit()


                                                    if cursor3.rowcount == 0:

                                                        with connection1.cursor() as cursor4:
                                                            cursor4.execute("INSERT INTO  oc21_manufacturer (name) VALUES (%s)",
                                                                        (vendor))
                                                            connection1.commit()

                                                            manu_id = cursor4.lastrowid

                                                            vendor_id = manu_id

                                                            with connection1.cursor() as cursor5:
                                                                cursor5.execute("INSERT INTO  oc21_manufacturer_to_store (manufacturer_id) VALUES (%s)",
                                                                        (manu_id))
                                                                connection1.commit()

                                                    else:
                                                        man_result = cursor3.fetchone()

                                                        vendor_id = man_result['manufacturer_id']


                                                    print ("Vendor ID :" + str(vendor_id))

                                                    today = date.today()
                                                    yesterday = today - timedelta(days = 1)

                                                    prod_id = -1

                                                    price = variant_price
                                                    print (price)
                                                    price = price.replace(",","")
                                                    price = price.replace("Your Low Price          ",'')
                                                    price = float(price)
                                                    price = price + 0.15 * price
                                                    price = float("{:.2f}".format(price))
                                                    print (price)

                                                    with connection1.cursor() as cursor7:
                                                        cursor7.execute(
                                                            "INSERT INTO  oc21_product (quantity,date_available,manufacturer_id,shipping,price,status,sort_order,date_added,date_modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                            (1,yesterday, int(vendor_id), 1,price, 1,1,yesterday,today))
                                                        connection1.commit()

                                                        prod_id = cursor7.lastrowid

                                                        print (prod_id)

                                                        with connection1.cursor() as cursor8:
                                                            cursor8.execute(
                                                                "INSERT INTO  oc21_product_description (product_id,name,description,tag,language_id) VALUES (%s,%s,%s,%s,%s)",
                                                                (int(prod_id), title, str(html), str(type),1))
                                                            connection1.commit()

                                                            main_id = cursor8.lastrowid


                                                        with connection1.cursor() as cursor9:
                                                            cursor9.execute(
                                                                "INSERT INTO  oc21_product_to_store (product_id,store_id) VALUES (%s,%s)",
                                                                (int(prod_id), 0))
                                                            connection1.commit()

                                                            main_id = cursor9.lastrowid


                                                        with connection1.cursor() as cursor11:
                                                            sql = "SELECT * FROM oc21_category_description WHERE name = %s"
                                                            adr = subcategory



                                                            cursor11.execute(sql, adr)
                                                            connection1.commit()

                                                            if cursor11.rowcount >= 1:
                                                                result = cursor11.fetchone()
                                                                parent_id = result['category_id']

                                                                if parent_id:

                                                                    with connection1.cursor() as cursor10:
                                                                        cursor10.execute(
                                                                            "INSERT INTO  oc21_product_to_category (product_id,category_id) VALUES (%s,%s)",
                                                                            (int(prod_id), parent_id))
                                                                        connection1.commit()

                                                                        main_id = cursor10.lastrowid


                                                                        with connection.cursor() as cursor41:
                                                                            sql = "DELETE FROM adi WHERE id = %s"
                                                                            adr = adi_id

                                                                            cursor41.execute(sql, adr)
                                                                            connection.commit()

                                                                            print(cursor41.rowcount, "record(s) deleted")


                                                else:
                                                    print ("Update Logic")

                                                    print (adi_id)

                                                    with connection.cursor() as cursor41:
                                                        sql = "DELETE FROM adi WHERE id = %s"
                                                        adr = adi_id

                                                        cursor41.execute(sql, adr)
                                                        connection.commit()

                                                        print(cursor41.rowcount, "record(s) deleted")


                                        except Exception as e:
                                            print ('Failed Query')
                                            print (e)

                                    except pymysql.Error as e:
                                        print ("ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1]))
                                        print ("Loop1")
                                        time.sleep(2)
                                        print("Was a nice sleep, now let me continue...")







                                except Exception as e:
                                    print ('Failed Query')
                                    print ("Loop2")
                                    print (e)





                    except Exception as e:
                        print ("Loop3")
                        print (e)
                        continue
        except Exception as e:
            print ('Failed Query')
            print ("Loop2")
            print (e)
    except pymysql.Error as e:
        print ("ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1]))
        print ("Loop1")
        time.sleep(2)
        print("Was a nice sleep, now let me continue...")





if __name__ == '__main__':
    get_list()