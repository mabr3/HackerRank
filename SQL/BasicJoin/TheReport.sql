SELECT CASE WHEN Grade >7 THEN Name ELSE NULL END as Name, Grade, Marks 
FROM Students join Grades
ON Marks BETWEEN Min_Mark AND Max_Mark
ORDER BY Grade desc, Name, Marks asc
