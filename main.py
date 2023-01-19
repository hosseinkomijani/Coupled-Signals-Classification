import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import glob

# data visualization:
# read dataset (csv -> pandas dataframe)
df1 = pd.read_csv("dataset1 Data1.csv", header=None)

plt.plot(df1[0])
plt.plot(df1[1])
plt.show()


# phase shift calculation
def phaseshift(data):
    
    df = pd.read_csv(data, header=None)
    rdata = np.zeros((1000, 2))
    rdata[:,0] = df[0]
    rdata[:,1] = df[1]

    # scale
    scaler = StandardScaler()
    scaler.fit(rdata)
    data = scaler.transform(rdata[200:])

    c = np.cov(np.transpose(data))
    phi = np.arccos(c[0,1])
    phi2deg = phi / np.pi*180
    return  phi, phi2deg
    

def phase_shift(data_group):
    phase_shift_radian=[]
    phase_shift_degree=[]
    for i in data_group:
        phi, phi2deg=phaseshift(i)
        phase_shift_radian.append(phi)
        phase_shift_degree.append(phi2deg)
            
    return  phase_shift_radian, phase_shift_degree
    
dataset1=glob.glob('dataset1*.csv')
dataset2=glob.glob('dataset2*.csv')

phase_shift_radian_dataset1, phase_shift_degree_dataset1 = phase_shift(dataset1)
phase_shift_radian_dataset2, phase_shift_degree_dataset2 = phase_shift(dataset2)

# results
print('phase_shift_radian_dataset1:', phase_shift_radian_dataset1, '\n')
print('phase_shift_radian_dataset2:', phase_shift_radian_dataset2, '\n')
print('phase_shift_degree_dataset1:', phase_shift_degree_dataset1, '\n')
print('phase_shift_degree_dataset2:', phase_shift_degree_dataset2, '\n')

print('mean of phase_shift_dataset1 (in radian):',np.mean(np.array(phase_shift_radian_dataset1)), '\n')
print('mean of phase_shift_dataset2 (in radian):',np.mean(np.array(phase_shift_radian_dataset2)), '\n')
print('std of phase_shift_dataset1 (in radian):', np.std(np.array(phase_shift_radian_dataset1)), '\n')
print('std of phase_shift_dataset2 (in radian):', np.std(np.array(phase_shift_radian_dataset2)), '\n')


# plot the dispersion of extracted features

x=np.ones(10)
plt.figure(figsize=(5,3.5))
plt.scatter(phase_shift_radian_dataset1,x)
plt.scatter(phase_shift_radian_dataset2,x)
plt.legend(['dataset1','dataset2'], loc='upper right')
plt.show()