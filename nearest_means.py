__author__ = 'rasheduzzaman'

import random as rnd


def accuracy(true_labels, output_labels):
    size = len(true_labels)
    correct = 0
    for i in range(0, size):
        if true_labels[i][0] == output_labels[i]:
            correct += 1
    return float(correct/size) * 100


def prediction(data, classes, class_mean):
    size = len(data)
    labels = [[row[i] for row in classes] for i in range(0, len(classes[0]))]
    labels = set(labels[0])
    predicted_labels = []
    lbl = list(labels)
    for i in range(0, size):
        temp = data[i]
        min_dist = []
        for j in range(0, len(class_mean)):
            dist = 0
            for k in range(0, len(temp)):
                dist += (temp[0] - class_mean[j][k]) ** 2
            min_dist.append(dist)
        min_index = min(range(0, len(min_dist)), key=min_dist.__getitem__)
        predicted_labels.append(lbl[min_index])
    return predicted_labels


def mean(data, classes):
    size = len(data)
    labels = [[row[i] for row in classes] for i in range(0, len(classes[0]))]
    labels = set(labels[0])
    cmean = []
    for label in labels:
        temp = []
        for i in range(0, size):
            if classes[i][0] == label:
                temp.append(data[i])
        sz = len(temp[0])
        mn = [float(sum(l)+1)/(len(l)+sz) for l in zip(*temp)]
        cmean.append(mn)
    return cmean


def split_dataset(data, labels, ratio):
    train_size = int(len(data) * ratio)
    train_set = []
    train_labels = []
    test_set = data.copy()
    test_labels = labels.copy()

    while len(train_set) != train_size:
        index = rnd.randrange(0, len(test_set))
        train_set.append(test_set.pop(index))
        train_labels.append(test_labels.pop(index))

    return train_set, train_labels, test_set, test_labels


def prepare_dataset(file_data, file_labels):
    data = [line.split() for line in file_data]
    data = [[float(column) for column in row] for row in data]
    classes = [line.split() for line in file_labels]
    classes = [[int(column) for column in row] for row in classes]
    return data, classes

if __name__ == '__main__':
    file_name_dataset = input("Enter a valid file name: ")
    file_name_labels = input("Enter a valid file name: ")

    dataset = open(file_name_dataset, 'r')
    labels = open(file_name_labels, 'r')

    data, classes = prepare_dataset(dataset, labels)

    trainset, trainlabels, testset, testlabels = split_dataset(data, classes, 0.7)

    class_mean = mean(trainset, trainlabels)

    output_labels_training = prediction(trainset, trainlabels, class_mean)
    print(accuracy(trainlabels, output_labels_training))

    output_labels_testing = prediction(testset, testlabels, class_mean)
    print(accuracy(testlabels, output_labels_testing))

