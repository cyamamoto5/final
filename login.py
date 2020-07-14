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
    #リストへの追加
    print("●ログイン画面●")
    login_input()
    login_error(login_input)
    cur.close()
    conn.close()

logg = login(login_input, login_error)
