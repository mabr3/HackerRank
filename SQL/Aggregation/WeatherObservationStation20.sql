SELECT ROUND(AVG(AUX.VAL),4) AS MEDIAN
FROM (SELECT LAT_N AS VAL,  @rownum:=@rownum+1 as `row_number`, @total_rows:=@rownum
     FROM STATION,  (SELECT @rownum:=0) r
     ORDER BY VAL) AS AUX
WHERE AUX.row_number IN ( FLOOR((@total_rows+1)/2), FLOOR((@total_rows+2)/2) );
