# this was a school project so has no real purpose


groups = ['A', 'B', 'C', 'D', 'E']
votedID = []
tutorGroups = []
candidates = []
abstainCount = 0


def election(candidates):
    # collect votes
    abstainCount = 0
    votedID = []
    for i in range(3):
        # create gap between votees
        print('\n' * 5)
        while True:
            # check id
            while True:
                # chceck id of student
                studentID = input('enter student ID: ')
                print()
                if studentID in votedID:
                    # chceck to see if that id has already been used
                    print('please use a different ID\n')
                else:
                    break
            if studentID not in votedID:
                # stop id being used again
                votedID.append(studentID)
                while True:
                    print('vote 0 to abstain from voting')
                    for ii in range(len(candidates)):
                        # print all of the candidates and the number to enter to vote for them
                        print(f'vote {ii + 1} for {candidates[ii][0]}')

                    try:
                        vote = int(input('\ncast vote: '))
                        print()
                        if vote == 0:
                            abstainCount += 1
                            break
                        elif 1 <= vote <= (len(candidates) + 1):
                            # adds a vote to that candidate's index position within the array
                            candidates[vote - 1][1] += 1
                            break
                        else:
                            print('please enter a valid vote\n')
                    except:
                        print('please enter a valid vote\n')
            break
    return abstainCount


# create tutor groups
for i in range(7, 12):
    for g in groups:
        tutorGroups.append(str(i) + g)

# validate tutor group
while True:
    userGroup = input('enter your tutor group: ')
    if userGroup.upper() in tutorGroups:
        break
    else:
        print('invalid tutor group, please re-enter\n')

# validate student count
while True:
    try:
        studentCount = int(input('how many students in your group?: '))
        if 28 <= studentCount <= 35:
            break
        else:
            print('invalid pupil count, please re-enter\n')
    except:
        print('invalid pupil count, please re-enter\n')

# validate number of candidates and input their names
while True:
    try:
        candidateCount = int(input('how many candidates in your group?: '))
        if isinstance(candidateCount, int):
            if 1 <= candidateCount <= 4:
                candidates = []
                for i in range(candidateCount):
                    candidateNames = input('please input each candidate name: ')
                    candidates.append([candidateNames, 0])
                if input('is this information correct? y/n: ') == 'y':
                    break
                else:
                    continue
            else:
                print('invalid candidate count, please re-enter')
    except:
        print('invalid candidate count, please re-enter: ')


abstainCount = election(candidates)
while True:
    maxList = []
    winners = []
    highest = 0
    for i in candidates:
        # find the highest number of votes between the candidates
        x = i[1]

        maxList.append(x)
        highest = max(maxList)

    for i in candidates:
        # find the candidates with the highest vote
        if i[1] == highest:
            winners.append(i[0])

    totalVotes = studentCount - abstainCount

    print(f'\nvotes for {userGroup}:')
    for i in range(len(candidates)):
        # statistics for class vote
        print(f'{candidates[i][0]} received {candidates[i][1]} votes')
        try:
            p = (candidates[i][1] / totalVotes) * 100
            percentage = '{:.2f}'.format(p)
            print(f'with a vote percentage of {percentage}%\n')
        except:
            print('with a vote percentage of 0%\n')

    print(f'the number of votes cast was {totalVotes}\nthe number of abstentions was {abstainCount}')

    if len(winners) == 1:
        # if there is only one winner then end the program
        print(f'the candidate with the most votes is {winners[0]}')
        break

    else:
        # print out all the winners
        print('\nthe candidates with the most votes are: \n')
        for i in winners:
            print(f'{i}\n')

        # rerun in event of tie
        print('\ndue to a tie, the election will be rerun\n')

        for i in range(4):
            # remove candidates who did not tie
            for ii in range(len(candidates)):
                try:
                    x = candidates[ii]
                    if x[1] != highest:
                        del candidates[ii]
                except:
                    print()

        for i in range(len(candidates)):
            # clear all of the current scores for the re run
            candidates[i][1] = 0
        abstainCount = election(candidates)
