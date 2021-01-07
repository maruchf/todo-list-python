import csv
todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
        str_title=str(title)
        todos.append(str_title)
        print("tu tarea ha sido agregada")    

def print_list():
    global todos
    print(f"Esta es la lista de tareas: Tienes {str(len(todos))} tareas")
    count=1
    for todo in todos:
        print(str(count)+'. '+todo)
        count=count+1

def delete_task(number_to_delete):
    global todos
    new_todos=[]
    number_to_delete=int(number_to_delete)-1
    for i in range(0,len(todos)):
        if i != number_to_delete:
            new_todos.append(todos[i])
    todos=new_todos    

def save_todos():
    # your code here
    pass

    
def load_todos():
    # your code here
    pass

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")