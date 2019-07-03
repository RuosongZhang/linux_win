cunkuan = int(input("Please input your money in bank:\n"))
zizhu = int(input("Please input your dad give your money:\n"))
cunkuan = cunkuan + zizhu 

if cunkuan > 100:
    print("I can buy baoma")
    if zizhu > 50:
        print("so happy, i can buy baoma 740")
    elif zizhu > 30:
        print("i can buy baoma 520")
    elif zizhu > 20:
        print("i can buy baoma 320")
    else:
        print("goto retake some car")
elif cunkuan > 50:
    print("I can buy fengtian")

elif cunkuan > 20:
    print("I can buy used car")

else:
    print("ride your bad bike")
