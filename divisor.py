#Find all divisors of a number and determine if it is prime number
def divisor(num):
        d = []
        for i in range(1,num+1):
                if num%i==0:
                        d.append(i)
        if len(d)==0:
                print("Wrong input!")
        else:
                if len(d)==2:
                        print("This is a prime number!")
                print("Its divisor(s) is/are below: ")
                for i in d:
                        print(i)
