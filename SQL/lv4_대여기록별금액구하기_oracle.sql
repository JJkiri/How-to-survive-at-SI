select h.history_id, trunc(c.daily_fee * (h.end_date - h.start_date + 1)*(1- nvl(d.discount_rate, 0)/100)) as fee
from car_rental_company_car c
join CAR_RENTAL_COMPANY_RENTAL_HISTORY h
on c.car_id = h.car_id
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
on c.car_type = d.car_type
AND d.duration_type = 
CASE
    WHEN (h.end_date - h.start_date + 1) >= 90 THEN '90일 이상'
    WHEN (h.end_date - h.start_date + 1) >= 30 THEN '30일 이상'
    WHEN (h.end_date - h.start_date + 1) >= 7  THEN '7일 이상'
    ELSE NULL  -- 7일 미만: 할인 없음
END
where c.car_type = '트럭'
order by fee desc, h.history_id desc