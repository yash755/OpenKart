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
                cursor.execute("SELECT * FROM adi_category GROUP BY subcategory LIMIT 1")
                # cursor.execute("SELECT * FROM adi WHERE subcategory IS NOT NULL LIMIT 10")
                connection.commit()


                for row in cursor:
                    try:
                        data = row
                        subcategory = data['subcategory']
                        category = data['category']

                        print (subcategory + '\n\n')

                        with connection.cursor() as cursor1:
                            sql = "SELECT * FROM adi WHERE subcategory  = %s IS NOT NULL LIMIT 1"
                            adr = subcategory

                            cursor1.execute(sql, adr)
                            connection.commit()

                            for row in cursor1:
                                print (row)

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
