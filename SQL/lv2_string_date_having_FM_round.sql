-- lv2_string_date2
-- group by, having, where
-- avg, order by alias
SELECT car_id, to_char(round(avg(end_date -start_date+ 1),1),'FM999,999.0') as AVERAGE_DURATION 
-- 문제 요구사항: 14.0 처럼 항상 소수점 첫째자리를 표기할것
-- 해결방안: to_char(value,'FM999.0') // 9의 경우 데이터가 존재하는경우 수 표기, 0은 항상표기
-- 주의사항: 오라클은 숫자를 문자로 바꿀때 항상 앞에 공백 생김, 따라서 FM으로 공백 제거 필요
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY car_id -- date > having
HAVING round(avg(end_date - start_date +1),1) >= 7 --6.96의 대여기간을 가지는 car_id를 반환해야하기때문에, 조건절에도 select 문과 동일하게 반올림조건을 반영해줘야한다
ORDER BY round(AVERAGE_DURATION,1) desc, --alias order by? 정렬도 마찬가지.
CAR_ID desc

--key: where vs having
--where: 집계 전 데이터 필터링 sample: X <= 5000
--having: 집계 후 데이터 필터링(group by x) sample: avg(y) <= 5000 <<집계가 아닌(!) 함수로 grouping // count,avg,sum 등등 사용