import numpy as np
import pandas as pd
import csv

class Inbody:
    def __init__(self,date,weight,smm,fat,bmr):
        self.date=date
        self.weight=weight
        self.smm=smm
        self.fat=fat
        self.bmr=bmr
        

history = [
#    Inbody(input(),int(input()),int(input()),int(input()),int(input()))
    Inbody(input(),int(input()),int(input()),int(input()),int(input())),
    Inbody(input(),int(input()),int(input()),int(input()),int(input()))
]

for history in history:
    print(str(history))