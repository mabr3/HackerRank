SELECT ROUND(SQRT(POWER(A-B,2)+ POWER(C-D,2)),4)
FROM (SELECT MIN(LAT_N) AS A, MAX(LAT_N) AS B, MIN(LONG_W) AS C, MAX(LONG_W) AS D FROM STATION) AS R;
