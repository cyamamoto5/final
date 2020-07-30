cart = 'shopping_cart.txt'
list = [0]
with open(cart, 'r', encoding='utf-8') as q:

    for s_line in q:
        list.append(s_line)

print(list[0])
print(list[0])
