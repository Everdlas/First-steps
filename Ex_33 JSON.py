import json
with open('group_people.json') as a:
    a = json.load(a)
    # for i in a:
    #     print(i)
    b={}
    for i in range(len(a)):
        # print(a[i]['id_group'])
        for j in a[i]['people']:
            if j['gender'] == 'Female' and j['year']>1977:
                # print(j)
                b[a[i]['id_group']] = b.get(a[i]['id_group'],0)+1
    print(b)
for i in b:
    print(i,b[i])