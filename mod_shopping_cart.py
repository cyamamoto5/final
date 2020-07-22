import unicodedata
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

item_name_list = []
storage_list = []
cg_abb_list = []
id_list = []



def get_east_asian_width_count(delete_cat):
    count = 0
    for c in delete_cat:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count


#読み込み
def mod_shopping_cart():
    print ("--------------------------------------------------------")
    print ("●カート表示●")
    cart = 'shopping_cart.txt'
    l = []

    with open(cart, 'r', encoding='utf-8') as q:
        n = 0
        for s_line in q:
            n = n + 1
            print (n,":", s_line.replace("\n", ""))

    print ("--------------------------------------------------------")
    print ("●カート登録・変更●")
    delete_cat = input("カテゴリ")
    delete_id = input("商品ID")
    delete_category = delete_cat +' - '+ delete_id

    with open(cart, mode='r', encoding='utf-8') as q:
        n = 0
        for f_line in q:
            n = n + 1
            if delete_category not in f_line:
                l.append(f_line)


    with open(cart, mode='w', encoding='utf-8') as f:
        for d in l:
            f.write("%s" % d)


    cur = conn.cursor()
    cur.execute('SELECT cg_abb FROM view_items WHERE cg_abb=%s', (delete_cat))
    add_card_cg_abb= cur.fetchall()
    for cart_cg_abb in add_card_cg_abb:
        for value in cart_cg_abb.values():
            cg_abb_list.append(value)

    cur.execute('SELECT id FROM view_items WHERE id=%s and cg_abb=%s', (delete_id, delete_cat))
    add_card_id= cur.fetchall()
    for cart_id in add_card_id:
        for value in cart_id.values():
            id_list.append(value)

    item_num = input ("個数：")
    while True:
        if item_num.isdecimal() == False:
            print ("数字で入力してください。")
            item_num = input ("個数：")
        cur.execute('SELECT storage FROM view_items WHERE id=%s and cg_abb=%s', (delete_id, delete_cat))
        add_card_storage= cur.fetchall()
        for cart_storage in add_card_storage:
            for value in cart_storage.values():
                storage_list.append(value)

        if int(item_num) > storage_list[0]:
            print (storage_list[0])
            print ("在庫が足りません")
            item_num = input ("個数：")
        elif int(item_num) == 0:
            print ("個数を入力してください")
            item_num = input ("個数：")
        else:
            asian = get_east_asian_width_count(delete_cat)
            if asian == 4 or asian == 3:
                print ("半角で入力して下さい")
                item_num = input ("個数：")
            else:
                break


    cur.execute('SELECT item_name, artist, selling_price, storage FROM view_items WHERE id=%s and cg_abb=%s', (delete_id, delete_cat))
    add_card_all= cur.fetchall()
    for cart_all in add_card_all:
        for value in cart_all.values():
            item_name_list.append(value)


    cur.close()
    conn.close()

    with open('shopping_cart.txt', mode='a', encoding='utf-8') as f:
        f.write(str.upper(delete_cat))
        f.write(" - ")
        f.write(delete_id)
        f.write(" - ")
        f.write(str(item_name_list[2]))
        f.write("円 ")
        f.write(" - ")
        f.write("在庫 ")
        f.write(str(item_name_list[3])
        f.write(" - ")
        f.write("個数 ")
        f.write(item_num)
        f.write(" - ")
        f.write(str(item_name_list[1]))
        f.write(" - ")
        f.write(str(item_name_list[0]))
        f.write('\n')


    with open('shopping_cart.txt', 'r', encoding='utf-8') as q:
        n = 0
        for s_line in q:
            n = n + 1
            print (n,":", s_line.replace("\n", ""))

mod_shopping_cart()
