# open a file
josh_file = open("josh.txt", "a")

# write to the file
# josh_file.write("\nPotato on couch")
numbers = [1, 2, 3]
for i in range(len(numbers)):
    num = numbers[i]
    josh_file.write("{}\n".format(num))

josh_file.close()

# read a file
# print(josh_file.read())

# close a file
# josh_file.close()


joe_file = open("joe.txt", "w")
joe_file.write("JOE")
joe_file.close()


# how to read lines from a file in python
new_file = open("new_file.txt")
file_items = new_file.readlines()

for i in range(len(file_items)):
    each_item = file_items[i]
    print("Before: {}".format(each_item))
    each_item[0:-1]
    file_items[i] = each_item[0:-1]
    print(file_items)

# print("These are the file items here: {}".format(file_items))
new_file.close()