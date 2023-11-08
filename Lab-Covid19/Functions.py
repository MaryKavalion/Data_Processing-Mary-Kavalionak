def make_ticks(list_to_shorten, n):
    ticks = []
    for i in range (len(list_to_shorten)):
        if (i+1) % n == 0:
            ticks.append(list_to_shorten[i])
    return ticks

def count_and_check(text, dataset, column_name, second_column_name):
    if dataset[column_name].nunique() == dataset[second_column_name].nunique():
        number = dataset[column_name].nunique()
        print (text, number)
    else:
        print ("Your data needs cleaning")