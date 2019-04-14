import sklearn
import csv
import random
import numpy as np
from sklearn.linear_model.logistic import LogisticRegression


with open("wine.txt", "r") as f:
    readCSV = csv.reader(f, delimiter =',')
    wine_name = []
    wine_data = []
    for row in readCSV:
        wine_name.append(row[0]) #adding first item from wine name list to array , this is the answer were testing for
        wine_data.append(row[1:]) #everything else into wine data , those are the attributes
    indices = [int(item) for item in range(len(wine_name))]
    random.shuffle(indices) #index for all data points, to randomly shuffle so that you dont jsyt test the first 30 becuase you will get the sameclass)

    training_indices = indices[30:]
    testing_indices = indices[:30]


    # training data
    training_labels = [wine_name(item) for item in training_indices]
    training_data = [wine_data(item) for item in training_indices]
    wine_type_train = np.asarray(training_labels)#coverts input to array
    wine_data_train = np.asarray(training_data)


    # testing data
    testing_labels = [wine_name(item) for item in testing_indices]
    testing_data = [wine_data(item) for item in testing_indices]
    wine_type_test = np.asarray(testing_labels)
    wine_data_test = np.asarray(testing_data)
    print(training_labels, training_labels)

    #converts to array from list
    #can do matrix operations from numpy library
    #takes items correponding to training indices, and then seperates data into training and trsting
    # ;30 is everyhing up to 30