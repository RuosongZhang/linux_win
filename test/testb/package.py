print("welcome to the express system")

weight = int(input("please enter weight:\n"))
num = input("please enter local number(01.others;02.dongsansheng/ningxia/qinghai/hainan;03.xinjiang/xizang;04.gangaotai/guowai):\n")

price = 0

if weight >= 3:
    if num == '01':
        price = 10+5*(weight-3)
    elif num == '02':
        price = 12+10*(weight-3)
    elif num == '03':
        price = 20+20*(weight-3)
    elif num == '04':
        price = "error"
        print("please connet company")
    else:
        print('enter wrong')
    

elif weight < 3 and weight > 0:
    if num == '01':
        price = 10
    elif num == '02':
        price = 12
    elif num == '03':
        price = 20
    elif num == '04':
        price = "error"
        print("No mail accepted. i'm sorry")
    else:
        print('enter wrong')

else:
    print('enter wrong')

print("Your package price is " ,price, 'yuan')

