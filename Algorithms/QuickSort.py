



def quick_sort(s = []):

    n = len(s)
    if n < 2:
        return

    pivot = s[0]

    l = []
    e = []
    g = []

    while not len(s) == 0:
        if s[0] < pivot:
            l.append(s.pop(0))
        elif s[0] > pivot:
            g.append(s.pop(0))
        else:
            e.append(s.pop(0))

    quick_sort(l)
    quick_sort(g)

    while not len(l) == 0:
        s.append(l.pop(0))
    while not len(e) == 0:
        s.append(e.pop(0))
    while not len(g) == 0:
        s.append(g.pop(0))