def bubble_sort(a):
    """Сортировка пузырьком по возрастанию"""
    if len(a)  < 2:
        return a

    i = 1
    l = len(a) - 1 

    while i <= l:
        j = i
        prev_j = j - 1
        while j <= l:
            prev_item = a[prev_j]
            cur_item = a[j]
            # Сортируем по возрастанию, если нужно поубыванию, то просто сменить знак
            if prev_item > cur_item:
                a[prev_j], a[j] = a[j], a[prev_j]
            
            j += 1
        i += 1

    return a
