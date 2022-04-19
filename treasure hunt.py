# this was a big school project

from random import randrange
from math import ceil, sqrt

#this function creates and displays the grid
def print_grid(g, size, show):
    print(' ', end=' ')
    for count in range(size):
        print(count, end=' ')
    print()
    count = 0
    for row in g:
        print(count, end=' ')
        count += 1
        for col in row:
            #controls whether the grid displays the positions of the treasure and skeletons or not
            if show == True:
                print(col, end=' ')
            else:
                if col == '@' or col == '/':
                    print('.', end=' ')
                else:
                    print(col, end=' ')

        print()

#this function creates and places the specified amounts of treasure and skeletons onto the grid
def setup(g, size):
    global treasure_pos
    global treasure_poslist
    global skel_poslist
    global tres_count
    show = False
    treasure_poslist = []
    skel_poslist = []
    ts_show = input('show skeletons and treasure? y/n: ')

    if ts_show == 'y':
        show = True
    else:
        show = False

    #begin generating and placing skeletons
    s = True
    while s:
        s_numb = int(input('how many skeletons?: '))
        if s_numb >= (size ** 2):
            print('sorry! please have less skeletons than the amount of space available!')
        else:
            s = False
    for i in range(s_numb):
        s_run = True

        while s_run:
            #looping and checking to see if the newly assigned position is equal to a currently filled position, and if so it regenerates the position
            #for i in range(len(skel_poslist)):
            skel_pos = [randrange(0, size), randrange(0, size)]
                #print(skel_poslist)
            if skel_pos not in skel_poslist:
                skel_poslist.append(skel_pos)
                break

        if show == True:
            g[skel_pos[1]][skel_pos[0]] = '/'

        skel_poslist.append(skel_pos)

    #begin generating and placing treasure
    t = True
    while t:
        tres_count = int(input('how much treasure?: '))

        if tres_count >= (size ** 2) - ((len(skel_poslist) // 2) - 1):
            print('sorry! please have less treasure than the amount of space available!')
            print(tres_count, (len(skel_poslist) // 2))
        elif tres_count == 0:
            print('sorry, please have at least 1 treasure!')
        else:
            t = False
    for i in range(tres_count):
        for i in range(tres_count):

            # looping and checking to see if the newly assigned position is equal to a currently filled position, and if so it regenerates the position
            t_run = True
            while t_run:
                treasure_pos = [randrange(0, size), randrange(0, size)]
                    #print(skel_poslist)
                if treasure_pos not in treasure_poslist:
                    if treasure_pos not in skel_poslist:
                        treasure_poslist.append(treasure_pos)
                        break

            if show == True:
                for loc in treasure_poslist:
                    g[loc[1]][loc[0]] = '@'
        return show
        treasure_poslist.append(treasure_pos)



#this function works out how far away the nearest treasure is to the most recently dug hole
def distance(x_cord, y_cord):
    lowest = 100
    for i in range(len(treasure_poslist)):
        for loc in treasure_poslist:
            a = sqrt((x_cord - loc[1]) ** 2 + (y_cord - loc[0]) ** 2)
            if a < lowest:
                lowest = a
                #print(lowest)

    return lowest

#this function takes dig inputs and checks whether you have hit a skeleton or treasure, and subsequently if you have won or lost the game
def game(g):
    global x_cord
    global y_cord
    global tres_count
    global run_hint
    #print(tres_count)
    #print(skel_poslist)
    #print(treasure_poslist)
    a = False
    b = False
    y_cord = 0
    x_cord = 0
    #print(skel_poslist)
    #print(treasure_poslist)
    #sets dig position
    y_cord = int(input('input your col cord to dig at: '))
    x_cord = int(input('input your row cord to dig at: '))

    tres_found = []
    state = 0
    #removes a skeleton from the grid if you hit it
    for i in range(len(skel_poslist)):
        for loc in skel_poslist:
            if x_cord == loc[1] and y_cord == loc[0]:
                b = True
                skel_poslist.remove(loc)

    if b == True:
        print('oh no! you were killed by a skeleton on your adventure :(')
        state = -1
        print("""
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠛⢻⣿⣯⣿⣿⣿⣶⣶⣶⣶⣤⣤⣤⣀⠄⠄
⠄⠄⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄
⠄⠄⠄⠄⠄⠄⠈⠻⣿⡛⠉⠭⠉⠉⢉⣿⣿⣧⠄⠄
⠄⠈⠙⠲⣶⠖⠄⠄⢿⣿⠄⠶⣶⣾⣿⣿⣿⣿⣧⠄
⠄⠄⠄⠄⠈⠄⠄⠄⠺⢿⡗⠄⣹⣿⣿⠿⣟⣿⡏⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠤⠤⢾⣿⣿⣿⣦⠘⡿⠄⠄
⠄⠄⠄⠄⠄⠄⠈⢻⡿⣷⣶⣶⣤⣤⣤⣶⣦⠁⠄
⠄⠄⠄⠄⠄⠄⠄⣽⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠘⠿⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄
        """)

    # removes the position of the treasure if you hit it
    for i in range(len(treasure_poslist)):
        for loc in treasure_poslist:
            if x_cord == loc[1] and y_cord == loc[0]:
                a = True
                treasure_poslist.remove(loc)

    if a == True:
        print('you found a treasure!')
        run_hint = False
        tres_count = len(treasure_poslist)
        g[x_cord][y_cord] = '@'
    #win the game when there are no more treasures on the grid
    if tres_count == 0:
        print('you managed to avoid all the skeletons and found the treasure!')
        state = 1
        print("""\
     ⠀⠀⠀⣤⣶⣶⡶⠦⠴⠶⠶⠶⠶⡶⠶⠦⠶⠶⠶⠶⠶⠶⠶⣄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⣀⣀⣀⣀⠀⢀⣤⠄⠀⠀⣶⢤⣄⠀⠀⠀⣤⣤⣄⣿⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⡷⠋⠁⠀⠀⠀⠙⠢⠙⠻⣿⡿⠿⠿⠫⠋⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣤⠞⠉⠀⠀⠀⠀⣴⣶⣄⠀⠀⠀⢀⣕⠦⣀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⣤⠾⠋⠁⠀⠀⠀⠀⢀⣼⣿⠟⢿⣆⠀⢠⡟⠉⠉⠊⠳⢤⣀⠀⠀⠀
    ⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⢀⣀⣾⣿⠃⠀⡀⠹⣧⣘⠀⠀⠀⠀⠀⠀⠉⠳⢤⡀
    ⠀⣿⡀⠀⠀⢠⣶⣶⣿⣿⣿⣿⡿⠁⠀⣼⠃⠀⢹⣿⣿⣿⣶⣶⣤⠀⠀⠀⢰⣷
    ⠀⢿⣇⠀⠀⠈⠻⡟⠛⠋⠉⠉⠀⠀⡼⠃⠀⢠⣿⠋⠉⠉⠛⠛⠋⠀⢀ ⢀⣿⡏
    ⠀⠘⣿⡄⠀⠀⠀⠈⠢⡀⠀⠀⠀⡼⠁⠀⢠⣿⠇⠀⠀⡀⠀⠀⠀⠀   ⡜⣼⡿⠀
    ⠀⠀⢻⣷⠀⠀⠀⠀⠀⢸⡄⠀⢰⠃⠀⠀⣾⡟⠀⠀⠸⡇⠀⠀⠀   ⢰⢧⣿⠃⠀
    ⠀⠀⠘⣿⣇⠀⠀⠀⠀⣿⠇⠀⠇⠀⠀⣼⠟⠀⠀⠀⠀⣇⠀⠀   ⢀⡟⣾⡟⠀⠀
  ⠀⠀  ⠀⢹⣿⡄⠀⠀⠀⣿⠀⣀⣠⠴⠚⠛⠶⣤⣀⠀⠀⢻⠀  ⢀⡾⣹⣿⠀
    ⠀⠀⠀⠀⢿⣷⠀⠀⠀⠙⠊⠁⠀⢠⡆⠀⠀⠀⠉⠛⠓⠋⠀  ⠸⢣⣿⠏⠀⠀⠀
    ⠀⠀⠀⠀⠘⣿⣷⣦⣤⣤⣄⣀⣀⣿⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣾⡟⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢹⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀

                    """)
    #if nothing has been found then the grid dig position is set to a different character
    else:
        g[x_cord][y_cord] = 'V'
        run_hint = True

    return state

#this function allows the player to use 3 hints and find (using the distance function) how close they are to the treasure
def hint(hints):
    if run_hint == True:
        if hints != 0:
            h_use = input(f'you have {hints} hint(s) remaining, would you like to use one? y/n: ')
            #decreases hint amount and gives a hint
            if h_use == 'y':
                hints -= 1
                distance_ = distance(x_cord, y_cord)

                if distance_ >= 4:
                    print('it seems rather desolate around here...')
                elif distance_ >= 3:
                    print('a clink of gold captures your attention. could you be getting closer?')
                elif distance_ >= 2:
                    print('you can almost smell the tang of gold')
                elif distance_ >= 1:
                    print('it feels as if it could be below your feet...')
        return hints
        print('--------------------------------------\n')

#this function initiates the other functions and makes the game run
def main():
    global hints
    global run_hint
    running = True
    hints = 3
    print(
        'welcome to the treasure hunt! input the coordinates and dig to find the treasure, but watch out for the skeletons!')
    size = int(input('what size grid do you want?: '))
    #labels all the grid positions with a character
    grid = [['.' for x in range(size)] for y in range(size)]
    print('--------------------------------------')

    #gives positions and then prints grid
    show = setup(grid, size)
    print_grid(grid, size, show)

    state = 0
    #loop controlling the game
    while state == 0:
        state = game(grid)

        if state == 0:
            print_grid(grid, size, show)
            hints = hint(hints)

    print_grid(grid, size, True)


main()

