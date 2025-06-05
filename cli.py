import time

import util

while True:
    clock = time.strftime("%b %d, %Y %H:%M:%S")
    print(f"The current time is {clock}")
    user_action = input("Type add <todo>, show, edit <number>, complete <number>, or exit")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]
        todos = util.read_todos('files/todos.txt')
        todos.append(todo + '\n')

        util.write_todos(todos)

    elif user_action.startswith('show'):
        todos = util.read_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}: {item.strip("\n")}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            index = number - 1
            new_todo = input("Enter the new todo: ") + "\n"
            todos = util.read_todos()
            todos[index] = new_todo
            util.write_todos(todos)
        except IndexError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = util.read_todos()
            index = number - 1
            removed = todos[index].strip("\n")
            todos.pop(index)
            util.write_todos(todos)
            print(f"Todo {removed} was removed from the list")
        except IndexError:
            print("There's no item with that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("That was not a valid option.")

print("bye Felicia")
