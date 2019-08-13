SELECT h.hacker_id, h.name, SUM(max_s.sc) as S
FROM Hackers h inner join 
(SELECT hacker_id, max(score) sc from Submissions GROUP BY challenge_id, hacker_id) max_s
on h.hacker_id = max_s.hacker_id
GROUP BY h.hacker_id, h.name
HAVING S <>0
ORDER BY S desc, h.hacker_id asc
