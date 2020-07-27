import unicodedata
import re
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

shopping_item_name_list = []
shopping_storage_list = []
shopping_storage_define_list = []
shopping_cg_abb_list = []
shopping_id_list = []
show_cart_list = []
more_five_list = []
shopping_all_price = []
shopping_all_cg_list = []
shopping_all_id = []
shopping_all_num = []

def error1():

    input1_str = input ("入力：")
    while True:
        if input1_str== "1" or input1_str== "2" or input1_str== "１" or input1_str== "２":
            input1 = int (input1_str)
            return(input1)
            break
        else:
            print("入力方法が間違っています。指定された数字で入力してください")
            print ("--------------------------------------------------------")
            input1_str = input ("入力：")



def get_east_asian_width_count_cat(add_or_cha_cat):
    count = 0
    for c in add_or_cha_cat:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count


def show_cart():
    print ("--------------------------------------------------------")
    print ("●カート表示●")
    cart = 'shopping_cart.txt'

    with open(cart, 'r', encoding='utf-8') as q:
        n = 0
        for s_line in q:
            n = n + 1
            print (n,":", s_line.replace("\n", ""))
    return n

def shopping():
    print ("--------------------------------------------------------")
    print ("●カート登録・変更●")
    print("追加・変更したい商品を選択してください")
    add_or_cha_cat = input("カテゴリ：")
    while True:
        shopping_cg_abb_list.clear()
        cur = conn.cursor()
        cur.execute('SELECT cg_abb FROM view_items WHERE cg_abb=%s', (add_or_cha_cat))
        add_card_cg_abb= cur.fetchall()
        for cart_cg_abb in add_card_cg_abb:
            for value in cart_cg_abb.values():
                shopping_cg_abb_list.append(value)

        if add_or_cha_cat == "cd" or add_or_cha_cat == "cD" or add_or_cha_cat == "Cd":
            print ("大文字で入力してください")
            add_or_cha_cat = input ("カテゴリ：")
        elif len(shopping_cg_abb_list) == 0:
            print ("カテゴリ名を入力してください")
            add_or_cha_cat = input ("カテゴリ：")
        else:
            asian = get_east_asian_width_count_cat(add_or_cha_cat)
            if asian == 4 or asian == 3:
                print ("半角で入力して下さい")
                add_or_cha_cat = input ("カテゴリ：")
            else:
                break
    add_or_cha_id = input("商品ID：")
    while True:
        shopping_id_list.clear()
        p = re.compile('[０-９]+')
        if add_or_cha_id.isdecimal() == False:
            print ("数字で入力してください。")
            add_or_cha_id= input ("商品ID：")
        cur.execute('SELECT id FROM view_items WHERE id=%s and cg_abb=%s', (add_or_cha_id,add_or_cha_cat))
        add_card_id= cur.fetchall()
        for cart_id in add_card_id:
            for value in cart_id.values():
                shopping_id_list.append(value)
        if p.fullmatch(add_or_cha_id) != None:
            print ("半角で入力してください")
            add_or_cha_id= input ("商品ID：")
        elif len(shopping_id_list) == 0:
            print ("商品IDを入力してください")
            add_or_cha_id= input ("商品ID：")

        else:
            break

    add_or_cha_category = add_or_cha_cat +' - '+ add_or_cha_id

    cart = 'shopping_cart.txt'
    with open(cart, mode='r', encoding='utf-8') as q:
        n = 0
        for f_line in q:
            n = n + 1

            if n <= 4:
                if add_or_cha_category not in f_line:
                    show_cart_list.append(f_line)
                elif add_or_cha_category in f_line:
                    more_five_list.append(1)

            elif n <= 5:
                if add_or_cha_category not in f_line:
                    show_cart_list.append(f_line)

                elif add_or_cha_category in f_line:
                    more_five_list.append(1)


    with open(cart, mode='w', encoding='utf-8') as f:
        for d in show_cart_list:
            f.write("%s" % d)

    if len(more_five_list) == 0 and n == 5:
        print("５件以上は追加できません。")

    if len(more_five_list) == 1 or n <= 4:
        more_five_list.clear()
        item_num = input ("個数：")
        while True:
            p = re.compile('[０-９]+')
            if item_num.isdecimal() == False:
                print ("数字で入力してください。")
                item_num = input ("個数：")
            cur.execute('SELECT storage FROM view_items WHERE id=%s and cg_abb=%s', (add_or_cha_id, add_or_cha_cat))
            add_card_storage= cur.fetchall()
            for cart_storage in add_card_storage:
                for value in cart_storage.values():
                    shopping_storage_list.append(value)

            if shopping_storage_list[0] == 0:
                print ("在庫がありません")
                item_num = "0"
                break

            elif int(item_num) > shopping_storage_list[0]:
                print (shopping_storage_list[0])
                print ("在庫が足りません")
                item_num = input ("個数：")
            else:
                if p.fullmatch(item_num) != None:
                    print ("半角で入力してください")
                    item_num = input ("個数：")
                else:
                    break


        cur.execute('SELECT item_name, artist, selling_price FROM view_items WHERE id=%s and cg_abb=%s', (add_or_cha_id, add_or_cha_cat))
        add_card_all= cur.fetchall()
        for cart_all in add_card_all:
            for value in cart_all.values():
                shopping_item_name_list.append(value)

        if int (shopping_storage_list[0]) > 3:
            shopping_storage_define_list.append("あり")
        elif int (shopping_storage_list[0]) == 0:
            shopping_storage_define_list.append("なし")
        elif int (shopping_storage_list[0]) > 0:
            shopping_storage_define_list.append(int (shopping_storage_list[0]))

        cur.close()
        shopping_all_cg_list.append(add_or_cha_cat)
        print(shopping_all_cg_list)
        shopping_all_id.append(add_or_cha_id)
        print(add_or_cha_id)


        if item_num != "0":
            with open('shopping_cart.txt', mode='a', encoding='utf-8') as f:
                f.write(str.upper(add_or_cha_cat))
                f.write(" - ")
                f.write(add_or_cha_id)
                f.write(" - ")
                f.write(str(shopping_item_name_list[2]))
                f.write(" 円 ")
                f.write(" - ")
                f.write("個数 ")
                f.write(item_num)
                f.write(" - ")
                f.write("在庫 ")
                f.write(str(shopping_storage_define_list[0]))
                f.write(" - ")
                f.write(str(shopping_item_name_list[1]))
                f.write(" - ")
                f.write(str(shopping_item_name_list[0]))
                f.write('\n')

        if item_num != "0":
            with open('shopping_cart_1.txt', mode='a', encoding='utf-8') as e:
                e.write(item_num)
                e.write(str.upper(add_or_cha_cat))
                e.write(add_or_cha_id)
                e.write('\n')



def con_shopping():
    show_cart()
    shopping()
    show_cart()
    print ("--------------------------------------------------------")
    print ("続けて追加・変更する場合は１を、それ以外は２を入力してください")
    input1 = error1()

    while True:
        shopping_item_name_list.clear()
        shopping_storage_list.clear()
        shopping_storage_define_list.clear()
        shopping_id_list.clear()
        show_cart_list.clear()
        shopping_item_name_list.clear()
        shopping_storage_list.clear()
        shopping_storage_define_list.clear()
        shopping_id_list.clear()
        show_cart_list.clear()


        if input1 == 1:
            shopping()
            show_cart()
            print ("--------------------------------------------------------")
            print ("続けて追加・変更する場合は１を、HOMEに戻るは2を入力してください")
            input1 = error1()
        elif input1 == 2:
            print ("pppp")
            break

con_shopping()
