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
                cursor.execute("SELECT * FROM adi_category GROUP BY subcategory")
                connection.commit()


                for row in cursor:
                    try:
                        data = row
                        subcategory = data['subcategory']
                        category = data['category']

                        try:
                            connection1 = pymysql.connect(host="security-supply.com",
                                                          user="security_ocar590",
                                                          passwd="27c@44pS]k",
                                                          db="security_ocar590",
                                                          charset='utf8mb4',
                                                          cursorclass=pymysql.cursors.DictCursor)

                            try:
                                with connection1.cursor() as cursor2:
                                    sql = "SELECT * FROM oc21_category_description WHERE name = %s"
                                    adr = subcategory

                                    cursor2.execute(sql, adr)
                                    connection1.commit()

                                    print (cursor2.rowcount)

                                    if cursor2.rowcount == 0:
                                        with connection1.cursor() as cursor3:
                                            sql = "SELECT * FROM oc21_category_description WHERE name = %s"
                                            adr = category

                                            cursor3.execute(sql, adr)
                                            connection1.commit()

                                            if cursor3.rowcount >= 1:
                                                result = cursor3.fetchone()
                                                parent_id = result['category_id']

                                                if parent_id:



                                                    try:
                                                        with connection1.cursor() as cursor4:
                                                            cursor4.execute(
                                                                "INSERT INTO oc21_category (status, top, sort_order) VALUES (%s,%s,%s)",
                                                                (1,1,1))

                                                            connection1.commit()

                                                            print(cursor4.lastrowid, "record inserted.")
                                                            print


                                                            # result2 = cursor3.fetchone()
                                                            category_id = cursor4.lastrowid
                                                            print (category_id)
                                                            with connection1.cursor() as cursor5:
                                                                cursor5.execute(
                                                                    "INSERT INTO  oc21_category_description (name,category_id,parent_id,language_id) VALUES (%s,%s,%s,%s)",
                                                                    (str(subcategory), category_id, parent_id, 1))

                                                            connection1.commit()

                                                            with connection1.cursor() as cursor5:
                                                                cursor5.execute(
                                                                    "INSERT INTO  oc21_category_to_store (store_id,category_id) VALUES (%s,%s)",
                                                                    (0, category_id))

                                                            connection1.commit()





                                                    except Exception as e:
                                                        print ('Failed Query')
                                                        print (e)






                            except Exception as e:
                                print ('Failed Query')
                                print (e)

                        except pymysql.Error as e:
                            print ("ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1]))
                            print ("Loop1")
                            time.sleep(2)
                            print("Was a nice sleep, now let me continue...")



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