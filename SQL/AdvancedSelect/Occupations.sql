/*Set the row counters*/
SET @rd = 0, @rp = 0, @rs =0, @ra=0;
/*min()/max() get the first non-null after group by*/
SELECT MIN(Doctor), MIN(Professor),MIN(Singer), MIN(Actor)
FROM(SELECT CASE
     WHEN Occupation = "Doctor" THEN (@rd := @rd+1)
     WHEN Occupation = "Professor" THEN (@rp := @rp+1)
     WHEN Occupation = "Singer" THEN (@rs := @rs+1)
     WHEN Occupation = "Actor" THEN (@ra := @ra+1)
     END as ROW_NR,
     CASE WHEN Occupation = 'Doctor' THEN Name END as Doctor,
     CASE WHEN Occupation = 'Professor' THEN Name END as Professor,
     CASE WHEN Occupation = 'Singer' THEN Name END as Singer,
     CASE WHEN Occupation = 'Actor' THEN Name END as Actor
     FROM OCCUPATIONS
     ORDER BY Name) 
     as T
GROUP BY ROW_NR
     
