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

invoice_cus_info_list = []
invoice_id_list = []
invoice_info_list = []
invoice_id_list2 = []
invoice_cus_info_list3 = []
invoice_info_list1 = []
detail_list1 = []
detail_list2 = []
detail_list3 = []
detail_list4 = []
detail_list5 = []

def error0():

    input1_str = input ("入力：")
    while True:
        if input1_str== "1" or input1_str== "１":
            input1 = int (input1_str)
            return(input1)
            break
        elif input1_str == "#" or input1_str =="＃":
            return(input1_str)
        else:
            print("入力方法が間違っています。指定された数字で入力してください")
            print ("--------------------------------------------------------")
            input1_str = input ("入力：")

def Purchase_statement():
    print ("--------------------------------------------------------")
    print("●購入明細●")
    print("「#」を入力、エンターで前画面へ戻る")
    print("受注IDを入力してください")

    str_invoice_id = input("入力：")
    print("\n")

    while True:
        if str_invoice_id == "#" or str_invoice_id == "＃":
            print("HOME")
        elif str_invoice_id.isdecimal() == False:
            print ("数字で入力してください。")
            str_invoice_id = input("入力：")
            if str_invoice_id == "#" or str_invoice_id == "＃":
                print("HOME")
        invoice_id = int(str_invoice_id)
        cur = conn.cursor()
        cur.execute('SELECT id FROM order_info')
        search_invoice_id= cur.fetchall()
        for id in search_invoice_id:
            for value in id.values():
                invoice_id_list.append(value)

        if invoice_id not in invoice_id_list:
            invoice_id_list2.clear()

            print("正しい受注IDを入力してください")
            invoice_id_list.clear()
            str_invoice_id = input("入力")
        else:
            invoice_id = int(str_invoice_id)
            invoice_id_list2.append(invoice_id)
            break

        cur.execute('SELECT customer_id FROM order_info where id=(%s)', (invoice_id_list2[0]))
        search_invoice_id= cur.fetchall()
        for id in search_invoice_id:
            for value in id.values():
                invoice_id_list.append(value)


def invoice_cus_info():

    cur = conn.cursor()
    cur.execute('SELECT customer_id FROM order_info where id=(%s)', (invoice_id_list2[0]))
    collect_invoice_cus_info = cur.fetchall()
    for collect_invoice_cus_info1 in collect_invoice_cus_info:
        for value in collect_invoice_cus_info1.values():
            invoice_cus_info_list3.append(value)


    cur.execute('SELECT name, postcode, address, cell, id FROM view_customers where id=(%s)', (invoice_cus_info_list3[0]))
    collect_invoice_cus_info = cur.fetchall()
    for collect_invoice_cus_info1 in collect_invoice_cus_info:
        for value in collect_invoice_cus_info1.values():
            invoice_cus_info_list.append(value)


def creat_invoice():
    cur = conn.cursor()
    cur.execute('SELECT order_date, taxed_total, total FROM order_info where id=(%s)', (invoice_id_list2[0]))
    collect_invoice_cus_info = cur.fetchall()
    for collect_invoice_cus_info2 in collect_invoice_cus_info:
        for value in collect_invoice_cus_info2.values():
            invoice_info_list.append(value)

    cur = conn.cursor()
    cur.execute('SELECT id FROM order_detail where order_id=(%s)', (invoice_id_list2[0]))
    collect_invoice_cus_info1 = cur.fetchall()
    for collect_invoice_cus_info2 in collect_invoice_cus_info1:
        for value in collect_invoice_cus_info2.values():
            invoice_info_list1.append(value)
    index = len(invoice_info_list1)



    if index >= 1:
        cur.execute('SELECT * FROM order_detail where id=(%s)', (invoice_info_list1[index - 1]))
        collect_invoice_cus_info1 = cur.fetchall()
        for collect_invoice_cus_info2 in collect_invoice_cus_info1:
            for value in collect_invoice_cus_info2.values():
                detail_list1.append(value)

    if index >= 2:
        cur.execute('SELECT * FROM order_detail where id=(%s)', (invoice_info_list1[index - 2]))
        collect_invoice_cus_info1 = cur.fetchall()
        for collect_invoice_cus_info2 in collect_invoice_cus_info1:
            for value in collect_invoice_cus_info2.values():
                detail_list2.append(value)
        detail1 = detail_list2[2], " - ",detail_list2[3], " - ", detail_list2[6], "円 - 個数", detail_list2[5], " - ", detail_list2[4]

    if index >= 3:
        cur.execute('SELECT * FROM order_detail where id=(%s)', (invoice_info_list1[index - 3]))
        collect_invoice_cus_info1 = cur.fetchall()
        for collect_invoice_cus_info2 in collect_invoice_cus_info1:
            for value in collect_invoice_cus_info2.values():
                detail_list3.append(value)

        detail3 = detail_list3[2], " - ",detail_list3[3], " - ", detail_list3[6], "円 - 個数", detail_list3[5], " - ", detail_list3[4]

    if index >= 4:
        cur.execute('SELECT * FROM order_detail where id=(%s)', (invoice_info_list1[index - 4]))
        collect_invoice_cus_info1 = cur.fetchall()
        for collect_invoice_cus_info2 in collect_invoice_cus_info1:
            for value in collect_invoice_cus_info2.values():
                detail_list4.append(value)
        detail4 = detail_list4[2], " - ",detail_list4[3], " - ", detail_list4[6], "円 - 個数", detail_list4[5], " - ", detail_list4[4]

    if index >= 5:
        cur.execute('SELECT * FROM order_detail where id=(%s)', (invoice_info_list1[index - 5]))
        collect_invoice_cus_info1 = cur.fetchall()
        for collect_invoice_cus_info2 in collect_invoice_cus_info1:
            for value in collect_invoice_cus_info2.values():
                detail_list5.append(value)
        detail5 = detail_list5[2], " - ",detail_list5[3], " - ", detail_list5[6], "円 - 個数", detail_list5[5], " - ", detail_list5[4]

    now = datetime.datetime.now()
    now1 = r'\PS_{0:%Y%m%d%H%M%S}'.format(now)+'.txt'
    YMD = '{0:%Y}'.format(now) + '年' + '{0:%m}'.format(now) + '月' + '{0:%d}'.format(now) + '日'
    file = os.path.abspath("Purchase_statement")
    now2 = file + now1
    invoice_line1 = '●請求書●　　（発行日'+ YMD + ')'

    print ("--------------------------------------------------------")
    print(invoice_line1)
    print("----------------------------")
    print("会員番号：", str(invoice_cus_info_list[4]))
    print(str(invoice_cus_info_list[0]), "様")
    print("〒", str(invoice_cus_info_list[1]))
    print(str(invoice_cus_info_list[2]))
    print("TEL", str(invoice_cus_info_list[3]))
    print("----------------------------")
    print("ご請求金額")
    print(str(invoice_info_list[2]),"円（税込み）")
    print("----------------------------")
    print("詳細")
    print("ｶﾃｺﾞﾘ - ID - 単価 - 個数 - 商品名")
    if index > 0:
        print(detail_list1[2], " - ", str(detail_list1[3]), " - ", str(detail_list1[6]), "円 - 個数", str(detail_list1[5]), " - ", detail_list1[4])
    if index > 1:
        print(detail_list2[2], " - ", str(detail_list2[3]), " - ", str(detail_list2[6]), "円 - 個数", str(detail_list2[5]), " - ", detail_list2[4])
    if index > 2:
        print(detail_list3[2], " - ", str(detail_list3[3]), " - ", str(detail_list3[6]), "円 - 個数", str(detail_list3[5]), " - ", detail_list3[4])

    if index > 3:
        print(detail_list4[2], " - ", str(detail_list4[3]), " - ", str(detail_list4[6]), "円 - 個数", str(detail_list4[5]), " - ", detail_list4[4])

    if index > 4:
        print(detail_list5[2], " - ", str(detail_list5[3]), " - ", str(detail_list5[6]), "円 - 個数", str(detail_list5[5]), " - ", detail_list5[4])

    print("----------------------------")

    print("小計：", str(invoice_info_list[1]), "円")

    print("送料：", str(invoice_info_list[2] - invoice_info_list[1]), "円")

    print("合計：", str(invoice_info_list[2]), "円")

    print("----------------------------")

    print("VV商店")
    print("03-3333-3333")
    print("東京都港区赤坂１－２－３")
    print ("--------------------------------------------------------")
    print("\n")


    print("この内容で決定しますか？決定する場合は１を入力してください")
    print("「#」を入力、エンターで前画面へ戻る")
    invoice = error0()
    print("\n")
    print("発行しました")
    print ("--------------------------------------------------------")

    if invoice == 1:

        f = open(now2, 'w', encoding='utf-8')
        f.write(invoice_line1)
        f.write("\n")
        f.write("----------------------------")
        f.write("\n")
        f.write("会員番号：")
        f.write(str(invoice_cus_info_list[4]))
        f.write("\n")
        f.write(str(invoice_cus_info_list[0]))
        f.write("様")
        f.write("\n")
        f.write("〒")
        f.write(str(invoice_cus_info_list[1]))
        f.write("\n")
        f.write(str(invoice_cus_info_list[2]))
        f.write("\n")
        f.write("TEL")
        f.write(str(invoice_cus_info_list[3]))
        f.write("\n")
        f.write("----------------------------")
        f.write("\n")
        f.write("ご請求金額")
        f.write(str(invoice_info_list[2]))
        f.write("円（税込み）")
        f.write("\n")
        f.write("----------------------------")
        f.write("\n")
        f.write("詳細")
        f.write("\n")
        f.write("ｶﾃｺﾞﾘ - ID - 単価 - 個数 - 商品名")
        f.write("\n")
        if index > 0:
            f.write(detail_list1[2])
            f.write(" - ")
            f.write(str(detail_list1[3]))
            f.write(" - ")
            f.write(str(detail_list1[6]))
            f.write("円 - 個数")
            f.write(str(detail_list1[5]))
            f.write(" - ")
            f.write(detail_list1[4])
            f.write("\n")
        if index > 1:
            f.write(detail_list2[2])
            f.write(" - ")
            f.write(str(detail_list2[3]))
            f.write(" - ")
            f.write(str(detail_list2[6]))
            f.write("円 - 個数")
            f.write(str(detail_list2[5]))
            f.write(" - ")
            f.write(detail_list2[4])
            f.write("\n")
        if index > 2:
            f.write(detail_list3[2])
            f.write(" - ")
            f.write(str(detail_list3[3]))
            f.write(" - ")
            f.write(str(detail_list3[6]))
            f.write("円 - 個数")
            f.write(str(detail_list3[5]))
            f.write(" - ")
            f.write(detail_list3[4])
            f.write("\n")
        if index > 3:
            f.write(detail_list4[2])
            f.write(" - ")
            f.write(str(detail_list4[3]))
            f.write(" - ")
            f.write(str(detail_list4[6]))
            f.write("円 - 個数")
            f.write(str(detail_list4[5]))
            f.write(" - ")
            f.write(detail_list4[4])
            f.write("\n")
        if index > 4:
            f.write(detail_list5[2])
            f.write(" - ")
            f.write(str(detail_list5[3]))
            f.write(" - ")
            f.write(str(detail_list5[6]))
            f.write("円 - 個数")
            f.write(str(detail_list5[5]))
            f.write(" - ")
            f.write(detail_list5[4])
            f.write("\n")
        f.write("----------------------------")
        f.write("\n")
        f.write("小計：")
        f.write(str(invoice_info_list[1]))
        f.write("円")
        f.write("\n")
        f.write("送料：")
        f.write(str(invoice_info_list[2] - invoice_info_list[1]))
        f.write("円")
        f.write("\n")
        f.write("合計：")
        f.write(str(invoice_info_list[2]))
        f.write("円")
        f.write("\n")
        f.write("----------------------------")
        f.write("\n")
        f.write("VV商店")
        f.write("\n")
        f.write("03-3333-3333")
        f.write("\n")
        f.write("東京都港区赤坂１－２－３")
        f.write("\n")

        f.close()

    else:
        home()





#creat_invoice()
invoice_id = Purchase_statement()
invoice_cus_info()
creat_invoice()
invoice_cus_info_list.clear()
invoice_id_list.clear()
invoice_info_list.clear()
invoice_id_list2.clear()
invoice_cus_info_list3.clear()
invoice_info_list1.clear()
detail_list1.clear()
detail_list2.clear()
detail_list3.clear()
detail_list4.clear()
detail_list5.clear()
