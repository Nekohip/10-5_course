import random

zone1 = int(input("輸入最小值"))
zone2 = int(input("輸入最大值"))
x =  random.randint(zone1,zone2)
#print(x)
for i in range(10):
    n=10
    bingo = False
    while True:
        try:
            m=n-i
            num = int(input(f"猜數字--{zone1}~{zone2}，還有{m}次機會: "))
            if num == x :
                print("你猜對了，我的朋友!")
                bingo = True
                break
            if num > x :
                print("猜小一點")
                if num < zone2:
                    zone2 = num-1
            else:
                print("猜大一點")
                if num > zone1:
                    zone1 = num+1
            break
        except Exception as e:
	        print(e)
    if bingo == True :
        break
print(f"結束!答案是{x}")