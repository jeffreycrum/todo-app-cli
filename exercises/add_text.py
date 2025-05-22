# user_input = input("Add a new member: ") + "\n"
# file = open("../files/members.txt", "r")
# users = file.readlines()
# file.close()
# 
# users.append(user_input + "\n")
# 
# f = open("../files/members.txt", "w")
# f.writelines(users)
# f.close()

numbers = [10.1, 12.3, 14.7]
numbers = [int(item) for item in numbers]
print(numbers)