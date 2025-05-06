import numpy as np
def calculate_variance(data):
    '''
  
    calculate the variance
    Paramaters: a list of numbers
    Returns: float
    
    '''
    mean = np.mean(data) # calculate mean
    variance = np.mean((data - mean) ** 2) # calculate variance
    return variance

trials = 1000 # number of trials 
tosses_per = 100 # number of rolls per trial
count6 = []  # list created to store data

for i in range(trials):
    tosses = np.random.randint(1, 7, size=tosses_per) # random tosses from 1 to 6
    count_sixes = np.count_nonzero(tosses == 6) # count the number of 6's in the toss
    count6.append(count_sixes) # append the count of 6's to the list
    
variance_of_sixes = calculate_variance(np.array(count6)) # calculate the variance of the 6's
print(variance_of_sixes) # result
print(f"The variance of the number of 6's in 100 die tosses 1000 times will be {variance_of_sixes}") # results with message 