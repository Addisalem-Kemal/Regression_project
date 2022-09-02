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
                 | - see https://en.wikipedia.org/wiki/FIPS_county_code for more details  |
 
