-- Create the table
CREATE TABLE tasks_schedule (
    task_id int,
    task_name varchar(255),
    details varchar(255),
    deadline date,
    additional_info varchar(255)
);

-- Rename the table
ALTER TABLE postgres.public.tasks_schedule RENAME TO task1;

-- Add a new column
ALTER TABLE postgres.public.task1 ADD COLUMN manager varchar(255);

-- Insert 3 rows
INSERT INTO postgres.public.task1 (task_id, task_name, details, deadline, additional_info, manager)
VALUES
    (1, 'first task', 'clear room', '2024-02-02', NULL, 'Jimmy'),
    (2, 'second task', 'plant trees', '2024-03-03', 'oak trees', 'Leon'),
    (3, 'third task', 'paint car', '2024-02-13', 'red metallic', 'Valentine');

-- Update row
UPDATE postgres.public.task1
SET deadline = '2024-02-12', additional_info = 'deep blue'
WHERE task_id = 3;

-- Delete a row
DELETE FROM postgres.public.task1
WHERE task_id = 1;
