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


order_list1 = order_line1.split()
order_list2 = order_line2.split()
order_list3 = order_line3.split()
order_list4 = order_line4.split()
order_list5 = order_line5.split()


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

sum = a*a_num + b*b_num + c*c_num + d*d_num + e*e_num
print(sum)
