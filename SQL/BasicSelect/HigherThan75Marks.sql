SELECT Name from STUDENTS
where Marks >75
order by SUBSTRING(UPPER(Name),LENGTH(Name)-2,3),ID;
