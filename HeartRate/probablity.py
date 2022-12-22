import pandas as pd
import matplotlib.pyplot as plt

# This is reading the data from the csv file and assigning the first column to HR1 and the second
# column to HR2.
df = pd.read_csv("Data.csv", sep="\t", skiprows=1, header = None).values

HR1= df[:,0]
HR2 = df[:,1]

# This is calculating the mean absolute error.
abs_Difference = abs(HR1-HR2)
MeanAbsoluteError = sum(abs_Difference)/len(abs_Difference)
print("Mean Absolute Error:",MeanAbsoluteError)

# This is calculating the root mean square error.
RootMeanSquareError = (sum((HR1-HR2)**2)/len(HR1))**0.5
print("Root Mean Square Error:",RootMeanSquareError)

# This is subtracting the mean of the HR1 and HR2 from the HR1 and HR2.
HR1coffeicent = HR1-HR1.mean()
HR2cofficient = HR2-HR2.mean()

# This is calculating the correlation coefficient.
Numerator = sum(HR1coffeicent*HR2cofficient)

HR1coffeicentsquared = sum(HR1coffeicent**2)
HR2cofficientsquared = sum(HR2cofficient**2)

Denominator = (HR1coffeicentsquared*HR2cofficientsquared)**0.5

r = Numerator/Denominator
print("Correlation Cofficient:",r)


# This is calculating the mean and difference between the two measures. It is then calculating the
# mean difference, standard deviation, upper limit and lower limit. It is then plotting the scatter
# plot of the mean and difference.

Mean = (HR1+HR2)/2
Difference = HR1-HR2

# print("Mean:",Mean)
# print("Difference:",Difference)

MeanDiff = sum(Difference)/len(Difference)
# print("Mean Difference:",MeanDiff)

StandardDeviation = (sum((Difference-MeanDiff)**2)/len(Difference))**0.5

UpperLimit = MeanDiff + 1.96*StandardDeviation
LowerLimit = MeanDiff - 1.96*StandardDeviation

plt.scatter(Mean,Difference)
plt.axhline(y=MeanDiff, color='black', linestyle='dashed')
plt.axhline(y=UpperLimit, color='r', linestyle='-')
plt.axhline(y=LowerLimit, color='orange', linestyle='-')
plt.xlabel("Average Two Measures")
plt.ylabel("Difference between Two Measures")
plt.show()