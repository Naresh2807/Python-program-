strs=["eat","tea","tan","ate","nat","bat"]
dis={}
for s in strs:
    key="".join(sorted(s))
    if key not in dis:
        dis[key]=[ ]
    dis[key].append(s)
print(dis)