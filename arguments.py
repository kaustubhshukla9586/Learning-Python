# def voter_id(number,name,age,gender):
#     print("======YOUR VOTER ID======".center(30))
#     print(f"Name: {name}".center(30))
#     print(f"Age: {age}".center(30))
#     print(f"Number: {number}".center(30))
#     print(f"Gender: {gender}".center(30))
#
# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# number=int(input("Enter your number: "))
# gender=input("Enter your gender: ")
# voter_id(number,name,age,gender)


def shivendralodu(n):
    if n == 0:
        return "done"
    else:
        print("n =", n)
        return shivendralodu(n-1)

shivendralodu(10)
