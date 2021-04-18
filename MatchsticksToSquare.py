class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if(len(matchsticks)<4):
            return False
        if(sum(matchsticks)%4!=0):
            return False
        max1 = sum(matchsticks)//4
        matchsticks.sort()
        def square(matchsticks, sides):
            if(len(matchsticks)==0):
                if(len(set(sides))==1):
                    return True
                else:
                    return False 
            t = matchsticks.pop()
            for i in range(0,4):
                sides[i]+=t
                if(sides[i]<=max1):
                    k = square(matchsticks,sides)
                    if(k==True):
                        return True
                sides[i]-=t
            matchsticks.append(t)
            return False
        
        
        return square(matchsticks, [0 for i in range(0,4)])
                    
