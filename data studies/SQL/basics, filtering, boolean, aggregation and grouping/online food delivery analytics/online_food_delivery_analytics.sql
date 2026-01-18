CREATE DATABASE online_food_delivery_analytics;

USE online_food_delivery_analytics;

CREATE TABLE customers (
customer_id INT AUTO_INCREMENT PRIMARY KEY,
customer_name VARCHAR(50) NOT NULL,
city VARCHAR(50) NOT NULL,
signup_date DATE,
is_premium BOOLEAN
);

