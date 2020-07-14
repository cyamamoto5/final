print ("--------------")
print ("★ようこそ、VV商店へ★")
print ("--------------")
print ("ログイン画面へ進むには１を\n新規登録画面へ進むには２を入力してください")
print ("--------------")

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

error_input1 = error1()

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

username_list = []
password_list = []

def login_input():
    cur = conn.cursor()
    username_input = input("ログインID入力")
    cur.execute('SELECT username FROM view_customers where username=(%s)', (username_input))
    collect_username = cur.fetchall()

    for username in collect_username:
        for value in username.values():
            username_list.append(value)

    password_input = input("パスワード入力")
    print ("--------------")
    cur.execute('SELECT username FROM view_customers where password=(%s)', (password_input))
    collect_password = cur.fetchall()

    for password in collect_password:
        for value in password.values():
            password_list.append(value)

def login_error(login_input):
    while True:
        if not username_list or not password_list:
            print ("入力内容が正しくありません。再入力をお願いします。\nパスワードの再設定は、以下のメールアドレスにお問い合わせください。\ncustomer@vv.com")
            print ("--------------")
            username_list.clear()
            password_list.clear()
            login_input()
        else:
            break

    while True:
        if username_list == password_list:
            print ("ok")
            return (username_list)
            break
        else:
            print ("入力内容が正しくありません。再入力をお願いします。\nパスワードの再設定は、以下のメールアドレスにお問い合わせください。\ncustomer@vv.com")
            print ("--------------")
            username_list.clear()
            password_list.clear()
            login_input()


def login(login_input, login_error):
    cur = conn.cursor()
    print("●ログイン画面●")
    #リストへの追加
    login_input()
    login_error(login_input)
    cur.close()
    conn.close()

logg = login(login_input, login_error)

def output1(error_input1, login):
    if error_input1 == 1:
        login(login_input, login_error)
    elif error_input1 == 2:
        print ("oKKKKKKKK")
