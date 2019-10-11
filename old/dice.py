#!/usr/bin/python
#class Solution:
#    # @param {int} n an integer
#    # @return {tuple[]} a list of tuple(sum, probability)
#    def getd(self, n, sumn):
#        if n == 0 or sumn < n or sumn > n*6:
#            return 0
#        elif n == 1:
#            return 1
#        else:
#            count = self.getd(n-1, sumn-1)+self.getd(n-1, sumn-2)+self.getd(n-1, sumn-3)+self.getd(n-1, sumn-4)+self.getd(n-1, sumn-5)+self.getd(n-1,sumn-6)
#            return count
#    def dicesSum(self, n):
#        # Write your code here
#        result = []
#        count=0.0
#        for i in range(n, n*6+1):
#            numv = i
#            countn = self.getd(n, numv)
#            
#            rate = float(countn)/(6**n)
#            result.append([numv, rate])
#            
#        return result
#
#a=Solution()
#print a.dicesSum(5)
result=[[1,1,1,1,1,1]]
for i in range(2,n+1):
    result_len=(side-1)*i+1
    result.append([0 for x in range(result_len)])
    for j in range(i,side*i+1):
        index = j-i
        if j - side <= (i-1):
            result[i-1][index]= sum(result[i-2][0:index+1])
        #elif j-1 > side*(i-1):
        #    result[i-1][index]= sum(result[i-2][j-(side*(i-1))-1:])
        #    print index,i,j,j-(side*(i-1))
        #    print result[i-1][index]
        else:
            starti = j-side-i+1
            endi = starti+6
            result[i-1][index] = sum(result[i-2][starti:endi])
        
print(result[n-1])
