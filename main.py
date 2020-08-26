# a = 10
# n = 20

# # generate a list within a specific range
# num_list = list(range(a, n))
# print(num_list)

# # append a new item to the list
# num_list.append('duck')
# print(num_list)


# a function that takes input from a user to append a new item to a list
some_list = ['dog', 'cat', 'bear']
print(some_list)

def append_input(a_list):
    b_list = a_list[:]
    b_list.append(input('Enter the new element you would like to append: '))
    return b_list

another_list = append_input(some_list)

print(another_list)


"""The following will give a nested list"""

list1 = [1, 2, 3]
list2 = [3, 4, 5]

list1.append(list2)

# Print the list after the appendation
print(list1)