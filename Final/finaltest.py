import pymysql.cursors

try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    passwd
conn = pymysql.connect(
    user='root',
    passwd='seigo2020',
    host='localhost',
    db='final_chie_db',
    cursorclass=pymysql.cursors.DictCursor
)

def test2 ():
    name = input("name")
    while True:
        if name.isdecimal() == True:
            print ("dame")
            name = input("name1")
        else:
            break
    postcode = input("postcode")

    cur = conn.cursor()

    cur.execute("USE final_chie_db")

    insert_id_stock = "INSERT INTO test1(id,name,postcode) values(0,%s,%s)"

    item_id_stock_list = [
        (name, postcode)
    ]

    for id in item_id_stock_list:
        cur.execute(insert_id_stock, id)

    cur.execute('UPDATE test1 set id = record_id where id = 0')



    conn.commit()
    cur.close()
    conn.close()


test2()
