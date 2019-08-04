from numpy import mat

dataMat = []
labelMat = []
fr = open('../data/logistic/temp.txt')
for line in fr:
    linearr = line.strip().split()
    if len(linearr) == 1:
        print('~~~~~~~~~~~~~~~~')
    dataMat.append([1.0, float(linearr[0]), float(linearr[1])])
    labelMat.append(int(linearr[2]))
print(dataMat)
print(labelMat)

dataMetrix = mat(dataMat)
print(dataMetrix)
print(type(dataMetrix))
print(dataMetrix.shape)
labelMat=mat(labelMat).transpose()
print(labelMat)
print(type(labelMat))
print(labelMat.shape)