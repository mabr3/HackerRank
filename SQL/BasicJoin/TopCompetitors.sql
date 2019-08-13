SELECT h.hacker_id, h.name
FROM Hackers h INNER JOIN Submissions s
ON h.hacker_id = s.hacker_id
INNER JOIN Challenges c on
c.challenge_id = s.challenge_id
INNER JOIN Difficulty d ON
d.difficulty_level = c.difficulty_level
WHERE s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(s.hacker_id) > 1
ORDER BY COUNT(h.hacker_id) desc, h.hacker_id asc
