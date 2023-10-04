def towerofhonai(n,source,destination,auxilary):
    if n==1:
        print("move disk 1 from source",source,"to destinaton",destination)
        return
    towerofhonai(n-1,source,auxilary,destination)
    print("move disk n frome source",source,"to destination",destination)
    towerofhonai(n-1,auxilary,destination,source)

n=4
towerofhonai(n,'A','B','C' )


def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input("enter the number:"))
print("the fibonacci value is:",fib(n))
        

def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
n=int(input("enter the number:"))
print("the factoirial value is:",fact(n))

    

    

