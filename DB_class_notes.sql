CREATE TABLE employee (
     id   INTEGER
    ,name TEXT 
);

INSERT INTO employee VALUES(1, 'john');
INSERT INTO employee VALUES(2, 'james');
INSERT INTO employee VALUES(3, 'kim');

SELECT id, name FROM employee;
SELECT * FROM employee;

SELECT * FROM employee WHERE id = 1;
SELECT * FROM employee WHERE name = 'kim';
SELECT * FROM employee WHERE name = 'aaa';

DELETE FROM employee WHERE id =1;
SELECT * FROM employee WHERE id = 1;

DELETE FROM employee WHERE name ='kim';
SELECT * FROM employee WHERE name = 'kim';

DROP TABLE employee;

CREATE TABLE people (
     id INTEGER
    ,name TEXT
    ,age INTEGER
    ,gender TEXT
);

INSERT INTO people VALUES (1, 'hello', 10, 'M');
INSERT INTO people VALUES (2, 'goodbye', 15, 'M');
INSERT INTO people VALUES (3, 'chair', 12, 'M');
INSERT INTO people VALUES (4, 'hello', 12, 'F');
INSERT INTO people VALUES (5, 'computer', 10, 'F');
INSERT INTO people VALUES (6, 'sesac', 13, 'F');

SELECT name, age FROM people;
SELECT * FROM people;
SELECT * FROM people WHERE name='hello';
SELECT * FROM people WHERE gender='M';
SELECT * FROM people WHERE gender='F';
SELECT * FROM people WHERE age=12;
SELECT * FROM people WHERE age<12;
SELECT * FROM people WHERE age<=12;
SELECT * FROM people WHERE age>12;
SELECT * FROM people WHERE age>=12;

SELECT * FROM people WHERE age IN (10, 11,12,13);

SELECT * FROM people WHERE age BETWEEN 10 and 12;

SELECT * FROM people ORDER BY age ASC;
SELECT * FROM people ORDER BY age DESC;

SELECT * FROM people ORDER BY name ASC;
SELECT * FROM people ORDER BY name DESC;

SELECT * FROM people WHERE gender='M' ORDER BY age DESC;

SELECT * FROM people WHERE gender='M' ORDER BY age DESC LIMIT 1;
SELECT * FROM people WHERE gender='M' ORDER BY age DESC LIMIT 3 OFFSET 3;


SELECT * FROM people ORDER BY id DESC LIMIT 10 OFFSET 20;
SELECT * FROM people ORDER BY id DESC LIMIT 10 OFFSET 30;
SELECT * FROM people ORDER BY id DESC LIMIT 10 OFFSET 40;
SELECT * FROM people ORDER BY id DESC LIMIT 10 OFFSET 50;


SELECT * FROM people WHERE gender LIKE 'M%';

INSERT INTO people VALUES(7,'help',18,'M');


SELECT * FROM people WHERE name LIKE 'o%';
SELECT * FROM people WHERE name LIKE '%o%';
SELECT * FROM people WHERE name LIKE '%o';

DROP TABLE people;

CREATE TABLE people (
     id INTEGER PRIMARY KEY
    ,name TEXT
    ,age INTEGER
    ,gender TEXT
);

INSERT INTO people VALUES (1, 'hello', 10, 'M');
INSERT INTO people VALUES (2, 'goodbye', 15, 'M');
INSERT INTO people VALUES (3, 'chair', 12, 'M');
INSERT INTO people VALUES (4, 'hello', 12, 'F');
INSERT INTO people VALUES (5, 'computer', 10, 'F');
INSERT INTO people VALUES (6, 'sesac', 13, 'F');
INSERT INTO people VALUES (3, 'error', 12, 'M');

SELECT DISTINCT name FROM people;

UPDATE people SET name='desk' WHERE name='chair';

SELECT * FROM people;

UPDATE people SET name='HELLO' WHERE name='hello';
UPDATE people SET name='hello' WHERE id=1;

DELETE FROM people WHERE id=2;
DELETE FROM people WHERE name='hello';

DROP TABLE people;

.table
.schema

CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);

INSERT INTO users(username, password) VALUES('alice','alice1234');
INSERT INTO users(username, password) VALUES('bob','bob1234');

sqlite

INSERT INTO users(username, password) VALUES('bob','bob1234');

UPDATE FROM user SET password='newpwd' WHERE username='shpark';

SELECT * FROM users;

CREATE TABLE product(id INTEGER PRIMARY KEY, name TEXT, price INTEGER);
INSERT INTO product VALUES(1, '마우스', 2000);

CREATE TABLE product(id INTEGER PRIMARY KEY, name TEXT, num INTEGER, price INTEGER, discount INTEGER);
INSERT INTO product(name, num, price, discount) VALUES('마우스', 7, 2500, 0);
INSERT INTO product(name, num, price, discount) VALUES('노트북', 2, 65000, 12000);
INSERT INTO product(name, num, price, discount) VALUES('모니터', 4, 35000, 0);
INSERT INTO product(name, num, price, discount) VALUES('프린터', 5, 8000, 2000);
INSERT INTO product(name, num, price, discount) VALUES('키보드', 4, 10000, 0);

SELECT name, num, price FROM product;
SELECT name, num, price, num*price FROM product;
SELECT name, num, price, num*price AS value FROM product;
SELECT *, price - discount AS 최종판매가 FROM product;

CREATE TABLE exam(name TEXT, result INTEGER);

INSERT INTO exam VALUES('Kim',75);
INSERT INTO exam VALUES('Lee',90);
INSERT INTO exam VALUES('Park',80);

SELECT name
     , reuslt
     , CASE
         WHEN result >= 80 THEN 'PASS'
         ELSE 'Fail!!'
       END AS judge
  FROM exam;

CREATE TABLE user(name TEXT, gender TEXT, city TEXT);
INSERT INTO user VALUES('user1','M','Seoul');
...

DELETE FROM user WEHRE name='user4'; /*2개 삭제*/

SELECT COUNT(*) FROM user;

SELECT gneder, COUNT(*) FROM user GROUP BY gender;

SELECT city FROM user;
SELECT city, COUNT(*) FROM user GROUP BY city;

SELECT gender, city, COUNT(*) FROM user GROUP BY gender, city;
SELECT city, gender, COUNT(*) FROM user GROUP BY city, gender;

SELECT city, COUNT(*) FROM user GROUP BY city HAVING count(*) >= 2;

SELECT SUM(num) FROM product;
SELECT SUM(price) FROM product;
SELECT SUM(discount) FROM product;

CREATE TABLE store(branch TEXT, salse INTEGER);
INSERT INTO stroe VALUES('서울', 150);
INSERT INTO stroe VALUES('부산', 450);
INSERT INTO stroe VALUES('대구', 300);
INSERT INTO stroe VALUES('서울', 250);


SELECT SUM(sales), TOTAL(sales) FROM store;

SELECT branch, SUM(sales) FROM store GROUP BY branch;
SELECT branch, COUNT(*), SUM(sales), AVG(sales) FROM store GROUP bY branch;
SELECT MAX(sales), MIN(sales) FROM store;
SELECT branch, MAX(sales), MIN(sales) FROM store;
SELECT branch, MAX(sales), MIN(sales) FROM store GROUP BY branch;

CREATE TABLE employee (id INTEGER, name TEXT, dept_id INTEGER);

INSERT INTO employee VALUES(1, 'user1',1);
INSERT INTO employee VALUES(2, 'user2',3);
INSERT INTO employee VALUES(3, 'user3',1);
INSERT INTO employee VALUES(4, 'user4',2);
INSERT INTO employee VALUES(5, 'user5',2);

CREATE TABLE dept (id INTEGER, name TEXT);

INSERT INTO dept VALUES(1, 'sales');
INSERT INTO dept VALUES(2, 'dev');
INSERT INTO dept VALUES(3, 'HR');

SELECT * FROM employee JOIN dept ON employee.dept_id = dept.id;
SELECT employee.id, employee.name, dept.name FROM employee JOIN dept ON employee.dept_id = dept.id;


SELECT COUNT(*) FROM customers;
SELECT * FROM customers LIMIT 1;
.schema customers


.mode csv
.import user.csv users
.import order.csv orders
.import store.csv stores
.import item.csv items
.import orderitem.csv orderitems

1.
SELECT CONCAT(FirstName ,' ', LastName) AS FullName, CustomerId, Country FROM customers WHERE Country != 'USA';
2.
SELECT * FROM customers WHERE Country = 'Brazil';
3.
SELECT c.FirstName || ' ' || c.LastName AS FullName
     , i.InvoiceId
     , i.InvoiceDate
     , i.BillingCountry
  FROM invoices i
  JOIN customers c
    ON i.CustomerId = c.CustomerId
 WHERE 1=1
   AND c.Country = 'Brazil';
4. 
SELECT *
  FROM employees
 WHERE 1=1
   AND Title LIKE'Sales%';

5.
SELECT BillingCountry
  FROM invoices
 WHERE 1=1
 GROUP BY BillingCountry;

6.
select i.InvoiceId
     , c.LastName||' '||c.FirstName
  from invoices i
  left join customers c on c.CustomerId = i.CustomerId
  left join employees e on e.EmployeeId = c.SupportRepId
 where 1=1;

7.
select InvoiceId
  from invoices inv
  join invoice_items itm on



select InvoiceId, sum(UnitPrice * Quantity)
  from invoice_items
 group by InvoiceId;