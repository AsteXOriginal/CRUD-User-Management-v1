array = []

# 1. A function without parameters. Adds a user to the array
def AppendUser():
    user = int(input('Enter number -> '))
    if user in array:
        print('You are already on the list')
    else:
        array.append(user)

# 2. A function without parameters. Changes the user's value if he entered everything and wants to change it
def ChangeUser():
    user = int(input('Enter your number -> '))
    if user in array:
        question = input('Do you want to change the value? ')
        if question.lower() == 'yes':
            newUser = int(input('Enter your number -> '))
            count = array.index(user)
            array[count] = newUser
        else:
            print('Bye')
    else:
        print('Error')

# 3. A function without parameters. Removes the user from the list, if it is there
def RemoveUser():
    user = int(input('Enter your number -> '))
    if user in array:
        question = input('Do you want to delete the value? ')
        if question.lower() == 'yes':
           array.remove(user)
        else:
            print('Bye')
    else:
        print('Error')
   
# 4. A function without parameters. Displays the entire list
def PrintAll():
    for i in range(len(array)):
        print(f"Index [{i}] = {array[i]}")

# 5.                
def main():
    while True:
        print("*1* - AppendUser\n*2* - ChangeUser\n*3* - RemoveUser\n*4* - PrintAll\n*0* - exit")         
        check = int(input("-> "))
        if check == 1:
            AppendUser()
        if check == 2:
            ChangeUser()
        if check == 3:
            RemoveUser()
        if check == 4:
            PrintAll()
        elif check == 0:
            break

main()
