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
sale_list = []
sale_cg_list1 = []
sale_cg_list2 = []
sale_rate_list = []
sale_price_list = []

cur = conn.cursor()

cur.execute('SELECT cg_abb FROM item_cg where sale_flag=(%s)', (1))
sale_info = cur.fetchall()
for sale_info1 in sale_info:
    for value in sale_info1.values():
        sale_cg_list1.append(value)

print(sale_cg_list1)


cur.execute('SELECT cg_abb FROM item_cg where sale_flag=(%s)', (2))
sale_info = cur.fetchall()
for sale_info1 in sale_info:
    for value in sale_info1.values():
        sale_cg_list2.append(value)

print(sale_cg_list2)

cur.execute('SELECT discount_rate FROM item_cg where sale_flag=(%s)', (1))
sale_info = cur.fetchall()
for sale_info1 in sale_info:
    for value in sale_info1.values():
        sale_rate_list.append(value)

print(sale_rate_list)

cur.execute('SELECT discount_price FROM item_cg where sale_flag=(%s)', (2))
sale_info = cur.fetchall()
count = 0
for sale_info1 in sale_info:
    for value in sale_info1.values():
        sale_price_list.append(value)

print(sale_price_list)

if len(sale_cg_list1) == 1:
    print("1")

if len(sale_cg_list1) == 2:
    print("2")

if len(sale_cg_list1) == 3:
    print("3")

if len(sale_cg_list1) == 4:
    print("4")

cur.execute('SELECT id, list_price FROM items where cg_abb=(%s)', (sale_cg_list2))
sale_info = cur.fetchall()
for sale_info1 in sale_info:
    for value in sale_info1.values():
        sale_list.append(value)

print(sale_list)
