import numpy as np
# import pandas as pd
# import random
# We find the z score for each of the data point in the dataset and if the z score is greater than 3
# then, we can classify that point as an outlier. Any point outside of 3 standard deviations would be an outlier.
# dataset= [10,12,12,13,12,11,14,13,151,10,10,10,100,12,14,153, 12,101, 10,11,12,15,12,13,12,11,14,13,15,10,15,12,10,14,13,15,10]

# Read data from csv - Credit Card Fraud Detection Dataset from Kaggle

# dataset = pd.read_csv('/usr/local/etc/creditDatasets/credit4.csv', error_bad_lines=False)
# dataset = pd.read_csv('/usr/local/etc/creditDatasets/creditcard.csv', error_bad_lines=False)
# dataset.head()
# dataset.count()
#
# def find_columns(dataset):
#     for col in dataset.columns:
#         print(col)

# data = pd.DataFrame(dataset['Amount'])#set the 'Amount' column as a new dataframe before convert it into a list
# data = pd.DataFrame(dataset['amount'])#set the 'Amount' column as a new dataframe before convert it into a list
# data.head()
#
# dataset
#
# # Convert the initial dataset into a list
# data_list = dataset['Amount'].to_list()
# data_list = dataset['amount'].to_list()
# data_list2 = dataset['nameOrig'].to_list()
# data_list3 = dataset['nameDest'].to_list()
# # len(data_list)
#######################################################################################################################
########################################################################################################################
# outliers = []
# Function that takes numeric data as an input argument
# Find the mean and standard deviation of the all the data points
def detect_outlier(data_1):
    outliers = []
    realId = []
    threshold = 1.5# Change it to 3
    data_1 = [float(item) for item in data_1]
    mean_1 = np.mean(data_1)
    std_1 = np.std(data_1)

    for counter, y in enumerate(data_1):
        c = counter
        z_score = (y - mean_1) / std_1
        if (np.abs(z_score) > threshold):
            outliers.append(y)
            realId.append(c)
    # return realId
    return (outliers,realId)
########################################################################################################################

# outlier_datapoints, id_datapoints = detect_outlier(data_list)
# outlier_datapoints = detect_outlier(data_list)

# data_list[359]


# outliers = []
# realId = []
# print(outlier_datapoints)

# for counter, y in enumerate(data_list):
#     outliers.append(y)
#     realId.append(counter)
#
# type(realId[0])
# len(outliers)==len(realId)


# find_columns(dataset)

# mean_1 = np.mean(data_list)
# std_1 = np.std(data_list)
# z_score = (2000000.00 - mean_1) / std_1
########################################################################################################################
#################################################Generator Creation#####################################################
# countries = ['Greece','Germany','Italy','China','USA','Brazil','Kenya','Japan','Cyprus','France','New Zealand','India',
#              'United Kingdom','Ireland','Ivory Coast','Argentina','Portugal','Thailand','Austria','Mexico','Australia']
#
# month = ['January','February','March','April','May','June',
#          'Jule','August','September','October','November','December']
#
# day = str(random.randint(1,30))
#
# time = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','00:00','08:00','09:00','10:00','11:00','12:00',
#         '13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00','24:00']
#
# # hour = random.randint(0,24)
# #
# # minute = random.randint(1,60)
#
# typeTran = ['CASH_IN','CASH_OUT','DEBIT','PAYMENT','TRANSFER']
#
# country = []
# daytime = []
# type = []
#
# # str(random.randint(1,30)) + ' ' + random.choice(month) + '_' + random.choice(time)
#
# d,d1 = dataset.shape
#
# for i in range(0,d):
#     country.append(random.choice(countries))
#     daytime.append(str(random.randint(1,30)) + ' ' + random.choice(month) + '_' + random.choice(time))
#     type.append(random.choice(typeTran))
#
# dataset['location'] = country
# dataset['daytime'] = daytime
# dataset['Type'] = type
#
# dataset.to_csv('/usr/local/etc/creditDatasets/credit4.csv',index = False, header=True)
# dataset.count()

# if hour < 10:
#     print('0'+str(hour))
# else:
#     print(str(hour))
########################################################################################################################
# import random

# str(random.randint(1,30))