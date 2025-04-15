import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as fit


# Problem 1
# import the data from csv using pandas
temperature_df = pd.read_csv("GlobalLandTemperaturesByState.csv")
# Filter the columns to only be temperature, date, and state, and only for years after 2000.
filtered_df = temperature_df.loc[temperature_df["dt"].str.startswith("2"), ["dt", "AverageTemperature", "State"]]
# Now also filter for only the states Wyoming, Nebraska, and South Dakota
filtered_df = filtered_df.loc[filtered_df["State"].isin(["Wyoming", "Nebraska", "South Dakota"])]
filtered_df.reset_index(drop=True, inplace=True)

# Problem 1.2
# Modify the dataframe to contain the average temperature over all 3 states for each date.
filtered_df = filtered_df.groupby("dt").mean("AverageTemperature").reset_index()

# Problem 1.3
# Plot the average temperature (y) for each date (x) using matplotlib.
# plt.figure(figsize=(6,6))
# plt.plot(filtered_df["dt"], filtered_df["AverageTemperature"], label="Average Temperature")
# plt.xticks(ticks=filtered_df["dt"][::10], rotation=45)
# plt.xlabel("Date")
# plt.ylabel("Average Temperature")
# plt.title("Average Temperature Over Time")
# # plt.show()

# Problem 1.4 
# Convert the date string to a number
filtered_df["dt"] = filtered_df["dt"].str.replace("-", "").astype(int)

# Problem 1.5
# Using scipy.optimize, define an appropriate model equation and 
# make an initial guess for its parameters and save this guess in an array.
def sin_wave(x,a,b,c,d):
    return a * np.sin(b * x + c) + d
initial_guess = np.array([15,2*np.pi/12,0,10])

# Problem 1.6
# Use scipy.optimize to fit the model to the data.
sin_params,covariance_matrix = fit.curve_fit(sin_wave, filtered_df.index, filtered_df["AverageTemperature"], p0=initial_guess)

# Problem 1.7
# Plot the original data and the fitted curve on the same graph.
plt.figure(figsize=(6,6))
plt.plot(filtered_df.index, filtered_df["AverageTemperature"], color='blue', label="Original Data")
plt.plot(filtered_df.index, sin_wave(filtered_df.index, sin_params[0], sin_params[1], sin_params[2], sin_params[3]), label="Fitted Curve", color='red')
plt.plot()
plt.xlabel("Month")
plt.ylabel("Average Temperature")
plt.title("Average Temperature Over Time")
plt.xticks(ticks=filtered_df.index[::10], labels=filtered_df["dt"][::10], rotation=45)
plt.legend()
plt.show()

# Problem 1.8
# Use the covariance matrix to calculate the errors for each parameter. 
a_error = np.sqrt(covariance_matrix[0][0])
b_error = np.sqrt(covariance_matrix[1][1])
c_error = np.sqrt(covariance_matrix[2][2])
d_error = np.sqrt(covariance_matrix[3][3])

# Problem 1.9
# Print the parameters and their errors.
print("Parameters and their errors:")
print("a: ", sin_params[0], "±", a_error)
print("b: ", sin_params[1], "±", b_error)
print("c: ", sin_params[2], "±", c_error)
print("d: ", sin_params[3], "±", d_error)


# # # # # Part 2 # # # # #


# Problem 1
# Read in the .dat file "global CCl4 MM.dat" using astropy.table's table library.
from astropy.table import Table 
ccl4_table = Table.read("global_CCl4_MM.dat", format="ascii")

# Problem 2
# Convert the astropy table into a pandas dataframe. Include the columns of date, 
# global mean concentration, and global mean concentration sd
ccl4_table = ccl4_table.to_pandas()
ccl4_table = ccl4_table.loc[:, ["CCl4ottoyr", "CCl4ottoGLm", "CCl4ottoGLsd"]]
ccl4_table.columns = ["date", "mean_concentration", "sd_concentration"]
print(ccl4_table)

# Problem 3
# Plot the mean concentration (y) for each date (x) using matplotlib. Also include the error in the graph.
plt.figure(figsize=(6,6))
plt.errorbar(ccl4_table.index, ccl4_table["mean_concentration"], yerr=ccl4_table["sd_concentration"], fmt='o', label="Error", ecolor='red', alpha=0.5)
plt.xlabel("Year")
plt.ylabel("Mean Concentration")
plt.title("Mean Concentration Over Time")
plt.xticks(ticks=ccl4_table.index[::12], labels=ccl4_table["date"][::12], rotation=45)
plt.show()

# Problem 4
# Fit a linear model to the data using scipy.optimize.
ccl4_table.dropna(inplace=True)
def line(x,m,b):
    return m * x + b
initial_guess = np.array([-0.1,100])
linear_params,covariance_matrix = fit.curve_fit(line, ccl4_table.index, ccl4_table["mean_concentration"], p0=initial_guess)

# Problem 5
# Calculate the reduced chi squared value for the fit. 
reduced_chi_squared = np.sum(((line(ccl4_table.index, linear_params[0], linear_params[1]) - ccl4_table["mean_concentration"])/ccl4_table["sd_concentration"])**2) / len(ccl4_table.index - len(linear_params))

# Problem 6
# Print the parameters, their errors, the final line equation, and the reduced chi squared value.
print("Parameters and their errors:")
print("m: ", linear_params[0], "±", np.sqrt(covariance_matrix[0][0]))
print("b: ", linear_params[1], "±", np.sqrt(covariance_matrix[1][1]))
print("Final line equation: y =",linear_params[0],"x","+",linear_params[1])
print("Reduced Chi Squared:", reduced_chi_squared)

# Problem 7
# Write if a linear model seems appropriate. Make a residual plot of the data.
plt.figure(figsize=(6,6))
plt.scatter(ccl4_table.index, ccl4_table["mean_concentration"] - line(ccl4_table.index, linear_params[0], linear_params[1]))
plt.xlabel("Year")
plt.ylabel("Residuals")
plt.title("Residuals Over Time")
plt.xticks(ticks=ccl4_table.index[::12], labels=ccl4_table["date"][::12], rotation=45)
plt.show()
# - The residual plot shows no clear error pattern, indicating that the linear fit is appropriate.

# Problem 8
# Write a sentence or two about the molecule, and how that background may indicate the trend you are seeing
# - The molecule, carbon tetrachloride, is a common solvent in chemistry labs. Its biggest use was seen as refrigerants and 
# - in fire extinguishers. Its use has seen great decrease over the years due to its harmful effects on the ozone layer. This backstory
# - near-perfectly aligns with the data seen. Although honestly it would be more expected to see a sharp decrease in the data,
# - rather than this linear trend, with the sharpest point being after an agreement called the Montreal Protocol.