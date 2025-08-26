while True:
    num = input("Enter a number (or q to quit): ")

    if num == "q":
        break

    num = int(num)

    if num <= 1:
        print(num, "is not a prime number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                break
        else:  # this else runs if the loop never breaks
            print(num, "is a prime number")
