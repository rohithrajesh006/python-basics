

tasks=[]
status_list={1:""}
while True:
    print("    Todo    \n 1.Add task \n 2.Show tasks \n 3.Mark task as done \n 4.show task status \n 5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        my_list=input("Enter the task to add:")
        print("Task added")
        tasks.append(my_list)
        
    elif choice==2:
        for a in tasks:
         print(a,"-->Not done")
    elif choice==3:
        for i in tasks:
            b=str(input(f"{i} --> task done or not done:"))
            if b.lower()=="task done":
              print(f"{i} : {b},good!!")
            elif b.lower()=="not done":
                print(f"{i} : {b},do the task")
            else:
                print("please specify if the task is done or not")
    elif choice==4:
        #status_list.update(":"b")





