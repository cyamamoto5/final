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

order_id_list = []
new_customers_list = []

def error1():

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

def money():
    print ("--------------------------------------------------------")
    print("●入金登録●")
    print("入金の確認が取れたお客様の受注履歴に記録を残します")
    print("「#」を入力、エンターで前画面へ戻る")
    print("受注IDを入力してください")

    str_order_id = input("入力：")

    while True:
        if str_order_id == "#" or str_order_id == "＃":
            print("HOME")
        elif str_order_id.isdecimal() == False:
            print ("数字で入力してください。")
            str_order_id = input("入力：")
            if str_order_id == "#" or str_order_id == "＃":
                print("HOME")
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
    print("入金確認が終了した場合は１を入力、入金が終了していない場合は０を入力して下さい")
    print("「#」を入力、エンターで前画面へ戻る")
    str_finish_payment = error1()
    if str_finish_payment == "#" or str_finish_payment == "＃":
        print("HOMEに戻る")
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
    decide_update = error1()
    if decide_update == 1:
        cur.execute('UPDATE order_info set payment=%s WHERE id=%s', (finish_payment, order_id))
        conn.commit()
    elif decide_update == "#" or decide_update == "＃":
        print("HOMEに戻る")
    else:
        print("\n")
        print("入力方法が間違っています。")
        decide_update = error1()


money()
