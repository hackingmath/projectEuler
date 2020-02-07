"""Euler 31 with Recursion"""

coins = [200,100,50,20,10,5,2,1]

def find_poss(money,maxcoin):
     """Finds the number of ways to
     make money."""
     output = 0
     if maxcoin == 7: return 1
     for i in range(maxcoin,8):
          if money-coins[i]==0: output += 1
          if money-coins[i]>0:
               output += find_poss(money-coins[i],i)
     return output

print(find_poss(200,0))
