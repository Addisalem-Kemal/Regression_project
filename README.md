# **Regression Project**

## Project Description:


The purpose of this project is to build a machine learning model that predicts the value of single unit properties that the tax district assesses using the property data from properties sold and purchased in the year 2017.

## Goals:
The goals of this project is as follows:

1  A Complete Jupyter Notebook Report that:
   - shows the step-by-step process of collecting and wrangling data, 
   - explores the possible drivers of the tax value, 
   - run a statistical analysis of various features and 
   - finally, model and test the chosen features using common regression techniques.
 
2  A README.md file containing:

  - Project description with goals
  - Data dictionary
  - Project planning (a step by step process through the data science pipeline)
  - Explanation of how this project and its findings can be reproduced
  - Key findings and takeaways from the project.
  
3  A wrangle.py file that holds the functions to acquire and prepare the data for machine learning algorithm.

## Project Planning:


### Projet Outline:

  - Acquisiton of data through Codeup SQL Server, using env.py file with username, password, and host
  - Prepare and clean data with python - Jupyter Notebook  
  - Explore data:
      - If value are what the dictionary says they are
      - null values
        - are the fixable or should they just be deleted
      - Categorical or continuous values
      - Make graphs that show
  - Run statistical analysis
  - Model data
  - Test Data
  - Conclude results
  - Further recommendations 
 
 ## Key Findings:
 
 ## Data Dictionary:
 
 | Attribute     | Definition                                                             | Data Type
 |---------------|------------------------------------------------------------------------|-----------------
 | parcelid      | unique identifier of parcels of property                               | primary key/int
 | bedrooms      | number of bedrooms in a property                                       | float
 | bathrooms     | number of bathrooms (including half-baths)                             | float
 | area          | total calculated living area of the property                           | float
 | year_built    | the year that the property was build                                   | float
 | tax_amount    | property tax assessed for the tax year                                 | float
 | tax_value     | total tax assessed value of a parcel                                   | float
 | fips          | Federal Information Processing Standard code                           | int
 | 
                 | - see https://en.wikipedia.org/wiki/FIPS_county_code for more details  |
                 
 - there were 63 columns worth of data points but had a lot of missing values that got filtered down to what was deemed relevant drivers.

## Stats

   - Surprisingly the number of bathrooms were a better driver for value than the bedrooms.
   - Area correlates best with the tax value of the chosen features.
   
## Modeling:

   - My best model was the Polynomial Regression model with a power of 2:
   - RMSE of 13615.6212 from a baseline of 511389.7412
   - RMSE improvement of 58534.1588
   - R2 Value of the model, 35.8%, indicates there is an improvement over the baseline but not a very strong fit overall.
   
### Recommendations:

   - The data had too many empty values that were not useful in the modeling. A more complete data could give a better model
   - Demographic and socio-economic data can be drivers since people care about the types of neighbors they have.
   - Crime data, school district data performance data may also be drivers.
   - If I had more time I would split them by counties and see if that imporoves the model
   - 
### Reproduce:
     - Pull all files from this repository
     - Add env.py file to the repository folder
     - Open Zillow_projest.ipynb and click through each cell to run
     - Each cell is commented with the actions of it and walks through the pipeline process
     - Random state set at 42

