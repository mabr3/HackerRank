SELECT submission_date s,
(SELECT COUNT(distinct hacker_id) 
 FROM Submissions s1
 WHERE submission_date=d.submission_date
 AND (SELECT COUNT(distinct s2.submission_date) 
     FROM Submissions s2 
     WHERE s2.hacker_id = s1.hacker_id
     AND s2.submission_date<d.submission_date)= dateDIFF(d.submission_date, '2016-03-01')),
(SELECT hacker_id 
 from Submissions 
 WHERE submission_date = s 
 GROUP BY hacker_id 
 ORDER BY COUNT(submission_id) desc, hacker_id asc 
 LIMIT 1) h,
(SELECT name 
 from Hackers 
 where hacker_id = h)
FROM (SELECT distinct submission_date 
      from submissions) d
GROUP BY s;
