-- Part 1
SELECT teacher.id, teacher.name, teacher.city 
FROM teacher

WHERE teacher.id NOT IN (SELECT webinar.teacher_id FROM webinar WHERE webinar.teacher_id is not NULL)
ORDER BY teacher.name;


-- PART 2:










