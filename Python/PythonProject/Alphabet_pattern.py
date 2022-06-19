# def alphbet_pattern():
import ipdb
ipdb.set_trace()
print("Enter number between 7 to 26 for Print  A to Z ,Recommend  Try 7 number, it  will give nice A to Z Triangle)")
print()
number_of_line = int(input("Enter number between 7 to 26 -- "))
print()

i = 1

# ascii code of A to Z is 65 to 90
char = 65

# outer loop
while i <= number_of_line:

    temp = char
    j = 1

    # Inner Loop
    while j <= i:
        if temp < 91:
            print(chr(temp), end=" ")

            # Main logic
            temp = temp + number_of_line - j

            j += 1
        else:
            break

    print()
    char += 1
    i += 1


# alphbet_pattern()
