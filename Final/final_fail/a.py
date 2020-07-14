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

new_username = input("ログインID入力")

def username_judge(new_username):
    while True:
        new_username_list = []
        cur = conn.cursor()
        cur.execute('SELECT username FROM view_customers where username=(%s)', (new_username))
        collect_new_username = cur.fetchall()

        for username in collect_new_username:
            for value in username.values():
                new_username_list.append(value)

        if len(new_username_list)>0:
            print ("すでに使われているユーザー名です。")
            print ("--------------")
            new_username = input("ログインID入力")
            new_username_list.clear()

        else:
            break

username_judge(new_username)
