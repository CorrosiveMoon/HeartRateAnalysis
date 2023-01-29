## Heart Rate Analysis

### Dependencies

-   pandas
-   matplotlib

### Description

This code uses a dataset in the form of a CSV file to analyze the heart rate measurements of two individuals. The dataset should be formatted with two columns, with the first column representing the heart rate measurement of the first individual and the second column representing the heart rate measurement of the second individual.

The code first imports the necessary libraries, pandas and matplotlib, then reads in the data from the CSV file using the read_csv method from pandas and assigns the first column to the variable HR1 and the second column to the variable HR2.

Next, the code calculates the Mean Absolute Error and Root Mean Square Error between the two sets of measurements. These values give an idea of how similar the two sets of measurements are.

The code then calculates the correlation coefficient between the two sets of measurements, which gives an idea of how closely the two sets of measurements are related.

Finally, the code plots a scatter plot of the mean of the two sets of measurements against the difference between the two sets of measurements. This plot also includes lines for the mean difference, upper limit, and lower limit, calculated using a standard deviation of 1.96.

### Usage

The user needs to provide the location of the data.csv file in the pd.read_csv method.

### Files Used

-   Data.csv

This code is useful for comparing the heart rate measurements of two individuals and can be used as a starting point for further analysis.
