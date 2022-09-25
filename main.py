# -- IMPORT FUNCTIONS FROM DEDICATED PYTHON FILES -- #
from calculation import *
from graph import *
from solver import *

# -- IMPORT MATPLOTLIB LIBRARY -- #
from matplotlib import *

print('>>>initializing program...')

# -- VARIABLE TELLS THE PROGRAM WHAT MENU IT IS IN -- #
current_menu = 'mm'

# -- PRINT MAIN MENU ITEMS -- #
def print_main_menu():
    current_menu = 'mm'
    return('\n-MAIN MENU- \n1. Calculation \n2. Graph \n3. Solver')

# -- PRINT CALCULATION MENU ITEMS -- #
def print_calculation_menu():
    print('\n- Calculation Mode')
    current_menu = 'calc'
    return('Type your calculation below:')

# -- PRINT GRAPH MENU ITEMS -- #
def print_graph_menu():
    print('\n- Graph Mode')
    current_menu = 'graph'
    return('Write graph equation below:')

def print_solver_menu():
    print('\n- Solver Mode')
    current_menu = 'solver'
    return('Write your equation below:')

# -- ANALYZE USER INPUT -- #
def take_input(userinput):
    if userinput == 'home':
        print_main_menu()
    elif userinput == 'quit':
        print('\n >>>Terminating program...')
        quit()
    else:
        if current_menu == 'mm':
            if userinput == '1':
                print(print_calculation_menu())
                user_in = input()
                take_input(user_in)
            elif userinput == '2':
                print(print_graph_menu())
                user_in = input()
                take_input(user_in)
            elif userinput == '3':
                print(print_solver_menu())
                user_in = input()
                take_input(user_in)
            else:
                print('\nUndefined mode selected. Returning to Main Menu')
                print_main_menu()
                user_in = input()
                take_input(user_in)
        elif current_menu == 'calc':
            user_in = input()
            print('\n' + calcmenu_calculate(user_in))
            user_in = input()
            take_input(user_in)
        elif current_menu == 'graph':
            user_in = input()
            print('\n' + graphmenu_graph(user_in))
            user_in = input()
            take_input(user_in)
        elif current_menu == 'solver':
            user_in = input()
            print('\n' + solvermenu_solve(user_in))
            user_in = input()
            take_input(user_in)
        else:
            print('An unknown error has occured, and Maryam had to terminate. Sorry for the inconvenience')
            print('\n >>>Terminating program...')
            quit()
            
            
print('\nWelcome to Maryam, created by Parsa Farjam \nCurrent Version: 0.0.0 ')

print(print_main_menu())
user_in = input()
take_input(user_in)

# -- LOOP TERMINATES WHEN USER ENTERS QUIT COMMAND -- #
#while True:
#    user_in = input()
#    take_input(user_in)
