def test_config():
    return True

def use_a_while_loop(num):

    counter = 0

    while(counter < num):#boolean expressions while true loops is false stops looping
        print(counter, counter < num, 'Hello')

        counter = counter + 1
        if(counter == 3):
            print(counter, counter < num, '')


def get_sum_of_squares(num):
    
    sum = 0

    while(num > 0):
        sum = sum + num * num
        num = num - 1 

    return sum

def display_menu():
    print('1-Use a while loop')
    print('2-Sum of squares')
    print('3-Exit')

def run_menu():
    user_option = '0'

    while(user_option != '3'):

        display_menu()

        user_option = input("Enter a menu option(1,2,3): ")

def handle_menu(user_option):

    if(user_option == '1'):
        num = input("Enter a number: ")
        result = use_a_while_loop
    elif(user_option == '2'):
        num = input("Enter a number")
        result = get_sum_of_squares(int(num))
        print ("Get sum of squares: ", result)
    elif(user_option == '3'):
        print
