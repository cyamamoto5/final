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

def cancel():
    print ("--------------------------------------------------------")
    print("●キャンセル登録●")
    print("キャンセルなどの依頼を受けたときに、受注履歴に記録を残します")
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
    print("当てはまる数値を入力してください")
    print("「#」を入力、エンターで前画面へ戻る")
    print("1: 全体キャンセル")
    print("2: 全体返品交換")
    print("3: 部分キャンセル")
    print("4: 部分返品交換")

    str_finish_cancel = error3()
    if str_finish_cancel == "#" or str_finish_cancel == "＃":
        print("HOMEに戻る")
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
            print("HOMEに戻る")
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
            print("HOMEに戻る")
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
            print("HOMEに戻る")
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
            print("HOMEに戻る")
        else:
            print("\n")
            print("入力方法が間違っています。")
            decide_update = error3()



cancel()
