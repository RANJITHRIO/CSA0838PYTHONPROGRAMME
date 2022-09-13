class Solution(object):
   def calculate(self, s):
      """
      :type s: str
      :rtype: int
      """
      stack = []
      i = 0
      x=""
      for j in s:
      if() j !=" ":
      x+=j
      s = x
      n = len(s)
      while i<n:
         if s[i] == '/':
            i+=1
         num,i = self.make_num(s,i)
         if stack[-1]<0:
            stack[-1] = -1*(abs(stack[-1])/num)
         else:
            stack[-1] = stack[-1]/num
      elif s[i] == '*':
         i+=1
         num,i = self.make_num(s,i)
         stack[-1] = stack[-1]*num
      elif s[i] == '-':
         i+=1
         num,i = self.make_num(s,i)
         stack.append(-num)
      elif s[i] =='+':
         i+=1
         num,i = self.make_num(s,i)
         stack.append(num)
      else:
         num,i = self.make_num(s,i)
         stack.append(num)
         i+=1
         return sum(stack)
   def make_num(self,s,i):
      start = i
      while i<len(s) and s[i]!= '/' and s[i]!= '*' and s[i]!= '-' and s[i]!='+':
      i+=1
   return int(s[start:i]),i-1
