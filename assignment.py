"""#arithmatic operator
a = 4
b = 2
print("integert quotient:",a//b)
print("remainder:",a%b)
print("exponential:",a**b)
print("product:",a*b)
print("Division:",a/b)
print("add :", a+b)
print("diff:",a-b)

#assignment operator
a = 6
b = 8
a+=b
print(a)

a=4
b=6
a-=b
b-=a
a/=b
print(a)"""

"""length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)

mark1 = float(input("Enter marks for Kannada: "))
mark2 = float(input("Enter marks for English: "))
mark3 = float(input("Enter marks for Hindi: "))
total = mark1 + mark2 + mark3 
average = total / 3
print("Total Marks :", total)
print("Average Marks :", average)

Principle = float(input("Enter the principle amount:"))
Time = float(input("Enter the time per year:"))
Rate_of_interest = float(input("Enter the Rate of interest:"))
Simple_interest = Principle*Time*Rate_of_interest/100
print("The simple interest is:",Simple_interest)"""

"""a = 6
b = 3
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

Number = float(input("Enter number is:"))
if Number == 100:
    print("The number is equal to 100.")
elif Number > 100:
    print("The number is greater than 100.")
else:
    print("The number is less than 100.")

string1 = input("Enter the string1:")
string2 = input("Enter the string2:")
if len(string1) == len(string2) :
   print("the lenght of both string is equal")
else: 
    print("the lenght of both string is not equal")"""

"""x = 10 
x+=5
x*=2
x-=3
print("The final value is:",x)

num = float(input("Enter a number: "))
a = num
b = num
c = num
a /= 2
print("After /= 2, the value is:", a)
b //= 2
print("After //= 2, the value is:", b)
c **= 2
print("After **= 2, the value is:", c)

fruits = ["apple","orange","pineapple","avacado","mango"]
print("apple" in fruits)
print("mango" in fruits)

word = input("Enter a string:")
print("H" in word)"""

"""list = [1,2,3,4,5]
print(3 in list)
print(7 not in list)

sentence = input("Enter a sentence:")
print("python" in sentence)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)

list1 = [32165]
list2 = [49875]
print("check both list is same or not:",list1 is list2)"""

"""age = int(input("enter your age"))
if age>=18:
    print("you can vote")
else:
    print("you can not vote")


num = int(input("enter your number"))
if num>0 :
    print(f"{num}is positive")
elif num<0:
    print(f"{num}is negative")
else :
    print(f"{num}is equal to zero")"""


"""color = input("Enter light color of traffic light (red,green,yellow): ").lower()
if color=="red":
    print("stop")
elif color=="green":
    print("go")
elif color=="yellow":
    print("wait")
else:
    print("invalid color")

Number = int(input("Guess your number:"))
if Number== 7:
    print("correct! you win!")
elif Number>=7:
    print("Too low!")
else:
    print("Too high!")

Marks = int(input("Enter their marks"))
if Marks>=90:
    print("Grade A")
elif Marks>=75:
    print("Grade B")
elif Marks>=50:
    print("Grade C")
else:
    print("fail")"""

"""n = int(input("Enter the number for factorial series:"))
i = 1
factory = 1
print("factorial series in while loop:")
while i<=n:
    factory = factory * i
    print(f"factorial of {i} = {factory}")
    i = i + 1

n = int(input("Enter the number for factorial series:"))
i = 1
factory = 1
print("factorial series in for loop:")
for i in range(1,n+1):
    factory = factory * i
    print(f"factorail of {i} = {factory}")"""

"""n = 1 
while n<=10:
    num = int(input("Enter number:"))
    if num %2==0:
        print(f"{num}is even")
    else:
        print(f"{num}is odd")"""


"""import random
print("WELCOME TO THE GAME CALLED ('Rock🪨', 'Paper📄', 'Scissors✂️')")
print("ARE YOU READY TO PLAY A CLASSIC GAME")
print("Here are the rules:")
print("Rock beats Scissors - Scissors beats Paper - Paper beats Rock")
Gamer = input("Enter one of the choice('Rock🪨', 'Paper📄', 'Scissors✂️'):")
computer_choice = random.choice(('Rock' ,'Paper','Scissors'))
print("Your choice =", Gamer)
print("computer_choice =", computer_choice)
if Gamer == computer_choice:
    print("ITS A TIE🤦")
elif Gamer == "Rock" and computer_choice == "Scissors":
    print("ROCK WINS🤷")
elif Gamer == "Scissors" and computer_choice == "Paper":
    print("SCISSORS WINS")
elif Gamer == "Paper" and computer_choice == "Rock":
    print("PAPER WINS🤷")
else:
    print("YOU LOOSE")
    print("THANK YOU FOR PLAYING")

play_again = input("Do yo want to play again: ('Yes'or'No'):")
if play_again != "Yes":
    Gamer = input("Enter one of the choice('Rock🪨', 'Paper📄', 'Scissors✂️'):")
    computer_choice = random.choice(('Rock' ,'Paper','Scissors'))
print("Your choice =", Gamer)
print("computer_choice =", computer_choice)
if Gamer == computer_choice:
    print("ITS A TIE🤦")
elif Gamer == "Rock" and computer_choice == "Scissors":
    print("ROCK WINS🤷")
elif Gamer == "Scissors" and computer_choice == "Paper":
    print("SCISSORS WINS🤷")
elif Gamer == "Paper" and computer_choice == "Rock":
    print("PAPER WINS🤷")
else:
    print("YOU LOOSE")
    print("THANKS FOR PLAYING GOODBYE!")"""


"""import random
print("WELCOME TO THE WORDLE GAME")
print("HERE ARE THE RULES:")
print("The player has to guess a 5 letter word")
print("FEEDBACK :"
"Correct letter in correct place✅")
"Correct letter in wrong place🔁")
"Letter not in the word❌")
 
def get_random_word():

list = ("Horse","Power","Lucky","Grape","Sugar","Trend")
secret_word = random.choice(list)
print("secret_word (Target):",secret_word)
attempts = 0
maximum_attempts = 6
print("Guess the 5 letter secret word You have 6 attempts.")
feedback = []
Guess = input("Enter a 5 letter word :")
feedback = (Guess,secret_word)
for i in range(5):
        if Guess[i] == secret_word[i]:
            feedback.append("Correct letter✅")
        elif Guess[i] in secret_word:
            feedback.append("Correct letter in wrong place🔁")
        else:
            feedback.append("Letter not in the word❌")
    secret_word feedback"""

          

"""import random
def print_welcome():
    print("Welcome to Wordle game")
    print("Guess the 5-letter word in 6 tries.")
    print("Feedback per letter: Correct = right place✅, Present = wrong place🔁, Absent = not in word❌")
    
WORDS = ["plant", "power", "human", "brush", "flame", "spear","fight"]

def get_random_word():
    return random.choice(WORDS)

def feedback(guess, secret):
    result = []
    for i in range(5):
        if guess[i] == secret[i]:
            result.append("Correct✅")
        elif guess[i] in secret:
            result.append("Present🔁")
        else:
            result.append("Absent❌")
    return result

def play_once():
    secret = get_random_word()
    attempts = 6

    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}/6 Enter a 5-letter word: ")
        if len(guess) != 5 or not guess.isalpha():
            print("Please enter a valid 5-letter word.")
            continue

        fb = feedback(guess, secret)
        print("Feedback:", " | ".join(fb))

        if guess == secret:
            print("You guessed the word!")
            return

    print(f"Out of tries! The word was: {secret}")

def main():
    print_welcome()
    while True:
        play_once()
        again = input("Play again? (yes/no): ")
        if again != "y":
            break

if __name__ == "__main__":
    main()   """

"""def greet_user(name, greeting='Hello'):
    print(f"{greeting}, {name}!")
greet_user("Pavan")
greet_user("Preetham","Hi")    

def power(base, exponent=2):
    return base ** exponent
print(power(9))   
print(power(4,4))

def student_info(name, age, grade):
    print(f" Name:{name},Age: {age},Grade : {grade}")
student_info(name ="Abhi", age =15 , grade = "9th")

def book_info(title, author, price):
    print(f" title :{title},{author},{price}")
book_info("The time machine", author = "Wells", price = "1999")

def print_numbers(*args):
    for number in args:
        print(number)
print_numbers(1, 2, 3)

def sum_all(*numbers):
    return sum(numbers)
print(sum_all(4,5,6))

def display_names(*names):
    for names in names:
        print(names)

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
greet(name="Prakash", age=25, city="Mysuru")

def print_student_data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
print_student_data(name="Rahul", age=16, class_="10th", grade="B")

def calculate_bill(**items):
    total = sum(items.values())
    return total
bill = calculate_bill(mango = 50, orange = 30, pineapple = 45)
print("Total bill amount:",bill)

def profile(name, *hobbies, **details):
    print(f"Name: {name}")
    
    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f"- {hobby}")
    else:
        print("No hobbies listed.")
    
    if details:
        print("Details:")
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No additional details.")

profile("Ajay","Reading","Painting",age = 25, city = "Banglore")


def order_summary(customer, items=None, *extras, **order_details):
    print(f"Customer: {customer}")
    
    if items is None:
        print("Items: No items selected")
    else:
        print(f"Items: {items}")
    
    if extras:
        print("Extras:")
        for extra in extras:
            print(f"- {extra}")
    else:
        print("No extras.")
    
    if order_details:
        print("Order Details:")
        for key, value in order_details.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No additional order details.")
order_summary("Vishnu",["Noodle","chats"],"Extra spicy",address = "Mysore", Payment = "cash")"""

"""class tree():
    def init_(self,tree_name):
        self.tree_name = tree_name
    def display(self):
        print(f"{self.tree_name}is a beatiful tree")

class plants(tree):
    def init_(self, tree_name,plants_name):
     super().init_(tree_name)
     self.plants_name = plants_name       

    def display(self):
       super().display()
       print(f" tomato plant is also beatiful{self.plants_name}")
ran = plants("banana","tomato")
ran.display()"""


"""class state:
    def __init__(self,state,district):
        self.state=state
        self.district=district
    def display_info(self):
        print(f"state: {self.state}")
        print(f"district: {self.district}")
my_state=state("Karnataka","Mysore")
my_state.display_info()  

class animal:
    def __init__(self,name,color,food):
        self.name=name
        self.color=color
        self.food=food
    def animal_info(self):
        print(f"My favarite animal is {self.name}\n{self.name} gives us milk, its color is {self.color} and it will eat {self.food}")
fav_animal=animal(name="cow",color="Black and white",food="grass")
fav_animal.animal_info()      

class tree:
    def __init__(self,tree_name,fruit_name,fruit_color):
        self.tree_name=tree_name
        self.fruit_name=fruit_name
        self.fruit_color=fruit_color
    def tree_info(self):
        print(f" There is a {self.tree_name}\n{self.tree_name} tree near my house, and it is filled with full of{self.fruit_name} I will pluked the fruits everytime and its color is {self.fruit_color}")
fav_tree=tree(tree_name="Mango",fruit_name="mango",fruit_color="yellow")
fav_tree.tree_info()"""


def test(x): 
 return x * 2 
print(test(3) + test(2)) 







        





























