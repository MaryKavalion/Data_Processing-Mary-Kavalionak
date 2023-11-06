def make_ticks(list_to_shorten, n):
    ticks = []
    for i in range (len(list_to_shorten)):
        if (i+1) % n == 0:
            ticks.append(list_to_shorten[i])
    return ticks