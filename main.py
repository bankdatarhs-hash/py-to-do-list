import json
import os
from time import sleep

on = False

FILE_PATH = 'tasks.json'

if os.path.exists(FILE_PATH): 
    print(f'Loading tasks from {FILE_PATH}...')
    sleep(2) # Load tasks dari json
    print('Tasks Loaded')
    on = True
    with open(FILE_PATH, 'r') as file:
        tasks = json.load(file)
else:
    tasks = [];

while on :
    sleep(0.5)
    print("\nMenu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Done")
    print("5. Update Task")
    print("6. Exit")
    print()
    choice = input("Enter your choice: ")
    if choice == "1": # liat tasks
        print('Tasks:')
        for i in tasks: 
            status = "Done" if i['done'] else "Not Done" # cek status task
            print(f"{tasks.index(i)+1}. {i['task']} - {status}") # print task + status
    elif choice == "2": # tambah task
        task = input ("Enter the task: ")
        tasks.append({"task": task, "done": False}) # tambah task ke list
        with open(FILE_PATH, 'w') as file:  # simpan ke json aa
            json.dump(tasks, file, indent=4)
        print("Task is successfully added!") # status udh ketambah atau enggak
    elif choice == "3": # hapus task
        print('Current Tasks:')
        for i in tasks: # print tasks sekarang
            status = "Done" if i['done'] else "Not Done"
            print(f"{tasks.index(i)+1}. {i['task']} - {status}")
        task_number = input("Enter the task number to remove: ")
        if task_number.isdigit() and 1 <= int(task_number) <= len(tasks): # kalau input vaild boleh gak valid keluar
            removed_task = tasks.pop(int(task_number) - 1) # hapus task dari list, -1 karena index mulai dari 0
            with open(FILE_PATH, 'w') as file: # save json biasalah
                json.dump(tasks, file, indent=4)
        print("Task is successfully removed!")
        sleep(0.5)
        print('Updated Tasks:')
        for i in tasks: # print sisa tasks
            status = "Done" if i['done'] else "Not Done"
            print(f"{tasks.index(i)+1}. {i['task']} - {status}")
    elif choice == "4": # nandain task selesai
        print('Current Tasks:')
        for i in tasks: # print tasks sekarang
            status = "Done" if i['done'] else "Not Done"
            print(f"{tasks.index(i)+1}. {i['task']} - {status}")
        task_number = input("Enter the task number to mark as done: ")
        if task_number.isdigit() and 1 <= int(task_number) <= len(tasks): # kalau input vaild boleh gak valid keluar
            tasks[int(task_number) -1]['done'] = True # tandain task selesai, -1 karena index mulai dari 0
            with open(FILE_PATH, 'w') as file: # save json AAAAAAAAAAAAAAAAAAAAA
                json.dump(tasks, file, indent=4)
        print("Task is successfully marked as done!")
    elif choice == "5": # update task
        print('Current Tasks:')
        for i in tasks: # print tasks sekarang
            status = "Done" if i['done'] else "Not Done"
            print(f"{tasks.index(i)+1}. {i['task']} - {status}")
        task_number = input("Enter the task number to update: ")
        if task_number.isdigit() and 1 <= int(task_number) <= len(tasks): # kalau input vaild boleh gak valid keluar
            new_task = input("Enter the updated task: ")
            tasks[int(task_number) -1]['task'] = new_task # update task, -1 karena index mulai dari 0
            with open(FILE_PATH, 'w') as file: # save json AAAAAAAAAAAAAAAAAAAAA
                json.dump(tasks, file, indent=4)
        print("Task is successfully marked as done!")
    elif choice == "6": # keluar
        print("Exiting...")
        sleep(1)
        on = False


