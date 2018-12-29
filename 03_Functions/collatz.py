def collatz(number):
    number = int(number)
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1



guess = int(input("Please enter a number: "))
try:
    while guess != 1:
        guess = collatz(guess)
        print guess

    print "Congrats! the number equals 1"

except NameError:
    print("Sorry, I didn't understand that.")


