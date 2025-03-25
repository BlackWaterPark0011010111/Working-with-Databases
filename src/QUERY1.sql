-- defining required columns & aggregating values  
SELECT teacher.id, teacher.name AS Teacher, 
COUNT(DISTINCT webinar.id) AS webinars , 
COUNT(registration.webinar_id) AS registrations

-- selecting and JOINING tables 
FROM teacher 
LEFT JOIN webinar ON webinar.teacher_id = teacher.id 
LEFT JOIN registration ON registration.webinar_id = webinar.id

-- grouping & Ordering
GROUP BY teacher.name
ORDER BY teacher.name


-- SELECT teacher.id, teacher.name, COUNT( teacher.name) AS count_webinars FROM teacher LEFT JOIN webinar ON webinar.teacher_id = teacher.id

-- GROUP BY DISTINCT teacher.name, teacher.id,  
-- ORDER BY teacher.name;

