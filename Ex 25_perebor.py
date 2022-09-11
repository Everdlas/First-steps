persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'), 
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'), 
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'), 
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'), 
    ('Amber Perez', 403445, 'M', '0602870126')
]
p={}
for i in range(10):
    p[persons[i][0]] = [['salary',persons[i][1]],['gender',persons[i][2]],['passport',persons[i][3]]]
# print(p)
data={}
for i in p:
    a = dict(p[i])
    # print(a)
    data[i] = a
# for i in data:
#     print(i,':',data[i])
# print(data)
