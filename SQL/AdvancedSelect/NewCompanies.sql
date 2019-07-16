SELECT c.company_code, c.founder,COUNT(distinct l.lead_manager_code), COUNT(distinct s.senior_manager_code), COUNT(distinct m.manager_code), COUNT(distinct e.employee_code)
FROM Company as c,Lead_Manager as l,Senior_Manager as s, Manager as m, Employee as e
where c.company_code=l.company_code
and l.lead_manager_code=s.lead_manager_code
and s.senior_manager_code=m.senior_manager_code
and m.manager_code=e.manager_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code;

