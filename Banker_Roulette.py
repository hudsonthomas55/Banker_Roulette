
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
    # Get the total number of names
number_people = len(names)
    # Pick random person assigned to a number in queue or list
random_choice = random.randint(0,number_people -1)
    #print(random_choice) # To determine number
    # Relate random choice to name
who_pays = names[random_choice]


message = f"{who_pays} is going to buy the meal today!"
print(message)