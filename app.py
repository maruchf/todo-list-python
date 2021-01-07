import csv
#Abrir un archivo csv para guardar el resultado
todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    """
    Esta función agrega una tarea a la lista todos e informa al usuario que fue agregada
    """
    global todos
    todos.append(title)
    print("Su tarea ha sido agregada")    

def print_list():
    """
    Esta función imprime las tareas agregadas a la lista previmente y le informa el total de tareas guardadas
    """
    global todos
    print("Esta es la lista de tareas:")
    count=1
    for todo in todos:
        print(str(count)+'. '+str(todos[count-1]))
        count=count+1
    print(f"Tareas totales= {str(len(todos))}")

def delete_task(number_to_delete):
    """
    Esta función elimina un elemento específico de la lista
    """
    global todos
    todos.pop(int(number_to_delete)-1)
    print(f"Su tarea {number_to_delete} ha sido eliminada")

    # Indicaciones de Deimian//Otra forma de hacerlo
    # global todos
    # new_todos=[]
    # number_to_delete=int(number_to_delete)-1
    # for i in range(0,len(todos)):
    #     if i != number_to_delete:
    #         new_todos.append(todos[i])
    # todos=new_todos    

def save_todos():
    """
    Esta función guarda las tareas de la lista en "todos.csv"
    """
    global todos
    with open("todos.csv","w",newline='') as f:#Duda: la documentación recomienda dejar newline='' 
        #para que el módulo csv haga el manejo con su propia interpretación "Footnotes 1(1,2): If newline=''
        #is not specified, newlines embedded inside quoted fields will not be interpreted correctly, and on
        #platforms that use \r\n linendings on write an extra \r will be added. It should always be safe 
        # to specify newline='', since the csv module does its own (universal) newline handling." 
        #en ese caso el salto de línea debe interpretarse en delimitador del reader o writer?
        wr = csv.writer(f,delimiter="\n")
        wr.writerow(todos)
        f.close()
    print("Tarea completada la lista ha sido guardada en: todos.csv")

def load_todos():
    """
    Esta función carga elementos en una lista llamada todos a partir del archivo todos.csv
    f hace referencia al csvfile 
    """
    global todos #duda: es necesario poner global en todas las funciones?
    with open('todos.csv', newline='') as f:
        reader = csv.reader(f,delimiter="\n")
        todos.clear()
        for row in reader:
            print(' *****  ' .join(row))
            todos.append(row)
    # cuando imprimo los elementos cargados desde csv aparecen '' y [], esto a qué se debe?

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