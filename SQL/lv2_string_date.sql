-- lv2, string_date
-- case then else(except) end / to_char
SELECT board_id, writer_id, title, price, 
case status -- case, when, then(as가 아님!) , else(예외처리), end 
    when 'SALE' then '판매중'  --문자열은 항상 ''(홑따옴표), ""(쌍따옴표)는 칼럼명에만!
    when 'RESERVED' then '예약중'
    when 'DONE' then '거래완료'
    else '예외처리'
    END as STATUS
FROM USED_GOODS_BOARD
WHERE to_char(CREATED_DATE,'YYYY-MM-DD') = '2022-10-05' --chr가 아닌 to_char, str >> '' used
ORDER BY board_id desc
-- status value 대응하여 출력하기 >> CASE - WHEN - END (select)구문