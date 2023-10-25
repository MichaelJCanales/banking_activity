# Instructions

You are a data engineer at a national Portuguese consumer bank, **Banking Objects of Portugal (BOofP)**.

Recently, a project has come across your team's desk to engineer a pipeline in Python to analyze stock data. This pipeline will be used by the machine learning team to restructure [terabytes](https://www.youtube.com/watch?v=-aYat9357mE) of data, which will subsequently be integrated with daily news headline data to measure how reliably [sentiment](https://aws.amazon.com/what-is/sentiment-analysis/) predicts stock price.

**Note**: If we were to do this in a traditional "big data" setting, we would most likely use something more powerful, such as [snowflake](https://docs.snowflake.com/en/user-guide/data-pipelines-intro) or [databricks](https://azure.microsoft.com/en-us/products/databricks) (both products that we will take a look at later). However, it's not uncommon for small teams to engineer their pipelines using a language like Python.

To achieve this, your team has decided to implement classes in Python. Your coworker has completed some basic steps of this pipeline but now relies on your OOP knowledge and documentation-reading skills to complete the rest and debug a few lines of code.

This repository represents an incomplete data engineering project that aims to satisfy the project goal above. We currently have a sample dataset of 9 weeks. The sections below contain instructions as to what exactly you must complete.

There is one difficulty level for this project.

Utilize documentation, your peers, readings, and classroom notes to complete this project. 

## Background

### Validation.py

Before beginning this project, note the `code/test/validate.py` module. 

You will use this script to validate if your code is running successfully as you complete each of the 3 parts. To validate if the `average01` function is working correctly, run

```bash
python -m code.test.validate pt1
```

To validate if both `average01` and `median01` is working correctly, you will run:

```bash
python -m code.test.validate pt2
```

And lastly, to run all 3 parts, including `stddev03`, you will run:

```bash
python -m code.test.validate pt3
```

### StockData.py

This project makes use of the OOP principle of [polymorphism](https://www.w3schools.com/python/python_polymorphism.asp). We implement a `StockData` class in the `StockData.py` file of this project. This class has two simple methods: one initialization method (where our data is initially set to `None`) and another `load()` method, which we use to load our data.

This class should remain unmodified, as all the code presents a complete solution. This class simply allows us to interact with our data using `self.data`.

Feel free to explore the code and documentation. See if you can trace the logic of this program. Reading code sharpens our coding skills.

### Metrics

Before diving into the code, it's essential to understand the meaning and significance of the metrics you'll be calculating:

**Average (Mean):**
The average, commonly known as the mean, gives us a central value of a dataset. By adding up all the numbers and then dividing by the count of numbers, we get a value that represents the "middle" of the dataset. While the average is useful, it can sometimes be skewed by very high or very low values.

**Median:**
Unlike the average, which considers all values equally, the median is the middle number in a sorted list of numbers. For an even number of values, it's the average of the two middle numbers. The median can provide a better sense of a dataset's central tendency when it contains outliers.

**Sample Standard Deviation:**
While the average and median give us central values, the standard deviation tells us about the spread of our data. A low standard deviation indicates that the values tend to be close to the mean, while a high standard deviation indicates that values are spread out over a wider range. The sample standard deviation specifically accounts for datasets that are a sample of a larger population, adjusting the calculation slightly compared to the "population" standard deviation.
 
## Part 1: Average

Your first task in the `average01` function of the `StockMetrics.py` file is to compute the average of stock prices from the given list of lists data. The data is in initially the form of strings. Also, there may be missing data points which you need to account for. 

1. Inside the `average01` function of the StockMetrics class, we begin by iterating over each row of self.data.

2. For each row, create a new list of valid numerical stock prices. Convert the strings to numbers, but be cautious and skip any values that are empty strings.

3. Compute the average of these valid prices for the current row. Remember, to compute the average, sum up all the values and then divide by the count of those values. After computing the average, round this answer to the nearest 3rd decimal place.

4. Append the computed average for the current row to your `averages` list.

## Part 2: Median

The next task, similar to the first, is to compute the median of each row of the data in the `median02` function of the `StockMetrics.py` file. Feel free to repurpose the code you've used above to accomplish this.

1. Before you iterate over each list in `self.data`, be sure to create a data structure that will save all of our median values.

2. As you loop through each list of `self.data`, ensure that you convert the strings to numbers and skip any values that are empty strings.

3. After completing this conversion, utilize the `median` function from the `statistics` module to calculate the median value. Do not round this answer.

4. Store the median for each row in the data structure that you've created before beginning our loop.

5. Be sure to return this value

## Part 3: Sample Standard Deviation

For this last part, you will compute the sample standard deviation for each row of data in `self.data` in the `stddev03` function of the `StockMetrics.py` file.

1. Before you iterate over each list in `self.data`, be sure to create a data structure that will save all of our standard deviation values.

2. As you loop through each list of `self.data`, ensure that you convert the strings to numbers and skip any values that are empty strings.

3. After completing this conversion, utilize the `stddev` function from the `statistics` module to calculate the sample standard deviation value. After computing the standard deviation, round this answer to the nearest 3rd decimal place.

4. Store the standard deviation for each row in the data structure that you've created before beginning our loop.

5. Be sure to return this value


**Hints:**

* A conditional check in a list comprehension can help you filter out any empty string values. This can also perform quick-type casting as well! 

```python
new_lst = [type(val) for row in val if val != " "]
```

* Once you solve one of these functions, the other functions will follow the same pattern. The only difference is the metric that we are calculating.

## Part 4: Post Write-Up

Lastly, all good projects are flush with documentation where needed.

After completing the 3 parts above, you will move on to filling out the documentation in the `README.md` file. 

## Submission

The due date for this project is `10/30`.

To submit this project, you will push a completed version of this repository to your GitHub and post a link to your repo in Canvas.

**Note**: You must upload this to GitHub and submit a GitHub link to receive a grade for this project.
