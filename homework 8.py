import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

###################################### Part 1 ######################################

# # Problem 1 # # 
# Your goal is to use matplotlib.pyplot and NumPy to plot several sine waves
# by looping through amplitude and frequency values.
# Write a function make_sin_wave that takes in 3 parameters: x, amplitude, and frequency, and outputs the resulting y point of a sine wave.
def make_sin_wave(x,amplitude,frequency):
    return amplitude * np.sin(frequency * x)
# # Problem 2 # # 
# Make an array using NumPy that contains 1000 points between 0 and 2π.
x = np.linspace(0, 2 * np.pi, num=1000)
# # Problem 3 # #
# Generate a frequency and amplitude array with 5 values each.
frequencies = np.array([1,2,3,4,5])
amplitudes = np.array([0.5,1,1.5,2,2.5])
colors = ['red','blue','green','orange','purple']
# # Problem 4 # #
# Create a figure using plt.figure(). Give an argument for figsize.
plt.figure(figsize=(10,10))
# # Problem 5 # #
# Loop through the frequencies and amplitudes using zip() and plot the sine waves. Use a different color for each sine wave.
sinargumentpair = list(zip(frequencies,amplitudes,colors))
for i in range(len(sinargumentpair)):
    plt.plot(x,make_sin_wave(x,sinargumentpair[i][1],sinargumentpair[i][0]),label=f"frequency: {sinargumentpair[i][0]}, amplitude: {sinargumentpair[i][1]}", color=sinargumentpair[i][2])
# # Problem 6 # #
# Add a title, labels, a grid, and a legend.
plt.title("Sine waves")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
#plt.show()

###################################### Part 2 ######################################

# # Problem 1 # #
# Load the data from stars.csv into a pandas DataFrame using pd.read_csv().
stars_df = pd.read_csv("stars.csv")
# # Problem 2 # #
# Print the first 5 rows, the number of rows and columns, the column names, and the data types.
print("First five rows:")
print(stars_df.head())
print("Number of rows and columns:")
print(stars_df.shape)
print("Column names:")
print(stars_df.columns.values)
print("Data types:")
print(stars_df.dtypes)
# # Problem 3 # #
# Calculate the average mass and temperature of the stars, the star with the largest radius, and how many stars have a spectral type that starts with "M"
avg_mass = np.mean(stars_df.iloc[:, 2])
avg_temp = np.mean(stars_df.iloc[:, 4])
biggest_star_radius = max(stars_df.iloc[:, 3])
for i in range(len(stars_df.iloc[:, 3])):
    if stars_df.iloc[:, 3][i] == biggest_star_radius:
        biggest_star = stars_df.iloc[i, 0]
num_mtype_stars = 0
for i in range(len(stars_df.iloc[:, 5])):
    if stars_df.iloc[:, 5][i][0] == 'M':
        num_mtype_stars += 1
print("The average star mass is:", avg_mass)
print("The average star temp is:", avg_temp)
print("The biggest star is:", biggest_star)
print("The number of M-type stars is:", num_mtype_stars)
# # Problem 4 # #
# Sort the stars by distance and give the 3 closest ones. 
stars_distance_df = stars_df.sort_values(by=['Distance (ly)'])
closest_stars = stars_distance_df.iloc[0:3,0].values
print("The three closest stars are:")
print(closest_stars)
# # Problem 5 # #
# Save a filtered dataframe of only M-type stars to a new csv file called m_type_stars.csv.
m_type_stars_df = stars_df
for i in range(len(m_type_stars_df.iloc[:, 5])):
    if m_type_stars_df.iloc[:,5][i][0] != 'M':
        m_type_stars_df = m_type_stars_df.drop(i)
m_type_stars_df.to_csv("m_type_stars.csv", index=False)

###################################### Part 3 ######################################

# # Problem 1 # #
# Load the data set "penguins"
penguins = sns.load_dataset("penguins")
# # Problem 2 # #
# Create a figure with side-by-side subplots.
fig, axes = plt.subplots(1,2, figsize=(12,6))
# # Problem 3 # #
# For the leftmost subplot, make a scatterplot, with a title, axis labels, and a legend
axes[0].scatter(penguins['flipper_length_mm'], penguins['bill_length_mm'], label='Flipper length vs Bill length', color='blue')
axes[0].set_title("Flipper length vs Bill length")
axes[0].set_xlabel("Flipper length (mm)")
axes[0].set_ylabel("Bill length (mm)")
axes[0].legend()
# # Problem 4 # #
# For the rightmost subplot, make a histogram of penguin body mass. 
axes[1].hist(penguins['body_mass_g'], bins=20, color='orange')
axes[1].set_title("Histogram of Penguin Body Mass")
axes[1].set_xlabel("Body mass (g)")
axes[1].set_ylabel("Frequency")
plt.show()