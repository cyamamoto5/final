import pymysql.cursors
import unicodedata
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

order_id_list = []
new_customers_list = []
user_id_list = []
cus_id_list = []
order_cus_info_list = []
order_list1 = []
purchase_id_list = []
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

def error3():

    input1_str = input ("入力：")
    while True:
        if input1_str== "1" or input1_str== "2" or input1_str== "3" or input1_str== "4" or input1_str== "１" or input1_str== "２" or input1_str== "３" or input1_str== "４":
            input1 = int (input1_str)
            return(input1)
            break
        elif input1_str == "#" or input1_str =="＃":
            return(input1_str)
        else:
            print("入力方法が間違っています。指定された数字で入力してください")
            print ("--------------------------------------------------------")
            input1_str = input ("入力：")

def error0():

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

def error1_0():

    input1_str = input ("入力：")
    while True:
        if input1_str== "1" or input1_str== "0" or input1_str== "１" or input1_str== "０":
            input1 = int (input1_str)
            return(input1)
            break
        elif input1_str == "#" or input1_str =="＃":
            return(input1_str)
        else:
            print("入力方法が間違っています。指定された数字で入力してください")
            print ("--------------------------------------------------------")
            input1_str = input ("入力：")

def error1():

    input1_str = input ("入力：")
    while True:
        if input1_str== "1" or input1_str== "2" or input1_str== "１" or input1_str== "２":
            input1 = int (input1_str)
            return(input1)
            break
        elif input1_str == "#" or input1_str =="＃":
            return(input1_str)
        else:
            print("入力方法が間違っています。指定された数字で入力してください")
            print ("--------------------------------------------------------")
            input1_str = input ("入力：")

def delivered():

    print ("--------------------------------------------------------")
    print("●出庫登録●")
    print("出庫を行ったことを受注履歴に記録として残します")
    print("「#」を入力、エンターで前画面へ戻る")
    print("受注IDを入力してください")

    str_order_id = input("入力：")

    while True:
        if str_order_id == "#" or str_order_id == "＃":
            home()
        elif str_order_id.isdecimal() == False:
            print ("数字で入力してください。")
            str_order_id = input("入力：")
            if str_order_id == "#" or str_order_id == "＃":
                home()
        else:
            order_id = int(str_order_id)
            cur = conn.cursor()
            cur.execute('SELECT id FROM order_info')
            search_order_id= cur.fetchall()
            for id in search_order_id:
                for value in id.values():
                    order_id_list.append(value)

        if order_id not in order_id_list:
            print("\n")
            print("正しい受注IDを入力してください")
            order_id_list.clear()
            str_order_id = input("入力")
            order_id = int(str_order_id)
        else:
            break
    print("\n")
    print("発送が終了した場合は１を入力、発送が終了していない場合は0を入力して下さい")
    print("「#」を入力、エンターで前画面へ戻る")
    str_finish_delivered = error1_0()
    if str_finish_delivered == "#" or str_finish_delivered == "＃":
        home()
    elif str_finish_delivered == 1:
        finish_delivered = int(str_finish_delivered)
        select_1 = "発送済"
    elif str_finish_delivered == 0:
        finish_delivered = 0
        select_1 = "未発送"
    print("\n")
    print("受注ID：", order_id, "  ", select_1)
    print("\n")
    print("この内容で決定しますか？決定する場合は１を入力してください")
    print("「#」を入力、エンターで前画面へ戻る")
    decide_update = error0()
    if decide_update == 1:
        cur.execute('UPDATE order_info set delivered=%s WHERE id=%s', (finish_delivered, order_id))
        conn.commit()
    elif decide_update == "#" or decide_update == "＃":
        home()

    else:
        print("\n")
        print("入力方法が間違っています。")
        decide_update = error0

def cancel():
    print ("--------------------------------------------------------")
    print("●キャンセル登録●")
    print("キャンセルなどの依頼を受けたときに、受注履歴に記録を残します")
    print("「#」を入力、エンターで前画面へ戻る")
    print("受注IDを入力してください")

    str_order_id = input("入力：")

    while True:
        if str_order_id == "#" or str_order_id == "＃":
            home()
        elif str_order_id.isdecimal() == False:
            print ("数字で入力してください。")
            str_order_id = input("入力：")
            if str_order_id == "#" or str_order_id == "＃":
                home()
        else:
            order_id = int(str_order_id)
            cur = conn.cursor()
            cur.execute('SELECT id FROM order_info')
            search_order_id= cur.fetchall()
            for id in search_order_id:
                for value in id.values():
                    order_id_list.append(value)

        if order_id not in order_id_list:
            print("\n")
            print("正しい受注IDを入力してください")
            order_id_list.clear()
            str_order_id = input("入力")
            order_id = int(str_order_id)
        else:
            break
    print("\n")
    print("当てはまる数値を入力してください")
    print("「#」を入力、エンターで前画面へ戻る")
    print("1: 全体キャンセル")
    print("2: 全体返品交換")
    print("3: 部分キャンセル")
    print("4: 部分返品交換")

    str_finish_cancel = error3()
    if str_finish_cancel == "#" or str_finish_cancel == "＃":
        home()
    elif str_finish_cancel == 1:
        finish_cancel = 1
        select_1 = "全体キャンセル"
        print("\n")
        print("受注ID：", order_id, "  ", select_1)
        print("\n")
        print("この内容で決定しますか？決定する場合は１を入力してください")
        print("「#」を入力、エンターで前画面へ戻る")
        decide_update = error3()
        if decide_update == 1:
            cur.execute('UPDATE order_info set cancel=%s WHERE id=%s', (finish_cancel, order_id))
            conn.commit()
        elif decide_update == "#" or decide_update == "＃":
            home()
        else:
            print("\n")
            print("入力方法が間違っています。")
            decide_update = error3()
    elif str_finish_cancel == 2:
        finish_cancel = 2
        select_1 = "全体返品交換"
        print("\n")
        print("受注ID：", order_id, "  ", select_1)
        print("\n")
        print("この内容で決定しますか？決定する場合は１を入力してください")
        print("「#」を入力、エンターで前画面へ戻る")
        decide_update = error3()
        if decide_update == 1:
            cur.execute('UPDATE order_info set cancel=%s WHERE id=%s', (finish_cancel, order_id))
            conn.commit()
        elif decide_update == "#" or decide_update == "＃":
            home()
        else:
            print("\n")
            print("入力方法が間違っています。")
            decide_update = error3()
    elif str_finish_cancel == 3:
        finish_cancel = 3
        select_1 = "部分キャンセル"
        print("\n")
        print("受注ID：", order_id, "  ", select_1)
        print("\n")
        print("この内容で決定しますか？決定する場合は１を入力してください")
        print("「#」を入力、エンターで前画面へ戻る")
        decide_update = error3()
        if decide_update == 1:
            cur.execute('UPDATE order_info set cancel=%s WHERE id=%s', (finish_cancel, order_id))
            conn.commit()
        elif decide_update == "#" or decide_update == "＃":
            home()
        else:
            print("\n")
            print("入力方法が間違っています。")
            decide_update = error3()
    elif str_finish_cancel == 4:
        finish_cancel = 4
        select_1 = "部分返品交換"
        print("\n")
        print("受注ID：", order_id, "  ", select_1)
        print("\n")
        print("この内容で決定しますか？決定する場合は１を入力してください")
        print("「#」を入力、エンターで前画面へ戻る")
        decide_update = error3()
        if decide_update == 1:
            cur.execute('UPDATE order_info set cancel=%s WHERE id=%s', (finish_cancel, order_id))
            conn.commit()
        elif decide_update == "#" or decide_update == "＃":
            home()
        else:
            print("\n")
            print("入力方法が間違っています。")
            decide_update = error3()

def ask_customer_ID():
    print ("--------------------------------------------------------")
    print("●入金登録●")
    print("入金の確認が取れたお客様の受注履歴に記録を残します")
    print("「#」を入力、エンターで前画面へ戻る")
    print("顧客IDを入力してください")
    str_order_id = input("入力：")
    print("\n")

    while True:
        if str_order_id == "#" or str_order_id == "＃":
            home()
        elif str_order_id.isdecimal() == False:
            print ("数字で入力してください。")
            str_order_id = input("入力：")
            if str_order_id == "#" or str_order_id == "＃":
                home()
        order_id = int(str_order_id)
        cur = conn.cursor()
        cur.execute('SELECT id FROM view_customers')
        search_order_id= cur.fetchall()
        for id in search_order_id:
            for value in id.values():
                user_id_list.append(value)

        if order_id not in user_id_list:
            print("\n")
            print("正しい顧客IDを入力してください")
            user_id_list.clear()
            str_order_id = input("入力")
        else:

            return order_id
            break

def purchase_history():
    ask = ask_customer_ID()
    cur = conn.cursor()
    cur.execute('SELECT id, order_date, total, payment, delivered,cancel,cancel_ID FROM order_info where customer_id=(%s)', (ask))
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
    if str_ask_purchase_id == "#" or str_ask_purchase_id == "＃":
        home()

    while True:
        if str_ask_purchase_id.isdecimal() == False:
            print ("数字で入力してください")
            str_ask_purchase_id = input("入力：")
            if str_ask_purchase_id == "#" or str_ask_purchase_id == "＃":
                home()
        else:
            ask_purchase_id = int(str_ask_purchase_id)
            if ask_purchase_id not in purchase_id_list:
                print("正しい受注IDを入力してください")
                str_ask_purchase_id = input("入力：")
                if str_ask_purchase_id == "#" or str_ask_purchase_id == "＃":
                    home()
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

def ask_more_history():
    purchase_history()
    purchase_detail()

    print ("--------------------------------------------------------")
    print("受注詳細をさらに展開したい場合は１を、Homeに戻る場合は２を入力してください")
    purchase_detail_input = error1()
    print("\n")

    while True:
        if purchase_detail_input == 1:
            purchase_detail()
            print ("--------------------------------------------------------")
            print("受注詳細をさらに展開したい場合は１を、Homeに戻る場合は２を入力してください")
            purchase_detail_input = error1()
        else:
            home()
            user_id_list.clear()
            cus_id_list.clear()
            purchase_list.clear()
            purchase_detail_list.clear()
            purchase_id_list.clear()
            break


def money():
    print ("--------------------------------------------------------")
    print("●入金登録●")
    print("入金の確認が取れたお客様の受注履歴に記録を残します")
    print("「#」を入力、エンターで前画面へ戻る")
    print("受注IDを入力してください")

    str_order_id = input("入力：")

    while True:
        if str_order_id == "#" or str_order_id == "＃":
            home()
            break
        elif str_order_id.isdecimal() == False:
            print ("数字で入力してください。")
            str_order_id = input("入力：")
            if str_order_id == "#" or str_order_id == "＃":
                home()
                break
        else:
            order_id = int(str_order_id)
            cur = conn.cursor()
            cur.execute('SELECT id FROM order_info')
            search_order_id= cur.fetchall()
            order_id_list.clear()
            for id in search_order_id:
                for value in id.values():
                    order_id_list.append(value)

        if order_id not in order_id_list:
            print("\n")
            print("正しい受注IDを入力してください")
            order_id_list.clear()
            str_order_id = input("入力")
            order_id = int(str_order_id)
        else:
            break
    print("\n")
    print("入金確認が終了した場合は１を入力、入金が終了していない場合は０を入力して下さい")
    print("「#」を入力、エンターで前画面へ戻る")
    str_finish_payment = error1_0()
    if str_finish_payment == "#" or str_finish_payment == "＃":
        home()
    elif str_finish_payment == 1:
        finish_payment = int(str_finish_payment)
        select_1 = "入金済み"
    elif str_finish_payment == 0:
        finish_payment = 0
        select_1 = "未入金"
    print("\n")
    print("受注ID：", order_id, "  ", select_1)
    print("\n")
    print("この内容で決定しますか？決定する場合は１を入力してください")
    print("「#」を入力、エンターで前画面へ戻る")
    decide_update = error0()
    if decide_update == 1:
        cur.execute('UPDATE order_info set payment=%s WHERE id=%s', (finish_payment, order_id))
        conn.commit()
    elif decide_update == "#" or decide_update == "＃":
        home()
    else:
        print("\n")
        print("入力方法が間違っています。")
        decide_update = error0()

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


def finish_system():
    print ("--------------------------------------------------------")
    print("●システム終了●")
    print("1: システムを終了します")
    print("2: Home")
    print("\n")

    finish_system_input = error1()
    if finish_system_input == 1:
        print ("--------------------------------------------------------")
        print("●システムを終了します●")
        import sys
        sys.exit()
    elif finish_system_input == 2:
        home()

def home():
    print ("--------------------------------------------------------")
    print("●ＨＯＭＥ●")
    print("1: 入金登録")
    print("2: 出庫登録")
    print("3: キャンセル登録")
    print("4: 明細書発行")
    print("5: 受注情報検索")
    print("6: システム終了")
    print ("--------------------------------------------------------")

    print("お進みいただく項目の選択をお願いします")
    home_input = input("入力：")
    while True:
        if home_input == "1" or home_input == "１":
            money()
            home()
            break
        elif home_input == "2" or home_input == "２":
            delivered()
            home()
            break
        elif home_input == "3" or home_input == "３":
            cancel()
            home()
            break
        elif home_input == "4" or home_input == "４":
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
            home()
            break
        elif home_input == "5" or home_input == "５":
            ask_more_history()
            home()
            break
        elif home_input == "6" or home_input == "６":
            finish_system()
            home()
            break
        else:
            print ("正しい書式で入力してください")
            home_input = input("入力：")

home()
