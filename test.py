s=('I','V','X','L','C','D','M')
#v=(1,5,10,50,100,500,1000)
n=3
roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
number=0
for i in range(len(s)-1):
    if roman[s[i]] < roman[s[(i+1)]]:
        number-=roman[s[i]]
    else:
        number+=roman[s[i]]

print(number+roman[s[-1]])