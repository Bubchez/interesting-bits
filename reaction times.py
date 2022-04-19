# this was a big school project so has no real purpose
# the focus was on array manipulation

import random

student_count = 50
ages = (12, 13, 14, 15, 16)
min_reaction = 0.01
max_reaction = 0.7
saturn = []
mars = []
houses = ('saturn', 'mars')


# randomly create data for saturn and mars
def create_data():
    for i in range(student_count):
        house = random.choice(houses)
        if house == 'saturn':
            age = random.choice(ages)
            reaction_time = round(random.uniform(min_reaction, max_reaction), 3)
            saturn.append([age, reaction_time])
        elif house == 'mars':
            age = random.choice(ages)
            reaction_time = round(random.uniform(min_reaction, max_reaction), 3)
            mars.append([age, reaction_time])


# input any more data values manually
def add_data():
    while True:
        try:
            entry_count = int(input('\nhow many entries would you like to make?: '))
            break
        except:
            print('\nplease enter a valid number')

    for i in range(entry_count):
        count = 0
        # using count lets the code jump straight back to where it was after it breaks due to an invald input
        while True:
            if count == 0:
                house = input('\nwhat house is this child in?: ')
                if house in houses:
                    count += 1
                else:
                    print('\nplease enter a valid house')

            elif count == 1:
                try:
                    age = int(input('how old is this child?: '))
                    if age in ages:
                        count += 1
                    else:
                        print('\nplease enter a valid age\n')
                except:
                    print('\nplease enter a valid age\n')

            elif count == 2:
                try:
                    reaction_time = round(float(input('to 3dp, what was their reaction speed?: ')), 3)
                    if min_reaction <= reaction_time <= max_reaction:
                        if house == 'mars':
                            mars.append([age, reaction_time])
                            break
                        elif house == 'saturn':
                            saturn.append([age, reaction_time])
                            break
                    else:
                        print('\nplease enter a valid time\n')
                except:
                    print('\nplease enter a valid time\n')


def house_stats(house):
    # average for the houses
    mean = 0
    for i in range(len(house)):
        av_time = house[i][1]
        mean += av_time

    tot_average = mean / len(house)
    return round(tot_average, 3)


def spec_data():
    # prints data specified by inputted data
    divisor = 0
    while True:
        house = input('\nwhich house?: ')
        if house == 'mars':
            house = mars
            break
        elif house == 'saturn':
            house = saturn
            break
        else:
            print('\nplease input a valid house')

    while True:
        try:
            age = int(input(f'which age group would you like to target?: '))
            if age in ages:
                av_age = 0
                for i in house:
                    age_time = i[1]
                    if i[0] == age:
                        av_age += i[1]
                        divisor += 1
                    else:
                        continue
                break
            else:
                print('\nplease enter a valid age\n')
        except:
            print('\nplease enter a valid age\n')

    slowest = 0.001
    for i in house:
        age_time = i[1]
        if i[1] > slowest:
            slowest = i[1]

    print(f'\nthe average for that age is {round((av_age / divisor), 3)}')
    print(f'the slowest time for that age was {slowest}')


def main():
    create_data()
    while True:
        while True:
            choice = input('press 1 to view house stats\n2 to view specific stats\n3 to add new data\n: ')
            if choice == '1':
                print(f'\nthe average time for mars was {house_stats(mars)}')
                print(f'the average time for saturn was {house_stats(saturn)}')
                break
            if choice == '2':
                spec_data()
                break
            if choice == '3':
                add_data()
                print(saturn, '\n', mars)
                break
            else:
                print('\nplease enter a valid input\n')

        if input('\nreturn to menu? y/n: ') == 'n':
            break
        else:
            print('\n')
            continue


main()
