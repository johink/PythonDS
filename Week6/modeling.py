"""STATISTICAL MODELING"""
import sklearn.datasets as data

#sklearn.datasets contains many sample datasets
#The load_xyz() function returns a dictionary object with four (possibly five) keys:  DESCR, data, feature_names, and target
boston = data.load_boston()

#DESCR contains a description of the dataset and what the columns mean
print(boston["DESCR"])

#data contains the values for the x variables
#feature_names contains the names for the columns
#and target contains the values of the target variable, 
#which is MEDV according to the description of the boston dataset
#The optional fifth key is target_names, and it only exists when the target variable is categorical

#%%
#Utilizing these built-in datasets and the sklearn documentation found 
#at http://scikit-learn.org/stable/user_guide.html conduct the following analyses

#PLEASE REMEMBER: it is perfectly okay to copy/paste code off the internet,
#as long as you understand what the code is doing.  Feel free to ask questions if you are stuck!

#%%
"""LINEAR REGRESSION"""
#Using the boston dataset, conduct a linear regression to find the least-squares regression line


#Do these relationships make sense?



#%%
"""LOGISTIC REGRESSION"""
#Using the breast cancer dataset, split using a 70/30 train/test split, with a random_state of 101
#build a logistic regression model to classify tumors as either malignant or benign



#How good is the model at diagnosing breast cancer?
#Provide some statistics, such as accuracy, sensitivity, specificity, etc.



#%%
"""CLASSIFICATION TREES"""
#Using the iris dataset, split using a 70/30 train/test split, with a random_state of 101
#build a classification tree which determines what type of flower is being examined



#How good is the model at classifying the different flower types?
#Provide some statistics, such as accuracy, sensitivity, specificity, etc.



#Is this model suffering from overfitting?  Try changing min_samples_split or min_samples_leaf and see if performance improves



#%%
"""RANDOM FOREST"""
#Using the digits dataset, split using a 70/30 train/test split, with a random_state of 101
#build a random forest which attempts to recognize handwritten digits
#When building the random forest, make sure to again set the random_state to 101



#Are there any digits that the random forest is particularly good/bad at identifying?




#%%
"""CLUSTERING"""
#Using the iris dataset, create a nearest-neighbors classification model using a 70/30 train/test split and a random_state of 101
#Create a nearest-neighbors classification model which predicts the type of flower
#Try experimenting with different n_neighbors values and weights to see which ones work best



#Let's pretend that we need to have a 100% sensitivity for Iris-Versicolour
#What's the highest cutoff we can assign to the predicted class probability of Iris-Versicolour to achieve this?




#%%
"""NAIVE BAYES"""
#Using the boston dataset and a Naive Bayes Classifier, predict whether or not the lot borders the Charles River
#Utilize a 70/30 train/test split and a random_state of 101





