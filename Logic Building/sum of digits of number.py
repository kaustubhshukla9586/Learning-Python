num = int(input("Enter Number: ")) # 1234
length = len(str(num))
sum = 0
while num!=0 :
    new = num % 10        # 4 , 3 , 2 , 1
    sum += new            # 0 + 4 = 4 + 3 = 7 + 2 = 9 + 1 = 10
    num = num // 10       # 1234 = 123 ,12 ,1

print(sum)




