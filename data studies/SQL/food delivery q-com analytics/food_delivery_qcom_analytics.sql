CREATE DATABASE online_food_delivery_analytics;

USE online_food_delivery_analytics;

CREATE TABLE customers (
customer_id INT AUTO_INCREMENT PRIMARY KEY,
customer_name VARCHAR(50) NOT NULL,
city VARCHAR(50) NOT NULL,
signup_date DATE,
is_premium BOOLEAN
);

INSERT INTO customers VALUES
(1,'Aditi','Mumbai','2023-01-10',1),
(2,'Rahul','Delhi','2023-01-15',0),
(3,'Neha','Mumbai','2023-02-01',1),
(4,'Arjun','Pune','2023-02-05',0),
(5,'Sara','Delhi','2023-02-10',1),
(6,'Kunal','Bangalore','2023-02-15',0),
(7,'Riya','Mumbai','2023-03-01',1),
(8,'Aman','Delhi','2023-03-05',0),
(9,'Pooja','Pune','2023-03-10',1),
(10,'Vikas','Bangalore','2023-03-15',0),
(11,'Isha','Mumbai','2023-03-20',1),
(12,'Sahil','Delhi','2023-03-25',0),
(13,'Meera','Pune','2023-04-01',1),
(14,'Nikhil','Bangalore','2023-04-05',0),
(15,'Ananya','Mumbai','2023-04-10',1),
(16,'Rohit','Delhi','2023-04-15',0),
(17,'Simran','Pune','2023-04-20',1),
(18,'Abhishek','Bangalore','2023-04-25',0),
(19,'Tanvi','Mumbai','2023-05-01',1),
(20,'Harsh','Delhi','2023-05-05',0),
(21,'Kriti','Pune','2023-05-10',1),
(22,'Varun','Bangalore','2023-05-15',0),
(23,'Sneha','Mumbai','2023-05-20',1),
(24,'Mohit','Delhi','2023-05-25',0),
(25,'Payal','Pune','2023-06-01',1),
(26,'Deepak','Bangalore','2023-06-05',0),
(27,'Nisha','Mumbai','2023-06-10',1),
(28,'Yash','Delhi','2023-06-15',0),
(29,'Ayesha','Pune','2023-06-20',1),
(30,'Manish','Bangalore','2023-06-25',0),
(31,'Kavya','Mumbai','2023-07-01',1),
(32,'Siddharth','Delhi','2023-07-05',0),
(33,'Ritu','Pune','2023-07-10',1),
(34,'Aditya','Bangalore','2023-07-15',0),
(35,'Palak','Mumbai','2023-07-20',1),
(36,'Gaurav','Delhi','2023-07-25',0),
(37,'Komal','Pune','2023-08-01',1),
(38,'Ashish','Bangalore','2023-08-05',0),
(39,'Shreya','Mumbai','2023-08-10',1),
(40,'Rakesh','Delhi','2023-08-15',0),
(41,'Mansi','Pune','2023-08-20',1),
(42,'Naveen','Bangalore','2023-08-25',0),
(43,'Rashmi','Mumbai','2023-09-01',1),
(44,'Prateek','Delhi','2023-09-05',0),
(45,'Sonia','Pune','2023-09-10',1),
(46,'Akhil','Bangalore','2023-09-15',0),
(47,'Ira','Mumbai','2023-09-20',1),
(48,'Karthik','Delhi','2023-09-25',0),
(49,'Divya','Pune','2023-10-01',1),
(50,'Ravi','Bangalore','2023-10-05',0),
(51,'Nandini','Mumbai','2023-10-10',1),
(52,'Suresh','Delhi','2023-10-15',0),
(53,'Lavanya','Pune','2023-10-20',1),
(54,'Ankit','Bangalore','2023-10-25',0),
(55,'Bhavna','Mumbai','2023-11-01',1),
(56,'Sunil','Delhi','2023-11-05',0),
(57,'Pallavi','Pune','2023-11-10',1),
(58,'Rahul','Bangalore','2023-11-15',0),
(59,'Apoorva','Mumbai','2023-11-20',1),
(60,'Vinay','Delhi','2023-11-25',0);

CREATE TABLE restaurants (
restaurant_id INT AUTO_INCREMENT PRIMARY KEY,
restaurant_name VARCHAR(50),
city VARCHAR(50),
rating FLOAT,
is_cloud_kitchen BOOLEAN
);

INSERT INTO restaurants VALUES
(101,'Spice Hub','Mumbai',4.3,0),
(102,'Burger Box','Delhi',4.1,1),
(103,'Green Bowl','Pune',4.6,0),
(104,'Pizza Planet','Mumbai',3.9,1),
(105,'Curry House','Delhi',4.4,0),
(106,'Wok Express','Bangalore',4.2,1),
(107,'Healthy Bites','Mumbai',4.7,0),
(108,'Tandoori Tales','Delhi',4.0,0),
(109,'Urban Cafe','Pune',4.1,1),
(110,'South Spice','Bangalore',4.5,0),
(111,'Roll Factory','Mumbai',3.8,1),
(112,'Biryani Adda','Delhi',4.6,0),
(113,'Salad Stop','Pune',4.4,0),
(114,'Pasta Street','Bangalore',4.0,1),
(115,'Street Chaat','Mumbai',3.9,0),
(116,'Grill Nation','Delhi',4.5,0),
(117,'Vegan Vault','Pune',4.7,0),
(118,'Quick Bites','Bangalore',3.7,1),
(119,'Punjabi Dhaba','Mumbai',4.2,0),
(120,'Wrap World','Delhi',4.1,1),
(121,'Soup Studio','Pune',4.3,0),
(122,'Rice Bowl','Bangalore',4.0,1),
(123,'Dessert Den','Mumbai',4.6,0),
(124,'Mexican Mania','Delhi',3.8,1),
(125,'Mediterranean Mezze','Pune',4.5,0),
(126,'Noodle Nation','Bangalore',4.2,1),
(127,'BBQ Bliss','Mumbai',4.4,0),
(128,'The Breakfast Club','Delhi',4.3,0),
(129,'Smoothie Bar','Pune',4.1,1),
(130,'Fast Feast','Bangalore',3.9,1);

CREATE TABLE orders (
order_id INT AUTO_INCREMENT PRIMARY KEY,
customer_id INT,
restaurant_id INT,
order_date DATE,
order_value DECIMAL,
delivery_fee DECIMAL,
order_status VARCHAR(30)
);

INSERT INTO orders VALUES
(1001,1,101,'2023-08-01',450,40,'Delivered'),
(1002,2,102,'2023-08-01',320,30,'Cancelled'),
(1003,3,104,'2023-08-02',720,0,'Delivered'),
(1004,4,103,'2023-08-02',260,20,'Delivered'),
(1005,5,105,'2023-08-03',580,50,'Delivered'),
(1006,6,106,'2023-08-03',340,30,'Delivered'),
(1007,7,107,'2023-08-04',900,0,'Delivered'),
(1008,8,108,'2023-08-04',410,40,'Delivered'),
(1009,9,109,'2023-08-05',290,20,'Cancelled'),
(1010,10,110,'2023-08-05',610,30,'Delivered'),
(1011,11,111,'2023-08-06',380,30,'Delivered'),
(1012,12,112,'2023-08-06',840,0,'Delivered'),
(1013,13,113,'2023-08-07',460,40,'Delivered'),
(1014,14,114,'2023-08-07',310,30,'Cancelled'),
(1015,15,115,'2023-08-08',520,50,'Delivered'),
(1016,16,116,'2023-08-08',690,30,'Delivered'),
(1017,17,117,'2023-08-09',980,0,'Delivered'),
(1018,18,118,'2023-08-09',270,20,'Delivered'),
(1019,19,119,'2023-08-10',430,40,'Delivered'),
(1020,20,120,'2023-08-10',360,30,'Delivered'),
(1021,21,121,'2023-08-11',510,50,'Delivered'),
(1022,22,122,'2023-08-11',290,20,'Cancelled'),
(1023,23,123,'2023-08-12',880,0,'Delivered'),
(1024,24,124,'2023-08-12',340,30,'Delivered'),
(1025,25,125,'2023-08-13',620,40,'Delivered'),
(1026,26,126,'2023-08-13',410,30,'Delivered'),
(1027,27,127,'2023-08-14',760,0,'Delivered'),
(1028,28,128,'2023-08-14',380,30,'Delivered'),
(1029,29,129,'2023-08-15',240,20,'Cancelled'),
(1030,30,130,'2023-08-15',450,40,'Delivered'),
(1031,31,101,'2023-09-01',520,50,'Delivered'),
(1032,32,102,'2023-09-01',310,30,'Delivered'),
(1033,33,103,'2023-09-02',470,40,'Delivered'),
(1034,34,104,'2023-09-02',680,0,'Delivered'),
(1035,35,105,'2023-09-03',590,50,'Delivered'),
(1036,36,106,'2023-09-03',330,30,'Cancelled'),
(1037,37,107,'2023-09-04',940,0,'Delivered'),
(1038,38,108,'2023-09-04',420,40,'Delivered'),
(1039,39,109,'2023-09-05',260,20,'Delivered'),
(1040,40,110,'2023-09-05',610,30,'Delivered'),
(1041,41,111,'2023-09-06',390,30,'Delivered'),
(1042,42,112,'2023-09-06',820,0,'Delivered'),
(1043,43,113,'2023-09-07',480,40,'Delivered'),
(1044,44,114,'2023-09-07',300,30,'Cancelled'),
(1045,45,115,'2023-09-08',540,50,'Delivered'),
(1046,46,116,'2023-09-08',710,30,'Delivered'),
(1047,47,117,'2023-09-09',1020,0,'Delivered'),
(1048,48,118,'2023-09-09',280,20,'Delivered'),
(1049,49,119,'2023-09-10',450,40,'Delivered'),
(1050,50,120,'2023-09-10',370,30,'Delivered'),
(1051,51,121,'2023-09-11',530,50,'Delivered'),
(1052,52,122,'2023-09-11',310,30,'Cancelled'),
(1053,53,123,'2023-09-12',910,0,'Delivered'),
(1054,54,124,'2023-09-12',350,30,'Delivered'),
(1055,55,125,'2023-09-13',640,40,'Delivered'),
(1056,56,126,'2023-09-13',420,30,'Delivered'),
(1057,57,127,'2023-09-14',780,0,'Delivered'),
(1058,58,128,'2023-09-14',390,30,'Delivered'),
(1059,59,129,'2023-09-15',250,20,'Cancelled'),
(1060,60,130,'2023-09-15',470,40,'Delivered'),
(1061,1,101,'2023-10-01',560,50,'Delivered'),
(1062,2,102,'2023-10-01',330,30,'Delivered'),
(1063,3,103,'2023-10-02',490,40,'Delivered'),
(1064,4,104,'2023-10-02',720,0,'Delivered'),
(1065,5,105,'2023-10-03',610,50,'Delivered'),
(1066,6,106,'2023-10-03',350,30,'Cancelled'),
(1067,7,107,'2023-10-04',980,0,'Delivered'),
(1068,8,108,'2023-10-04',440,40,'Delivered'),
(1069,9,109,'2023-10-05',270,20,'Delivered'),
(1070,10,110,'2023-10-05',630,30,'Delivered'),
(1071,11,111,'2023-10-06',400,30,'Delivered'),
(1072,12,112,'2023-10-06',860,0,'Delivered'),
(1073,13,113,'2023-10-07',510,40,'Delivered'),
(1074,14,114,'2023-10-07',320,30,'Cancelled'),
(1075,15,115,'2023-10-08',560,50,'Delivered'),
(1076,16,116,'2023-10-08',730,30,'Delivered'),
(1077,17,117,'2023-10-09',1040,0,'Delivered'),
(1078,18,118,'2023-10-09',290,20,'Delivered'),
(1079,19,119,'2023-10-10',470,40,'Delivered'),
(1080,20,120,'2023-10-10',390,30,'Delivered'),
(1081,21,121,'2023-10-11',550,50,'Delivered'),
(1082,22,122,'2023-10-11',320,30,'Cancelled'),
(1083,23,123,'2023-10-12',940,0,'Delivered'),
(1084,24,124,'2023-10-12',360,30,'Delivered'),
(1085,25,125,'2023-10-13',670,40,'Delivered'),
(1086,26,126,'2023-10-13',430,30,'Delivered'),
(1087,27,127,'2023-10-14',810,0,'Delivered'),
(1088,28,128,'2023-10-14',410,30,'Delivered'),
(1089,29,129,'2023-10-15',260,20,'Cancelled'),
(1090,30,130,'2023-10-15',490,40,'Delivered'),
(1091,31,101,'2023-11-01',580,50,'Delivered'),
(1092,32,102,'2023-11-01',340,30,'Delivered'),
(1093,33,103,'2023-11-02',510,40,'Delivered'),
(1094,34,104,'2023-11-02',760,0,'Delivered'),
(1095,35,105,'2023-11-03',630,50,'Delivered'),
(1096,36,106,'2023-11-03',360,30,'Cancelled'),
(1097,37,107,'2023-11-04',1020,0,'Delivered'),
(1098,38,108,'2023-11-04',460,40,'Delivered'),
(1099,39,109,'2023-11-05',290,20,'Delivered'),
(1100,40,110,'2023-11-05',650,30,'Delivered'),
(1101,41,111,'2023-11-06',420,30,'Delivered'),
(1102,42,112,'2023-11-06',890,0,'Delivered'),
(1103,43,113,'2023-11-07',540,40,'Delivered'),
(1104,44,114,'2023-11-07',330,30,'Cancelled'),
(1105,45,115,'2023-11-08',580,50,'Delivered'),
(1106,46,116,'2023-11-08',760,30,'Delivered'),
(1107,47,117,'2023-11-09',1080,0,'Delivered'),
(1108,48,118,'2023-11-09',300,20,'Delivered'),
(1109,49,119,'2023-11-10',490,40,'Delivered'),
(1110,50,120,'2023-11-10',410,30,'Delivered'),
(1111,51,121,'2023-11-11',570,50,'Delivered'),
(1112,52,122,'2023-11-11',330,30,'Cancelled'),
(1113,53,123,'2023-11-12',980,0,'Delivered'),
(1114,54,124,'2023-11-12',380,30,'Delivered'),
(1115,55,125,'2023-11-13',700,40,'Delivered'),
(1116,56,126,'2023-11-13',450,30,'Delivered'),
(1117,57,127,'2023-11-14',840,0,'Delivered'),
(1118,58,128,'2023-11-14',430,30,'Delivered'),
(1119,59,129,'2023-11-15',280,20,'Cancelled'),
(1120,60,130,'2023-11-15',520,40,'Delivered');

SELECT * FROM customers;

SELECT * FROM restaurants;

SELECT * FROM orders;

/* QUESTIONS (EASY):
1. Show all columns from the customers table.
2. List customer names and cities only.
3. Show all distinct cities where customers live.
4. Display the top 3 highest order values.
5. List all delivered orders.
6. Show customer names with an alias user_name.
7. List all orders where delivery fee is greater than 30.
8. Show restaurants that are cloud kitchens.
9. Fetch all customers who signed up after 2023-04-01.
10.Display orders sorted by order value (highest first). */

-- 1
SELECT * FROM customers;

-- 2
SELECT
	customer_name,
    city
FROM customers;

-- 3
SELECT
	city
FROM customers
GROUP BY city;

-- 4
SELECT
	order_value
FROM orders
ORDER BY order_value DESC
LIMIT 3;

-- 5
SELECT 
	order_id
FROM orders
WHERE order_status = 'Delivered';

-- 6
SELECT 
	customer_name AS user_name
FROM customers;

-- 7
SELECT
	order_id
FROM orders
WHERE delivery_fee > 30
ORDER BY order_id DESC;

-- 8
SELECT 
	restaurant_name AS cloud_kitchens
FROM restaurants
WHERE is_cloud_kitchen = 1;

-- 9
SELECT
	customer_id,
    customer_name
FROM customers
WHERE signup_date > '2023-04-01';

-- 10
SELECT 
	order_id
FROM orders
ORDER BY order_value DESC;

/* QUESTIONS (MEDIUM):
1. Find all orders with value between ₹300 and ₹600.
2. List customers from Mumbai or Delhi who are premium.
3. Show restaurants with rating ≥ 4.2.
4. Find orders where status is not delivered.
5. Display customers whose names start with ‘A’.
6. Show all orders with zero delivery fee.
7. List distinct restaurant IDs that received orders.
8. Sort orders by date and then by order value.
9. Find customers who are not premium.
10. Show orders placed in August 2023. */

-- 1
SELECT 
	order_id,
    order_value
FROM orders
WHERE order_value BETWEEN 300 AND 600
ORDER BY order_value DESC;

-- 2
SELECT 
	customer_id,
    customer_name,
    city,
    is_premium
FROM customers
WHERE (city = 'Mumbai' OR city = 'Delhi') AND is_premium = 1;

-- 3
SELECT 
	restaurant_name,
    rating
FROM restaurants
WHERE rating >= 4.2
ORDER BY rating DESC;

-- 4
SELECT
	order_id,
    order_status
FROM orders
WHERE order_status != 'Delivered';

-- 5
SELECT 
	customer_id,
    customer_name
FROM customers
WHERE customer_name LIKE 'a%';

-- 6
SELECT 
	order_id,
    delivery_fee
FROM orders
WHERE delivery_fee = 0;

-- 7
SELECT DISTINCT restaurant_id
FROM orders;

-- 8
SELECT 
	order_id, 
    order_date, 
    order_value
FROM orders
ORDER BY order_date DESC, order_value DESC;

-- 9
SELECT
	customer_id,
    customer_name,
    is_premium
FROM customers
WHERE is_premium = 0;

-- 10
SELECT 
	order_id,
    order_date
FROM orders
WHERE order_date BETWEEN '2023-08-01' AND '2023-08-31'
ORDER BY order_date DESC;

/* QUESTIONS (HARD):
Count total number of orders.
Find the total revenue generated (order_value).
Calculate average order value per city.
Find total number of orders per restaurant.
Show only restaurants with more than 1 order.
Find max, min, and avg order value.
Count how many delivered vs cancelled orders exist.
Calculate total delivery fee collected per city.
Find average rating of cloud kitchens vs non-cloud kitchens.
Show number of premium vs non-premium customers. */

-- 1
SELECT
	COUNT(order_id) AS total_orders
FROM orders;

-- 2
SELECT
	SUM(CASE WHEN order_status = 'Delivered' THEN order_value ELSE 0 END) AS total_revenue
FROM orders;

-- 3
SELECT
    restaurants.city,
    AVG(orders.order_value) AS avg_order_value
FROM orders
JOIN restaurants 
    ON orders.restaurant_id = restaurants.restaurant_id
WHERE orders.order_status = 'Delivered'
GROUP BY restaurants.city;

-- 4
SELECT
	COUNT(order_id) AS total_orders,
    restaurant_id
FROM orders
GROUP BY restaurant_id
ORDER BY restaurant_id ASC;

-- 5
SELECT
	restaurant_id
FROM orders
GROUP BY restaurant_id
HAVING COUNT(order_id) > 1;

-- 6
SELECT
	MAX(order_value) AS max_order_value,
    MIN(order_value) AS min_order_value,
    AVG(order_value) AS avg_order_value
FROM orders;

-- 7
SELECT
	SUM(CASE WHEN order_status = 'Delivered' THEN 1 ELSE 0 END) AS orders_delivered,
    SUM(CASE WHEN order_status = 'Cancelled' THEN 1 ELSE 0 END) AS orders_cancelled
FROM orders;

-- 8
SELECT
	restaurants.city,
    SUM(orders.delivery_fee) AS total_delivery_fee
FROM orders 
JOIN restaurants
	ON orders.restaurant_id = restaurants.restaurant_id
WHERE orders.order_status = 'Delivered'
GROUP BY restaurants.city;

-- 9
SELECT
	AVG(CASE WHEN is_cloud_kitchen = 1 THEN rating END) AS avg_rating_cloud_kitchen,
    AVG(CASE WHEN is_cloud_kitchen = 0 THEN rating END) AS avg_rating_non_cloud_kitchen
FROM restaurants;

-- 10
SELECT
	SUM(CASE WHEN is_premium = 1 THEN 1 ELSE 0 END) AS premium_customers,
    SUM(CASE WHEN is_premium = 0 THEN 1 ELSE 0 END) AS non_premium_customers
FROM customers;

/* QUESTIONS (VERY HARD):
1. Calculate net order value (order_value - delivery_fee) for each order.
2. Find customers who have placed more than 1 order.
3. Show revenue per restaurant only for delivered orders.
4. Categorize orders as:
	- High Value (>500)
	- Medium Value (300–500)
	- Low Value (<300)
5. Find cities where average order value is greater than ₹400.
6. Calculate % of cancelled orders.
7. Find restaurants whose average order value > overall average.
8. Count premium customer orders vs non-premium customer orders.
9. Show monthly order count.
10. Identify restaurants that have never received a cancelled order. */

-- 1
SELECT
	order_id,
    order_value,
    delivery_fee,
	(order_value - delivery_fee) AS net_order_value
FROM orders
ORDER BY net_order_value DESC;

-- 2
SELECT 
	customer_id,
    COUNT(order_id) AS orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 1;

-- 3
SELECT 
	restaurant_id,
    SUM(order_value) AS restaurant_revenue
FROM orders
WHERE order_status = 'Delivered'
GROUP BY restaurant_id
ORDER BY restaurant_revenue DESC;

-- 4
SELECT
    order_id,
    CASE
        WHEN order_value > 500 THEN 'High'
        WHEN order_value BETWEEN 300 AND 500 THEN 'Medium'
        ELSE 'Low'
    END AS order_value_category
FROM orders
ORDER BY order_value DESC;

-- 5
SELECT 
	restaurants.city,
    AVG(orders.order_value) AS avg_order_value
FROM orders
JOIN restaurants
	ON orders.restaurant_id = restaurants.restaurant_id
GROUP BY restaurants.city
HAVING avg_order_value > 400;

-- 6
SELECT
	SUM(CASE WHEN order_status = 'Cancelled' THEN 1 ELSE 0 END) / COUNT(order_id) * 100.0 AS percent_cancelled
FROM orders;

-- 7
SELECT
    restaurant_id,
    AVG(order_value) AS restaurant_avg
FROM orders
GROUP BY restaurant_id
HAVING AVG(order_value) >
       (SELECT AVG(order_value) FROM orders);

-- 8
SELECT
	COUNT(CASE WHEN customers.is_premium = 1 THEN orders.order_id END) AS premium_orders,
    COUNT(CASE WHEN customers.is_premium = 0 THEN orders.order_id END) AS non_premium_orders
FROM orders
JOIN customers
	ON orders.customer_id = customers.customer_id;

-- 9
SELECT
    CASE
        WHEN order_date BETWEEN '2023-08-01' AND '2023-08-31' THEN 'August'
        WHEN order_date BETWEEN '2023-09-01' AND '2023-09-30' THEN 'September'
        WHEN order_date BETWEEN '2023-10-01' AND '2023-10-31' THEN 'October'
        ELSE 'November'
    END AS monthly_order_category,
    COUNT(order_id) AS monthly_orders
FROM orders
GROUP BY monthly_order_category
ORDER BY monthly_orders DESC;

-- 10
SELECT
    restaurant_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY restaurant_id
HAVING SUM(CASE WHEN order_status = 'Cancelled' THEN 1 ELSE 0 END) = 0;

/* QUESTIONS (HOTS):
1. Which city is least profitable after deducting delivery fees?
2. Are premium users actually ordering higher-value orders? Prove with data.
3. Identify restaurants that rely heavily on discounted delivery (0 fee).
4. If free delivery is given for orders > ₹500, how many orders qualify?
5. Rank cities by average order value.
6. Find customers who order frequently but spend less.
7. Which restaurant would you remove from the platform and why (data-backed)?
8. Simulate a policy:
	“Remove cloud kitchens with rating < 4 and avg order value < 350” — who gets removed?
9. Create a profitability flag per order:
	- Profitable if net value > 400
	- Loss
10. From data alone, suggest one business strategy improvement. */

-- 1
SELECT 
		SUM(orders.order_value - orders.delivery_fee) AS profits_after_deduction,
        restaurants.city
FROM orders
JOIN restaurants
	ON orders.restaurant_id = restaurants.restaurant_id
WHERE orders.order_status = 'Delivered'
GROUP BY restaurants.city
ORDER BY profits_after_deduction ASC 
LIMIT 1;

-- 2
SELECT 
	CASE
		WHEN customers.is_premium = 1 THEN 'premium_user'
        WHEN customers.is_premium = 0 THEN 'non_premium_user'
	END AS user_type,
    SUM(CASE WHEN orders.order_status = 'Delivered' THEN orders.order_value ELSE 0 END) AS final_value
    FROM orders
    JOIN customers
		ON orders.customer_id = customers.customer_id
	GROUP BY user_type
	ORDER BY final_value DESC;

-- 3
SELECT
		restaurants.restaurant_id, 
        restaurants.restaurant_name,
        COUNT(orders.order_id) AS free_delivery
FROM orders
JOIN restaurants
	ON orders.restaurant_id = restaurants.restaurant_id
WHERE delivery_fee = 0
GROUP BY restaurants.restaurant_id, restaurants.restaurant_name;

-- 4
SELECT 
		SUM(CASE WHEN order_value > 500 THEN 1 ELSE 0 END) AS applicable_discount
FROM orders;

-- 5
SELECT 
		restaurants.city,
        AVG(orders.order_value) AS avg_value
FROM orders
JOIN restaurants
	ON orders.restaurant_id = restaurants.restaurant_id
GROUP BY restaurants.city
ORDER BY avg_value DESC;

-- 6
SELECT
    customers.customer_id,
    customers.customer_name,
    COUNT(orders.order_id) AS frequency,
    AVG(orders.order_value) AS avg_order_value
FROM orders
JOIN customers
    ON orders.customer_id = customers.customer_id
GROUP BY customers.customer_id, customers.customer_name
HAVING COUNT(orders.order_id) > 1 AND AVG(orders.order_value) < 500
ORDER BY frequency DESC;

-- 7
SELECT 
    restaurants.restaurant_id,
    restaurants.restaurant_name,
    restaurants.city,
    COUNT(orders.order_id) AS total_orders,
    SUM(orders.order_value) AS total_revenue,
    AVG(orders.order_value) AS avg_order_value,
    SUM(CASE WHEN orders.order_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders,
    ROUND(
        SUM(CASE WHEN orders.order_status = 'Cancelled' THEN 1 ELSE 0 END) * 1.0 
        / COUNT(orders.order_id),
        2
    ) AS cancellation_rate
FROM orders 
JOIN restaurants 
    ON orders.restaurant_id = restaurants.restaurant_id
GROUP BY restaurants.restaurant_id, restaurants.restaurant_name, restaurants.city
ORDER BY 
    cancellation_rate DESC,
    total_revenue ASC,
    avg_order_value ASC
LIMIT 1;

-- 8
SELECT
		restaurants.restaurant_id,
        restaurants.restaurant_name,
		restaurants.rating,
        AVG(CASE WHEN orders.order_status = 'Delivered' THEN orders.order_value END) AS avg_order_value
FROM orders
JOIN restaurants
	ON orders.restaurant_id = restaurants.restaurant_id
GROUP BY restaurants.restaurant_id, restaurants.restaurant_name
HAVING restaurants.rating < 4 AND AVG(CASE WHEN orders.order_status = 'Delivered' THEN orders.order_value ELSE 0 END) < 350
ORDER BY 
		restaurants.rating ASC,
        avg_order_value ASC;

-- 9


-- 10