""" The Fibonacci sequence is a series of numbers in which each number after the first two is
    the sum of the two preceding numbers. 
    For example, the first ten numbers in the Fibonacci sequence are:
                    0, 1, 1, 2, 3, 5, 8, 13, 21, 34"""
                
def fibonacci(n):
    a,b =0,1            # this 2 will be in every series 
    result =[]
    while b < n:         
        result.append(b)
        a,b = b, a+b    # a= b and b becomes a+b which is previous number + current number.
    return result


print(fibonacci(50))  

