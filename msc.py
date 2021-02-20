import pymysql.cursors
import time


def get_list():


    try:
        connection1 = pymysql.connect(host="security-supply.com",
                                      user="security_ocar590",
                                      passwd="27c@44pS]k",
                                      db="security_ocar590",
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection1.cursor() as cursor2:
                cursor2.execute("SELECT * FROM oc21_category")
                connection1.commit()


                print (cursor2.rowcount)


                for row in cursor2:
                    data = row

                    category = data['category_id']
                    print (category)



                    with connection1.cursor() as cursor3:
                        sql = "SELECT * FROM oc21_category_description WHERE category_id = %s"
                        adr = category

                        cursor3.execute(sql, adr)
                        connection1.commit()

                        if cursor3.rowcount >=1:
                            print (cursor3.fetchone())

                        else:
                            with connection1.cursor() as cursor4:
                                sql = "DELETE FROM oc21_category WHERE category_id = %s"
                                adr = category

                                cursor4.execute(sql, adr)
                                connection1.commit()

                                print(cursor4.rowcount, "record(s) deleted")



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