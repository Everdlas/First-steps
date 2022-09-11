with open('Alphabet.json') as b:
    with open('Abracadabra__1_.txt') as a:
        import json
        b = json.load(b)
        # print(a.read())
        # print(b)
        q=''
        for i in a:
            for j in i:
                if j in b:
                    q += b[j]
                else:
                    q += j
        print(q)