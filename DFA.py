def tranzitie(q,nr):
    for l in M:
        if l[0]==q and l[1]==nr:
            return l[2]
    return False

def dfa(q,cuv):
    if len(cuv)==1:
        drum.append(q)
        q1=tranzitie(q,cuv)
        drum.append(q1)
        if q1 not in SF:
            return False
        return True
    else:
        c=str(cuv)[0]
        drum.append(q)
        q1=tranzitie(q,c)
        if q1==False:
            return False
        rcv=str(cuv)[1:]
        return dfa(q1,rcv)
    
def citire_dfa():
    global init,SF
    print("Intorduceti cuvantul:")
    d=input()
    if len(d)==0 and init in SF:
        print("Cuvantul vid este acceptat.")
    if len(d)==0 and init not in SF:
        print("Cuvantul vid nu este acceptat.")

    if len(d)>0:
        b=dfa(init,d)
        if b==True:
            print("Cuvant acceptat!")
            print(*drum,sep='->')
        else:
            print("Cuvant neacceptat!")
    del drum[0:]


f=open("input3.txt") #verificat
# f=open("input2.txt") #verificat
# f=open("input1.txt") #verificat 

init=f.readline().strip()
L=[x.strip() for x in f.readlines()]
M=[x.split() for x in L]
SF=M[len(M)-1]
del M[len(M)-1]
drum=[]

citire_dfa()


