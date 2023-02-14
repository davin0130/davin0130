# user_info 테이블에서 조건에 맞는 user 수 출력하기
# 조건 : join_date = 2023, age가 20 이상 25 이하
select count(user_id) from user_info where year(join_date) = '2023' and (age BETWEEN 20 AND 25);

# product 테이블에서 가장 가격 높은 상품 출력
SELECT max(PRICE) as MAX_PRICE FROM PRODUCT WHERE PRICE = (SELECT max(PRICE) FROM PRODUCT);

# 가장 최근에 들어온 시간 구하기
SELECT DATETIME AS 시간 FROM ANIMAL_INS WHERE DATETIME = (SELECT MAX(DATETIME) FROM ANIMAL_INS);
# 가장 최초로 들어온 시간 구하기
SELECT DATETIME AS 시간 FROM ANIMAL_INS WHERE DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS);