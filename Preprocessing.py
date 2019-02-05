import numpy as np
from sklearn import preprocessing

input_data = np.array([[5.1, -2.9, 3.3],
                      [-1.2, 7.8, -6.1],
                      [3.9, 0.4, 2.1],
                      [7.3, -9.9, -4.5]])

#Binarization
data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data)
print("\n Binarized Data: \n", data_binarized)

#Mean removal

print("\n Before")
print("\n Mean:", input_data.mean(axis=0))
print("\n Standard Deviation", input_data.std(axis=0))

#Removal

data_scaled = preprocessing.scale(input_data)
print("\n After")
print("\n Mean =", data_scaled.mean(axis=0))
print("\n Standard Deviation = ", data_scaled.std(axis=0))


#Min Max Scaling

scaling_data = preprocessing.MinMaxScaler(feature_range=(0, 1))
scaled_data = scaling_data.fit_transform(input_data)
print("\n Min max scaled data: ", scaled_data)

#Normalization

Normalized_L1 = preprocessing.normalize(input_data, norm='l1')
Normalized_L2 = preprocessing.normalize(input_data, norm='l2')
print("\nL1 Normalized data: \n",Normalized_L1)
print("\nL2 Normalized data: \n",Normalized_L2)



