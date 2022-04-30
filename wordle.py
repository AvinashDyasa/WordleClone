
from itertools import count
import random
words = []
count = 0
with open('sgb-words.txt') as f:
    for line in f:
        words.append(line.strip('\n'))
random_index = random.randint(0, len(words)-1)
ans = words[random_index]


def ask():
    global guess
    guess = input('''   "*" will represnt correct letter and correct position of the alphabet 
   "-" will represnt correct letter but wrong position of the alphabet
   "_" will represent wrong letter and wrong position of the alphabet 
         Guess:''')


def comp(guess, ans):
    result = []
    global count
    count += 1
    for i in range(5):
        if(guess[i] == ans[i]):
            result.append('*')
        elif(guess[i] in ans):
            result.append("-")
        else:
            result.append("_")
    print(result)
    if count < 6:
        ask()
        check()
    else:
        print("Better luck next time")


def check():
    if(len(guess) == 5):

        if (bool(guess in words) == False):
            print("word is not in dictionary")
        elif guess == ans:
            print("Correct guess")
        else:
            comp(guess, ans)

    elif(count == 6):
        print("Better luck next time")
    else:
        print('Word should be 5 letters long')


ask()
check()
