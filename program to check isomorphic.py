def isomorphic (s1,s2):
    if len(s1) !=len(s2):
        return false
    else:
        d1,d2={},{}
        for i in range (len(s1)):
            a,b=s1[i],s2[i]
            if(a not in d1):
                d2[b]=a
                if d1[a]!=b or d2[b]!=a:
                     return false
            return true
        s1=input("enter a string:")
        s2=input("enter a string:")
        print(isometric(s1,s2))
                    
            
