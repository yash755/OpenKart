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
                cursor.execute("SELECT * FROM adi_category GROUP BY category")
                connection.commit()


                for row in cursor:
                    try:
                        data = row
                        category = data['category']
                        subCategory = data['subcategory']

                        print (category)



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

    try:
        connection1 = pymysql.connect(host="security-supply.com",
                                      user="security_ocar590",
                                      passwd="27c@44pS]k",
                                      db="security_ocar590",
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection1.cursor() as cursor2:
                # cursor2.execute(
                #     "INSERT INTO oc21_category (status, top, sort_order) VALUES (%s,%s,%s)",
                #     (1,1,1))
                cursor2.execute("SELECT * FROM oc21_category")
                connection1.commit()

                result = cursor2.fetchone()

                category_id = result['category_id']

                try:
                    with connection1.cursor() as cursor2:
                        # cursor2.execute(
                        #     "INSERT INTO oc21_category (status, top, sort_order) VALUES (%s,%s,%s)",
                        #     (1,1,1))

                        sql = "SELECT * FROM oc21_category_description WHERE = %s"
                        adr = category_id

                        cursor2.execute("SELECT * FROM oc21_category_description WHERE = '25'")
                        connection1.commit()

                        result = cursor2.fetchone()

                        category_id = result['category_id']

                        print (result)

                        print (result['category_id'])

                        print ("Inserted")
                except Exception as e:
                    print ('Failed Query')
                    print (e)

                print (result)

                print (result['category_id'])

                print ("Inserted")
        except Exception as e:
            print ('Failed Query')
            print (e)

    except pymysql.Error as e:
        print ("ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1]))
        print ("Loop1")
        time.sleep(2)
        print("Was a nice sleep, now let me continue...")


if __name__ == '__main__':
    get_list()