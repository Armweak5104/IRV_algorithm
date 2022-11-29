def runoff(voters):
    firstChoice = {}
    iterator = False
    while iterator == False:
        totalVotes = 0
        for i in voters[0]:
            firstChoice[i] = 0
        for i in range(0,len(voters)):
            firsts  = voters[i][0]
            for j in firstChoice.keys():
                if firsts == j:
                    firstChoice[j] += 1
                    totalVotes+=1
        #print(f"////////{firstChoice}")
        for i in firstChoice.keys():
            j = firstChoice[i]
            if j/totalVotes > 0.5:
                iterator = True
                return i
        minval = min(firstChoice.values())
        smallest = [k for k, v in firstChoice.items() if v==minval]
        #print(smallest)
        for i in smallest:
            firstChoice.pop(i)

        if len(firstChoice)== 0:
            iterator = True
            return None

        counter = 0
        while counter < len(voters):
            for i in voters[counter]:
                for j in smallest:
                    if i == j:
                        voters[counter].pop(voters[counter].index(i))
            counter+=1
        for i in voters:
            lists = i
            for j in lists:
                for z in smallest:
                    if j == z:
                        lists.pop(lists.index(j))
