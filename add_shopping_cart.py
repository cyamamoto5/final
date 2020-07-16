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


def get_east_asian_width_count(category):
    count = 0
    for c in category:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count


#読み込み
def add_shopping_cart(get_east_asian_width_count):
    print ("カート表示")
    with open('shopping_cart.txt', 'r', encoding='utf-8') as q:
        n = 0
        for s_line in q:
            n = n + 1
            print (n,":",s_line.replace("\n", ""))


    print ("カートに追加したい商品を選択して下さい")
    category = input ("カテゴリ：")
    while True:
        cur = conn.cursor()
        cur.execute('SELECT cg_abb FROM view_items WHERE cg_abb=%s', (category))
        add_card_cg_abb= cur.fetchall()
        for cart_cg_abb in add_card_cg_abb:
            for value in cart_cg_abb.values():
                cg_abb_list.append(value)

        if len(cg_abb_list) == 0:
            print ("カテゴリ名を入力してください")
            category = input ("カテゴリ：")
        else:
            asian = get_east_asian_width_count(category)
            if asian == 4 or asian == 3:
                print ("半角で入力して下さい")
                category = input ("カテゴリ：")
            else:
                break

    item_id = input ("商品ID：")
    while True:
        if item_id.isdecimal() == False:
            print ("数字で入力してください。")
            item_id = input ("商品ID：")
        cur.execute('SELECT id FROM view_items WHERE id=%s and cg_abb=%s', (item_id,category))
        add_card_id= cur.fetchall()
        for cart_id in add_card_id:
            for value in cart_id.values():
                id_list.append(value)
        if len(id_list) == 0:
            print ("商品IDを入力してください")
            item_id = input ("商品ID：")
        else:
            asian = get_east_asian_width_count(category)
            if asian == 4 or asian == 3:
                print ("半角で入力して下さい")
                item_id = input ("商品ID：")
            else:
                break

    item_num = input ("個数：")
    while True:
        if item_num.isdecimal() == False:
            print ("数字で入力してください。")
            item_num = input ("個数：")
        cur.execute('SELECT storage FROM view_items WHERE id=%s and cg_abb=%s', (item_id,category))
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
            asian = get_east_asian_width_count(category)
            if asian == 4 or asian == 3:
                print ("半角で入力して下さい")
                item_num = input ("個数：")
            else:
                break


    cur.execute('SELECT item_name, artist, selling_price, storage FROM view_items WHERE id=%s and cg_abb=%s', (item_id,category))
    add_card_all= cur.fetchall()
    for cart_all in add_card_all:
        for value in cart_all.values():
            item_name_list.append(value)


    cur.close()
    conn.close()

    with open('shopping_cart.txt', mode='a', encoding='utf-8') as f:
        f.write(str.upper(category))
        f.write(" - ")
        f.write(item_id)
        f.write(" - ")
        f.write(str(item_name_list[2]))
        f.write("円 ")
        f.write(" - ")
        f.write("在庫 ")
        f.write(str(item_name_list[3]))
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
            print (n,":",s_line.replace("\n", ""))

add_shopping_cart(get_east_asian_width_count)
