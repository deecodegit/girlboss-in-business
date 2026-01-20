# **Learning Project 1 - Online Food Delivery Analytics**



### **Purpose**

The purpose of this project is to analyze a food delivery platform’s relational database using SQL, with emphasis on query construction, data filtering, aggregation, conditional logic, and analytical reasoning.

The project progresses from basic data retrieval to high-order analytical queries, enabling structured learning and evaluation of SQL capabilities.



### **Business Context**

You are a data analyst at an online food delivery platform (Blinkit/Zomato/Swiggy-like).



The business wants to understand:

* Customer behavior
* Restaurant performance
* Order patterns
* Revenue and operational efficiency



### **Data Sets**

`customers`
\[Data File](data studies/SQL/online food delivery analytics/customers.csv)



`orders`
\[Data File](data studies/SQL/online food delivery analytics/orders.csv)



`restaurants`
\[Data File](data studies/SQL/online food delivery analytics/restaurants.csv)

### 

### **Analysing the business using SQL**



Write queries using SQL for the following:

#### 

#### Customer Base Analysis

*(Who your users are, how they behave, and their value)*



* Show all columns from the customers table
* List customer names and cities only
* Show all distinct cities where customers live
* Show customer names with an alias `user\\\\\\\\\\\\\\\_name`
* Fetch all customers who signed up after `2023-04-01`
* List customers from Mumbai or Delhi who are premium
* Display customers whose names start with ‘A’
* Find customers who are not premium
* Show number of premium vs non-premium customers
* Find customers who have placed more than 1 order
* Count premium customer orders vs non-premium customer orders
* Are premium users actually ordering higher-value orders? Prove with data
* Find customers who order frequently but spend less



#### Order \& Revenue Analysis

*(Money flow, order behavior, demand patterns)*



* Display the top 3 highest order values
* List all delivered orders
* List all orders where delivery fee is greater than 30
* Display orders sorted by order value (highest first)
* Find all orders with value between ₹300 and ₹600
* Find orders where status is not delivered
* Show all orders with zero delivery fee
* Sort orders by date and then by order value
* Show orders placed in August 2023
* Count total number of orders
* Find the total revenue generated `order\\\\\\\\\\\\\\\_value`
* Find max, min, and avg order value
* Count how many delivered vs cancelled orders exist
* Calculate net order value (`order\\\\\\\\\\\\\\\_value` - `delivery\\\\\\\\\\\\\\\_fee`) for each order
* Categorize orders as High / Medium / Low value
* Calculate % of cancelled orders
* Show monthly order count
* If free delivery is given for orders > ₹500, how many orders qualify?
* Rank cities by average order value
* Create a profitability flag per order (Profitable / Loss)



## Restaurant Performance \& Quality

*(Which restaurants perform well, which don’t, and why)*



* Show restaurants that are cloud kitchens
* Show restaurants with rating ≥ 4.2
* List distinct restaurant IDs that received orders
* Find total number of orders per restaurant
* Show only restaurants with more than 1 order
* Find average rating of cloud kitchens vs non-cloud kitchens
* Show revenue per restaurant only for delivered orders
* Find restaurants whose average order value > overall average
* Identify restaurants that have never received a cancelled order
* Which restaurant would you remove from the platform and why (data-backed)?
* Simulate policy: “Remove cloud kitchens with rating < 4 and avg order value < 350” — who gets removed?



#### Operational \& Policy Impact Analysis

*(Decisions, efficiency, profitability, strategy)*



* Calculate total delivery fee collected per city
* Find cities where average order value is greater than ₹400
* Which city is least profitable after deducting delivery fees?
* Identify restaurants that rely heavily on discounted delivery (0 fee)
* From data alone, suggest one business strategy improvement



### **SQL Concepts Covered**

* Core SQL Foundations
* Filtering and Boolean Logic
* Sorting, Time and Date Handling
* Aggregation Functions and Metrics
* `GROUP BY` and `HAVING`
* Conditional Logic with `CASE WHEN`
* Mathematical and Expression-based Queries
* Basic JOINs and Multi-table Analysis
* Subqueries and Advanced Comparisons
* Ranking and Comparative Analytics



### **How to Use:**

#### 

#### Set Up the Database



You may use any SQL-supported database tool of your choice (MySQL, PostgreSQL, SQLite, etc.).

This project was built and tested using MySQL Workbench.



* Create a new database (e.g., online\_food\_delivery\_analytics)
* Create the following tables:

 	- `customers`

 	- `orders`

 	- `restaurants`

* Import the provided CSV files into their respective tables:

 	- `customers.csv`

 	- `orders.csv`

 	- `restaurants.csv`



*Ensure correct data types for dates, numeric values, and categorical fields while importing.*



#### Analyze the Business Using SQL



* Navigate to the “Analysing the business using SQL” section in this repository.
* Write SQL queries to answer each question under:

 	- Customer Base Analysis

 	- Order \& Revenue Analysis

 	- Restaurant Performance \& Quality

 	- Operational \& Policy Impact Analysis



The questions are intentionally ordered from basic to advanced to support structured learning.



You are encouraged to:

* Write queries incrementally
* Experiment with alternative approaches
* Validate results using aggregates and cross-checks



### **Expected Learning Outcome**

By completing this project, you should be able to:

* Write efficient SQL queries from basic to advanced level
* Perform real-world style business analysis using SQL
* Translate raw data into actionable insights
* Simulate business policies and evaluate their impact using data
