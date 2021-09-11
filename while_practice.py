time = 3
time = int(time)
while time > 0:
    time= time - 1
    password = input('請輸入密碼(最多三次)')
    if password != 'a123456':
        print('密碼錯誤')
        if time > 0:
            print('您還有', time, '次機會')
        else:
            print('您的帳號已上鎖，請聯絡系統管理員')

    else:
        print('登入成功')
        break
        

