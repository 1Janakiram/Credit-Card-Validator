# TODO
import math


# getting CC number
def get_CC_num():
    while True:
        n = int(input("Number: "))
        if n > 0:
            return n
            break


# Getting the total sum in Luhn's Algorithm
def total_sum(CC_num):
    a, sum, rsum, count = [0, 0, 0, 0]

    while CC_num > 0:
        a = CC_num % 10
        # count+=1
        # sum of remaining elements
        if count % 2 == 0:
            rsum += a
        # multiplying the elements by 2 and adding the individual digits
        else:
            a = a * 2
            if a > 9:
                isum = 0
                b = a % 10
                isum += b + 1

                a = isum
            sum += a
        CC_num = CC_num // 10
        count += 1

    return rsum + sum


# finding the first two digits
def first_two_digits(CC_num):
    length = math.floor(math.log10(CC_num)) + 1

    return CC_num // (10 ** (length - 2))


a = [13, 15, 16]
CC_num = get_CC_num()
ldigit = total_sum(CC_num) % 10
length = math.floor(math.log10(CC_num)) + 1
# verifying the CC number length
if length in a:
    # Validating the CC number
    if ldigit == 0:
        # checking the Type of card
        if first_two_digits(CC_num) in [34, 37]:
            print("AMEX")
        elif first_two_digits(CC_num) in (x for x in range(51, 56)):
            print("MASTERCARD")
        elif (first_two_digits(CC_num) // 10) == 4:
            print("VISA")
        else:
            print("INVALID")

    else:
        print("INVALID")

else:
    print("INVALID")
