"""
This calculator can perform any function that python can handle. Additionally, it can graph multiple equations on the same plot.
"""

import matplotlib.pyplot as plt
import numpy as np
import sys

accepted_answers = ['y','n','yes','no']
accepted_yes = ['y','yes']

def graph():
    """
    Graphs various equations based on user input
    """
    answer = "yes"
    counter = 0
    fig, ax = plt.subplots()
    ax.set(title = 'Graph',
            xlim=(-10, 10), xticks=np.arange(-9, 10), xlabel = 'X Axis',
            ylim=(-10, 10), yticks=np.arange(-9, 10), ylabel = 'Y Axis')
    ax.grid()

    while answer in accepted_yes:
        counter += 1
        x = np.arange(-10,11,0.01)
        while True:
            try:
                y = input("Please enter an expression (MUST be in terms of x and only x): ")
                if y == "":
                    sys.exit()
                else:
                    y = eval(y)
                    break
            except Exception as e:
                print(f"Error: {e}\nPlease try again.")

        ax.plot(x,y, label = f'Line {counter}', linewidth = 2, marker = 'o', markevery = 100)
        while True:
            answer = input("Would you like to plot another line? (Y/N): ").strip().lower()
            if answer == "":
                sys.exit()
            elif answer in accepted_answers:
                break
            else:
                print("That is not an accepted answer. Try again.")

    ax.legend()
    plt.show()

def solve():
    """
    Solves an equation based on user input
    """
    while True:
        try:
            solved = input("Please enter an expression: ")
            if solved == "":
                sys.exit()
            else:
                print(f"Answer: {eval(solved)}")
                break
        except Exception as e:
            print(f"Error: {e}")

#starts program
continue_prog = "yes"
while continue_prog in accepted_yes:
    
    answer = input("Would you like to solve an expression or graph equations? (solve/graph): ").lower().strip()
    if answer == "":
        sys.exit()
    elif answer == "graph":
        graph()
    elif answer == "solve":
        solve()
    else:
        print("That is not an accepted answer. Try again.")
        continue

    while True:
        continue_prog = input("Would you like to continue the program? (Y/N): ").strip().lower()
        if continue_prog == "":
            sys.exit()
        elif continue_prog in accepted_answers:
            break
        else:
            print("That is not an accepted answer. Try again.")

    