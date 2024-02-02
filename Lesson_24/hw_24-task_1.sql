-- write a query in SQL to display the first name, last name, department number, and department name for each employee
SELECT e.first_name AS "First Name",
       e.last_name AS "Last Name",
       e.department_id AS "Department Number",
       d.department_name AS "Department Name"
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- write a query in SQL to display the first and last name, department, city, and state province for each employee
SELECT e.first_name AS "First Name",
       e.last_name AS "Last Name",
       d.department_name AS "Department",
       l.city AS "City",
       l.state_province AS "State/Province"
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id;

-- write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
SELECT e.first_name AS "First Name",
       e.last_name AS "Last Name",
       e.department_id AS "Department Number",
       d.department_name AS "Department Name"
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.department_id IN (40, 80);

-- write a query in SQL to display all departments including those where does not have any employee
SELECT d.department_id AS "Department ID",
       d.department_name AS "Department Name",
       COUNT(e.employee_id) AS "Number of Employees"
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
ORDER BY d.department_id;

-- write a query in SQL to display the first name of all employees including the first name of their manager
SELECT e.first_name AS "Employee First Name",
       CONCAT(m.first_name, ' (Manager)') AS "Manager First Name"
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id
ORDER BY e.employee_id;

-- write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
SELECT j.job_title,
       CONCAT(e.first_name, ' ', e.last_name) AS "Full Name",
       (j.max_salary - e.salary) AS "Salary Difference"
FROM employees e
JOIN jobs j ON e.job_id = j.job_id;

-- write a query in SQL to display the job title and the average salary of employees
SELECT j.job_title,
       AVG(e.salary) AS "Average Salary"
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title;

-- write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
SELECT CONCAT(e.first_name, ' ', e.last_name) AS "Full Name",
       e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE l.city = 'London';

-- write a query in SQL to display the department name and the number of employees in each department
SELECT d.department_name, COUNT(e.employee_id) AS "Number of Employees"
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;
