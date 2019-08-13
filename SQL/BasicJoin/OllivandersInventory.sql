SELECT w.id, wp.age, w.coins_needed, w.power
FROM Wands w LEFT OUTER JOIN Wands_Property wp
ON w.code = wp.code
WHERE wp.is_evil = 0
AND w.coins_needed = (SELECT MIN(w2.coins_needed) FROM Wands w2 where w.code=w2.code and w.power=w2.power)
ORDER BY w.power desc, wp.age desc
