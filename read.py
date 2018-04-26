import arff
import numpy as np
import os

BASE_DATA = 'datasets\data'
def loaddata():
    for file in os.listdir(BASE_DATA):
        filepath = os.path.join(BASE_DATA, file)
        data = arff.load(open(filepath))
        print(data['data'][:10])
        return

if __name__ == "__main__":
    loaddata()
# data = arff.load(open('1year.arff'))
# print(data['data'][:10])