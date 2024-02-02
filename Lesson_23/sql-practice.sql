-- 1. Show the category_name and description from the categories table sorted by category_name.
select category_name, description from categories order by category_name asc;

-- 2. Show the product_name and unit_price from the products table sorted by unit_price in descending order.
select product_name, unit_price from products order by unit_price desc;

-- 3. Show all the contact_name, address, city of all customers which are not from 'Germany', 'Mexico', 'Spain'
select contact_name, address, city FROM customers where country Not In ('Germany', 'Mexico', 'Spain');

-- 4. Show all the contact_name, city, and country of customers from countries other than 'USA', 'Canada', and 'Mexico'.
select contact_name, city, country FROM customers where country Not In ('USA', 'Canada', 'Mexico');

-- 5. Show order_date, shipped_date, customer_id, Freight of all orders placed between '2019-05-01' and '2019-06-30'.
select order_date, shipped_date, customer_id, freight FROM orders where order_date between '2017-05-01' and '2017-06-30';

-- 6. Show order_date, shipped_date, customer_id, Freight of all orders placed on 2018 Feb 26
select order_date, shipped_date, customer_id, freight FROM orders where order_date = '2018-02-26';

-- 7. Show the employee_id, order_id, customer_id, required_date, shipped_date from all orders shipped later than the required date
select employee_id, order_id, customer_id, required_date, shipped_date FROM orders where shipped_date > required_date;

-- 8. Show the company_name, contact_name, fax number of all customers that has a fax number.
select company_name, contact_name, fax FROM customers where fax IS NOT NULL;

-- 9. Show the employee_id, order_id, customer_id, required_date, shipped_date from all orders where shipped_date is earlier than required_date.
select employee_id, order_id, customer_id, required_date, shipped_date FROM orders where shipped_date < required_date;

-- 10. Show the supplier_name, contact_name, phone number of all suppliers that have a phone number.
select company_name, contact_name, phone FROM suppliers where phone IS NOT NULL;

-- 11. Show the first_name, last_name, hire_date of employees hired before '2022-01-01'.
select first_name, last_name, hire_date from employees where hire_date < '2022-01-01';

-- 12. Show the product_name, quantity_per_unit, units_in_stock of all products that have less than 10 units in stock.
select product_name, quantity_per_unit, units_in_stock from products where units_in_stock < 10;

-- 13. Show the company_name, contact_name, contact_title of customers that have a contact_title.
select company_name, contact_name, contact_title from customers where contact_title IS NOT NULL;

-- 14. Show the order_id, ship_country, ship_region of orders where ship_country is not 'USA' and ship_region is not empty.
select order_id, ship_country, ship_region from orders where not ship_country = 'USA' and NOT ship_region = '';

-- 15. Show the employee_id, last_name, first_name of the employees who have the title 'Sales Representative'.
select employee_id, last_name, first_name FROM employees where title IS 'Sales Representative';

-- 16. List the products that were ordered more than once in a single order. Display the product name, order ID, and quantity ordered.
select product_name, order_id, quantity from order_details join products on order_details.product_id = products.product_id group by order_details.order_id having count (order_details.order_id) > 1;

-- 17. Retrieve the top 10 most ordered categories of products. Display the category name and the total quantity of products ordered within each category.
select product_id, SUM(quantity) from order_details group by product_id order by SUM(quantity) desc limit 10;
SELECT categories.category_name, SUM(order_details.quantity) as total_quantity_ordered FROM order_details JOIN products ON order_details.product_id = products.product_id JOIN categories ON products.category_id = categories.category_id GROUP BY categories.category_name LIMIT 5;

-- 18. Find the employees who have never handled any orders. Display their names and hire dates.
select employee_id from employees EXCEPT Select employee_id from orders;         ???

-- 19. Retrieve a list of orders with the customer's company name and the employee's first and last names. Include only orders placed after January 1, 2010
select customers.company_name, orders.order_id, orders.order_date, employees.first_name, employees.last_name
from orders
join customers
	on customers.customer_id = orders.customer_id
join employees
	on employees.employee_id = orders.employee_id
where order_date > '2010-01-01'
order by customers.company_name

-- 20. Retrieve a list of customers and suppliers who are located in the same city. Display the company name and city for both customers and suppliers. If a city doesn't have any customers or suppliers, show "No Data" for the missing side.
select distinct customers.company_name as customers_company_name, customers.city as customers_city, suppliers.company_name as suppliers_company_name, suppliers.city as suppliers_city
from customers
join orders
	on orders.customer_id = customers.customer_id
join order_details
	on order_details.order_id = orders.order_id
Join products
	on products.product_id = order_details.product_id
join suppliers
	on suppliers.supplier_id = products.supplier_id

---------------------------------------------------

WITH CustomerCities AS (
    SELECT DISTINCT customers.company_name, customers.city
    FROM customers
    JOIN orders ON customers.customer_id = orders.customer_id
    JOIN order_details ON orders.order_id = order_details.order_id
),
SupplierCities AS (
    SELECT DISTINCT suppliers.company_name, suppliers.city
    FROM suppliers
    JOIN products ON suppliers.supplier_id = products.supplier_id
    JOIN order_details ON products.product_id = order_details.product_id
)

-- Performing a FULL OUTER JOIN on these subqueries and ordering by city
SELECT 
    COALESCE(CustomerCities.company_name, 'No Data') AS customers_company_name,
    COALESCE(SupplierCities.company_name, 'No Data') AS suppliers_company_name,
    COALESCE(CustomerCities.city, SupplierCities.city, 'No Data') AS city
FROM CustomerCities
FULL OUTER JOIN SupplierCities ON CustomerCities.city = SupplierCities.city
ORDER BY city;

-- 21. Generate a detailed report that showcases product details, product categories, and customer orders. Display the product name, category name, customer's company name, and the order date for all orders containing products from a specific category.
select orders.order_date, orders.order_id, products.product_name, categories.category_name, customers.company_name
from orders
join customers on customers.customer_id = orders.customer_id
join order_details on order_details.order_id = orders.order_id
join products on products.product_id = order_details.product_id
join categories on categories.category_id = products.category_id
order by categories.category_id

-- 22. Create a report that combines supplier information, product details, and employee territories. Display the supplier's company name, product name, and the territory description for employees responsible for orders containing these products.
select orders.order_id, suppliers.company_name as supplier_company_name, products.product_name, territories.territory_description as employee_location
from suppliers
join products on products.supplier_id = suppliers.supplier_id
join order_details on order_details.product_id = products.product_id
join orders on orders.order_id = order_details.order_id
join employees on employees.employee_id = orders.employee_id
join employee_territories as et on et.employee_id = employees.employee_id
join territories on territories.territory_id = et.territory_id


------------------------------
-- check employee id to territory description correspondence

select e.employee_id, t.territory_id, t.territory_description
from employees as e
join employee_territories as et on e.employee_id = et.employee_id
join territories as t on t.territory_id = et.territory_id
where e.employee_id = 5