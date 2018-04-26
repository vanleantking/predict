import arff

data = arff.load(open('1year.arff'))
print(data['data'][:10])