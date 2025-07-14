-- 1. 특정 사용자가 주문한 주문 목록을 모두 출력하시오
SELECT o.*
  FROM orders o -- pk:Id, 10_000
  LEFT JOIN users u -- pk:u.Id, 1_000
    ON o.UserId  = u.Id
 WHERE 1=1
   AND u.Id = 'a0534612-6f5a-403e-8c06-31e4f6885640'
--   AND u.Name = '박하준'

-- 2. 나이가 20대인 사용자만 출력하시오
SELECT u.*
  FROM users u -- pk:u.Id, 1_000
 WHERE 1=1
   AND '2' <= u.Age
   AND u.Age < 3
   
-- 3. 특정 사용자가 주문한 상점명과 상품명을 모두 출력하시오
SELECT s.Name
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
SELECT i.Name
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
;
   
-- 5. 특정 사용자가 주문한 매출액의 합산을 구하시오
SELECT sum(i.UnitPrice)
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

-- 6. 상점별 월간 통계(매출액)을 구하시오
SELECT s.Name
	 , substr( o.OrderAt, 1, 7) AS monthly
     , sum(i.UnitPrice) AS rst
  FROM orderitems oi -- pk:oi.Id, 30_000
  LEFT JOIN orders o -- pk:Id, 10_000
    ON o.Id = oi.OrderId
  LEFT JOIN stores s -- pk:s.Id, 100
    ON s.Id = o.StoreId
  LEFT JOIN items i  -- pk:i.Id, 20
    ON i.Id = oi.ItemId
  GROUP BY s.Id, substr( o.OrderAt, 1, 7) 
;

-- 7. 특정 사용자가 방문한 상점의 빈도가 높은 순서대로 소팅하여 상위 5개만 구하시오
SELECT s.Name
     , count(*)
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
 GROUP BY s.Id
 ORDER BY 2 DESC
 LIMIT 7
;

-- 8. 구매한 매출액의 합산이 가장 높은 사용자 10명을 구하고 각각의 매출액을 구하시오
SELECT u.Id
	 , u.Name 
     , sum(i.UnitPrice) AS spent_amount
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
 GROUP BY u.Id
 ORDER BY 3 DESC
    LIMIT 10
;

SELECT * from  users g ;-- pk:u.Id, 1_000;
SELECT COUNT (1) from items i; -- pk:i.Id, 20

SELECT * FROM sqlite_schema;
SELECT * FROM PRAGMA_TABLE_INFO('orderitems');