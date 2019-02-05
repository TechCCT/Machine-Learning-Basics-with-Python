import numpy as np
from sklearn import preprocessing

#Sample labels

input_labels = ['red', 'black', 'green', 'yellow', 'white']


#Creating label encoder

encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

#Mapping between words and numbers

print("\nLabel mapping: ")
for i, item in enumerate(encoder.classes_):
    print(item, '-->', i)


#Encoding a set of randomly ordered labels

test_labels = ['green', 'red', 'black']
encoded_values = encoder.transform(test_labels)
print("\nLabels = ",test_labels)
print("Encoded values = ", list(encoded_values))

#Decoding a set of random values

encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\n Encoded Values = ", encoded_values)
print("Decoded labels = ", list(decoded_list))
