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

username_list = ['memequeen']
password_list = ['akasakataro']
order_cus_info_list = []

cur = conn.cursor()
cur.execute('SELECT name, postcode, address, cell, id FROM view_customers where username=(%s) and password=(%s)', (username_list[0], password_list[0]))
collect_order_cus_info = cur.fetchall()

for collect_order_cus_info1 in collect_order_cus_info:
    for value in collect_order_cus_info1.values():
        order_cus_info_list.append(value)



print(order_cus_info_list[0],"様")
print("TEL",order_cus_info_list[3])
print("〒",order_cus_info_list[1], " ",order_cus_info_list[2])
