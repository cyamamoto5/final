def error1():
    input1_str = input ("入力：")

    while True:
        if input1_str== "1" or input1_str== "2" or input1_str== "１" or input1_str== "２":
            print ("right")
            break
        else:
            print("入力方法が間違っています。指定された数字で入力してください。")
            print ("--------------")
            input1_str = input ("入力：")

            while True:
                if input1_str.isdecimal() == True:
                    break
                else:
                    print("入力方法が間違っています。数字で入力してください")
                    print ("--------------")
                    input1_str = input ("入力：")

error1()
