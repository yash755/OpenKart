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
                            sql = "SELECT * FROM adi WHERE subcategory  = %s IS NOT NULL LIMIT 2"
                            adr = subcategory

                            cursor1.execute(sql, adr)
                            connection.commit()

                            for row in cursor1:
                                try:
                                    data = row

                                    print (data)


                                except:
                                    print ("Error")

                    except:
                        print ("Erpr")

        except:
            print ("Erpr")
    except:
        print ("Erpr")