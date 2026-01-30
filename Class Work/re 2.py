import re
pattern=r'h.t'
text='hot hat hit hut heat height'
res=re.findall(pattern,text)
print(res)

pattern=r'^m.t'
text='mit hot hat hut heat height'
res2=re.findall(pattern,text)
print(res2)


pattern=r'^m.t$'
text='mit hot hat hut heat might'
res2=re.findall(pattern,text)
print(res2)


pattern=r'[ameog]'
text='mit hot123 hat hut heat might'
res2=re.findall(pattern,text)
print(res2)

pattern=r'[1-9]'