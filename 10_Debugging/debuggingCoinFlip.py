import random
guess = ''
while guess not in ('heads', 'tails'):
    print("guess the coin toss! Enter heads or tails!")
    guess = input()

toss = random.randint(0,1) # 0 is tails, 1 is heads
if toss == 0:
    toss = "tails"
else:
    toss = 'heads'

if toss == guess:
    print('You got it!')

else:
    print('Nope! You wrong. Play again')
    guess = input()
    if toss == guess: 
        print('You got it!')

    else:
        print('Nope. you are truly awful at guessing.')