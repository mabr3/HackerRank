SET sql_mode='';

SELECT c.contest_id, c.hacker_id, c.name, SUM(total_submissions) s1, SUM(total_accepted_submissions) s2, SUM(total_views) s3, SUM(total_unique_views) s4
FROM Contests c JOIN Colleges cc ON c.contest_id = cc.contest_id
JOIN Challenges ch ON ch.college_id = cc.college_id
LEFT JOIN (SELECT challenge_id, SUM(total_views) as total_views, SUM(total_unique_views) as total_unique_views
          FROM View_Stats GROUP BY challenge_id) v ON v.challenge_id = ch.challenge_id
LEFT JOIN (SELECT challenge_id, SUM(total_submissions) as total_submissions, SUM(total_accepted_submissions) as total_accepted_submissions
           FROM Submission_Stats GROUP BY challenge_id ) s ON s.challenge_id = ch.challenge_id 
GROUP BY c.contest_id,c.hacker_id, c.name

