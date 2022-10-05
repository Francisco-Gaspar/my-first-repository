#Exercise 0
i = 0
while i <= 4:
    print("Hello everybody")
    i = i + 1

#exercise 1
beatles = [
    "John",
    "Paul",
    "George",
    "Ringo"]

numbers = [0, 3, -11, 99]

print(type(beatles))
print(len(beatles))
print(beatles[2])

#exercise 2
# %%
#using a while loop
def print_list_with_while(list):
    index = 0

    while index < len(list):
       index = index + 1

guys = ["kiko", "paco", "julien"]
print_list_with_while(guys)

#For loops are more efficient than while loops at interating between list
def print_list_with_for(list):
    for element in list:
        print(element)

print_list_with_for(guys)
# %%
#we can add lists togheter and multiply strings by numbers
ramones = ["Edd", "jonnhie", "Dee-dee", "markee"]
kiko = ["francisco", "gaspar"]

print(ramones + kiko)
ramones[2] = "kiko"
print(ramones)
print(kiko * 2)
# %%
#.append adds someone to a list
coding_club =[]
coding_club.append("kiko")
coding_club.append("johnnie")
print(coding_club
)
# %%
#pop removes something from list
coding_club.pop(1)
print(coding_club)
# %%
#Using previous functions on new lists
print_list(kiko)
# %%