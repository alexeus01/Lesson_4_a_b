## 1
#  Try this:
# colors = ["red", "orange", "yellow"]
# for color in colors:
#     print("Here is a color that I know:")
#     print(color)
#     print()
# print("-----------------------")
# print("The for-loop has ended.")

## 2
#  This is a way to imagine how the code above works.
# colors = ["red", "orange", "yellow"]

# color = colors[0]
# print("Here is a color that I know:")
# print(color)
# print()

# color = colors[1]
# print("Here is a color that I know:")
# print(color)
# print()

# color = colors[2]
# print("Here is a color that I know:")
# print(color)
# print()

# print("-----------------------")
# print("The for-loop has ended.")

## 3
## Try this:
# # Change it so the name is capitalized when printed without modifying the list.
# names = ["sam", "lisa", "micah", "dave"]
# for name in names:
#     print(f"Hello {name}.")
# print("Welcome to the Python course.")


## 4
## Copy and modify the previous example like so:
## for each name, display "Have a good day, ____. I hope you enjoyed experimenting with python."
## (Fill in the blank with the name.)

## 5
#  Try this:
# ages = [26, 37, 55, 10, 5]
# for age in ages:
#     print(f"One of the people in my list is {age} years old.")
#     print(f"In two years, that person will be {age + 2} years old.")
#     print()


## 6
## Copy and modify the previous example so that for each age,
## it displays "5 years ago, that person was ___ years old."


## 7
## For each of the following numbers, display "Half of __ is ___". For example, "Half of 21 is 10.5"
# numbers = [21, 40, 32, 10, 8, 3]

## 8
## Try this:
# for num in range(1,5):
    # print(num)


## 9
## Copy and modify the previous example to print the numbers 1 to 6.

## 10
# # Try this.
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print(f"The temperature was {temp}")

    
## 11
#  Try this.
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print(f"The temperature was {temp}")
#     if temp > 90:
#         print("That's hot.")


## 12
## Copy and modify the previous question to display the
## temperature and display whether it is above or below freezing.


## 12b
#  Try this to see the impact of indentation. How do you fix it?
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print("Looking at the temperatures.")
# print(f"One of the temperatures in the list is {temp}")
# if temp > 90:
#     print("That's hot.")


# ## 13
# ## Try this:
# x = input("Say a word: ")
# if x.endswith("s"):
#     print("That ends with an 's', so it might be plural.")
# print("That's all I have to say.")


## 14
## Modify the previous example so that if the user input ends with "day",
## then the computer will display "I think that's a day of the week."

## 15
# ## Try this:
# fruits = ["strawberry", "mango", "raspberry", "blueberry", "grape", "melon"]
# berryCount = 0
# for fr in fruits:
#     if fr.endswith("berry"):
#         berryCount += 1
# print("I've finished counting the fruits.")
# print(f"There were {berryCount} that ended with berry.")


## 16
## Using `startswith` (which works quite similarly to endswith),
## count how many of the fruits start with 'm'.
## Then display the count.


## 17
## Given this list, count how many temperatures are above freezing.
## Display the count.
# temps_in_F = [90, 30, 47, 82, 68, 100, 25, 40]


## 18
## Copy and modify the previous example to show the user how many
## temperatures are above freezing and how many are below freezing.

## 19
## Make a list of five names.
## Use a for-loop to display each name capitalized, all-lowercase, and all-uppercase.


## 20
## Copy and modify the previous exercise so that it uses
## `random.sample` to pick only 3 names of the five available names.
## As before, display each name capitalized, all-lowercase, and all-uppercase.
## Do not forget import random as the first line of your code.
##########################
## INSTRUCTOR CHECK
##########################

## 21
## Using the given list.
## Ask the user for a letter.
## Ask the user for a number.
## Create a for loop that finds names that start with the given letter.
## and are longer than the provided number of characters.
## Display any name that meets both criteria (pay attention to capitalization).
## At the end display "Those are the names that meet your criteria."
# actors = ["Timothy", "Arnold", "Jennifer", "Jason", "Sylvester", "Danny", "Bob", "Catherine"]