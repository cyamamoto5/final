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

def username_judge(username):
    new_username_list = []
    cur = conn.cursor()
    cur.execute('SELECT username FROM view_customers where username=(%s)', (username))
    collect_new_username = cur.fetchall()

    for username1 in collect_new_username:
        for value in username1.values():
            new_username_list.append(value)

    while True:
        if len(new_username_list)>0:
            print ("すでに使われているユーザー名です。")
            print ("--------------")
            new_username_list.clear()
            username_judge()
        else:
            break
def add_customers (username_judge):
    username = input("ログインID：")
    cur = conn.cursor()
    cur.execute("USE final_chie_db")

    while True:
        import re
        p = re.compile('[a-zA-Z0-9]+')
        if len(username)> 33:
            print("長すぎです。32桁以内の大文字小文字英語か数字で入力してください。")
            username = input("ログインID：")
        if len(username)<8:
            print("短すぎです。8桁以上の大文字小文字英語か数字で入力してください。")
            username = input("ログインID：")
        elif re.search(r'[a-zA-Z0-9]+', username):
            break
        else:
            print("正しいパスワードを入力してください。")
            username = input("ログインID：")
        username_judge(username)


        cur.close()
    conn.close()

add_customers (username_judge)
