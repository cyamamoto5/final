import pymysql.cursors
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

username_list = ['memequeen']
password_list = ['akasakataro']
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



def show_cart():
    cart = 'shopping_cart.txt'

    with open(cart, 'r', encoding='utf-8') as q:
        n = 0
        for s_line in q:
            n = n + 1
            print (n,":", s_line.replace("\n", ""))
    return n

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
        cur.execute('SELECT fee FROM shipping_fee where name=(%s)', ("10000円以上"))
        collect_shipping_fee1 = cur.fetchall()

        for shipping_fee1 in collect_shipping_fee1:
            for value in shipping_fee1.values():
                shipping_fee_list.append(value)

    if numprice < 10000:
        cur = conn.cursor()
        cur.execute('SELECT fee FROM shipping_fee where name=(%s)', ("10000円未満"))
        collect_shipping_fee2 = cur.fetchall()
        shipping_fee_list = []

        for shipping_fee2 in collect_shipping_fee2:
            for value in shipping_fee2.values():
                shipping_fee_list.append(value)


    #送料＋合計
    print("合計金額：", numprice)
    print("配送料：", shipping_fee_list[0])
    print("_________________")
    print("合計：", numprice + shipping_fee_list[0])

    l = numprice
    m = shipping_fee_list[0]
    n = numprice + shipping_fee_list[0]

    list.append(l)
    list.append(m)
    list.append(n)

def order_cus_info():
    cur = conn.cursor()
    cur.execute('SELECT name, postcode, address, cell, id FROM view_customers where username=(%s) and password=(%s)', (username_list[0], password_list[0]))
    collect_order_cus_info = cur.fetchall()

    for collect_order_cus_info1 in collect_order_cus_info:
        for value in collect_order_cus_info1.values():
            order_cus_info_list.append(value)


    print(order_cus_info_list[0],"様")
    print("TEL",order_cus_info_list[3])
    print("〒",order_cus_info_list[1], " ",order_cus_info_list[2])

def register():
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
                print ("--------------------------------------------------------")
                print("HOMEに戻る")

            else:
                print("HOMEに戻る")
        else:
            print("HOMEに戻る")

    else:
        print("HOMEに戻る")

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
        (order_cus_id_list[0], shipping_fee_list[0], YMD, l, n)
    ]
    for new_order in add_order_info_list:
        cur.execute(add_order_info, new_order)
    conn.commit()

    #order_infoからIDを選ぶ
    cur.execute('SELECT id FROM order_info where id=(SELECT MAX(id) FROM order_info)')
    order_id = cur.fetchall()
    for cus_order_id in order_id:
        for value in cus_order_id.values():
            order_id_list.append(value)

    #order_infoからItem_nameを選ぶ
    cur.execute('SELECT item_name FROM view_items where id=(%s) and cg_abb=(%s)', (order_id1, order_cat1))
    order_item_name1 = cur.fetchall()
    for cus_order_id in order_item_name1:
        for value in cus_order_id.values():
            order_item_name1_list.append(value)

    cur.execute('SELECT item_name FROM view_items where id=(%s) and cg_abb=(%s)', (order_id2, order_cat2))
    order_item_name2 = cur.fetchall()
    for cus_order_id in order_item_name2:
        for value in cus_order_id.values():
            order_item_name2_list.append(value)

    cur.execute('SELECT item_name FROM view_items where id=(%s) and cg_abb=(%s)', (order_id3, order_cat3))
    order_item_name3 = cur.fetchall()
    for cus_order_id in order_item_name3:
        for value in cus_order_id.values():
            order_item_name3_list.append(value)

    cur.execute('SELECT item_name FROM view_items where id=(%s) and cg_abb=(%s)', (order_id4, order_cat4))
    order_item_name4 = cur.fetchall()
    for cus_order_id in order_item_name4:
        for value in cus_order_id.values():
            order_item_name4_list.append(value)

    cur.execute('SELECT item_name FROM view_items where id=(%s) and cg_abb=(%s)', (order_id5, order_cat5))
    order_item_name5 = cur.fetchall()
    for cus_order_id in order_item_name5:
        for value in cus_order_id.values():
            order_item_name5_list.append(value)

    #order_detailからIDを選ぶ

    idx01 = len(order_item_name1_list)
    idx02 = len(order_item_name2_list)
    idx03 = len(order_item_name3_list)
    idx04 = len(order_item_name4_list)
    idx05 = len(order_item_name5_list)

    if order_list1[0] != "0":
        order_sum1 = order_price1*order_num1
        add_order_info = "INSERT INTO order_detail(order_id, item_cg, item_id, item_name, item_sum, item_price, item_num) values(%s,%s,%s,%s,%s,%s,%s)"
        add_order_info_list1 = [
            (order_id_list[0], order_cat1, order_id1, order_item_name1_list[idx01 - 1], order_sum1, order_price1, order_num1)
        ]
        for new_order1 in add_order_info_list1:
            cur.execute(add_order_info, new_order1)
        conn.commit()

    if order_list2[0] != "0":
        order_sum2 = order_price2*order_num2
        add_order_info = "INSERT INTO order_detail(order_id,item_cg, item_id, item_name, item_sum, item_price, item_num) values(%s,%s,%s,%s,%s,%s,%s)"
        add_order_info_list = [
            (order_id_list[0], order_cat2, order_id2, order_item_name2_list[idx02 - 1], order_sum2, order_price2, order_num2)
        ]
        for new_order in add_order_info_list:
            cur.execute(add_order_info, new_order)
        conn.commit()

    if order_list3[0] != "0":
        order_sum3 = order_price3*order_num3
        add_order_info = "INSERT INTO order_detail(order_id,item_cg, item_id, item_name, item_sum, item_price, item_num) values(%s,%s,%s,%s,%s,%s,%s)"
        add_order_info_list = [
            (order_id_list[0], order_cat3, order_id3, order_item_name3_list[idx03 - 1], order_sum3, order_price3, order_num3)
        ]
        for new_order in add_order_info_list:
            cur.execute(add_order_info, new_order)
        conn.commit()

    if order_list4[0] != "0":
        order_sum4 = order_price4*order_num4
        add_order_info = "INSERT INTO order_detail(order_id,item_cg, item_id, item_name, item_sum, item_price, item_num) values(%s,%s,%s,%s,%s,%s,%s)"
        add_order_info_list = [
            (order_id_list[0], order_cat4, order_id4, order_item_name4_list[idx04 - 1], order_sum4, order_price4, order_num4)
        ]
        for new_order in add_order_info_list:
            cur.execute(add_order_info, new_order)
        conn.commit()

    if order_list5[0] != "0":
        order_sum5 = order_price5*order_num5
        add_order_info = "INSERT INTO order_detail(order_id,item_cg, item_id, item_name, item_sum, item_price, item_num) values(%s,%s,%s,%s,%s,%s,%s)"
        add_order_info_list1 = [
            (order_id_list[0], order_cat5, order_id5, order_item_name5_list[idx05 - 1], order_sum5, order_price5, order_num5)
        ]
        for new_order in add_order_info_list1:
            cur.execute(add_order_info, new_order)
        conn.commit()

cart = 'shopping_cart.txt'
list = [0]
with open(cart, 'r', encoding='utf-8') as q:

    for s_line in q:
        list.append(s_line)

print(list[0])
print(len(list))

aa = len(list)
if list[aa - 1] == 0:
    print("no")
else:
    print("yes")

register()

creat_invoice()
insert_order_info()
