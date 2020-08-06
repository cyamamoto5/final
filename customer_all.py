import unicodedata
import re
import pymysql.cursors
import math
import datetime
import os

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
cus_id_list = []
order_cus_info_list = []
order_list2 = []
purchase_id_list = []
username_list = []
password_list = []
item_cg_name_list = []
item_cg_abb_list =[]
choose_cg_abb_list = []
choose_id_list = []
choose_item_name_list = []
choose_artist_list = []
choose_selling_price_list = []
choose_storage_list = []
show_cus_id_list = []
show_cus_name_list = []
show_cus_postcode_list = []
show_cus_address_list = []
show_cus_cell_list = []
show_cus_email_list = []
shopping_cg_abb_list = []
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
shopping_tax_list = []
show_cus_id_list = []
show_cus_name_list1 = []
show_cus_postcode_list = []
show_cus_address_list = []
show_cus_cell_list = []
show_cus_email_list = []
show_cus_password_list = []
all_cus_info_list = []
order_cus_info_list = []
list = []
list2 = []
order_cus_id_list = []
shipping_fee_list = []
order_id_list = []
order_item_name1_list = [0]
order_item_name2_list = [0]
order_item_name3_list = [0]
order_item_name4_list = [0]
order_item_name5_list = [0]



def error1():
    input1_str = input ("入力：")
    while True:
        if input1_str== "1" or input1_str== "2" or input1_str== "１" or input1_str== "２":
            input1 = int (input1_str)
            return(input1)
            break

        else:
            print ("--------------------------------------------------------")
            print("入力方法が間違っています。指定された数字で入力してください")
            input1_str = input ("入力：")

def error5():
    input1_str = input ("入力：")
    while True:
        if input1_str== "1" or input1_str== "2" or input1_str== "3" or input1_str== "4" or input1_str== "5"  or input1_str== "6" or input1_str== "１" or input1_str== "２" or input1_str== "３" or input1_str== "４" or input1_str== "５" or input1_str== "６":
            input1 = int (input1_str)
            return(input1)
            break
        if input1_str == "#" or input1_str =="＃":
            return(input1_str)
        else:
            print("入力方法が間違っています。指定された数字で入力してください")
            print ("--------------------------------------------------------")
            input1_str = input ("入力：")

def error6():
    input1_str = input ("入力：")
    while True:
        if input1_str== "1" or input1_str== "2" or input1_str== "3" or input1_str== "4" or input1_str== "5" or input1_str== "6" or input1_str== "7" or input1_str== "１" or input1_str== "２" or input1_str== "３" or input1_str== "４" or input1_str== "５" or input1_str== "６" or input1_str== "７":
            input1 = int (input1_str)
            return(input1)
            break
        else:
            print("入力方法が間違っています。指定された数字で入力してください")
            print ("--------------------------------------------------------")
            input1_str = input ("入力：")

def login_input():
    cur = conn.cursor()
    username_input = input("ログインID：")
    if username_input == "#" or username_input == "＃":
        first_screen()
        error_input1 = error1()

    cur.execute('SELECT username FROM view_customers where username=(%s)', (username_input))
    collect_username = cur.fetchall()

    for username in collect_username:
        for value in username.values():
            username_list.append(value)

    password_input = input("パスワード：")
    if password_input == "#" or password_input == "＃":
        first_screen()
        error_input1 = error1()

    print ("--------------------------------------------------------")
    cur.execute('SELECT username FROM view_customers where password=(%s) and username=(%s)', (password_input, username_input))
    collect_password = cur.fetchall()

    for password in collect_password:
        for value in password.values():
            password_list.append(value) #ログイン画面

def show_cus_name (login_input):
    username2 = login_error(login_input, show_cus_name)
    username1 = username2[0]
    cur = conn.cursor()

    cur.execute('SELECT name FROM view_customers where username=%s',(username1))
    collect_new_username3 = cur.fetchall()
    for username3 in collect_new_username3:
        for value in username3.values():
            show_cus_name_list1.append(value)


    print(show_cus_name_list1[0], "さん、こんにちは")

def login_error(login_input, show_cus_name):
    while True:
        if not username_list or not password_list:
            print ("入力内容が正しくありません。再入力をお願いします。\nパスワードの再設定は、以下のメールアドレスにお問い合わせください。\ncustomer@vv.com")
            print ("--------------------------------------------------------")
            username_list.clear()
            password_list.clear()
            login_input()
        else:
            break

    while True:
        if username_list == password_list:
            return (username_list)
            break
        else:
            print ("入力内容が正しくありません。再入力をお願いします。\nパスワードの再設定は、以下のメールアドレスにお問い合わせください。\ncustomer@vv.com")
            print ("--------------------------------------------------------")
            username_list.clear()
            password_list.clear()
            login_input()

def login(login_input, login_error):
    cur = conn.cursor()
    print ("--------------------------------------------------------")
    print("●ログイン画面●")
    print("「#」を入力、エンターで前画面に戻る")
    #リストへの追加
    login_input()
    login_error(login_input, show_cus_name)

def add_customers (error1):
    print ("--------------------------------------------------------")
    print("●新規会員登録画面●")
    name = input("氏名（45文字以内）：")
    if name == "#" or name == "＃":
        first_screen()
        error_input1 = error1()
    while True:
        if name.isdecimal() == True:
            print ("文字列で入力してください。")
            print ("--------------------------------------------------------")
            name = input("氏名（45文字以内）：")
            if name == "#" or name == "＃":
                first_screen()
                error_input1 = error1()
        elif len(name)> 33:
            print("長すぎです。32文字以内で入力してください。")
            print ("--------------------------------------------------------")
            name = input("氏名（45文字以内）：")
            if name == "#" or name == "＃":
                first_screen()
                error_input1 = error1()
        elif len(name)< 2:
            print("苗字とお名前を入力してください。")
            print ("--------------------------------------------------------")
            name = input("氏名（45文字以内）：")
            if name == "#" or name == "＃":
                first_screen()
                error_input1 = error1()
        else:
            break

    postcode_str = input("郵便番号（7桁数値）：")
    if postcode_str == "#" or postcode_str == "＃":
        first_screen()
        error_input1 = error1()
    while True:
        if postcode_str.isdecimal() == False:
            print ("数字で入力してください。")
            postcode_str = input("郵便番号（7桁数値）：")
            if postcode_str == "#" or postcode_str == "＃":
                first_screen()
                error_input1 = error1()
        elif len(postcode_str) != 7:
            print("7文字で入力してください。")
            print ("--------------------------------------------------------")
            postcode_str = input("郵便番号（7桁数値）：")
            if postcode_str == "#" or postcode_str == "＃":
                first_screen()
                error_input1 = error1()
        else:
            postcode = int(postcode_str)
            break

    address = input("住所（45文字以内）：")
    if address == "#" or address == "＃":
        first_screen()
        error_input1 = error1()
    while True:
        if len(address)> 45:
            print("長すぎです。45文字以内で入力してください。")
            print ("--------------------------------------------------------")
            address = input("住所（45文字以内）：")
            if address == "#" or address == "＃":
                first_screen()
                error_input1 = error1()
        if len(address)< 5:
            print("お届け先の住所を入力してください。")
            print ("--------------------------------------------------------")
            address = input("住所（45文字以内）：")
            if address == "#" or address == "＃":
                first_screen()
                error_input1 = error1()
        else:
            break

    cell = input("電話番号（10,11桁数値）：")
    if cell == "#" or cell == "＃":
        first_screen()
        error_input1 = error1()
    while True:
        if cell.isdecimal() == False:
            print ("数字で入力してください。")
            print ("--------------------------------------------------------")
            cell = input("電話番号（10,11桁数値）：")
            if cell == "#" or cell == "＃":
                first_screen()
                error_input1 = error1()
        elif len(cell) == 10 or len(cell) == 11:
            break
        else:
            print("10or11桁で入力してください。")
            print ("--------------------------------------------------------")
            cell = input("電話番号（10,11桁数値）：")
            if cell == "#" or cell == "＃":
                first_screen()
                error_input1 = error1()

    email = input("メールアドレス（45文字英数字記号）：")
    if email == "#" or email == "＃":
        first_screen()
        error_input1 = error1()
    while True:
        if len(email)> 65:
            print("長すぎです。64文字以内で入力してください。")
            print ("--------------------------------------------------------")
            email = input("メールアドレス（45文字英数字記号）：")
            if email == "#" or email == "＃":
                first_screen()
                error_input1 = error1()
        elif re.match(r'[a-z\d._]+@[a-z]+\.[a-z]+', email):
            break
        else:
            print("正しいメールアドレスを入力してください。")
            print ("--------------------------------------------------------")
            email = input("メールアドレス（45文字英数字記号）：")
            if email == "#" or email == "＃":
                first_screen()
                error_input1 = error1()

    password = input("パスワード（8桁以上45桁以下英数字）：")
    if password == "#" or password == "＃":
        first_screen()
        error_input1 = error1()
    while True:
        p = re.compile('[a-zA-Z0-9]+')
        if len(password)> 33:
            print("長すぎです。32桁以内の大文字小文字英語か数字で入力してください。")
            print ("--------------------------------------------------------")
            password = input("パスワード（8桁以上45桁以下英数字）：")
            if password == "#" or password == "＃":
                first_screen()
                error_input1 = error1()
        if len(password)<8:
            print("短すぎです。8桁以上の大文字小文字英語か数字で入力してください。")
            print ("--------------------------------------------------------")
            password = input("パスワード（8桁以上45桁以下英数字）：")
            if password == "#" or password == "＃":
                first_screen()
                error_input1 = error1()
        elif re.search(r'[a-zA-Z0-9]+', password):
            break
        else:
            print("正しいパスワードを入力してください。")
            print ("--------------------------------------------------------")
            password = input("パスワード（8桁以上45桁以下英数字）：")
            if password == "#" or password == "＃":
                first_screen()
                error_input1 = error1()


    cur = conn.cursor()
    cur.execute("USE final_chie_db")

    username = input("ログインID：")
    if username == "#" or username == "＃":
        first_screen()
        error_input1 = error1()
    while True:
        p = re.compile('[a-zA-Z0-9]+')
        if len(password)> 33:
            print("長すぎです。32桁以内の大文字小文字英語か数字で入力してください。")
            print ("--------------------------------------------------------")
            username = input("ログインID：")
            if username == "#" or username == "＃":
                first_screen()
                error_input1 = error1()
        if len(password)<8:
            print("短すぎです。8桁以上の大文字小文字英語か数字で入力してください。")
            print ("--------------------------------------------------------")
            username = input("ログインID：")
            if username == "#" or username == "＃":
                first_screen()
                error_input1 = error1()
        elif re.search(r'[a-zA-Z0-9]+', username):

            new_username_list = []
            cur = conn.cursor()
            cur.execute('SELECT username FROM view_customers where username=(%s)', (username))
            collect_new_username = cur.fetchall()

            for username in collect_new_username:
                for value in username.values():
                    new_username_list.append(value)

            if len(new_username_list)>0:
                print ("すでに使われているユーザー名です。")
                print ("--------------------------------------------------------")
                new_username_list.clear()
                username = input("ログインID：")
                if username == "#" or username == "＃":
                    first_screen()
                    error_input1 = error1()
            else:
                break

        else:
            print("正しい書式で入力してください。")
            print ("--------------------------------------------------------")
            username = input("ログインID：")
            if username == "#" or username == "＃":
                first_screen()
                error_input1 = error1()
    print ("--------------------------------------------------------")
    print ("名前：",name,"\n", "〒：",postcode,"\n","住所（45文字以内）：", address, "\n","TEL：", cell, "\n","メール：", email, "\n", "パスワード（8桁以上45桁以下英数字）：",password, "\n", "ユーザーID：",username)
    print ("この内容で決定しますか？決定は1を再度編集は2を押してください")
    error_input1 = error1()
    print ("--------------------------------------------------------")
    if error_input1 == 1:
        add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(0,%s,%s,%s,%s,%s,%s,%s)"
        new_customers_list = [
            (name, postcode, address, cell, email, password, username)
        ]
        for new_cus in new_customers_list:
            cur.execute(add_customers, new_cus)
        cur.execute('UPDATE customers set id = record_id where id = 0')

        conn.commit()
        username_list.append(username)
        password_list.append(username)

    elif error_input1 == 2:
        add_customers(error1)
    elif error_input1 == "#" or error_input1 == "＃":
        add_customers()

def output1(error_input1, login, add_customers):
    if error_input1 == 1:
        login(login_input, login_error)
    elif error_input1 == 2:
        add_customers (error1)
    elif error_input1 == "#" or  error_input1 == "＃":
        print("入力方法が間違っています。指定された数字で入力してください")
        first_screen()

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
    print("「#」を入力、エンターで前画面に戻る")
    choose_cg_abb = input("カテゴリ：")

    if choose_cg_abb == "#" or choose_cg_abb == "＃":
        home()
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
            if choose_cg_abb == "#" or choose_cg_abb == "＃":
                home()

        elif len(shopping_cg_abb_list) == 0:
            print ("カテゴリ名を入力してください")
            choose_cg_abb = input ("カテゴリ：")
            if choose_cg_abb == "#" or choose_cg_abb == "＃":
                home()

        else:
            asian = get_east_asian_width_count_cat(choose_cg_abb)
            if asian == 4 or asian == 3:
                print ("正しい書式で入力してください")
                choose_cg_abb = input ("カテゴリ：")
                if choose_cg_abb == "#" or choose_cg_abb == "＃":
                    home()
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

    cur.execute('SELECT item_detail FROM view_items WHERE cg_abb=(%s)', (choose_cg_abb))
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
            elif 5 >= value >= 1:
                choose_storage_list.append(value)
            elif value == 0:
                choose_storage_list.append("なし")

    print ("\n")
    print("ｶﾃｺﾞﾘID - 商品ID - 税込 - 個数 - 在庫 - 商品詳細 - 商品")
    for index, (a, b, c, d, e, f) in enumerate(zip(choose_cg_abb_list, choose_id_list, choose_item_name_list, choose_artist_list, choose_selling_price_list, choose_storage_list)):
        print(a, "-",b, "-",e,"円", "- 在庫",f, "-", d, "-", c)

def get_east_asian_width_count_cat(add_or_cha_cat):
    count = 0
    for c in add_or_cha_cat:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

def error2():
    input1_str = input ("入力：")
    while True:
        if input1_str== "1" or input1_str== "2" or input1_str== "１" or input1_str== "２" or input1_str== "3" or input1_str== "３":
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
    print ("検索を続ける場合は１、カート画面に移動する場合は２、Homeに戻る際は３を入力してください")
    input1 = error2()
    if input1 == 1:
        show_search_items(show_item_cg, search_items)
    if input1 == 2:
        con_shopping()
    if input1 == 3:
        home()

def get_east_asian_width_count_cat(add_or_cha_cat):
    count = 0
    for c in add_or_cha_cat:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

def show_cart():
    register_list = [0]
    cart = 'shopping_cart.txt'
    with open(cart, 'r', encoding='utf-8') as q:
        for s_line in q:
            register_list.append(s_line)

    register_length = len(register_list)
    if register_list[register_length - 1] == 0:
        print("カートが空です")
        register_list.clear()
    else:
        print("ｶﾃｺﾞﾘID - 商品ID - 税込 - 個数 - 在庫 - 商品詳細 - 商品")
        with open(cart, 'r', encoding='utf-8') as q:
            n = 0
            for s_line in q:
                n = n + 1
                print (n,":", s_line.replace("\n", ""))
        return n

def shopping():
    print ("--------------------------------------------------------")
    print ("●カート登録・変更●")
    print("「#」を入力、エンターで前画面へ戻る")
    print("追加・変更したい商品を選択してください")
    print("カートに入っている商品は個数の変更が可能です。変更する個数を入力してください")
    print("カートから消したい商品があるときは個数を0にしてください")
    print("カートに追加できる最大個数は5個です")
    add_or_cha_cat = input("カテゴリ：")
    if add_or_cha_cat == "#" or add_or_cha_cat == "＃":
        home()
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
            if add_or_cha_cat == "#" or add_or_cha_cat == "＃":
                home()
        elif len(shopping_cg_abb_list) == 0:
            print ("カテゴリ名を入力してください")
            add_or_cha_cat = input ("カテゴリ：")
            if add_or_cha_cat == "#" or add_or_cha_cat == "＃":
                home()
        else:
            asian = get_east_asian_width_count_cat(add_or_cha_cat)
            if asian == 4 or asian == 3:
                print ("半角で入力して下さい")
                add_or_cha_cat = input ("カテゴリ：")
                if add_or_cha_cat == "#" or add_or_cha_cat == "＃":
                    home()
            else:
                break
    add_or_cha_id = input("商品ID：")
    if add_or_cha_id == "#" or add_or_cha_id == "＃":
        home()
    while True:
        shopping_id_list.clear()
        p = re.compile('[０-９]+')
        if add_or_cha_id.isdecimal() == False:
            print ("数字で入力してください。")
            add_or_cha_id= input ("商品ID：")
            if add_or_cha_id == "#" or add_or_cha_id == "＃":
                home()
        cur.execute('SELECT id FROM view_items WHERE id=%s and cg_abb=%s', (add_or_cha_id,add_or_cha_cat))
        add_card_id= cur.fetchall()
        for cart_id in add_card_id:
            for value in cart_id.values():
                shopping_id_list.append(value)
        if p.fullmatch(add_or_cha_id) != None:
            print ("半角で入力してください")
            add_or_cha_id= input ("商品ID：")
            if add_or_cha_id == "#" or add_or_cha_id == "＃":
                home()
        elif len(shopping_id_list) == 0:
            print ("商品IDを入力してください")
            add_or_cha_id= input ("商品ID：")
            if add_or_cha_id == "#" or add_or_cha_id == "＃":
                home()
        else:
            break

    add_or_cha_category = add_or_cha_cat +' - '+ add_or_cha_id

    cart = 'shopping_cart.txt'
    with open(cart, mode='r', encoding='utf-8') as q:
        n = 0
        for f_line in q:
            n = n + 1

            if n <= 5:
                if add_or_cha_category not in f_line:
                    show_cart_list.append(f_line)

                elif add_or_cha_category in f_line:
                    more_five_list.append(1)


    with open(cart, mode='w', encoding='utf-8') as f:
        for d in show_cart_list:
            f.write("%s" % d)

    if len(more_five_list) == 0 and n == 5:
        print("\n")
        print("５件以上は追加できません。")

    if len(more_five_list) == 1 or n <= 4:
        more_five_list.clear()
        item_num = input ("個数：")
        if item_num == "#" or item_num == "＃":
            home()
        while True:
            p = re.compile('[０-９]+')
            if item_num.isdecimal() == False:
                print ("数字で入力してください。")
                item_num = input ("個数：")
                if item_num == "#" or item_num == "＃":
                    home()
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
                print("\n")
                print ("在庫が足りません")
                item_num = input ("個数：")
            else:
                if p.fullmatch(item_num) != None:
                    print ("半角で入力してください")
                    item_num = input ("個数：")
                else:
                    break


        cur.execute('SELECT item_name, item_detail, selling_price FROM view_items WHERE id=%s and cg_abb=%s', (add_or_cha_id, add_or_cha_cat))
        add_card_all= cur.fetchall()
        for cart_all in add_card_all:
            for value in cart_all.values():
                shopping_item_name_list.append(value)


        if int (shopping_storage_list[0]) > 5:
            shopping_storage_define_list.append("あり")
        elif int (shopping_storage_list[0]) == 0:
            shopping_storage_define_list.append("なし")
        elif 5 >= int (shopping_storage_list[0]) > 0:
            shopping_storage_define_list.append(int (shopping_storage_list[0]))


        cur.execute('SELECT tax FROM item_cg WHERE cg_abb=%s', (add_or_cha_cat))
        add_tax_all= cur.fetchall()
        for tax_all in add_tax_all:
            for value in tax_all.values():
                shopping_tax_list.append(value)

        cur.close()


        shopping_all_cg_list.append(add_or_cha_cat)
        shopping_all_id.append(add_or_cha_id)
        taxed_price = math.floor(shopping_tax_list[0]*shopping_item_name_list[2])


        if item_num != "0":
            with open('shopping_cart.txt', mode='a', encoding='utf-8') as f:
                f.write(str.upper(add_or_cha_cat))
                f.write(" - ")
                f.write(add_or_cha_id)
                f.write(" - ")
                f.write(str(taxed_price))
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
    print("\n")
    show_cart()
    shopping()
    print("\n")
    show_cart()
    print ("--------------------------------------------------------")
    print ("続けて追加・変更する場合は１を、Homeに戻る場合は２を入力してください")
    input1 = error1()

    while True:
        shopping_item_name_list.clear()
        shopping_storage_list.clear()
        shopping_storage_define_list.clear()
        shopping_id_list.clear()
        show_cart_list.clear()
        shopping_tax_list.clear()

        if input1 == 1:
            shopping()
            show_cart()
            print ("--------------------------------------------------------")
            print ("続けて追加・変更する場合は１を、HOMEに戻る場合は2を入力してください")
            input1 = error1()
        elif input1 == 2:
            home()
            break
        else:
            print("\n")
            print("入力方法が間違っています。指定された数字で入力してください")
            input1 = error1()

def show_cus_info (login_input):
    username1 = username_list[0]
    cur = conn.cursor()

    cur.execute('SELECT id FROM customers as a where a.record_id =(select c.record_id from customers AS c where a.id = c.id order by c.record_id DESC LIMIT 1) and username=%s',(username1))
    collect_new_username10 = cur.fetchall()
    for username10 in collect_new_username10:
        for value in username10.values():
            show_cus_id_list.append(value)
            all_cus_info_list.append(value)

    cur.execute('SELECT name FROM customers as a where a.record_id =(select c.record_id from customers AS c where a.id = c.id order by c.record_id DESC LIMIT 1) and username=%s',(username1))
    collect_new_username3 = cur.fetchall()
    for username3 in collect_new_username3:
        for value in username3.values():
            show_cus_name_list.append(value)
            all_cus_info_list.append(value)

    cur.execute('SELECT postcode FROM customers as a where a.record_id =(select c.record_id from customers AS c where a.id = c.id order by c.record_id DESC LIMIT 1) and username=%s',(username1))
    collect_new_username4 = cur.fetchall()
    for username4 in collect_new_username4:
        for value in username4.values():
            show_cus_postcode_list.append(value)
            all_cus_info_list.append(value)

    cur.execute('SELECT address FROM customers as a where a.record_id =(select c.record_id from customers AS c where a.id = c.id order by c.record_id DESC LIMIT 1) and username=%s',(username1))
    collect_new_username5 = cur.fetchall()
    for username5 in collect_new_username5:
        for value in username5.values():
            show_cus_address_list.append(value)
            all_cus_info_list.append(value)

    cur.execute('SELECT cell FROM customers as a where a.record_id =(select c.record_id from customers AS c where a.id = c.id order by c.record_id DESC LIMIT 1) and username=%s',(username1))
    collect_new_username6 = cur.fetchall()
    for username6 in collect_new_username6:
        for value in username6.values():
            show_cus_cell_list.append(value)
            all_cus_info_list.append(value)

    cur.execute('SELECT email FROM customers as a where a.record_id =(select c.record_id from customers AS c where a.id = c.id order by c.record_id DESC LIMIT 1) and username=%s',(username1))
    collect_new_username7 = cur.fetchall()
    for username7 in collect_new_username7:
        for value in username7.values():
            show_cus_email_list.append(value)
            all_cus_info_list.append(value)

    cur.execute('SELECT password FROM customers as a where a.record_id =(select c.record_id from customers AS c where a.id = c.id order by c.record_id DESC LIMIT 1) and username=%s',(username1))
    collect_new_username8 = cur.fetchall()
    for username8 in collect_new_username8:
        for value in username8.values():
            show_cus_password_list.append("●●●●●●")
            all_cus_info_list.append("●●●●●●")

    cur.execute('SELECT username FROM customers as a where a.record_id =(select c.record_id from customers AS c where a.id = c.id order by c.record_id DESC LIMIT 1) and username=%s',(username1))
    collect_new_username11 = cur.fetchall()
    for username11 in collect_new_username11:
        for value in username11.values():
            all_cus_info_list.append(value)
    print ("--------------------------------------------------------")
    print ("●会員情報●")
    for index, (a, b, c, d, e, f) in enumerate(zip(show_cus_name_list,show_cus_postcode_list,show_cus_address_list,show_cus_cell_list,show_cus_email_list,show_cus_password_list)):
        print("1: 名前：",a,"\n2: 郵便番号：",b,"\n3: 住所：",c,"\n4: 電話番号：",str(d),"\n5: Email：",e,"\n6: パスワード：", f)
    show_cus_id_list.clear()
    show_cus_name_list.clear()
    show_cus_postcode_list.clear()
    show_cus_address_list.clear()
    show_cus_cell_list.clear()
    show_cus_email_list.clear()
    show_cus_password_list.clear()

    cur.close()

def show_list(show_cus_info):
    return all_cus_info_list

def mod_cus_info(show_list):
    show_list2 = show_list(show_cus_info)
    print ("--------------------------------------------------------")
    print("●会員情報編集●")
    print("編集する内容を選んでください")
    print("「#」を入力、エンターで前画面へ戻る")
    mod_cus = error5()

    if mod_cus == "#" or mod_cus == "＃":
        home()

    elif mod_cus == 1:
        while True:
            print("変更内容を入力してください")
            mod1 = input("氏名（45文字以内）")
            if mod1 == "#" or mod1 == "＃":
                home()
            while True:
                if mod1.isdecimal() == True:
                    print ("文字列で入力してください。")
                    print ("--------------------------------------------------------")
                    mod1 = input("氏名（45文字以内）：")
                    if mod1 == "#" or mod1 == "＃":
                        home()
                elif len(mod1)> 33:
                    print("長すぎです。32文字以内で入力してください。")
                    print ("--------------------------------------------------------")
                    mod1 = input("氏名（45文字以内）：")
                    if mod1 == "#" or mod1 == "＃":
                        home()
                elif len(mod1)< 2:
                    print("苗字とお名前を入力してください。")
                    print ("--------------------------------------------------------")
                    mod1 = input("氏名（45文字以内）：")
                    if mod1 == "#" or mod1 == "＃":
                        home()
                else:
                    break
            print ("--------------------------------------------------------")
            print("氏名（45文字以内）：", mod1)
            print("この内容で確定する場合は１を、変更前に戻す場合は２を入力してください")
            input2 = error1()

            if input2 == 1:
                add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                new_customers_list = [
                    (show_list2[0], mod1, int(show_list2[2]), show_list2[3], str(show_list2[4]), show_list2[5], show_list2[6], show_list2[7])
                ]
                cur = conn.cursor()
                for new_cus in new_customers_list:
                    cur.execute(add_customers, new_cus)
                cur.execute('UPDATE customers set id = record_id where id = 0')
                break
            if input2 == 2:
                mod_cus_info(show_list)

    elif mod_cus == 2:
        while True:
            print("変更内容を入力してください")
            str_mod2 = input("郵便番号（7桁数値）：")
            if str_mod2 == "#" or str_mod2 == "＃":
                home()
            while True:
                if str_mod2.isdecimal() == False:
                    print ("数字で入力してください。")
                    str_mod2 = input("郵便番号（7桁数値）：")
                    if str_mod2 == "#" or str_mod2 == "＃":
                        home()
                elif len(str_mod2) != 7:
                    print("7文字で入力してください。")
                    print ("--------------------------------------------------------")
                    str_mod2 = input("郵便番号（7桁数値）：")
                    if str_mod2 == "#" or str_mod2 == "＃":
                        home()
                else:
                    mod2 = int(str_mod2)
                    break
            print ("--------------------------------------------------------")
            print("郵便番号（7桁数値）：", mod2)
            print("この内容で確定する場合は１を、変更前に戻す場合は２を入力してください")
            input2 = error1()
            if input2 == 1:
                add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                new_customers_list = [
                    (show_list2[0], show_list2[1], int(mod2), show_list2[3], str(show_list2[4]), show_list2[5], show_list2[6], show_list2[7])
                ]

                cur = conn.cursor()
                for new_cus in new_customers_list:
                    cur.execute(add_customers, new_cus)
                cur.execute('UPDATE customers set id = record_id where id = 0')
                cur.close()
                break
            if input2 == 2:
                mod_cus_info(show_list)

    elif mod_cus == 3:
        while True:
            print("変更内容を入力してください")
            mod3 = input("住所（45文字以内）：")
            if mod3 == "#" or mod3 == "＃":
                home()
            while True:
                if len(mod3)> 50:
                    print("長すぎです。50文字以内で入力してください。")
                    print ("--------------------------------------------------------")
                    mod3 = input("住所（45文字以内）：")
                    if mod3 == "#" or mod3 == "＃":
                        home()
                if len(mod3)< 5:
                    print("お届け先の住所を入力してください。")
                    print ("--------------------------------------------------------")
                    mod3 = input("住所（45文字以内）：")
                    if mod3 == "#" or mod3 == "＃":
                        home()
                else:
                    break
            print ("--------------------------------------------------------")
            print("住所（45文字以内）：", mod3)
            print("この内容で確定する場合は１を、変更前に戻す場合は２を入力してください")
            input2 = error1()
            if input2 == 1:
                add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                new_customers_list = [
                    (show_list2[0], show_list2[1], int(show_list2[2]), mod3, str(show_list2[4]), show_list2[5], show_list2[6], show_list2[7])
                ]

                cur = conn.cursor()
                for new_cus in new_customers_list:
                    cur.execute(add_customers, new_cus)
                cur.execute('UPDATE customers set id = record_id where id = 0')
                cur.close()
                break
            if input2 == 2:
                mod_cus_info(show_list)

    elif mod_cus == 4:
        while True:
            print("変更内容を入力してください")
            mod4 = input("電話番号（10,11桁数値）：")
            if mod4 == "#" or mod4 == "＃":
                home()
            while True:
                if mod4.isdecimal() == False:
                    print ("数字で入力してください。")
                    print ("--------------------------------------------------------")
                    mod4 = input("電話番号（10,11桁数値）：")
                    if mod4 == "#" or mod4 == "＃":
                        home()
                elif len(mod4) == 10 or len(mod4) == 11:
                    break
                else:
                    print("10or11桁で入力してください。")
                    print ("--------------------------------------------------------")
                    mod4 = input("電話番号（10,11桁数値）：")
                    if mod4 == "#" or mod4 == "＃":
                        home()

            print ("--------------------------------------------------------")
            print("電話番号（10,11桁数値）：", mod4)
            print("この内容で確定する場合は１を、変更前に戻す場合は２を入力してください")
            input2 = error1()
            if input2 == 1:
                add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                new_customers_list = [
                    (show_list2[0], show_list2[1], int(show_list2[2]), show_list2[3], str(mod4), show_list2[5], show_list2[6], show_list2[7])
                ]

                cur = conn.cursor()
                for new_cus in new_customers_list:
                    cur.execute(add_customers, new_cus)
                cur.execute('UPDATE customers set id = record_id where id = 0')
                cur.close()
                break
            if input2 == 2:
                mod_cus_info(show_list)

    elif mod_cus == 5:
        while True:
            print("変更内容を入力してください")
            mod5 = input("入力：")
            if mod5 == "#" or mod5 == "＃":
                home()
            while True:
                if len(mod5)> 65:
                    print("長すぎです。64文字以内で入力してください。")
                    print ("--------------------------------------------------------")
                    mod5 = input("メールアドレス（45文字英数字記号）：")
                    if mod5 == "#" or mod5 == "＃":
                        home()
                elif re.match(r'[a-z\d._]+@[a-z]+\.[a-z]+', mod5):
                    break
                else:
                    print("正しいメールアドレスを入力してください。")
                    print ("--------------------------------------------------------")
                    mod5 = input("メールアドレス（45文字英数字記号）：")
                    if mod5 == "#" or mod5 == "＃":
                        home()

            print ("--------------------------------------------------------")
            print("メールアドレス（45文字英数字記号）：", mod5)
            print("この内容で確定する場合は１を、変更前に戻す場合は２を入力してください")
            input2 = error1()

            if input2 == 1:
                add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                new_customers_list = [
                    (show_list2[0], show_list2[1], int(show_list2[2]), show_list2[3], str(show_list2[4]), mod5, show_list2[6], show_list2[7])
                ]
                cur = conn.cursor()
                for new_cus in new_customers_list:
                    cur.execute(add_customers, new_cus)
                cur.execute('UPDATE customers set id = record_id where id = 0')
                cur.close()
                break
            if input2 == 2:
                mod_cus_info(show_list)

    elif mod_cus == 6:
        print("変更内容を入力してください")
        mod6 = input("パスワード（8桁以上45桁以下英数字）：")
        if mod6 == "#" or mod6 == "＃":
            home()
        while True:
            p = re.compile('[a-zA-Z0-9]+')
            if len(mod6)> 33:
                print("長すぎです。32桁以内の大文字小文字英語か数字で入力してください。")
                print ("--------------------------------------------------------")
                mod6 = input("パスワード（8桁以上45桁以下英数字）：")
                if mod6 == "#" or mod6 == "＃":
                    home()
            if len(mod6)<8:
                print("短すぎです。8桁以上の大文字小文字英語か数字で入力してください。")
                print ("--------------------------------------------------------")
                mod6 = input("パスワード（8桁以上45桁以下英数字）：")
                if mod6 == "#" or mod6 == "＃":
                    home()
            elif re.search(r'[a-zA-Z0-9]+', mod6):
                break
            else:
                print("正しいパスワードを入力してください。")
                print ("--------------------------------------------------------")
                mod6 = input("パスワード（8桁以上45桁以下英数字）：")
                if mod6 == "#" or mod6 == "＃":
                    home()

            print ("--------------------------------------------------------")
            print("メールアドレス（45文字英数字記号）：", mod6)
            print("この内容で確定する場合は１を、変更前に戻す場合は２を入力してください")
            input2 = error1()
            if input2 == 1:
                add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                new_customers_list = [
                    (show_list2[0], show_list2[1], int(show_list2[2]), show_list2[3], str(show_list2[4]), show_list2[5], mod6, show_list2[7])
                ]
                cur = conn.cursor()
                for new_cus in new_customers_list:
                    cur.execute(add_customers, new_cus)
                cur.execute('UPDATE customers set id = record_id where id = 0')
                cur.close()
                break
            if input2 == 2:
                mod_cus_info(show_list)

    show_list2.clear()

    conn.commit()

def mod_cus_info_output1(error1):
    print ("--------------------------------------------------------")
    print("編集は1を、HOMEに戻る場合は2を入力してください")
    error_input3 = error1()
    if error_input3 == 1:
        mod_cus_info(show_list)
        show_cus_info (login_input)
        mod_cus_info_output1(error1)

    elif error_input3 == 2:
        home()

def purchase_history():
    print ("--------------------------------------------------------")
    print("●購入履歴●")
    cur = conn.cursor()
    cur.execute('SELECT id FROM view_customers where username = (%s)', (username_list[0]))
    collect_order_cus_info = cur.fetchall()

    for collect_order_cus_info1 in collect_order_cus_info:
        for value in collect_order_cus_info1.values():
            cus_id_list.append(value)


    cur.execute('SELECT id, order_date, total, payment, delivered,cancel,cancel_ID FROM order_info where customer_id=(%s)', (cus_id_list[0]))
    collect_order_cus_info = cur.fetchall()

    print("受注ID　購入日     　　　　　　　税込合計　入金済み　出荷済　ｷｬﾝｾﾙ　ｷｬﾝｾﾙ前ID")
    for i in collect_order_cus_info:#受注IDの取り出し
        purchase_list = []
        for j in i.values():#リストにIDを追加
            purchase_list.append(j)
        purchaseid = purchase_list[0]
        purchase_id_list.append(purchaseid)


        print(purchase_list[0],"　　", purchase_list[1],"　", purchase_list[2],"円"," 　", purchase_list[3],"　", purchase_list[4], "　",purchase_list[5], "　",purchase_list[6], end = '\n')

def purchase_detail():
    print ("--------------------------------------------------------")
    print("受注詳細を検索します。受注IDを入力してください")
    print("「#」を入力、エンターで前画面へ戻る")
    str_ask_purchase_id = input("入力")
    while True:
        if str_ask_purchase_id == "#" or str_ask_purchase_id == "＃":
            home()
        elif str_ask_purchase_id.isdecimal() == False:
            print ("数字で入力してください")
            str_ask_purchase_id = input("受注IDを入力してください")
        else:
            ask_purchase_id = int(str_ask_purchase_id)
            if ask_purchase_id not in purchase_id_list:
                print("正しい受注IDを入力してください")
                str_ask_purchase_id = input("受注IDを入力してください")
            else:
                break
    print("\n")
    cur = conn.cursor()
    cur.execute('SELECT * FROM order_detail where order_id=(%s)', (ask_purchase_id))
    collect_order_cus_info1 = cur.fetchall()
    print("受注詳細ID　　ｶﾃｺﾞﾘID　商品ID　個数　　商品価格　小計金額　商品名")
    for i in collect_order_cus_info1:#受注IDの取り出し
        purchase_detail_list = []
        for j in i.values():#リストにIDを追加
            purchase_detail_list.append(j)
        purchaseid1 = purchase_detail_list[0]

        print(purchase_detail_list[0],"　　　　　", purchase_detail_list[2],"　　", purchase_detail_list[3],"　　　", purchase_detail_list[5], "　　", purchase_detail_list[6],"円", "　",purchase_detail_list[7],"円", "　",purchase_detail_list[4], end = '\n')

def cancel_info():
    print ("--------------------------------------------------------")
    print("●お問い合わせ情報●")
    print("・通常キャンセル / 変更")
    print("通常は、発送前のみキャンセル交換可能です。")
    print("\n")
    print("・不良品返品 / 交換")
    print("不良品の場合のみ、発送後の返品交換に対応いたします。")
    print("お手数ではございますが、メールにて商品の現業を映した写真を")
    print("添付していただくようお願いいたします。")
    print("返品配送に関する情報を追って連絡いたします。")
    print("\n")
    print("・VVメールアドレス")
    print("キャンセル / 返品 / 交換に関する連絡はこちら")
    print("ccshouten_cancel@vv.com")

def order_total_price():
    count = 0
    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            count += 1

    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        if count > 0:
            order_line1 = f.readlines()[0]
        else:
            order_line1 = '0 - 0 - 0 円  - 個数 0 - 在庫 0 - 0'

    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        if count > 1:
            order_line2 = f.readlines()[1]
        else:
            order_line2 = '0 - 0 - 0 円  - 個数 0 - 在庫 0 - 0'

    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        if count > 2:
            order_line3 = f.readlines()[2]
        else:
            order_line3 = '0 - 0 - 0 円  - 個数 0 - 在庫 0 - 0'

    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        if count > 3:
            order_line4 = f.readlines()[3]
        else:
            order_line4 = '0 - 0 - 0 円  - 個数 0 - 在庫 0 - 0'

    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        if count > 4:
            order_line5 = f.readlines()[4]
        else:
            order_line5 = '0 - 0 - 0 円  - 個数 0 - 在庫 0 - 0'

    #行のデータを分解してリスト化
    order_list1 = order_line1.split()
    order_list2 = order_line2.split()
    order_list3 = order_line3.split()
    order_list4 = order_line4.split()
    order_list5 = order_line5.split()

    #リスト内から必要な要素を取得
    if len(order_list1) > 0:
        a = int(order_list1[4])
        a_num = int(order_list1[8])
    else:
        a = 0
        a_num = 0

    if len(order_list2) > 0:
        b = int(order_list2[4])
        b_num = int(order_list2[8])
    else:
        b = 0
        b_num = 0

    if len(order_list3) > 0:
        c = int(order_list3[4])
        c_num = int(order_list3[8])
    else:
        c = 0
        c_num = 0

    if len(order_list4) > 0:
        d = int(order_list4[4])
        d_num = int(order_list4[8])
    else:
        d = 0
        d_num = 0

    if len(order_list5) > 0:
        e = int(order_list5[4])
        e_num = int(order_list5[8])
    else:
        e = 0
        e_num = 0

    #個数×値段
    numprice = a*a_num + b*b_num + c*c_num + d*d_num + e*e_num

    shipping_fee_list = []
    #配送料
    if numprice >= 10000:
        cur = conn.cursor()
        cur.execute('SELECT fee_taxed,id FROM shipping_fee where name=(%s)', ("10000円以上"))
        collect_shipping_fee1 = cur.fetchall()
        for shipping_fee1 in collect_shipping_fee1:
            for value in shipping_fee1.values():
                shipping_fee_list.append(value)

    if numprice < 10000:
        cur = conn.cursor()
        cur.execute('SELECT fee_taxed,id FROM shipping_fee where name=(%s)', ("10000円未満"))
        collect_shipping_fee2 = cur.fetchall()
        for shipping_fee2 in collect_shipping_fee2:
            for value in shipping_fee2.values():
                shipping_fee_list.append(value)


    #送料＋合計
    print("合計金額：", numprice, "円")
    print("配送料：", shipping_fee_list[0], "円")
    print("_________________")
    print("合計：", numprice + shipping_fee_list[0], "円")


    l = numprice
    m = shipping_fee_list[0]
    n = numprice + shipping_fee_list[0]

    list.append(l)
    list.append(m)
    list.append(n)

def order_cus_info():
    cur = conn.cursor()
    cur.execute('SELECT name, postcode, address, cell, id FROM view_customers where username=(%s)', (username_list[0]))
    collect_order_cus_info = cur.fetchall()

    for collect_order_cus_info1 in collect_order_cus_info:
        for value in collect_order_cus_info1.values():
            order_cus_info_list.append(value)


    print(order_cus_info_list[0],"様")
    print("TEL",order_cus_info_list[3])
    print("〒",order_cus_info_list[1], " ",order_cus_info_list[2])

def register():
    register_list = [0]
    cart = 'shopping_cart.txt'
    with open(cart, 'r', encoding='utf-8') as q:
        for s_line in q:
            register_list.append(s_line)

    register_length = len(register_list)
    if register_list[register_length - 1] == 0:
        print("\n")
        print("カートが空です")
        register_list.clear()
        home()
    else:
        print("●レジ：カート内商品確定●")
        show_cart()
        print ("\n")
        print ("カート内商品を確定し、お届け先の確認をする場合には１を、Homeに戻る場合には２を入力してください")
        error_input1 = error1()
        if error_input1 == 1:
            print ("--------------------------------------------------------")
            print("●レジ：お届け先確定●")
            print("お届けする宛先は以下の通りです。")
            order_cus_info()
            print ("\n")
            print("お届け先を確定し、注文を確定する場合は１を、お届け先を変更する場合は2を入力し、Home画面から会員情報の編集へ進んでください")
            error_input2 = error1()
            if error_input2 == 1:
                print ("--------------------------------------------------------")
                print("●レジ：注文確定●")
                order_total_price()
                print("\n")
                print("注文を確定した後には、サイトから注文内容を変更することはできません。注文確定後のキャンセルは、サイト上の「お問い合わせ情報」をご一読の上ご連絡ください")
                print("注文を確定する場合は１を、Homeに戻る場合は２を入力してください")
                error_input1 = error1()
                if error_input1 == 1:
                    print ("--------------------------------------------------------")
                    print("注文確定しました")


                else:
                    home()
            else:
                home()

        else:
            home()

def creat_invoice():
    now = datetime.datetime.now()
    now1 = r'\BILL_{0:%Y%m%d%H%M%S}'.format(now)+'.txt'
    YMD = '{0:%Y}'.format(now) + '年' + '{0:%m}'.format(now) + '月' + '{0:%d}'.format(now) + '日'

    file = os.path.abspath("BILL")
    now2 = file + now1

    invoice_line1 = '●請求書●　　（発行日'+ YMD + ')'

    cart = 'shopping_cart.txt'
    with open(cart, 'r', encoding='utf-8') as q:
        n = 0
        for s_line in q:
            aaa = s_line.replace("\n", "")
            list2.append(aaa)

    count = 0
    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            count += 1

    f = open(now2, 'w', encoding='utf-8')
    f.write(invoice_line1)
    f.write("\n")
    f.write("----------------------------")
    f.write("\n")
    f.write("会員番号：")
    f.write(str(order_cus_info_list[4]))
    f.write("\n")
    f.write(str(order_cus_info_list[0]))
    f.write("様")
    f.write("\n")
    f.write("〒")
    f.write(str(order_cus_info_list[1]))
    f.write("\n")
    f.write(str(order_cus_info_list[2]))
    f.write("\n")
    f.write("TEL")
    f.write(str(order_cus_info_list[3]))
    f.write("\n")
    f.write("----------------------------")
    f.write("\n")
    f.write("ご請求金額")
    f.write(str(list[2]))
    f.write("円")
    f.write("\n")
    f.write("----------------------------")
    f.write("\n")
    f.write("詳細")
    f.write("\n")
    f.write("\n")
    f.write("ｶﾃｺﾞﾘ - ID - 単価 - 個数 - 商品名")
    f.write("\n")
    if count > 0:
        f.write(str(list2[0]))
        f.write("\n")
    if count > 1:
        f.write(str(list2[1]))
        f.write("\n")
    if count > 2:
        f.write(str(list2[2]))
        f.write("\n")
    if count > 3:
        f.write(str(list2[3]))
        f.write("\n")
    if count > 4:
        f.write(str(list2[4]))
        f.write("\n")
    f.write("----------------------------")
    f.write("\n")
    f.write("小計：")
    f.write(str(list[0]))
    f.write("円")
    f.write("\n")
    f.write("送料：")
    f.write(str(list[1]))
    f.write("円")
    f.write("\n")
    f.write("合計：")
    f.write(str(list[2]))
    f.write("円")
    f.write("\n")
    f.write("----------------------------")
    f.write("\n")
    f.write("振込先")
    f.write("\n")
    f.write("赤坂銀行　赤坂支店　普通　口座番号：１２３１２３１　口座名義：ブイブイショウテン")
    f.write("\n")

    f.close()

def insert_order_info():

    count = 0
    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            count += 1

    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        if count > 0:
            order_line1 = f.readlines()[0]
        else:
            order_line1 = '0 - 0 - 0 円  - 個数 0 - 在庫 0 - 0'

    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        if count > 1:
            order_line2 = f.readlines()[1]
        else:
            order_line2 = '0 - 0 - 0 円  - 個数 0 - 在庫 0 - 0'

    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        if count > 2:
            order_line3 = f.readlines()[2]
        else:
            order_line3 = '0 - 0 - 0 円  - 個数 0 - 在庫 0 - 0'

    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        if count > 3:
            order_line4 = f.readlines()[3]
        else:
            order_line4 = '0 - 0 - 0 円  - 個数 0 - 在庫 0 - 0'

    with open('shopping_cart.txt', mode='rt', encoding='utf-8') as f:
        if count > 4:
            order_line5 = f.readlines()[4]
        else:
            order_line5 = '0 - 0 - 0 円  - 個数 0 - 在庫 0 - 0'

    #行のデータを分解してリスト化
    order_list1 = order_line1.split()
    order_list2 = order_line2.split()
    order_list3 = order_line3.split()
    order_list4 = order_line4.split()
    order_list5 = order_line5.split()

    #リスト内から必要な要素を取得
    if len(order_list1) > 0:
        order_cat1 = order_list1[0]
        order_id1 = int(order_list1[2])
        order_price1 = int(order_list1[4])
        order_num1 = int(order_list1[8])

    else:
        order_cat1 = "AA"
        order_id1 = 0
        order_price1 = 0
        order_num1 = 0

    if len(order_list2) > 0:
        order_cat2 = order_list2[0]
        order_id2 = int(order_list2[2])
        order_price2 = int(order_list2[4])
        order_num2 = int(order_list2[8])
    else:
        order_cat2 = "AA"
        order_id2 = 0
        order_price2 = 0
        order_num2 = 0

    if len(order_list3) > 0:
        order_cat3 = order_list3[0]
        order_id3 = int(order_list3[2])
        order_price3 = int(order_list3[4])
        order_num3 = int(order_list3[8])
    else:
        order_cat3 = "AA"
        order_id3 = 0
        order_price3 = 0
        order_num3 = 0

    if len(order_list4) > 0:
        order_cat4 = order_list4[0]
        order_id4 = int(order_list4[2])
        order_price4 = int(order_list4[4])
        order_num4 = int(order_list4[8])
    else:
        order_cat4 = "AA"
        order_id4 = 0
        order_price4 = 0
        order_num4 = 0

    if len(order_list5) > 0:
        order_cat5 = order_list5[0]
        order_id5 = int(order_list5[2])
        order_price5 = int(order_list5[4])
        order_num5 = int(order_list5[8])
    else:
        order_cat5 = "AA"
        order_id5 = 0
        order_price5 = 0
        order_num5 = 0


    #個数×値段
    numprice = order_price1*order_num1 + order_price2*order_num2 + order_price5*order_num3 + order_price4*order_num4 + order_price5*order_num5


    #配送料
    if numprice >= 10000:
        cur = conn.cursor()
        cur.execute('SELECT fee FROM shipping_fee where name=(%s)', ("10000円以上"))
        collect_shipping_fee1 = cur.fetchall()

        for shipping_fee1 in collect_shipping_fee1:
            for value in shipping_fee1.values():
                shipping_fee_list.append(value)

    if numprice < 10000:
        cur = conn.cursor()
        cur.execute('SELECT fee, id FROM shipping_fee where name=(%s)', ("10000円未満"))
        collect_shipping_fee2 = cur.fetchall()

        for shipping_fee2 in collect_shipping_fee2:
            for value in shipping_fee2.values():
                shipping_fee_list.append(value)


    #送料＋合計
    l = numprice
    m = shipping_fee_list[0]
    n = numprice + shipping_fee_list[0]


    cur.execute('SELECT id FROM view_customers where username=(%s)', (username_list[0]))
    order_cus_id = cur.fetchall()
    for cus_id in order_cus_id:
        for value in cus_id.values():
            order_cus_id_list.append(value)

    now = datetime.datetime.now()
    now1 = '{0:%Y%m%d%H%M%S}'.format(now)
    YMD = '{0:%Y}'.format(now) + '年' + '{0:%m}'.format(now) + '月' + '{0:%d}'.format(now) + '日' + '{0:%H}'.format(now) + '時' + '{0:%M}'.format(now) + '分'


    list.append(l)
    list.append(m)
    list.append(n)

    #order_info追加
    add_order_info = "INSERT INTO order_info(customer_id,shipping_id, order_date, taxed_total,total) values(%s,%s,%s,%s,%s)"

    add_order_info_list = [
        (order_cus_id_list[0], shipping_fee_list[1], YMD, l, n)
    ]
    for new_order in add_order_info_list:
        cur.execute(add_order_info, new_order)
    conn.commit()

    #order_infoからIDを選ぶ
    order_id_list.clear()
    cur.execute('SELECT id FROM order_info where id=(SELECT MAX(id) FROM order_info)')
    order_id = cur.fetchall()
    for cus_order_id in order_id:
        for value in cus_order_id.values():
            order_id_list.append(value)

    #order_infoからItem_nameを選ぶ
    cur.execute('SELECT item_name, storage FROM view_items where id=(%s) and cg_abb=(%s)', (order_id1, order_cat1))
    order_item_name1 = cur.fetchall()
    for cus_order_id in order_item_name1:
        for value in cus_order_id.values():
            order_item_name1_list.append(value)

    cur.execute('SELECT item_name, storage FROM view_items where id=(%s) and cg_abb=(%s)', (order_id2, order_cat2))
    order_item_name2 = cur.fetchall()
    for cus_order_id in order_item_name2:
        for value in cus_order_id.values():
            order_item_name2_list.append(value)

    cur.execute('SELECT item_name, storage FROM view_items where id=(%s) and cg_abb=(%s)', (order_id3, order_cat3))
    order_item_name3 = cur.fetchall()
    for cus_order_id in order_item_name3:
        for value in cus_order_id.values():
            order_item_name3_list.append(value)

    cur.execute('SELECT item_name, storage FROM view_items where id=(%s) and cg_abb=(%s)', (order_id4, order_cat4))
    order_item_name4 = cur.fetchall()
    for cus_order_id in order_item_name4:
        for value in cus_order_id.values():
            order_item_name4_list.append(value)

    cur.execute('SELECT item_name, storage FROM view_items where id=(%s) and cg_abb=(%s)', (order_id5, order_cat5))
    order_item_name5 = cur.fetchall()
    for cus_order_id in order_item_name5:
        for value in cus_order_id.values():
            order_item_name5_list.append(value)


    idx01 = len(order_item_name1_list)
    idx02 = len(order_item_name2_list)
    idx03 = len(order_item_name3_list)
    idx04 = len(order_item_name4_list)
    idx05 = len(order_item_name5_list)


    #在庫調整
    if order_list1[0] != "0":
        order_item_storage1 = order_item_name1_list[idx01 - 1]
        cur = conn.cursor()
        left_storage = order_item_storage1 - order_num1
        cur.execute('UPDATE items set storage=%s WHERE id=%s', (left_storage, order_id1))
        conn.commit()
        cur = conn.cursor()
        left_storage_info1 = "INSERT INTO storage(item_id, fluctuation, out_s) values(%s,%s,%s)"
        minus_storage1 =  - + order_num1
        minus_storage_list1 = [
            (order_id1, minus_storage1, 1)
        ]
        for new_order1 in minus_storage_list1:
            cur.execute(left_storage_info1, new_order1)
        conn.commit()

    if order_list2[0] != "0":
        order_item_storage2 = order_item_name2_list[idx02 - 1]
        cur = conn.cursor()
        left_storage = order_item_storage2 - order_num2
        cur.execute('UPDATE items set storage=%s WHERE id=%s', (left_storage, order_id2))
        conn.commit()
        cur = conn.cursor()
        left_storage_info2 = "INSERT INTO storage(item_id, fluctuation, out_s) values(%s,%s,%s)"
        minus_storage2 =  - + order_num2
        minus_storage_list2 = [
            (order_id2, minus_storage2, 1)
        ]
        for new_order2 in minus_storage_list2:
            cur.execute(left_storage_info2, new_order2)
        conn.commit()

        if order_list3[0] != "0":
            order_item_storage3 = order_item_name3_list[idx03 - 1]
            cur = conn.cursor()
            left_storage = order_item_storage3 - order_num3
            cur.execute('UPDATE items set storage=%s WHERE id=%s', (left_storage, order_id3))
            conn.commit()
            cur = conn.cursor()
            left_storage_info3 = "INSERT INTO storage(item_id, fluctuation, out_s) values(%s,%s,%s)"
            minus_storage3 =  - + order_num3
            minus_storage_list3 = [
                (order_id3, minus_storage3, 1)
            ]
            for new_order3 in minus_storage_list3:
                cur.execute(left_storage_info3, new_order3)
            conn.commit()

        if order_list4[0] != "0":
            order_item_storage4 = order_item_name4_list[idx04 - 1]
            cur = conn.cursor()
            left_storage = order_item_storage4 - order_num4
            cur.execute('UPDATE items set storage=%s WHERE id=%s', (left_storage, order_id4))
            conn.commit()
            cur = conn.cursor()
            left_storage_info4 = "INSERT INTO storage(item_id, fluctuation, out_s) values(%s,%s,%s)"
            minus_storage4 =  - + order_num4
            minus_storage_list4 = [
                (order_id4, minus_storage4, 1)
            ]
            for new_order4 in minus_storage_list4:
                cur.execute(left_storage_info4, new_order4)
            conn.commit()

        if order_list5[0] != "0":
            order_item_storage5 = order_item_name5_list[idx05 - 1]
            cur = conn.cursor()
            left_storage = order_item_storage5 - order_num5
            cur.execute('UPDATE items set storage=%s WHERE id=%s', (left_storage, order_id5))
            conn.commit()
            cur = conn.cursor()
            left_storage_info5 = "INSERT INTO storage(item_id, fluctuation, out_s) values(%s,%s,%s)"
            minus_storage5 =  - + order_num5
            minus_storage_list5 = [
                (order_id5, minus_storage5, 1)
            ]
            for new_order5 in minus_storage_list5:
                cur.execute(left_storage_info5, new_order5)
            conn.commit()


    #order_detailからIDを選ぶ

    if order_list1[0] != "0":
        order_sum1 = order_price1*order_num1
        add_order_info = "INSERT INTO order_detail(order_id, item_cg, item_id, item_name, item_sum, item_price, item_num) values(%s,%s,%s,%s,%s,%s,%s)"
        add_order_info_list1 = [
            (order_id_list[0], order_cat1, order_id1, order_item_name1_list[idx01 - 2], order_sum1, order_price1, order_num1)
        ]
        for new_order1 in add_order_info_list1:
            cur.execute(add_order_info, new_order1)
        conn.commit()

    if order_list2[0] != "0":
        order_sum2 = order_price2*order_num2
        add_order_info = "INSERT INTO order_detail(order_id,item_cg, item_id, item_name, item_sum, item_price, item_num) values(%s,%s,%s,%s,%s,%s,%s)"
        add_order_info_list = [
            (order_id_list[0], order_cat2, order_id2, order_item_name2_list[idx02 - 2], order_sum2, order_price2, order_num2)
        ]
        for new_order in add_order_info_list:
            cur.execute(add_order_info, new_order)
        conn.commit()

    if order_list3[0] != "0":
        order_sum3 = order_price3*order_num3
        add_order_info = "INSERT INTO order_detail(order_id,item_cg, item_id, item_name, item_sum, item_price, item_num) values(%s,%s,%s,%s,%s,%s,%s)"
        add_order_info_list = [
            (order_id_list[0], order_cat3, order_id3, order_item_name3_list[idx03 - 2], order_sum3, order_price3, order_num3)
        ]
        for new_order in add_order_info_list:
            cur.execute(add_order_info, new_order)
        conn.commit()

    if order_list4[0] != "0":
        order_sum4 = order_price4*order_num4
        add_order_info = "INSERT INTO order_detail(order_id,item_cg, item_id, item_name, item_sum, item_price, item_num) values(%s,%s,%s,%s,%s,%s,%s)"
        add_order_info_list = [
            (order_id_list[0], order_cat4, order_id4, order_item_name4_list[idx04 - 2], order_sum4, order_price4, order_num4)
        ]
        for new_order in add_order_info_list:
            cur.execute(add_order_info, new_order)
        conn.commit()

    if order_list5[0] != "0":
        order_sum5 = order_price5*order_num5
        add_order_info = "INSERT INTO order_detail(order_id,item_cg, item_id, item_name, item_sum, item_price, item_num) values(%s,%s,%s,%s,%s,%s,%s)"
        add_order_info_list1 = [
            (order_id_list[0], order_cat5, order_id5, order_item_name5_list[idx05 - 2], order_sum5, order_price5, order_num5)
        ]
        for new_order in add_order_info_list1:
            cur.execute(add_order_info, new_order)
        conn.commit()

def finish_system():
    print ("--------------------------------------------------------")
    print("●システム終了●")
    print("1: システムを終了します")
    print("2: Home")
    print("\n")
    print("システムを終了する場合、カート内の商品はリセットされます")

    finish_system_input = error1()
    if finish_system_input == 1:
        print ("--------------------------------------------------------")
        print("●ご利用ありがとうございました●")
        print("\n")
        print("またのご利用お待ちしております")
        print("VV商店")
        clear_cart()
        import sys
        sys.exit()
    elif finish_system_input == 2:
        home()

def clear_cart():
    with open('shopping_cart.txt', mode='w', encoding='utf-8'):
        pass

def home():
    print ("--------------------------------------------------------")
    print("●ＨＯＭＥ●")
    print("1: 商品検索")
    print("2: 商品選択")
    print("3: カート")
    print("4: 会員情報")
    print("5: 購入履歴")
    print("6: お問い合わせ情報")
    print("7: 購入終了")
    print ("--------------------------------------------------------")

    print("お進みいただく項目の選択をお願いします")
    home_input = error6()
    if home_input == 1:
        show_search_items(show_item_cg, search_items)

    elif home_input == 2:
        con_shopping()

    elif home_input == 3:
        register()
        creat_invoice()
        insert_order_info()
        clear_cart()
        home()

    elif home_input == 4:
        show_cus_info (login_input)
        show_list1 = show_list(show_cus_info)
        mod_cus_info_output1(error1)

    elif home_input == 5:
        purchase_history()
        purchase_detail()

        print ("--------------------------------------------------------")
        print("受注詳細をさらに展開したい場合は１を、Homeに戻る場合は２を入力してください")
        purchase_detail_input = error1()
        while True:
            if purchase_detail_input == 1:
                purchase_detail()
                print ("--------------------------------------------------------")
                print("受注詳細をさらに展開したい場合は１を、Homeに戻る場合は２を入力してください")
                purchase_detail_input = error1()
            else:
                home()
                break
                cus_id_list.clear()
                purchase_list.clear()
                purchase_detail_list.clear()
                purchase_id_list.clear()


    elif home_input == 6:
        cancel_info()
        home()
    elif home_input == 7:
        finish_system()

def first_screen():
    clear_cart()
    print ("--------------------------------------------------------")
    print ("ログイン画面へ進むには１を\n新規登録画面へ進むには２を入力してください")
    print("\n")
    error_input1 = error1()
    output1(error_input1, login, add_customers)
    show_cus_name (login_input)
    home()


print ("--------------------------------------------------------")
print ("★ようこそ、VV商店へ★")

first_screen()
home()
