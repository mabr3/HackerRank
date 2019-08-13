SELECT t1.X, t1.Y
FROM Functions t1 inner join Functions t2
ON t1.X=t2.Y
AND t1.Y = t2.X
GROUP BY t1.X, t1.Y
HAVING t1.X < t1.Y or COUNT(t1.X)>1
ORDER BY t1.X asc

