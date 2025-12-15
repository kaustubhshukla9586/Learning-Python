num = int(input("Enter a number: ")) #taking input
number = [] #created a list to store all the prime numbers
for n in range(2, num+1): #selected the range 2,num+1 because 1 is divisible by everything and num+1 is there because the upper limit is excluding
    for m in range(2, n): # we have to check the range from (2,i) because in that range we will check if i is a prime number or not
        if n % m == 0: #in this statement we are checking all the numbers between 2,n which is m if its divisible by n, if its perfectly divisible by m then it won't be a prime number
             break # if n is divisible then it is obvious that its not a prime number
    else: #if the condition goes here it means that the break was not triggered just because the break was not triggered its evident that the n is a prime number so we append it into the list
        number.append(n)
# print(*number)
for i in number:
    print(i,end=" ")

# There are two ways to print a list - using the asterik operator or the loop + end method.







