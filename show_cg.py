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

item_cg_name_list = []
item_cg_abb_list =[]

def show_item_cg(item_cg_name_list, item_cg_abb_list):
    cur = conn.cursor()
    cur.execute('SELECT cg_abb FROM item_cg')
    collect_item_cg_abb = cur.fetchall()

    for item_cg_abb in collect_item_cg_abb:
        for value in item_cg_abb.values():
            item_cg_abb_list.append(value)

    cur.execute('SELECT cg_name FROM item_cg')
    collect_item_cg_name = cur.fetchall()

    for item_cg_name in collect_item_cg_name:
        for value in item_cg_name.values():
            item_cg_name_list.append(value)

    print ("カテゴリ - カテゴリ名")
    for index, (i, j) in enumerate(zip(item_cg_abb_list, item_cg_name_list)):
        print(i, "-", j)

    cur.close()
    conn.close()
    
show_item_cg(item_cg_name_list, item_cg_abb_list)
