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

                        try:
                            connection1 = pymysql.connect(host="security-supply.com",
                                                         user="security_ocar590",
                                                         passwd="27c@44pS]k",
                                                         db="security_ocar590",
                                                         charset='utf8mb4',
                                                         cursorclass=pymysql.cursors.DictCursor)

                            print (connection1)

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