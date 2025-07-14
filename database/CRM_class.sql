
-- 1. 특정 사용자가 주문한 주문 목록을 모두 출력하시오
SELECT u.Id , u.Name, o.OrderAt 
  FROM orders o -- pk:Id, 10_000
  LEFT JOIN users u -- pk:u.Id, 1_000
    ON o.UserId  = u.Id
 WHERE 1=1
   AND u.Id = 'a0534612-6f5a-403e-8c06-31e4f6885640'
--   AND u.Name = '박하준'

-- 2. 나이가 20대인 사용자만 출력하시오
SELECT * FROM users WHERE cast(age AS integer) BETWEEN 20 AND 29;

-- 3. 특정 사용자가 주문한 상점명과 상품명을 모두 출력하시오
SELECT u.id AS 고객ID
	 , u.name AS 고객명
	 , o.orderat AS 주문시간
     , s.Name AS 상점
     , i.Name
  FROM orderitems oi -- pk:oi.Id, 30_000
  LEFT JOIN orders o -- pk:Id, 10_000
    ON o.Id = oi.OrderId
  LEFT JOIN stores s -- pk:s.Id, 100
    ON s.Id = o.StoreId
  LEFT JOIN items i  -- pk:i.Id, 20
    ON i.Id = oi.ItemId
  LEFT JOIN users u -- pk:u.Id, 1_000
    ON o.UserId  = u.Id -- 30_000
 WHERE 1=1
   AND u.Id = 'a0534612-6f5a-403e-8c06-31e4f6885640'
--   AND u.Name = '박하준'
;
  
-- 4. 특정 사용자가 주문한 유닉한 상품명의 목록을 구하시오
SELECT i.Name AS 상품명
     , count(oi.ItemId) AS 갯수
  FROM orderitems oi -- pk:oi.Id, 30_000
  LEFT JOIN orders o -- pk:Id, 10_000
    ON o.Id = oi.OrderId 
  LEFT JOIN items i  -- pk:i.Id, 20
    ON i.Id = oi.ItemId
  LEFT JOIN users u -- pk:u.Id, 1_000
    ON o.UserId  = u.Id -- 30_000
 WHERE 1=1
   AND u.Id = 'a0534612-6f5a-403e-8c06-31e4f6885640'
--   AND u.Name = '박하준'
  GROUP BY i.Name
  ORDER BY 2 DESC;
;
   
-- 5. 특정 사용자가 주문한 매출액의 합산을 구하시오
SELECT sum(CAST(i.UnitPrice AS integer)) AS 매출
  FROM orderitems oi -- pk:oi.Id, 30_000
  LEFT JOIN orders o -- pk:Id, 10_000
    ON o.Id = oi.OrderId
  LEFT JOIN items i  -- pk:i.Id, 20
    ON i.Id = oi.ItemId
  LEFT JOIN users u -- pk:u.Id, 1_000
    ON o.UserId  = u.Id -- 30_000
 WHERE 1=1
   AND u.Id = 'a0534612-6f5a-403e-8c06-31e4f6885640'
--   AND u.Name = '박하준'
;   

CREATE TABLE IF NOT EXISTS users(
  id TEXT PRIMARY KEY
, Name TEXT
, Gender TEXT
, Age integer
, Birthdate date
, Address TEXT
);
CREATE TABLE IF NOT EXISTS orders(
  Id TEXT PRIMARY KEY
, OrderAt datetime
, StoreId TEXT
, UserId TEXT
);
CREATE TABLE IF NOT EXISTS stores(
  Id TEXT PRIMARY KEY
, Name TEXT
, "type" TEXT
, Address TEXT
);
CREATE TABLE IF NOT EXISTS orderitems(
  Id TEXT PRIMARY KEY
, OrderId TEXT
, ItemId TEXT
);
CREATE TABLE IF NOT EXISTS items(
  Id TEXT PRIMARY KEY
, Name TEXT
, "Type" TEXT
, UnitPrice integer
);