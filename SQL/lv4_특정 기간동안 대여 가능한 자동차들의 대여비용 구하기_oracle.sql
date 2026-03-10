-- pseudo code

-- Requirement(1): 세단 or SUV (car) and not in between start_date end_date (history)
-- Requirement(2): 50만 <= Daily_Fee * 30 < 200만  
-- Column Car_id, car_type , sum * (daily_fee) 
-- order by fee desc, car_type asc, car_id desc



select c.car_id, c.car_type, c.daily_fee * 30 * (1-d.discount_rate/100) as fee
from CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
on c.car_type = d.car_type
where d.DURATION_TYPE = '30일 이상' 
    and c.car_id not in(
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    where to_date('2022-11-30','yyyy-mm-dd') >= start_date and end_date >= to_date('2022-11-01','yyyy-mm-dd'))
    and 500000<=c.daily_fee * 30 * (1-d.discount_rate/100) and c.daily_fee * 30 * (1-d.discount_rate/100) <
2000000
    and (c.car_type = '세단' or c.car_type ='SUV')

order by fee desc, car_type asc, car_id desc