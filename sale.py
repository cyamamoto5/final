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

cur = conn.cursor()
cur.execute('UPDATE items as IT INNER JOIN item_cg as CG ON IT.cg_abb = CG.cg_abb SET IT.sale_price = IT.list_price*CG.discount_rate WHERE CG.sale_flag = 1')
conn.commit()
cur.execute('UPDATE items as IT INNER JOIN item_cg as CG ON IT.cg_abb = CG.cg_abb SET IT.selling_price = IT.sale_price WHERE CG.sale_flag = 1')
conn.commit()
cur.execute('UPDATE items as IT INNER JOIN item_cg as CG ON IT.cg_abb = CG.cg_abb SET IT.sale_price = CG.discount_price WHERE CG.sale_flag = 2')
conn.commit()
cur.execute('UPDATE items as IT INNER JOIN item_cg as CG ON IT.cg_abb = CG.cg_abb SET IT.selling_price = IT.sale_price WHERE CG.sale_flag = 2')
conn.commit()
cur.execute('UPDATE items as IT INNER JOIN item_cg as CG ON IT.cg_abb = CG.cg_abb SET IT.selling_price = IT.list_price WHERE CG.sale_flag is NULL')
conn.commit()
