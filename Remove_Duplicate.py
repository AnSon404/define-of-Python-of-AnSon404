#lst should be a list

def d_duplicate(lst):
        a = []
        for i in lst:
                if i not in a:
                        a.append(i)
        return a

def r_duplicate(lst):
        return list(set((lst)))
