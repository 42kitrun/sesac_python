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

SELECT * FROM employee JOIN dept ON employee.dept_id = dept_id;
SELECT employee.id, employee.name, dept.name FROM employee JOIN dept ON employee.dept_id = dept_id;

/*  연습문제   */
/* 1. full names, customer ID and country) who are not in the US.*/
SELECT CONCAT(c.FirstName,' ',c.LastName) AS FUllname
     , c.CustomerId
     , c.Country
 FROM customers c
WHERE 1=1
  AND c.Country != 'USA';

/* 2. showing the Customers from Brazil */
SELECT c.*
  FROM customers c
 WHERE 1=1
   AND c.Country = 'Brazil';
 
/* 3. who are from Brazil. show the customer's full name, Invoice ID, Date of the invoice and billing country. */
SELECT c.FirstName||' '||c.LastName AS FullName 
	 , i.InvoiceId
	 , i.InvoiceDate
	 , i.BillingCountry
  FROM invoices i 
  JOIN customers c ON c.CustomerId = i.CustomerId
 WHERE 1=1
   AND c.Country = 'Brazil';

/* 4. only the Employees who are Sales Agents */
SELECT *
  FROM employees e 
 WHERE 1=1
   AND e.Title LIKE 'Sale%Agent';

/* 5. a unique/distinct list of billing countries from the Invoice table */
SELECT BillingCountry
  FROM invoices i 
 GROUP BY BillingCountry;

/* 6. the invoices associated with each sales agent. the Sales Agent's full name. */
SELECT i.InvoiceId
     , e.FirstName||' '||e.LastName AS SalesName
  FROM invoices i 
  LEFT JOIN customers c ON c.CustomerId = i.CustomerId
  JOIN employees e ON e.EmployeeId = c.SupportRepId
 WHERE 1=1
   AND e.Title LIKE 'Sale%Agent';

/* 7. the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers. */
SELECT i.InvoiceId
	 , c.CustomerId
	 , i.Total
	 , c.FirstName||' '||c.LastName AS CustomerName 
	 , c.Country
	 , e.FirstName||' '||e.LastName AS SalesName
  FROM invoices i /* i.InvoiceId:412 */
  LEFT JOIN customers c /* c.CustomerId:59 */
 		 ON c.CustomerId = i.InvoiceId /*412*/
  LEFT JOIN employees e /* e.EmployeeId:8 */
  		 ON e.EmployeeId = c.SupportRepId /*412*/
 WHERE 1=1
   AND e.Title LIKE 'Sale%Agent'
 GROUP BY i.InvoiceId, c.CustomerId /*412*/;
 
/* 8. How many Invoices were there in 2009 and 2011 */
SELECT count(*) -- 166 
  FROM invoices i -- i.InvoiceId:412 
 WHERE 1=1
   AND (strftime('%Y',i.InvoiceDate) = '2009'
       OR strftime('%Y',i.InvoiceDate) = '2011');

-- 9. the respective total sales for each of those years
SELECT strftime('%Y',i.InvoiceDate) AS Billing
	 , sum(i.Total)
  FROM invoices i -- i.InvoiceId:412 
 WHERE 1=1
 GROUP BY strftime('%Y',i.InvoiceDate );

-- 10. the InvoiceLine table,COUNTs the number of line items for Invoice ID 37.
SELECT count(ii.InvoiceLineId) AS LineItemNum
  FROM invoice_items ii --pk:ii.InvoiceLineId, 2_240
 WHERE 1=1
   AND ii.InvoiceId = 37 -- 4);

-- 11. COUNTs the number of line items for each Invoice.
SELECT ii.InvoiceId
	 , count(ii.InvoiceLineId) AS LineItemNum
  FROM invoice_items ii --pk:ii.InvoiceLineId, 2_240
 WHERE 1=1
 GROUP BY ii.InvoiceId;
   
-- 12. the purchased track name with each invoice line item.
SELECT ii.InvoiceLineId, t.Name
  FROM invoice_items ii --pk:ii.InvoiceLineId, 2_240
  LEFT JOIN tracks t -- pk:t.TrackId, 3_503
    ON t.TrackId = ii.TrackId -- 2_240
 WHERE 1=1;

-- 13. the purchased track name AND artist name with each invoice line item.
SELECT t.Name
	 , art.Name
  FROM invoice_items ii --pk:ii.InvoiceLineId, 2_240
  LEFT JOIN tracks t -- pk:t.TrackId, 3_503
    ON t.TrackId = ii.TrackId -- 2_240
  LEFT JOIN albums alb -- pk:alb.AlbumId, 347
    ON alb.AlbumId = t.AlbumId -- 2_240
  LEFT JOIN artists art -- pk:art.ArtistId, 275
    ON art.ArtistId = alb.ArtistId -- 2_240
 GROUP BY t.Name, art.Name;
    
-- 14. the # of invoices per country
SELECT i.BillingCountry 
     , count(*)
  FROM invoices i -- i.InvoiceId, 412
 GROUP BY i.BillingCountry
 
-- 15. the total number of tracks in each playlist. The Playlist name 
SELECT p.PlaylistId -- playlist
	 , p.Name
	 , count( pt.TrackId) --  트랙의 수
  FROM playlists p -- pk:p.PlaylistId, 18
  JOIN playlist_track pt -- pk:pt.PlaylistId, 8_715
    ON pt.PlaylistId = p.PlaylistId
 WHERE 1=1
 GROUP BY p.PlaylistId;

-- 16. all the Tracks, but displays no IDs. include the Album name, Media type and Genre.
SELECT t.Name AS TrackName
	 , t.Composer
	 , t.Milliseconds
	 , t.Bytes
 	 , t.UnitPrice
 	 , alb.Title AS AlbumName
 	 , mt.Name   AS MediaType
 	 , g.Name    AS Genre
  FROM tracks t -- pk:t.TrackId, 3_503
  LEFT JOIN albums alb -- pk:alb.AlbumId, 347
    ON alb.AlbumId = t.AlbumId -- 3_503
  LEFT JOIN media_types mt -- pk:mt.MediaTypeId, 5
    ON mt.MediaTypeId = t.MediaTypeId -- 3_503
  LEFT JOIN genres g -- pk:g.GenreId, 25
    ON g.GenreId = t.GenreId -- 3_503
;

-- 17. all Invoices but includes the # of invoice line items.
SELECT i.InvoiceId
	 , count(ii.InvoiceLineId)
  FROM invoices i -- i.InvoiceId, 412 
  JOIN invoice_items ii --pk:ii.InvoiceLineId, 2_240
    ON ii.InvoiceId = i.InvoiceId -- 
 WHERE 1=1
 GROUP BY i.InvoiceId
;

-- 18. total sales made by each sales agent.
SELECT e.EmployeeId
	 , e.Title
	 , count(i.Total) AS TotalCount
	 , sum(i.Total)   AS TotalSum
  FROM invoices i /* i.InvoiceId:412 */
  LEFT JOIN customers c /* c.CustomerId:59 */
 		 ON c.CustomerId = i.InvoiceId /*412*/
  LEFT JOIN employees e /* e.EmployeeId:8 */
  		 ON e.EmployeeId = c.SupportRepId /*412*/
 WHERE 1=1
   AND e.Title LIKE 'Sale%Agent'
 GROUP BY e.EmployeeId  /*412*/;

-- 19. Which sales agent made the most in sales in 2009
WITH tot AS (
SELECT e.EmployeeId
	 , concat(e.FirstName,' ',e.LastName) AS Name
	 , sum(i.Total) AS total
  FROM invoices i /* i.InvoiceId:412 */
  LEFT JOIN customers c /* c.CustomerId:59 */
 		 ON c.CustomerId = i.InvoiceId /*412*/
  LEFT JOIN employees e /* e.EmployeeId:8 */
  		 ON e.EmployeeId = c.SupportRepId /*412*/
 WHERE e.Title LIKE 'Sale%Agent'
   AND strftime('%Y',i.InvoiceDate) = '2009' 
 GROUP BY e.EmployeeId )
 SELECT tot.EmployeeId
 	  , tot.Name
 	  , tot.total
   FROM tot
  WHERE 1=1
    AND tot.total = (SELECT max(tot.total)
                       FROM tot);

-- 20. Which sales agent made the most in sales over all?
WITH tot AS (
SELECT e.EmployeeId
	 , concat(e.FirstName,' ',e.LastName) AS Name
	 , sum(i.Total) AS total
  FROM invoices i /* i.InvoiceId:412 */
  LEFT JOIN customers c /* c.CustomerId:59 */
 		 ON c.CustomerId = i.InvoiceId /*412*/
  LEFT JOIN employees e /* e.EmployeeId:8 */
  		 ON e.EmployeeId = c.SupportRepId /*412*/
 WHERE e.Title LIKE 'Sale%Agent'
 GROUP BY e.EmployeeId )
SELECT tot.EmployeeId
 	  , tot.Name
 	  , tot.total
   FROM tot
  WHERE 1=1
    AND tot.total = (SELECT max(tot.total)
                       FROM tot);

-- 21. the count of customers assigned to each sales agent.
SELECT e.EmployeeId
     , count(c.CustomerId) AS CustomerNum
  FROM employees e -- pk:e.EmployeeId, 8
  JOIN customers c -- pk:c.CustomerId, 59
    ON e.EmployeeId = c.SupportRepId
 WHERE 1=1
   AND e.Title LIKE 'Sale%Agent'
 GROUP BY e.EmployeeId

-- 22. the total sales per country.
SELECT i.BillingCountry
     , sum(i.Total) AS TotalSales
  FROM invoices i -- pk:i.InvoiceId, 412
 WHERE 1=1
 GROUP BY i.BillingCountry;
 
-- 23. Which country's customers spent the most? 
SELECT i.BillingCountry
     , sum(i.Total) OVER (PARTITION BY i.BillingCountry) AS TotalSum
  FROM invoices i -- pk:i.InvoiceId, 412
  JOIN customers c -- pk:c.CustomerId, 59
    ON c.CustomerId = i.CustomerId
 WHERE 1=1
 ORDER BY TotalSum DESC
 LIMIT 1;
 
-- 24. the most purchased track of 2013
WITH mp AS (
SELECT t.TrackId
	 , t.Name
	 , i.InvoiceDate
	 , count(*) AS tot
  FROM invoice_items ii -- pk:ii.InvoiceLineId, 2_240
  JOIN tracks t -- pk:t.TrackId, 3_503
    ON ii.TrackId  = t.TrackId -- 2_240
  JOIN invoices i -- i.InvoiceId, 412 
    ON ii.InvoiceId = i.InvoiceId -- 2_240
 WHERE strftime('%Y', i.InvoiceDate) = '2013' -- 442
 GROUP BY t.TrackId)
SELECT *
  FROM mp
 WHERE 1=1
   AND mp.tot = (SELECT max(tot)
				   FROM mp);

SELECT DISTINCT ii.TrackId
  FROM invoice_items ii -- pk:ii.InvoiceLineId, 2_240
  JOIN invoices i -- i.InvoiceId, 412 
    ON ii.InvoiceId = i.InvoiceId -- 2_240
 WHERE 1=1
   AND strftime('%Y', i.InvoiceDate) = '2013' -- 442
;


-- 25. shows the top 5 most purchased songs.
SELECT t.TrackId
	 , count(ii.InvoiceLineId) AS psc
  FROM invoice_items ii -- pk:ii.InvoiceLineId, 2_240
  JOIN tracks t -- pk:t.TrackId, 3_503
    ON ii.TrackId  = t.TrackId -- 2240
  JOIN genres g -- pk:g.GenreId, 25 
    ON g.GenreId = t.GenreId AND g.GenreId <=17
 GROUP BY t.TrackId
 ORDER BY psc DESC
-- LIMIT 5
;

-- 26. the top 3 best selling artists.
SELECT a.ArtistId
	 , a.Name 
  	 , count(ii.InvoiceLineId)
  FROM invoice_items ii -- pk:ii.InvoiceLineId, 2_240
  JOIN tracks t -- pk:t.TrackId, 3_503
    ON ii.TrackId  = t.TrackId -- 2_240
  JOIN albums alb -- pk:alb.AlbumId, 347
    ON alb.AlbumId = t.AlbumId -- 2_240
  JOIN artists a -- pk:a.ArtistId, 275
    ON a.ArtistId = alb.ArtistId -- 2_240
 WHERE 1=1
 GROUP BY a.ArtistId
 ORDER BY 3 DESC		
 LIMIT 3
;

-- 27. the most purchased Media Type.
SELECT mt.MediaTypeId
	 , mt.Name 
  	 , count(ii.InvoiceLineId)
  FROM invoice_items ii -- pk:ii.InvoiceLineId, 2_240
  JOIN tracks t -- pk:t.TrackId, 3_503
    ON ii.TrackId  = t.TrackId -- 2_240
  JOIN media_types mt -- pk:mt.MediaTypeId, 5
    ON mt.MediaTypeId = t.MediaTypeId 
 WHERE 1=1
 GROUP BY mt.MediaTypeId
 ORDER BY 3 DESC		
 LIMIT 1
;

-----------------------------------------------------------------------------------------------



SELECT COUNT (1) from  genres g -- pk:g.GenreId, 25;

SELECT * FROM sqlite_schema;
SELECT * FROM PRAGMA_TABLE_INFO('genres');