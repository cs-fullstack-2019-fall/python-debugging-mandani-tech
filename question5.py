# ### Problem 5:
# Create the list: squad = ["One", "Two", "Three", "Four", "Five"]. Print the list in reverse without using a list method.

squad = ["One", "Two", "Three", "Four", "Five"]
for index in range(len(squad)-1, -1, -1):
    print(squad[index])

    #error fixed syntax error for was suppose to be in
    # square brackets for index of an array