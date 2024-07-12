-- https://leetcode.com/problems/students-and-examinations

select st.student_id, st.student_name, su.subject_name, count(ex.student_id) as attended_exams
from Students st
cross join Subjects su
left join Examinations ex
on ex.student_id = st.student_id and ex.subject_name = su.subject_name
group by st.student_id, su.subject_name
order by st.student_id, su.subject_name
