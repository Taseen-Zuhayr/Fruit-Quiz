import random

class fruitquiz:
    def __init__(self):
        self.fruits = { 'apple' : 'red',
                        'mango' : 'yellow',
                        'watermelon' : 'green',
                        'banana': 'yellow'}

    def quiz(self):
        while True:
            fruit,color = random.choice(list(self.fruits.items()))
            print("What is the colour of the",fruit)
            user = input("Enter answer: ")
            if user.lower() == color:
                print("Correct answer!!!")
            else:
                print("Wrong Answer!")
                option = int(input("1-stop, 0-continue: "))
                if option:
                    break

fq = fruitquiz()
fq.quiz()