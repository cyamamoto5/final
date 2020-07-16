cart = 'shopping_cart.txt'
l = []

with open(cart, 'r', encoding='utf-8') as q:
    n = 0
    for s_line in q:
        n = n + 1
        print (n,":", s_line.replace("\n", ""))

print ("AAAA")

delete_category = input("カテゴリ - 商品ID：")

with open(cart, mode='r', encoding='utf-8') as q:
    n = 0
    for f_line in q:
        n = n + 1
        if delete_category not in f_line:
            print (n,":", f_line.replace("\n", ""))
            l.append(f_line)


with open(cart, mode='w', encoding='utf-8') as f:
    for d in l:
        f.write("%s" % d)
