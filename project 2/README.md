# First ML Workflow

Here we classify an image whether it is a bicycle or motorcycle.

## Overview
In this project we create a general ML workflow on AWS.

We learn how to create Endpoints, use Lambda and Step Functions. And finally we learn how to monitor ML workflow with Model Monitor.

## Lambda Functions
All lambda functions are located in [lambda_functions/](lambda_functions/)

## Step Function
Step Function's JSON Definition is located in [step_function/](step_function/)

Screenshot of working Step Function:

### Succeded Step Function:
![Screenshot.png](step_function/Screenshot_1.png)

### Failed Step Function:
![Screenshot.png](step_function/Screenshot_2.png)

## Visualization
The vizualization demonstrates the resulting inferences:

### Scatter plot:
![scatter.png](vizualization/scatter.png)

### Histogram:
![hist.png](vizualization/hist.png)

### Box plot:
![boxplot.png](vizualization/boxplot.png)