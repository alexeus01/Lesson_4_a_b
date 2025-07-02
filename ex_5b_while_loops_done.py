## 1
## Try this.
# count = 10
# print(f"count is {count}.")
# count += 1
# print(f"I changed count. Now, it's {count}.")
# count -= 2
# print(f"I changed it again. Now, it's {count}.")


# ## 2
# ## Modify the above example so it asks the user for a number.


# ## 3
# ## Try this.
# count = 3
# print(count)
# count -= 1
# print(count)
# count -= 1
# print(count)
# count -= 1
# print("Reached zero. Proof:")
# print(count)


## 4
## Let's make the previous example less repetitive.
## Try this:
# count = 3
# while count > 0:
#     print(count)
#     count -= 1
# print("Reached zero. Proof:")
# print(count)


## 5
## Modify the previous example to let the user pick where to start the count.
# x = int(input("Pick a number between 10 and 20: "))
# count = x
# while count > 0:
#     print(count)
#     count -= 1
# print("Reached zero. Proof:")
# print(count)

## 6
## Modify the previous example to display
# x = int(input("Pick a number between 10 and 20: "))
# count = x
# while count > 0:
#     print("Launch in", count)
#     count -= 1
# print("Liftoff")

## "Launch in 3"
## "Launch in 2"
## "Launch in 1"
## "Liftoff!"


## 7
## Try this:
# import time
# print("Start...")
# time.sleep(1)
# print("Done.")


## 8
## Modify the previous example to let the user pick the number of delay seconds.
# import time
# x = int(input("Decide how many seconds the timer should delay: "))
# print("Start...")
# time.sleep(x)
# print("Done.")

## 9
## Modify the earlier "Liftoff" example to add a small delay to make it more fun.
## (It should wait a second after each number is displayed.)
# import time

# x = int(input("Pick a number between 1 and 10: "))
# count = x
# while count > 0:
#     print("Launch in", count)
#     time.sleep(1)
#     count -= 1
# print("Liftoff")

## 10
## Try this.
# keepGoing = "yes"
# while keepGoing == "yes":
#     print("Since the variable keepGoing is still 'yes', I am going to keep going.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, you typed something other than 'yes', so I stopped.")


## 11
## Copy and modify the previous example like so:
## If the user types "y", then keep looping.
# keepGoing = "y"
# while keepGoing == "y":
#     print("Since the variable keepGoing is still 'y', I am going to keep going.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, you typed something other than 'yes', so I stopped.")

## 12
## Try this:
# keepGoing = "yes"
# while keepGoing == "yes" or keepGoing == "y":
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")


# ## 13
# ## Here's another way to do it:
# keepGoing = "yes"
# while keepGoing in ["yes", "y"]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")


# ## 14
# ## Here's the opposite:
# keepGoing = "yes"
# while keepGoing not in ["no", "no thanks"]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")   


## 14b
## This example is functionally equivalent, but uses the `break` approach.
## Notice that this avoids having to initialize a variable before the loop.
# while 2 + 2 == 4:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
#     if keepGoing in ["no", "no thanks"]:
#         break
# print("Ok, stopping.")


## 15
## Copy one of the previous two examples. Change it like so:
## Continue looping if the user types any of these: "hey", "woo", or "yes".
# keepGoing = "yes"
# while keepGoing in ["yes","hey","woo",]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")