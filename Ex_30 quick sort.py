def quick_sort(s):
    elem=s[0]
    left=list(filter(lambda x: x<elem,s))
    center= [i for i in s if i == elem]
    right=list(filter(lambda x: x>elem,s))
    if len(s)<=1:
        return s
    return quick_sort(left)+center+quick_sort(right)
