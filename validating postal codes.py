import re
a=input()
b=re.compile(r'^[1-9]([0-9]){5}$')
if(b.search(a) and len(re.findall(r'(\d)(?=\d\1)',a))<2):
    print('True')
else:
    print('False')