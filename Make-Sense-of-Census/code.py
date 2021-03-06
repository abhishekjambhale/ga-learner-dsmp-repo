# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path,delimiter=",", skip_header=1)
print(data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((data,new_record),axis=0)
print(census)
#Code starts here



# --------------
#Code starts here
age = np.array(census)[:,0]
max_age = np.max(age)
print('Maximum age is :',max_age)
min_age = np.min(age)
print('Minimum age is :',min_age)
age_mean = np.mean(age)
print('Mean age is :',age_mean)
age_std = np.std(age)
print('Standard deviation of age is :',age_std)


# --------------
#Code starts here
race = np.array(census)[:,2]
print(race)
race_0 = census[census[:,2]==0]
# print('Race 0 is :',race_0)
race_1 = census[census[:,2]==1]
# print('Race 1 is :',race_1)
race_2 = census[census[:,2]==2]
# print('Race 2 is :',race_2)
race_3 = census[census[:,2]==3]
# print('Race 3 is :',race_3)
race_4 = census[census[:,2]==4]
# print('Race 4 is :',race_4)
len_0 = len(race_0)
print('Length of Race 0 is :',len_0)
len_1 = len(race_1)
print('Length of Race 1 is :',len_1)
len_2 = len(race_2)
print('Length of Race 2 is :',len_2)
len_3 = len(race_3)
print('Length of Race 3 is :',len_3)
len_4 = len(race_4)
print('Length of Race 4 is :',len_4)

minority_race = 3


# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
working_hours_sum = np.sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
# print(high)
low = census[census[:,1]<=10]
# print(low)
avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)
avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)


