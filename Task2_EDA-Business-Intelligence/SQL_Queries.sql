-- SQL Query 1: Top 5 Products by Revenue

SELECT Product,
SUM(Total_Sales) AS Revenue
FROM sales_data
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5;

-- SQL Query 2: City-wise Sales Performance

SELECT City,
SUM(Total_Sales) AS Total_Revenue
FROM sales_data
GROUP BY City
ORDER BY Total_Revenue DESC;

-- SQL Query 3: Category-wise Sales Performance

SELECT Category,
SUM(Total_Sales) AS Revenue
FROM sales_data
GROUP BY Category
ORDER BY Revenue DESC;

-- SQL Query 4: Gender-wise Sales Analysis

SELECT Gender,
SUM(Total_Sales) AS Revenue
FROM sales_data
GROUP BY Gender
ORDER BY Revenue DESC;

-- SQL Query 5: Average Sales per Customer

SELECT Customer_Name,
AVG(Total_Sales) AS Average_Sales
FROM sales_data
GROUP BY Customer_Name
ORDER BY Average_Sales DESC
LIMIT 10;

-- SQL Query 6: Product-wise Quantity Sold

SELECT Product,
SUM(Quantity) AS Total_Quantity
FROM sales_data
GROUP BY Product
ORDER BY Total_Quantity DESC;

-- SQL Query 7: Monthly Sales Trend

SELECT strftime('%m', Order_Date) AS Month,
SUM(Total_Sales) AS Monthly_Sales
FROM sales_data
GROUP BY Month
ORDER BY Month;
