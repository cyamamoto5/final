import pymysql.cursors
import unicodedata

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
choose_cg_abb_list = []
choose_id_list = []
choose_item_name_list = []
choose_artist_list = []
choose_selling_price_list = []
choose_storage_list = []
username_list = []
password_list = []
show_cus_id_list = []
show_cus_name_list = []
show_cus_postcode_list = []
show_cus_address_list = []
show_cus_cell_list = []
show_cus_email_list = []
show_cus_password_list = []
shopping_cg_abb_list = []



def show_item_cg(item_cg_name_list, item_cg_abb_list):
    item_cg_name_list.clear()
    item_cg_abb_list.clear()
    choose_cg_abb_list.clear()
    choose_id_list.clear()
    choose_item_name_list.clear()
    choose_artist_list.clear()
    choose_selling_price_list.clear()
    choose_storage_list.clear()
    print("●カテゴリリスト●")
    print("ID - カテゴリ名")
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

    for index, (i, j) in enumerate(zip(item_cg_abb_list, item_cg_name_list)):
        print(i, "-", j)

def search_items():
    print ("--------------------------------------------------------")
    print("●商品検索●")
    print('カテゴリを選択してください。')
    choose_cg_abb = input("カテゴリ：")
    while True:
        shopping_cg_abb_list.clear()
        cur = conn.cursor()
        cur.execute('SELECT cg_abb FROM view_items WHERE cg_abb=%s', (choose_cg_abb))
        add_card_cg_abb= cur.fetchall()
        for cart_cg_abb in add_card_cg_abb:
            for value in cart_cg_abb.values():
                shopping_cg_abb_list.append(value)

        if choose_cg_abb == "cd" or choose_cg_abb == "cD" or choose_cg_abb == "Cd":
            print ("大文字で入力してください")
            choose_cg_abb = input ("カテゴリ：")
        elif len(shopping_cg_abb_list) == 0:
            print ("カテゴリ名を入力してください")
            choose_cg_abb = input ("カテゴリ：")
        else:
            asian = get_east_asian_width_count_cat(choose_cg_abb)
            if asian == 4 or asian == 3:
                print ("正しい書式で入力してください")
                choose_cg_abb = input ("カテゴリ：")
            else:
                break


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
            if value > 5:
                choose_storage_list.append("あり")
            elif 5 >= value > 1:
                choose_storage_list.append(value)
            elif value == 0:
                choose_storage_list.append("なし")

    print ("--------------------------------------------------------")
    for index, (a, b, c, d, e, f) in enumerate(zip(choose_cg_abb_list, choose_id_list, choose_item_name_list, choose_artist_list, choose_selling_price_list, choose_storage_list)):
        print(a, "-",b, "-",e,"円", "- 在庫",f, "-", d, "-", c)


    cur.close()

def get_east_asian_width_count_cat(add_or_cha_cat):
    count = 0
    for c in add_or_cha_cat:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

def error1():
    input1_str = input ("入力：")
    while True:
        if input1_str== "1" or input1_str== "2" or input1_str== "１" or input1_str== "２":
            input1 = int (input1_str)
            return(input1)
            break
        else:
            print("入力方法が間違っています。指定された数字で入力してください")
            print ("--------------")
            input1_str = input ("入力：")

def show_search_items(show_item_cg, search_items):
    print ("--------------------------------------------------------")
    show_item_cg(item_cg_name_list, item_cg_abb_list)
    search_items()
    print ("--------------------------------------------------------")
    print ("検索を続ける場合は１、カート画面に移動する場合は２、Homeに戻る際は３を")
    input1 = error1()
    if input1 == 1:
        show_search_items(show_item_cg, search_items)
    if input1 == 3:
        home(show_search_items)


def home(show_search_items):
    print ("--------------------------------------------------------")
    print("●ＨＯＭＥ●")
    print("1: 商品検索")
    print("2: 商品選択")
    print("3: カート表示")
    print("4: 会員情報")
    print("5: 購入履歴")
    print("6: 購入終了")
    print ("--------------------------------------------------------")

    print("お進みいただく項目の選択をお願いします")
    home_input = input("入力：")
    if home_input == "1":
        show_search_items(show_item_cg, search_items)

    elif home_input == "2":
        print("まだできてないよ")
    else:
        print ("正しい書式で入力してください")

home(show_search_items)
