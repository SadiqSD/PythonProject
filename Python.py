# Python for non - programmers
#A leader is ment to surffet but as time goes on all the pain will disappere and joy will soon emerge

#You have to do something that will atract the next follower

#'*functions
# orders of number

#let's assume that you make that app and it hold's the data of many people but the on of the poeple in the
#was having 20$ and then he spent some so we could simpy activate it buy doing this below

#let's make some people happy
#
# import random
# random_numbers = random.randint(1,200)
# random = random.randint(1,5)
# random_text = ""
#
# if random == 1:
#     random_text = f"you're the most butifull person i have ever seen you you smile."
# if random == 2:
#     random_text = f"Keep smiling, because life is a beautiful thing and there's so much to smile about."
# if random == 3:
#     random_text = f"Life is either a daring adventure or nothing at all. your luck number"
# if random == 4:
#         random_text = f"You own your own happiness, so don't let people control you"
# if random == 5:
#     random_text = f"Many people will not belive in you but makes sure you belive in you"
#
# print(f"{random_text} your lucy number is : {random_numbers}")
#
#


# string = '23 youre amazing'
# print(string.isdigit())
#
#
# fev_movie = ["ironman","spiderman","superman","Dune"]
#
#
# del(fev_movie[0])
# del(fev_movie[0])
# del(fev_movie[0])
#
#
#
# #changing things inside list
#
#
#
#
# print(fev_movie)








#will be updated later

#meaning of the lucky numbers



#strings

#for loop



#dictionary
# name = {"sadiq": 18, "ibrahim":12, "murtala": 44}
# name["musa"] = 24
# name["khalid"] = 22
# print(name)
# print(len(name))
#
# new_dic = {12:True, 67:False}
# new_dic[55] = True
# del (new_dic[12])
# print(new_dic)
# print(len(new_dic))
#

# if you use a len on a strin you definetly counting the numbers not the character



#if you use a len on a dictionary you definetly counting the numbers not the character

# text = """
# a b a a c b
# """
# print(text.split())
#
# word_count = {}
#
# for word in text.split():
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1


#
# print(word_count)


#we are counting the words

text = """
We're not in love
We share no stories
Just something in your eyes
Don't be afraid
The shadows know me
Let's leave the world behind
Take me through the night
Fall into the dark side
We don't need the light
We'll live on the dark side
I see it
Let's feel it
While we're still young and fearless
Let go of the light
Fall into the dark side
Fall into the dark side
Give into the dark side
Let go of the light
Fall into the dark side
Beneath the sky
As black as diamonds
We're running out of time (Time, time)
Don't wait for truth
To come and blind us
Let's just believe their lies
Believe it
I see it
I know that you can feel it
No secrets worth keeping
So fool me like I'm dreaming
Take me through the night
Fall into the dark side
We don't need the light
We'll live on the dark side
I see it
Let's feel it
While we're still young and fearless
Let go of the light
Fall into the dark side
Fall into the dark side
Give into the dark side
Let go of the light
Fall into the dark side
Take me through the night
Fall into the dark side
We don't need the light
We'll live on the dark side
I see it
Let's feel it
While we're still young and fearless
Let go of the light
Fall into the dark side
"""


# word_count = {}
# for word in text.split():
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print(word_count)
#









#challenge
"""create meaning of every letter of your name and when ever printed,
 print the letter which each of the meaning with it"""




#small lib doc
#the int oprator
"""The in operator checks, True or False, if something appears anywhere in a string. In this and other string comparisons, characters much 
match exactly, so 'a' matches 'a', but does not match 'A'.(Mnemonic: this is the same word "in" as used in the for-loop.)"""

# #fuction
# def string(name):
#     return name.upper()
#
#
# #return in function
# list = ["sadiq","murtala","ibrahim"]
# for name in list:
#     print(string(name))
#
# comment
# I know how to do this nick, am happy
"""This is why i love python wllh """

#input

# some_text = input("input some text ")
# prompt = input("enter 1 to uppercase or two to lowercase ")
#
# if prompt == "1":
#     print(some_text.upper())
# elif prompt == "2":
#     print(some_text.lower())


# python how do computer's read function
# A function that can cheack the len of your name


# functions for len
# functions for randomizing object either number or letters

#len
# def len(name):
#     return len(name)
# name_return = len("ibrahim")
#
#
# user = input("what is your name? ")
# print(name_return(user))

# guesing game
import random
import time
print("Hi am going to pick a number between 1 and 100")
time.sleep(2)
print("Picking a number...")
time.sleep(2)
guess = int(input("what is your guess? "))
guess_count = 1
correct_number = random.randint(1,100)

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("you need to guess heigher: "))
    else:
        guess = int(input("you need to guess lower"))

print(f"congrat, The right answer was {correct_number} and it took you {guess_count} guesses")





