def balanced(n):
    listAns =[]

    def isValid(list, x):
        # create a list where the items of the list are the index of the number in the solution
        indexList = [i for i, e in enumerate(list) if e == x]
        #check if the number is separated by A integers
        if len(indexList) >= 3:
            return False
        if len(indexList)==2 and (indexList[1]-indexList[0]!=x+1):
            return False
        return True

    def solve(ans,n):
        #check if the list size is 2n
        if len(ans)==2*n:
            listAns.append(ans)

        #backtracking
        for i in range(1,n+1):
            temp = ans
            temp.append(i)
            if isValid(temp,i):
                ans = temp
                if solve(ans,n)[0]:
                    return True 
            ans.pop(-1)
        return False, listAns

    x = solve([],n)[1]
    if len(x)==1:
        print(0)
    else:
        print(len(x))
