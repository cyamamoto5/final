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


def add_customers (error1):
    name = input("氏名：")
    while True:
        if name.isdecimal() == True:
            print ("文字列で入力してください。")
            print ("--------------")
            name = input("氏名：")
        elif len(name)> 33:
            print("長すぎです。32文字以内で入力してください。")
            print ("--------------")
            name = input("氏名：")
        elif len(name)< 2:
            print("苗字とお名前を入力してください。")
            print ("--------------")
            name = input("氏名：")
        else:
            break

    postcode_str = input("郵便番号：")
    while True:
        if postcode_str.isdecimal() == False:
            print ("数字で入力してください。")
            postcode_str = input("郵便番号：")
        elif len(postcode_str) != 7:
            print("7文字で入力してください。")
            print ("--------------")
            postcode_str = input("郵便番号：")
        else:
            postcode = int(postcode_str)
            break

    address = input("住所：")
    while True:
        if len(address)> 50:
            print("長すぎです。50文字以内で入力してください。")
            print ("--------------")
            address = input("住所：")
        if len(address)< 5:
            print("お届け先の住所を入力してください。")
            print ("--------------")
            address = input("住所：")
        else:
            break

    cell = input("電話番号：")
    while True:
        if cell.isdecimal() == False:
            print ("数字で入力してください。")
            print ("--------------")
            cell = input("電話番号：")
        elif len(cell) == 10 or len(cell) == 11:
            break
        else:
            print("10or11桁で入力してください。")
            print ("--------------")
            cell = input("電話番号：")

    email = input("メールアドレス：")
    while True:
        import re
        if len(email)> 65:
            print("長すぎです。64文字以内で入力してください。")
            print ("--------------")
            email = input("メールアドレス：")
        elif re.match(r'[a-z\d._]+@[a-z]+\.[a-z]+', email):
            break
        else:
            print("正しいメールアドレスを入力してください。")
            print ("--------------")
            email = input("メールアドレス：")

    password = input("パスワード：")
    while True:
        import re
        p = re.compile('[a-zA-Z0-9]+')
        if len(password)> 33:
            print("長すぎです。32桁以内の大文字小文字英語か数字で入力してください。")
            print ("--------------")
            password = input("パスワード：")
        if len(password)<8:
            print("短すぎです。8桁以上の大文字小文字英語か数字で入力してください。")
            print ("--------------")
            password = input("パスワード：")
        elif re.search(r'[a-zA-Z0-9]+', password):
            break
        else:
            print("正しいパスワードを入力してください。")
            print ("--------------")
            password = input("パスワード：")


    cur = conn.cursor()
    cur.execute("USE final_chie_db")

    username = input("ログインID：")
    while True:
        import re

        p = re.compile('[a-zA-Z0-9]+')
        if len(password)> 33:
            print("長すぎです。32桁以内の大文字小文字英語か数字で入力してください。")
            print ("--------------")
            username = input("ログインID：")
        if len(password)<8:
            print("短すぎです。8桁以上の大文字小文字英語か数字で入力してください。")
            print ("--------------")
            username = input("ログインID：")
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
                print ("--------------")
                new_username_list.clear()
                username = input("ログインID：")
            else:
                break

        else:
            print("正しい書式で入力してください。")
            print ("--------------")
            username = input("ログインID：")
    print ("--------------")
    print (name,"\n", postcode,"\n", address, "\n", cell, "\n", email, "\n", password, "\n", username)
    print ("この内容で決定しますか？決定は1を再度編集は2を押してください")
    error_input1 = error1()

    if error_input1 == 1:
        add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(0,%s,%s,%s,%s,%s,%s,%s)"
        new_customers_list = [
            (name, postcode, address, cell, email, password, username)
        ]
        for new_cus in new_customers_list:
            cur.execute(add_customers, new_cus)
        cur.execute('UPDATE customers set id = record_id where id = 0')

        conn.commit()
        cur.close()
        conn.close()

    elif error_input1 == 2:
        add_customers(error1)


add_customers(error1)
