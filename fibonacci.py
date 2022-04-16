#x is amount(s) of fibonacci
#x should be a number

def fibonacci(x):
        b = [1,1]
        for i in range(2,x):
                b.append(b[i-2]+b[i-1])
        return b[0:x]
