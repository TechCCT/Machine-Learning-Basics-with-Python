# Machine-Learning-Basics-with-Python
Preprocessing of data preparation for ingestion by machine learning algorithms and it's conversion into the right format
Several preprocessing techniques starting with binarization:

-Binarization

-Mean removal

-Scaling

-Normalization

# Binarization
This process is used to convert our numerical values into boolean values.

# Mean Removal
Used to remove the mean from feature vector, so that each feature is centered on zero. In order to remove bias from the features
in our vector.

# Scaling 
The value of each feature can vary between many random values. So it becomes important to scale those features so that it is a level playing field for the machine learning algorithm to train on.

# Normalization
We use normalization to modify the values in the feature vector so that we can measure them on a common scale. Most common forms are L1 normalization and L2 normalizatioin, where L1 refers to Least Absolute Deviations and L2 as Least Squares.This works by making sure the sum of squares is 1. L1 being more robust than L2.


# Label Encoding
While performing classificatio, we usually deal with a lot of labels. These labels can be in the form of words, numbers, or something else. Since, machine learning functions in **sklearn** expects them to be numbers. So if they are already numbers, then we can use them directly to start training. But this is not usually the case.
