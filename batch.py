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

username_list = ["hakase"]
cus_id_list = []
order_cus_info_list = []
order_list2 = []
purchase_id_list = []


cur = conn.cursor()
cur.execute('SELECT items.cg_abb,items.id, items.item_name, items.condition_flag,order_detail.item_price,order_detail.item_num, order_detail.item_sum, sum(item_sum) FROM order_info  LEFT OUTER JOIN order_detail on order_info.id = order_detail.order_id  LEFT OUTER JOIN items on items.id = order_detail.item_id  where "2020年08月06日00時00分"<= order_info.order_date and "2020年08月07日00時00分" > order_info.order_date  GROUP BY items.cg_abb,items.id,order_detail.item_price  ')
collect_order_cus_info = cur.fetchall()
for i in collect_order_cus_info:#受注IDの取り出し
    purchase_list = []
    for j in i.values():#リストにIDを追加
        purchase_list.append(j)
    purchaseid = purchase_list[0]
    purchase_id_list.append(purchaseid)
    print(purchase_list)

print(purchase_id_list)
