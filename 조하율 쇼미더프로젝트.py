import random
import time

a=[1,2,3,4,5,6,7,8,9]
b= random.choices(a,weights=[1,1,1,1,10,1,3,2,1],k=4)
print(b)
k= '1'

while  k != 'EOF' :
    time.sleep(1)
    d=int (input("몇개를 사실건가요\n"))

    for i in range (d) :
        c=random.choices(a,weights=[1,1,1,1,10,1,3,2,1],k=4)
        if c != b:
            print("꽝")
        if c == b:
            print("당첨")
    k=input("나가시려면 EOF를 누르세요\n")
