SELECT s.name
FROM Students s inner join Friends f
ON s.ID = f.ID
INNER JOIN Packages p 
ON s.ID = p.ID
INNER JOIN Packages pf
ON f.Friend_ID = pf.ID
WHERE p.Salary < pf.Salary
ORDER BY pf.Salary
