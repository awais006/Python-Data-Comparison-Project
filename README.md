## Python Data Comparison Project

This Python project involves fetching data from API, JSON data handling, working with Parquet files
and performing calculations. 

I will compare two product lists - actual data from url and expected data stored in Parquet file.

### Actual data
I get Products data from `https://dummyjson.com/products`
- **Total amount of products > 100** (I have used query parameters in the above path)
- Final price for each product is calculated using 2 fields from the response - "price" and "discountPercentage"
- **Here - expected data is not overwritten with actual data!** New field is added to save actual data.

### Expected data 
Stored in `./data/product_prices_calculated.parquet`
- Final price in expected data has been rounded to 2 decimal places

### Questions
1. What product is the most expensive according to actual data?
2. What product is missing in expected data?
3. For how many rows final price in expected data matches with calculated price from actual data?

### Features
1. Get actual data from URL
2. Read expected from Parqeut file
3. Show the most expensive product
4. Used Lamda function to Get Expensive product from API JSON data
4. Show list of products that are present in API JSON data but missing from Parquet file
5. Show list of products where Final price is same in API JSON data and Parquet file.


**Code follows PEP8 standards.** 
- It is easy to read, effective and explicit.
- Modular programming is used to create seperate functions for each step.