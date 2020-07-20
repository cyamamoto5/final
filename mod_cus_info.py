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

show_cus_id_list = []
show_cus_name_list = []
show_cus_postcode_list = []
show_cus_address_list = []
show_cus_cell_list = []
show_cus_email_list = []
show_cus_password_list = []
all_cus_info_list = []


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
    cur.close()

def show_cus_info (login_input):
    username1 = input("AAAA")
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
            show_cus_password_list.append(value)
            all_cus_info_list.append(value)

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
    print (show_list2)
    print ("--------------------------------------------------------")
    print("●会員情報編集●")
    print("編集する内容を選んでください")
    mod_cus = input("入力：")

    if mod_cus == "1":
        print("変更内容を入力してください")
        mod1 = input("入力：")
        add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        new_customers_list = [
            (show_list2[0], mod1, int(show_list2[2]), show_list2[3], str(show_list2[4]), show_list2[5], show_list2[6], show_list2[7])
        ]

        cur = conn.cursor()
        for new_cus in new_customers_list:
            cur.execute(add_customers, new_cus)
        cur.execute('UPDATE customers set id = record_id where id = 0')
        cur.close()

    elif mod_cus == "2":
        print("変更内容を入力してください")
        mod2 = input("入力：")

        add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        new_customers_list = [
            (show_list2[0], show_list2[1], int(mod2), show_list2[3], str(show_list2[4]), show_list2[5], show_list2[6], show_list2[7])
        ]

        cur = conn.cursor()
        for new_cus in new_customers_list:
            cur.execute(add_customers, new_cus)
        cur.execute('UPDATE customers set id = record_id where id = 0')
        cur.close()

    elif mod_cus == "3":
        print("変更内容を入力してください")
        mod3 = input("入力：")


        add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        new_customers_list = [
            (show_list2[0], show_list2[1], int(show_list2[2]), mod3, str(show_list2[4]), show_list2[5], show_list2[6], show_list2[7])
        ]

        cur = conn.cursor()
        for new_cus in new_customers_list:
            cur.execute(add_customers, new_cus)
        cur.execute('UPDATE customers set id = record_id where id = 0')
        cur.close()

    elif mod_cus == "4":
        print("変更内容を入力してください")
        mod4 = input("入力：")


        add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        new_customers_list = [
            (show_list2[0], show_list2[1], int(show_list2[2]), show_list2[3], str(mod4), show_list2[5], show_list2[6], show_list2[7])
        ]

        cur = conn.cursor()
        for new_cus in new_customers_list:
            cur.execute(add_customers, new_cus)
        cur.execute('UPDATE customers set id = record_id where id = 0')
        cur.close()

    elif mod_cus == "5":
        print("変更内容を入力してください")
        mod5 = input("入力：")
        add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        new_customers_list = [
            (show_list2[0], show_list2[1], int(show_list2[2]), show_list2[3], str(show_list2[4]), mod5, show_list2[6], show_list2[7])
        ]
        cur = conn.cursor()
        for new_cus in new_customers_list:
            cur.execute(add_customers, new_cus)
        cur.execute('UPDATE customers set id = record_id where id = 0')
        cur.close()

    elif mod_cus == "6":
        print("変更内容を入力してください")
        mod6 = input("入力：")
        add_customers = "INSERT INTO customers(id, name, postcode, address, cell, email, password, username) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        new_customers_list = [
            (show_list2[0], show_list2[1], int(show_list2[2]), show_list2[3], str(show_list2[4]), show_list2[5], mod6, show_list2[7])
        ]
        cur = conn.cursor()
        for new_cus in new_customers_list:
            cur.execute(add_customers, new_cus)
        cur.execute('UPDATE customers set id = record_id where id = 0')
        cur.close()

    show_list2.clear()

    conn.commit()


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


def mod_cus_info_output1(error1):
    print ("--------------------------------------------------------")
    print("編集は1を、HOMEに戻るは2を入力してください")
    error_input1 = error1()
    if error_input1 == 1:
        mod_cus_info(show_list)
        show_cus_info (login_input)
        mod_cus_info_output1(error1)

    elif error_input1 == 2:
        print ("oKKKKKKKK")

show_cus_info (login_input)
show_list1 = show_list(show_cus_info)
mod_cus_info_output1(error1)


conn.close()
