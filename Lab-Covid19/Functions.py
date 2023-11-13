import pandas as pd

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

class Person:
    def __init__ (self, index):
        genders = pd.read_excel("./Data/Covid19.xlsx", sheet_name="Totalt antal per kön")
        self.index = index
        
class Gender(Person):
    def __init__(self, index, genders):
        super().__init__(index)
        self.genders = genders

    def both_genders(self, other, case):
        return self.genders.loc[self.index][case] + other.genders.loc[other.index][case]

    def procent_cases(self, other, case):
        return self.genders.loc[self.index][case]/self.both_genders(other, case)*100
