# $ pip3 install pandas
# pip3 install matplotlib
# https://www.geeksforgeeks.org/data-visualization-different-charts-python/

# import pandas and matplotlib 
import sys
import pandas as pd 
import matplotlib.pyplot as plt 
  
### Same code from Dataframe as other charts ###

# create 2D array of table given above 
data = [['E001', 'M', 34, 123, 'Normal', 350], 
        ['E002', 'F', 40, 114, 'Overweight', 450], 
        ['E003', 'F', 37, 135, 'Obesity', 169], 
        ['E004', 'M', 30, 139, 'Underweight', 189], 
        ['E005', 'F', 44, 117, 'Underweight', 183], 
        ['E006', 'M', 36, 121, 'Normal', 80], 
        ['E007', 'M', 32, 133, 'Obesity', 166], 
        ['E008', 'F', 26, 140, 'Normal', 120], 
        ['E009', 'M', 32, 133, 'Normal', 75], 
        ['E010', 'M', 36, 133, 'Underweight', 40] ] 
  
# dataframe created with 
# the above data array 
df = pd.DataFrame(data, columns = ['EMPID', 'Gender',  
                                    'Age', 'Sales', 
                                    'BMI', 'Income'] ) 
  

### For each numeric attribute of dataframe ###
'''
    A box plot is a graphical representation of statistical data based on the minimum, 
    first quartile, median, third quartile, and maximum. The term “box plot” comes from the 
    fact that the graph looks like a rectangle with lines extending from the top and bottom. Because of the extending lines, this type of graph is sometimes called a box-and-whisker plot. For quantile and median refer to this Quantile and median.
'''
df.plot.box() 
  
# individual attribute box plot 
plt.boxplot(df['Income']) 
plt.show() 