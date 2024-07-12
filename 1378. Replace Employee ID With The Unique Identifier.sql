-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier

select EmployeeUNI.unique_id, Employees.name
from Employees
left join EmployeeUNI
ON Employees.id=EmployeeUNI.id
