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

show_item_cg(item_cg_name_list, item_cg_abb_list)


print ("--------------------------------------------------------")
print('カテゴリを選択してください。')
choose_cg_abb = input("カテゴリ入力：")

choose_cg_abb_list = []
choose_id_list = []
choose_item_name_list = []
choose_artist_list = []
choose_selling_price_list = []
choose_storage_list = []

def search_items():
    cur = conn.cursor()
    cur.execute('SELECT cg_abb FROM view_items WHERE cg_abb=(%s)', (choose_cg_abb))
    collect_choose_cg_abb = cur.fetchall()
    for cg_abb in collect_choose_cg_abb:
        for value in cg_abb.values():
            choose_cg_abb_list.append(value)

    cur.execute('SELECT id FROM view_items WHERE cg_abb=(%s)', (choose_cg_abb))
    collect_choose_id = cur.fetchall()
    for id in collect_choose_id:
        for value in id.values():
            choose_id_list.append(value)

    cur.execute('SELECT item_name FROM view_items WHERE cg_abb=(%s)', (choose_cg_abb))
    collect_item_name_id = cur.fetchall()
    for item_name in collect_item_name_id:
        for value in item_name.values():
            choose_item_name_list.append(value)

    cur.execute('SELECT artist FROM view_items WHERE cg_abb=(%s)', (choose_cg_abb))
    collect_artist_id = cur.fetchall()
    for artist in collect_artist_id:
        for value in artist.values():
            choose_artist_list.append(value)

    cur.execute('SELECT selling_price FROM view_items WHERE cg_abb=(%s)', (choose_cg_abb))
    collect_selling_price= cur.fetchall()
    for selling_price in collect_selling_price:
        for value in selling_price.values():
            choose_selling_price_list.append(value)

    cur.execute('SELECT storage FROM view_items WHERE cg_abb=(%s)', (choose_cg_abb))
    collect_storage= cur.fetchall()
    for storage in collect_storage:
        for value in storage.values():
            choose_storage_list.append(value)

    for index, (a, b, c, d, e, f) in enumerate(zip(choose_cg_abb_list, choose_id_list, choose_item_name_list, choose_artist_list, choose_selling_price_list, choose_storage_list)):
        print(a, "-", b, "-", d, "-", c, "-", e,"円", "-", f)


    cur.close()
    conn.close()

search_items()
