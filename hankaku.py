import unicodedata
text = ["Ｃ"]

def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    print(count)

get_east_asian_width_count(text)
