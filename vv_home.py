import pymysql.cursors
import unicodedata

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
    if home_input == "1":
        show_search_items(show_item_cg, search_items)

    elif home_input == "2":
        print("まだできてないよ")
    else:
        print ("正しい書式で入力してください")

home()
