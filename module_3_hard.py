data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
summa = 0

def List_(i):
    summa = 0
    for j in i:
        if type(j) == str:
            summa += len(j)
        elif type(j) == int:
            summa += j
        elif type(j) == set:
            summa += Set_(j)
    return summa

def Dict_(i):
    summa = 0
    prom = []
    for k, v in i.items():
        prom.append(k)
        prom.append(v)
    summa += List_(prom)
    return summa

def Tuple_(i):
    summa = 0
    if i == ():
        summa += 0
    else:
        for j in i:
            if type(j) == int:
                summa += j
            elif type(j) == str:
                summa += len(j)
            elif type(j) == list:
                summa += List_(j)
            elif type(j) == dict:
                summa += Dict_(j)
            elif type(j) == tuple:
                summa += Tuple_(j)
    return summa

def Set_(i):
    summa = 0
    for j in i:
        if type(j) == tuple:
            summa += Tuple_(j)
    return summa



def summator():
    summator_ = 0
    prom=[]
    for i in data_structure:
        if type(i) == int:
            summator_ += i
        elif type(i) == str:
            summator_ += len(i)
        elif type(i) == list:
            summator_ += List_(i)
        elif type(i) == dict:
            summator_ += Dict_(i)
        elif type(i) == tuple:
            summator_ += Tuple_(i)
    return summator_


print(summator())
