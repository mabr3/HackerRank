SELECT months*salary AS earnings, COUNT(*)
FROM Employee
where months*salary in (SELECT MAX(months*salary) FROM Employee)
GROUP BY earnings;
