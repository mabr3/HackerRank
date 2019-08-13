SELECT h.hacker_id, h.name, COUNT(*) as chal_count
FROM Hackers as h LEFT OUTER JOIN Challenges c
ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING chal_count = (SELECT MAX(t.cnt) FROM (SELECT COUNT(*) cnt FROM Challenges GROUP BY hacker_id) t)
    OR chal_count in (SELECT z.c2 FROM (SELECT COUNT(*) c2 FROM Challenges GROUP BY hacker_id) z GROUP BY z.c2 HAVING COUNT(z.c2) = 1)
ORDER BY COUNT(*) desc, h.hacker_id asc
