#数学问题解决方案
print('welcome')
print('Mathematical problem solving scheme')
print('单位转换输入1\n')
choie1 =int(input('请输入需要的功能：'))

if choie1 ==1:
	print('需要转换功能：人民币输入1\n面积转换输入2\n时间转换输入3\n质量转换输入4\n')
	choie = int(input('需要使用的功能输入数字即可:'))

	if choie == 1:#人民币转换
		print('欢迎使用人民币转换')
		money = int(input('需要转换:角到分输入1\n元到角输入2\n元到分输入3\n'))
		if money ==1:
			Angle = float(input('需要转换角个数：'))
			Score = Angle * 10
			print("%0.2f角等于%0.2f分" %(Angle,Score))
		elif money ==2:#元到角
			yuan = float(input('需要转换元：'))
			angle = yuan*10#元 *10 = 角
			print("%0.2f元等于%0.2f角" %(yuan,angle))
		elif money ==3:#元到分
			yuan1 =float(input('需要转换元：'))
			score = yuan1 *100#分 =元*100#分小写
			print("%0.2f元等于%0.2f分" %(yuan1,score))
		else:
			print('输入错误')
			

	elif choie ==2:#面积转换
		print('欢迎收益面积转')
		print('平方厘米转平方毫米输入1\n平方分米转平方厘米输入2\n平方米转平方分米输入3\n公顷转平方米输入4\n平方千米转公顷输入5\n')
		Area = int(input('需要转换的功能：'))
		if Area ==1:
			Cm = float(input('转换平方厘米：'))
			Mm = Cm *100#平方毫米=平方厘米*100
			print("%0.2f平方厘米等于%0.2f平方毫米" %(Cm,Mm))
		elif Area==2:
			Decimeter = float(input('转换平方米：'))
			cm =  Decimeter *100#平方厘米 =平方分米*100
			print("%0.2f平方分米等于%0.2f平方厘米" %(Decimeter , cm))

		elif Area==3:
			Decimeter = float(input('转换平方米：'))
			cm =  Decimeter *100#平方厘米 =平方分米*100
			print("%0.2f平方分米等于%0.2f平方厘米" %(Decimeter , cm))

		elif Area==4:
			Hectare = float(input('转换公顷：'))
			metre1 =Hectare *100#平方米=公顷*100
			print("%0.2f公顷等于%0.2f平方米" %(Hectare , metre1))

		elif Area ==5:
			kilometre = float(input('转换平方千米：'))
			hectare = kilometre *100
			print("%0.2f平方千米等于%0.2f公顷" %(kilometre ,hectare))

		else:
			print('输入错误')
		

	elif choie ==3:#时间转换
		print('''
		1时 = 60分钟
		1分 = 60秒
		1天 = 24小时
		1年 = 12月
		1世纪 = 100年
		''')
		print('欢迎使用时间转换')
		print('反向算法输入1\n正向算法输入2\n')
		choie2 = int(input('需要的功能：'))
		if choie2==1:
			print("输入分钟输入1\n小时输入2\n月输入3\n年输入4\n")
			choice = int(input('需要转换的项目：'))
			if choice==1:
				minute = float(input('输入转换分钟：'))
				hours = minute/60
				print('%0.2f分钟等于%0.2f小时' %(minute , hours))
			elif choice ==2:
				hours1 = float(input('需要转换的小时：'))
				day = hours1/24
				print('%0.2f小时等于%0.2f天' %(hours1 ,day))

			elif choice ==3:
				month =float(input('需要转换月份总数：'))
				year = month/12
				print('%0.2f月份等于%0.2f年' %(month , year))
			elif choice ==4:
				year1 =float(input('需要转换的年份：'))
				century = year1/100
				print('%0.2f年等于%0.2f世纪' %(year1 , century))
			else:
				print('输入错误')
				

		elif choie2 ==2:
			print('小时输入1\n天输入2\n年输入3\n世纪输入4\n')
			choice1 = int(input('需要做的功能：'))
			if choice1 ==1:
				time = int(input('需要转换小时'))
				minute1 = time *60
				print('%d小时等于%d分钟' %(time , minute1))
			elif choice1 ==2:
				day1 = int(input('需要转换的天数：'))
				time2 = day1 *24
				print('%d天等于%d小时' %(day1 , time2))
			elif choice1 ==3:
				year2 = int(input('需要转换的年份总合：'))
				month1 = year2 *12
				print('%d年等于%d月' %(year2 , month1))

			elif choice1 ==4:
				century1 = int(input('需要转换的世纪总和：'))
				year3 = century1 *100
				print('%d世纪等于%d年' %(century1 , year3))

		else:
			print('输入错误')

	elif choie ==4:#质量转换
		print('kg转换g输入1\nkg到公斤输入2\nt到kg输入3\n')
		chant = int(input('需要的功能：'))
		if chant ==1:
			print('kg转换g输入1\ng转换kg输入2\n')
			num = int(input('需要的转换：'))
			if num==1:
				kg = float(input('需要转换的kg数：'))
				g = kg  *1
				print('%0.2fkg等于%0.2fg' %(kg ,g))
			elif num ==2:
				g = float(input('需要转换的g数：'))
				kg = g  *1000
				print('%0.2fg等于%0.2fkg' %(g ,kg))
			else:
				print('输入错误')
			

		elif chant ==2:
			print('kg到公斤输入1\n公斤到kg输入2\n')
			num1=int(input('需要转换的功能：'))
			if num1 ==1:
				kg1 =float(input('转换的公斤数：'))
				gjin = kg1
				print('%0.2fkg等于%0.2f公斤' %(kg1 ,gjin))
			elif num1 ==2:
				gjin1 =float(input('需要转换的公斤数：'))
				kg1 = gjin1
				print('%0.2f公斤等于%0.2fkg' %(gjin1 ,kg1))

			else:
				print('输入错误')

		elif chant ==3:
			print('t到kg输入1\nkg到t输入2\n')
			num2 = int(input('需要的功能：'))
			if num2==1:
				t  = float(input('需要转换的t数：'))
				kg3 =t *1000
				print('%0.2ft等于%0.2fkg' %(t ,kg3))
			elif num2 ==2:
				kg03 = float(input('需要转换的kg数：'))
				t = kg03/1000
				print('%0.2fkg等于%0.2ft' %(kg03 ,t ))
			else:
				print('press enter')

		else:
			print('输入错误')

	
		

		
		
		



	
		
else:
	print('press enter')
input('press enter')





