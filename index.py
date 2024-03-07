'''
Exceptions - handle and recover from erros in our scripts

Recursion - function that called itslef (e;g factorial)
Stacks

6! = 6*5*4*3*2*1 - factorial
6! = 6*5!

4!=24
  1 2 3 4
  1 3 2 4
  2 1 3 4


0! = 1 

1! = 1

'''

# def recurse():
#      print("inside recurse()")
#      recurse()


# recurse()


# try:
#     #place any code liable that will raise an error/ exception
#     response = int(input("Please enter a number: "))

# except ValueError as e:

# #except Exception: - not a good practice catching all errors
#     # if any exception is raised we ended up in a except block
#     print("Please eneter a numeric value")
#     print(e)
# else:
#     # only run if no no exception is thrown, everything works at this point
#     print("in the else block response=", response)

"""

Recursion

"""

# product = 1
# for i in range(6,0,-1): # 6 5  3 2 1
#     product *= i
#     print(product)



def factorial(n):
    if n == 0:
     return 1
    return n * factorial(n - 1)


factorial(6)


"""
Stack: data structure that LIFO (last in first out) that holds any functions that needs to be run


factorial(0) 1
factorial(1) 1
factorial(2) 2* 1!
factorial(3) 3* 2!
factorial(4) 4* 3!
factorial(5) 5* 4!
factorial(6) 6* 5!   bottom of the stack


"""

# paper is 

def fold(height, times):
   

# print("End of script")