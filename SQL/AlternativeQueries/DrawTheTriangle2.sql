set @n = 0;
select repeat('* ', @n := @n + 1) from information_schema.tables
limit 20;
