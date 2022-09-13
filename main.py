def guess(n):
    import sys
    guesslist=[]
    while len(guesslist)!=n or len(set(guesslist))!=n: 
        a=(6-n)*" "  
        guess=input(a)
        if int(guess)==-1: 
            print(f"the number is: {m}")
            sys.exit()
        guesslist=[]
        for i in guess:
            guesslist.append(int(i))
        if len(guesslist)!=n or len(set(guesslist))!=n:
            print("please numbers not equal")
            continue
    else:
        return guesslist
    guess(n)
def chose():
    i=int(input("please chose one of 3️⃣,4️⃣,5️⃣:\t"))
    if i>2 and i<6:
        print("for giving up write -1")
        return game(i)
    else:
        chose()
def game(n):
    import random
    sayilist=[1,2,3,4,5,6,7,8,9]
    tutulansayi=[]
    for i in range (n):
        k=random.choice(sayilist)
        if not (0 in sayilist) and len(sayilist)==9:
            sayilist.append(0)
        sayilist.remove(k)
        tutulansayi.append(k)
    global m
    m=""
    for i in tutulansayi:
        m+=str(i)
    print(" input \t\tsıra \t  quess\t\t➕\t\t➖")
    q,sira=0,0
    while q!=n:
        newguess=guess(n)
        q,r=0,0
        k=set(tutulansayi).intersection(set(newguess))
        for i in k:
            t=tutulansayi.index(i)==newguess.index(i)
            if t:
                q+=1
            else:
                r+=1
        stri=""
        for t in newguess:
            stri+=str(t)
        sira += 1
        print(f"\t\t\t{str(sira).center(4)}\t {stri.center(5)}\t{str(q).center(10)}{str(r).center(6)}")

    print("Congratulations🥳🎉")
print("Welcome")
chose()
