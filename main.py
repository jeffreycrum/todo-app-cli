

def read_todos():
    with open('files/todos.txt', 'r') as file:
        content = file.readlines()
    return content


def write_todos(content):
    with open('files/todos.txt', 'w') as file:
        file.writelines(content)


while True:
    user_action = input("Type add, show, edit, complete, or exit")
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
        if len(user_action) > 3:
            todo = user_action[4:]
        else:
            todo = input("Enter a todo: ") + "\n"
        todos = read_todos()
        todos.append(todo)

        write_todos(todos)
    elif 'show' in user_action:
        todos = read_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}: {item.strip("\n")}")
    elif 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))
        index = number - 1
        new_todo = input("Enter the new todo: ") + "\n"
        todos = read_todos()
        todos[index] = new_todo
        write_todos(todos)
    elif 'complete' in user_action:
        number = int(input("Number of the todo to complete: "))
        todos = read_todos()
        index = number - 1
        removed = todos[index].strip("\n")
        todos.pop(index)
        write_todos(todos)
        print(f"Todo {removed} was removed from the list")
    elif 'exit' in user_action:
        break
    else:
        print("That was not a valid option.")

print("bye Felicia")
