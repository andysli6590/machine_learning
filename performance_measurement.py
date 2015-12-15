__author__ = 'rasheduzzaman'

file_name = "./data.txt"

#file_name = input("Enter a valid file name: ")

file = open(file_name, 'r')

data = []
data = [line.split() for line in file]

data = [[int(column) for column in row] for row in data]

TP = FP = FN = TN = 0

for i in range(0, len(data)):
    if data[i][2] == 1 and data[i][1] == 1:
            TP += 1
    elif data[i][2] == 1 and data[i][1] == -1:
            FP += 1
    elif data[i][2] == -1 and data[i][1] == 1:
            FN += 1
    else:
            TN += 1

E = (FP + FN) / (TP + FP + FN + TN)

BER = 1.0/2 * ((FP/(FP+TN)) + (FN/(FN+TP)))

Precision = TP / (TP + FP)

Recall = TP / (TP + FN)

print(E)

print(BER)

print(Precision)

print(Recall)

file.close()