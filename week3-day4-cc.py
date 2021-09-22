
#Q1. What will be the output ? (Easy) (5 marks)
#def printMax(a, b):
 #   if a > b:
  #      print(a, 'is maximum')
   # elif a == b:
    #    print(a, 'is equal to', b)
 #   else:
  #      print(b, 'is maximum')
#printMax(3, 4)

# Answer: 4 is maximum

#Q2. What will be the output ? 
#x = 50
#def func(x):
#    print('x is', x)
#    x = 2
#    print('Changed local x to', x)
#func(x)
#print('x is now', x)

# answer:  x is 50
#         Changed local x to 2
#         x is now 50

#Q3. Write a function which will take a str as input and will return a string where vowels are removed. 
#Str = ABCDEFG
#Result = BCDFG
#Ans :
def func(s):
  print("input string", s)
  s = "ABCDEFG"
  print("updated string", s)
a = input()
func(a)   