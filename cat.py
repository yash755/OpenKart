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
            #with connection.cursor() as cursor:
            cursor = connection.cursor()
            cursor.execute("SELECT category FROM adi_category GROUP BY category")
                #connection.commit()


            numrows = cursor.rowcount

            for x in range(0, numrows):
                row = cursor.fetchone()
                print (row[0])

            # for row in rows:
            #         # try:
            #     data = row
            #     category = data['category']
            #
            #
            #     print (category)


                    # except Exception as e:
                    #     print ("Loop3")
                    #     print (e)
                    #     continue
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
    while True:
        get_list()