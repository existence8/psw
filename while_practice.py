time = 3
time = int(time)
while time > 0:
    password = input('請輸入密碼(最多三次)')
    if password != 'a123456':
        time= time - 1
        print('您還有', time, '次機會')
    else:
        print('登入成功')
        break
        

