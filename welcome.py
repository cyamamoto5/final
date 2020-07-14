print ("--------------")
print ("★ようこそ、VV商店へ★")
print ("--------------")
print ("ログイン画面へ進むには１を\n新規登録画面へ進むには２を入力してください")
print ("--------------")

def error1():

    input1_str = input ("入力：")
    while True:
        if input1_str== "1" or input1_str== "2" or input1_str== "１" or input1_str== "２":
            input1 = int (input1_str)
            return(input1)
            break
        else:
            print("入力方法が間違っています。指定された数字で入力してください")
            print ("--------------")
            input1_str = input ("入力：")

error_input1 = error1()

def output1(error_input1):
    if error_input1 == 1:
        print ("ok")
    elif error_input1 == 2:
        print ("oKKKKKKKK")


output1(error_input1)
