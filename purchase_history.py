import pymysql.cursors
import re

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

username_list = ["memequeen"]
cus_id_list = []
order_cus_info_list = []
order_list2 = []
purchase_id_list = []

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

def purchase_history():
    cur = conn.cursor()
    cur.execute('SELECT id FROM view_customers where username = (%s)', (username_list[0]))
    collect_order_cus_info = cur.fetchall()

    for collect_order_cus_info1 in collect_order_cus_info:
        for value in collect_order_cus_info1.values():
            cus_id_list.append(value)


    cur.execute('SELECT id, order_date, total, payment, delivered,cancel,cancel_ID FROM order_info where customer_id=(%s)', (cus_id_list[0]))
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
    str_ask_purchase_id = input("入力")
    while True:
        if str_ask_purchase_id.isdecimal() == False:
            print ("数字で入力してください")
            str_ask_purchase_id = input("受注IDを入力してください")
        else:
            ask_purchase_id = int(str_ask_purchase_id)
            if ask_purchase_id not in purchase_id_list:
                print("正しい受注IDを入力してください")
                str_ask_purchase_id = input("受注IDを入力してください")
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

purchase_history()
purchase_detail()

print ("--------------------------------------------------------")
print("受注詳細をさらに展開したい場合は１を、Homeに戻る場合は２を入力してください")
purchase_detail_input = error1()
while True:
    if purchase_detail_input == 1:
        purchase_detail()
        print ("--------------------------------------------------------")
        print("受注詳細をさらに展開したい場合は１を、Homeに戻る場合は２を入力してください")
        purchase_detail_input = error1()
    else:
        print("HOMEに戻る")
        break

#cus_id_list.clear()
#purchase_list.clear()
#purchase_detail_list.clear()
#purchase_id_list.clear()
#
