n = int(input("n = ")) 
def factorial_rec(n):
     if n == 0 or n == 1:
         return 1
     return n * factorial_rec(n - 1)
def factorial_iter(n):
     f = 1
     for i in range(2, n + 1):
         f *= i
     return f
print("\nRezultate factorial pentru n =", n)
print("Recursiv :", factorial_rec(n))
print("Iterativ :", factorial_iter(n))