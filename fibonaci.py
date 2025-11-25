x=int(input('nr X: '))
def fibonacci_recursori(n):
   if n==0:
     return 0 
   if n==1:
    return 1
    return fibonacci_recursori(n-1)+fibonacci_recursori(n-2)
    print(f'element al nr {x} din sir fibonaci: {fibonacci_recursori(x)} ') 
    def fibonacci_iterativ(n):
        sumfib=0
        if n==0:
           return 0 
        if n==1:
             return 1
        for i in range(n,0,-1):
             sumfib+=i
             return sumfib
             print(f'element al nr {x} din sir fibonaci: {fibonacci_iterativ(x)} ')