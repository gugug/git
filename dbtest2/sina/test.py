__author__ = 'gu'

a = [1,2,3,4,5,6]
b = [3,4,5,6,7,8]

d = {'x': 1, 'y': 2, 'z': 3}

ab = zip(a,b)

dictab = { }

  # for key_id in no_repeat_list:
                # all_dict.setdefault(key_id, tw)  # id作为键，时间博文绑定后作为值
print len(dictab)
dictab.setdefault("a",ab)

print type(dictab.keys())
print (dictab.keys())
print type(dictab.values())

print (dictab.values())

for i in dictab.values():
    print len(i)
    print i
    for j in i:
        print j
        print j[0]
        print j[1]
