def tranzitie(q,nr):
    f=[]
    for l in M:
        if l[0]==q and l[1]==nr:
            f.append(l[2])
    return f

def NFA(ind,q,cuv):
    global dic,dimensiune,v,SF,nfa
    c=cuv[0]
    for stare in dic[q]:
        v[ind] = stare
        if v[ind] in tranzitie(q,c):
            if ind == dimensiune-1:
                if v[dimensiune-1] in SF:
                    nfa=True
                    print(*v[0:], sep="->")
            else:
                NFA(ind+1,stare,cuv[1:]) 

f=open("input7nfa.txt") #verificat
# f=open("input6nfa.txt") #verificat
# f=open("input5nfa.txt") #verificat
# f=open("input4nfa.txt") #verificat

init=f.readline().strip()
L=[x.strip() for x in f.readlines()]
M=[x.split() for x in L]    #lista cu liste din fisierul text
SF=M[len(M)-1]  #lista stari finale
del M[len(M)-1]

stari=[M[i][0] for i in range(0,len(M))]    
stari.extend([M[i][2] for i in range(0,len(M))])
st=list(set(stari))    #lista starilor din automat

dic={st[i]:[] for i in range(0,len(st))}    #constuim dictionarul cu stari
for l in range(len(M)):
    dic[M[l][0]].append(M[l][2])
for l in dic:
    dic[l]=list(set(dic[l]))

print("Intorduceti cuvantul:")
cv=input()

if len(cv)==0:
    if init in SF:
        print("Cuvantul vid este acceptat")
    else:
        print("Cuvantul vid nu este acceptat")
else:
    dimensiune=len(cv)+1    #dimensiunea solutiei
    x=0
    v = [0]*dimensiune  #vectorul in care memoram o solutie
    v[0]=init
    nfa=False
    NFA(1,init,cv)
    
    if nfa ==False:
        print("Cuvant neacceptat!")

    else:
        print("Cuvant acceptat!")



