#密碼重試程式
#password = 'a123456'
#讓使用者重複輸入密碼
#最多輸入三次
#如果正確就印出 "登入成功!"
#如果不正確就印出 "密碼錯誤! 還有__次機會!"

password = 'a123456'
t = 3
while True:
	pwd = input('Please key in the password : ')
	if pwd == password:
		print('Sign in suceesfully!')
		break #escape the loop
	else:
		t = t - 1
		print('Wrong Password', t, 'chances lift')
		if t < 1:
	            print('Congratulations to the locked account!!!')
	            break

#password = 'a123456'
#i = 3
#while i > 0:
#    pwd = input('Please key in the password : ')
#    if pwd == password:
#        print('Sign in suceesfully!')
#        break
#    else:
#        i = i - 1
#        print('Wrong Password!', i, chances left)
