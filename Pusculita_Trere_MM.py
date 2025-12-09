valm=[1,5,10,25,50]
nr=[1,2,3,4,5]
def Sol_Pos(a,b,c,d,e):
    if (nr[0]*a+nr[1]*b+nr[2]*c+nr[3]*d+nr[4]*e==g) and (a+b+c+d+e==n):
        return True
    else:
        return False
def Prel_Sol(a,b,c,d,e):
    SumMin=-1
    Sum=valm[0]*a+valm[1]*b+valm[2]*c+valm[3]*d+valm[4]*e
    if Sum>SumMin:
        SumMin=Sum
    if SumMin==-1:
       SumMin=Sum
    return print(SumMin)
n=int(input('Dati numarul de monede din pusculita n='))
g=int(input('Dati greutatea monedelor din pusculita g='))
for a in range (0,n):
    for b in range (0,n):
       for c in range (0,n):
         for d in range (0,n):
             for e in range (0,n):
                 if (Sol_Pos(a,b,c,d,e)):
                  Prel_Sol(a,b,c,d,e)