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

def show_cus_info (login_input):
    username1 = input("AAAA")
    cur = conn.cursor()

    cur.execute('SELECT name FROM view_customers where username=%s',(username1))
    collect_new_username3 = cur.fetchall()
    for username3 in collect_new_username3:
        for value in username3.values():
            show_cus_name_list.append(value)

    cur.execute('SELECT postcode FROM view_customers where username=%s',(username1))
    collect_new_username4 = cur.fetchall()
    for username4 in collect_new_username4:
        for value in username4.values():
            show_cus_postcode_list.append(value)

    cur.execute('SELECT address FROM view_customers where username=%s',(username1))
    collect_new_username5 = cur.fetchall()
    for username5 in collect_new_username5:
        for value in username5.values():
            show_cus_address_list.append(value)

    cur.execute('SELECT cell FROM view_customers where username=%s',(username1))
    collect_new_username6 = cur.fetchall()
    for username6 in collect_new_username6:
        for value in username6.values():
            show_cus_cell_list.append(value)

    cur.execute('SELECT email FROM view_customers where username=%s',(username1))
    collect_new_username7 = cur.fetchall()
    for username7 in collect_new_username7:
        for value in username7.values():
            show_cus_email_list.append(value)

    cur.execute('SELECT password FROM view_customers where username=%s',(username1))
    collect_new_username8 = cur.fetchall()
    for username8 in collect_new_username8:
        for value in username8.values():
            show_cus_password_list.append(value)

    print ("会員情報")
    for index, (a, b, c, d, e, f) in enumerate(zip(show_cus_name_list,show_cus_postcode_list,show_cus_address_list,show_cus_cell_list,show_cus_email_list,show_cus_password_list)):
        print("名前：",a,"\n〒：",b,"\n住所：",c,"\n電話番号：",e,"\nEmail：",d,"\nパスワード：", f)

    cur.close()
    conn.close()
show_cus_info ()
