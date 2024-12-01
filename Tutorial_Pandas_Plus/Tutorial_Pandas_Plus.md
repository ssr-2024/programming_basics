# Pandas Plus
---
Hello, Dear Friend!  

In this tutorial, you’ll learn how to organize and clean a messy Excel file using Python's powerful **pandas** library. In real-world scenarios, data files are rarely perfectly formatted. You might encounter Excel sheets with the data all in one messy sheet.

To work effectively with data visualization libraries like **Plotly** or **Matplotlib**, having a well-structured Excel sheet is crucial. This means having a clear header row, an index column, and consistently formatted data throughout. A clean, well-organized dataset not only makes it easier to visualize data but also enhances the accuracy and efficiency of your analysis.

This tutorial will guide you through the process of using **pandas** to:
- **Split and organize data** into individual, well-formatted sheets.
- Prepare your data for seamless use in data analysis and visualization.

By the end of this tutorial, you’ll have the skills to transform messy, complex spreadsheets into clean, organized datasets that are ready for analysis. Let’s get started and make data cleaning a breeze! 

If you are at any point stuck with the exercises, you can consult the *Cheatsheet.md* file which contains the solutions to the code you will have to complete
## O. Download the messy excel file
In the provided folder, you will find a file called *messyfile.xlsx* This is your starting point. Open the excel file and make yourself familiar.

ProTip: Download the extension called [Excel Viewer](vscode:extension/GrapeCity.gc-excelviewer), this will make your life and this tutorial way easier.


## Task 1: Creating new sheets using delimiters
If you inspect the *messyfile.xlsx* file closely, you will be able to find these lines in certain rows:
```
---------------
````
These are called delimiters, which are frequently used in excel to separate data. So if your messy excel sheet has these delimiters, you can use them to devide the data into different sheets and make your life way easier. In this example the first part of the excel file is not interessting. The lower part is more important and we want devide it into three different sheets:
- CLUSTER STATISTICS FOR 5 CLUSTERS 
- RELOCATION: K-Means Cluster Analysis with 5 clusters
- K-MEANS CLUSTER STATISTICS FOR 5 CLUSTERS

For your first task, open the *Task1.py* file and complete the code in two sections.
To be able to use the new functions, you can read the following documentations
1. [Iloc function](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)
2. [str.contains](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html)

## Task 2: Creating sheets using headers
Great job on creating your new excel file.

For the second task, let's just focus on the sheet "CLUSTER STATISTICS FOR 5". This sheet contains several tables which are of great intrest, but they are not devide by a delimiter. Therefore the first method would not work.

That's why this task will teach you to create new sheets from tables using their headers.

Open the *Task2.py* file and complete the code. Use your newely created excel sheet as the basis.

You will have to define two functions, one which identifies the startrow based on the exact match of a keyword and one with only a partial match. 
*(because if the title contains special caracters, which have been removed by sanitization because excel sheet names can't contain special caracters, it won't be an exact match and therfore the first method will not work)*

For creating the `find_section_start_partial` you can use the Methode 1 described in this [guide](https://www.geeksforgeeks.org/select-rows-that-contain-specific-text-using-pandas/) to create the variable **matches**

For creating the `find_section_start_exact` you could define the variable **matches** differently using the [str.strip](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.strip.html) function and the `==` operator which you already know.

Good Luck!


# Ending
Congratulations on completing this little tutorial.
If you now want to continue working with this data and for example create your own lineplots displaying each cluster, you could continue with the tutorial of Robin Schärer.