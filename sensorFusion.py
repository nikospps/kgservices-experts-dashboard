import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sb
from scipy import stats
import time

# %matplotlib inline
fw = 10 # figure width
# Despite noisy measurement of individual sensors, We can calculate an optimal estimate of all conditions
x = np.linspace(-100,100,1000)
mean0 = 0.0   # e.g. meters or miles
var0  = 20.0

plt.figure(figsize=(fw,5))
plt.plot(x,mlab.normpdf(x, mean0, var0), label='Normal Distribution')
plt.ylim(0, 0.1)
plt.legend(loc='best')
plt.xlabel('Position')
plt.show()
plt.close()

# The Mean is meters, calculated from velocity*dt or step counter or wheel encoder ...
# VarMove is the Estimated or determined with static measurements
meanMove = 25.0
varMove  = 10.0
plt.figure(figsize=(fw,5))
plt.plot(x,mlab.normpdf(x, meanMove, varMove), label='Normal Distribution')
plt.ylim(0, 0.1)
plt.legend(loc='best')
plt.xlabel('Distance moved')
plt.show()
plt.close()

# Both Distributions have to be merged together $\mu_\text{new}=\mu_\text{0}+\mu_\text{move}$ is the
# new mean and $\sigma^2_\text{new}=\sigma^2_\text{0}+\sigma^2_\text{move}$ is the new variance

def predict(var, mean, varMove, meanMove):
    new_var = var + varMove
    new_mean= mean+ meanMove
    return new_var, new_mean

new_var, new_mean = predict(var0, mean0, varMove, meanMove)
plt.figure(figsize=(fw,5))
plt.plot(x,mlab.normpdf(x, mean0, var0), label='Beginning Normal Distribution')
plt.plot(x,mlab.normpdf(x, meanMove, varMove), label='Movement Normal Distribution')
plt.plot(x,mlab.normpdf(x, new_mean, new_var), label='Resulting Normal Distribution')
plt.ylim(0, 0.1);
plt.legend(loc='best')
plt.title('Normal Distributions of 1st Kalman Filter Prediction Step')
plt.savefig('Kalman-Filter-1D-Step.png', dpi=150)
plt.show()
plt.close()

# What you see: The resulting distribution is flat > uncertain.
# The more often you run the predict step, the flatter the distribution get
#
# First Sensor Measurement (Position) is coming in...
#
# Sensor Defaults for Position Measurements
# (Estimated or determined with static measurements)

meanSensor = 25.0
varSensor = 12.0
plt.figure(figsize=(fw,5))
plt.plot(x,mlab.normpdf(x, meanSensor, varSensor))
plt.ylim(0, 0.1)
plt.show()
plt.close()
# Now both Distributions have to be merged together $\sigma^2_\text{new}=\cfrac{1}{\cfrac{1}
# {\sigma^2_\text{old}}+\cfrac{1}{\sigma^2_\text{Sensor}}}$ is the new variance and the new mean value is
# $\mu_\text{new}=\cfrac{\sigma^2_\text{Sensor} \cdot \mu_\text{old} + \sigma^2_\text{old} \cdot
# \mu_\text{Sensor}}{\sigma^2_\text{old}+\sigma^2_\text{Sensor}}$
def correct(var, mean, varSensor, meanSensor):
    new_mean=(varSensor*mean + var*meanSensor) / (var+varSensor)
    new_var = 1/(1/var +1/varSensor)
    return new_var, new_mean

var, mean = correct(new_var, new_mean, varSensor, meanSensor)
plt.figure(figsize=(fw,5))
plt.plot(x,mlab.normpdf(x, new_mean, new_var), label='Beginning (after Predict)')
plt.plot(x,mlab.normpdf(x, meanSensor, varSensor), label='Position Sensor Normal Distribution')
plt.plot(x,mlab.normpdf(x, mean, var), label='New Position Normal Distribution')
plt.ylim(0, 0.1)
plt.legend(loc='best')
plt.title('Normal Distributions of 1st Kalman Filter Update Step')
plt.show()
plt.close()