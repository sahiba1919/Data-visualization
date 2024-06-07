# Data-visualization
The visualization and analysis performed on the Medium dataset aim to provide insights into the articles' performance and characteristics.
Dataset Overview:

The dataset contains various columns such as ID, date, title, subtitle, publication, claps, reading time, responses, and URL.
The initial exploration includes displaying the first few rows of the dataset and printing its shape.

Data Cleaning:
The 'image' column is dropped as it's not required for analysis.
Column positions are rearranged for better readability.
Columns are renamed to have more descriptive names.

Data Transformation:
A new column 'Total' is created, summing up the numeric columns' values.
Summary statistics are generated for the dataset.
Data Quality Check:

Missing values are checked and found to be zero in all columns.
Exploratory Data Analysis (EDA):

The dataset is sorted by the 'Total' column in descending order.
The top 5 articles with the highest 'Total' values (sum of numeric columns) are transposed to display their 'Claps' and 'Publication'.
Minimum and maximum numbers of claps are printed.
Counts of posts for each publication are calculated and displayed, along with their percentage distribution.
A bar plot is created to visualize the distribution of publications.
Insights:

The mean reading time for articles is calculated.
The titles of articles with the maximum number of claps and responses are identified, along with their respective indices.
The publications with articles having the maximum number of claps and responses are determined.
The analysis provides insights into article performance, publication distribution, and characteristics based on the provided Medium dataset.



