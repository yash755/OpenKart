import pymysql.cursors
import time


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
                cursor.execute("SELECT * FROM adi_category GROUP BY subcategory LIMIT 2")
                # cursor.execute("SELECT * FROM adi WHERE subcategory IS NOT NULL LIMIT 10")
                connection.commit()


                for row in cursor:
                    try:
                        data = row
                        subcategory = data['subcategory']
                        category = data['category']

                        print (subcategory + '\n\n')

                        with connection.cursor() as cursor1:
                            sql = "SELECT * FROM adi WHERE subcategory  = %s IS NOT NULL LIMIT 10"
                            adr = subcategory

                            cursor1.execute(sql, adr)
                            connection.commit()

                            for row in cursor1:
                                try:
                                    data = row

                                    handle = data['handle']
                                    title = data['title']
                                    html = data['html']
                                    vendor = data['vendor']

                                    variant_price = data['variant_price']
                                    variant_barcode = data['variant_barcode']

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


                                                    print ("Vendor ID " + str(vendor_id))


                                                else:
                                                    print ("No")
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