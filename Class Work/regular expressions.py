import re
pattern = r"[0-9]"
res=re.search(pattern,"abc4def")
print("Search Result:",res.group())
print(res.group()if res else "No match found")
matches=re.findall(pattern,"abc4def5ghi6")
print("Findall Matches:",matches)
print(res)
res=re.finditer(pattern,"abc4def5ghi6")
print("Finditer Matches:")

pattern=r"[,.>:;]"
res=re.split(pattern,"Hello, world. Welcome: to; Python> programming")
print("Split Result:",res)
pattern=r"123"
res=re.sub(pattern,"456","abc123def123ghi")
print("Substitution Result:",res)