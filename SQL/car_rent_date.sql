-- 목표: 조건에 따라 값을 반환함 '새로창조' / where의 경우 조건에 맞는 값을 '필터링'
-- case > when + then > (else) > end as
select HISTORY_ID,CAR_ID,to_char(START_DATE,'YYYY-MM-DD') AS START_DATE,to_char(END_DATE,'yyyy-mm-dd') AS END_DATE,

case 
when end_date - start_date + 1 >=30 then '장기 대여' --날짜 차이의 경우 +1을 해야 당일 대여기간 1일짜리가 포함됨
else '단기 대여'
end as RENT_TYPE

from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE to_char(start_date,'yyyy-mm-dd') like '2022-09%' 
ORDER BY HISTORY_ID DESC 