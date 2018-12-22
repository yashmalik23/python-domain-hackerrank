import re
r=re.compile(r'(\s([&]){2}\s)')
p=re.compile(r'(\s([|]){2}\s)')
for i in range(int(input())):
    a=input()
    while r.search(a):
        a=re.sub('(\s([&]){2}\s)',' and ',a)
    while p.search(a):    
        a=re.sub('(\s([|]){2}\s)',' or ',a)
    print(a)
        
