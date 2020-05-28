import numpy as np
import matplotlib.pyplot as plt
import pdb

def base(t, current_time, p=0.8, d=0.18):
    # The function takes as an input two variables that specify 
    # when the study repetitions happend, and when we are testing (in seconds). 
    # It's output is the base level activation at the time of testing
    #
    # Inputs:
    #  t: a np.array where each value is a time stamp for a study occurence. 
    #    For example, if we are simulating base level for 3 study repetitions 
    #    at times 0, 10 and 60, t would be [0, 10, 60]
    #  current_time: a scalar that specifies the time of testing
    t = np.array(t)
    B = 0.                             # initial base-level strength
    delta_B = np.array([0.] * len(t))  # vector for storing increments
    delta_B[0] = p * (1-B)             # initial increment
    
    # calculate base-level prior to each study and new increment
    #import pdb; pdb.set_trace()
    for i in range(1, len(t)):
        if t[i] <= current_time:
            decayed_delta_B = delta_B[0:i] * (1+t[i]-t[0:i]) ** (-d)
            B = sum(decayed_delta_B)
            delta_B[i] = (1-B) * p
        
    # calculate base-level at time of testing
    idx = t <= current_time
    decayed_delta_B = delta_B[idx] * (1+current_time-t[idx]) ** (-d)
    B = np.nansum(decayed_delta_B)
    return(B)
	
def expanding_vs_contracting():
	# plot example as a function of test lag
	test_t = np.arange(0,500,0.1)
	b_val1 = [base([0,30,90,180], t) for t in test_t]   # expanding
	b_val2 = [base([0,90,150,180], t) for t in test_t]  # contracting
	plt.subplot(3,1,1)
	plt.plot(test_t, b_val1, 'b')
	plt.subplot(3,1,2)
	plt.plot(test_t, b_val2, 'r')
	plt.subplot(3,1,3)
	plt.plot(test_t, b_val1, 'b')
	plt.plot(test_t, b_val2, 'r')
	plt.show()
	
def massed_vs_spaced():
	# plot example as a function of test lag
	test_t = np.arange(0,400,0.1)
	b_val1 = [base([220,230,240], t) for t in test_t]   # expanding
	b_val2 = [base([0,120,240], t) for t in test_t]  # contracting
	plt.subplot(3,1,1)
	plt.plot(test_t, b_val1, 'b')
	plt.subplot(3,1,2)
	plt.plot(test_t, b_val2, 'r')
	plt.subplot(3,1,3)
	plt.plot(test_t, b_val1, 'b')
	plt.plot(test_t, b_val2, 'r')
	plt.show()

if __name__ == '__main__':
    massed_vs_spaced()
    expanding_vs_contracting()