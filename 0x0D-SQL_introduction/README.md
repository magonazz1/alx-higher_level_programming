# 0x0D SQL Introduction

## Project Overview
This project focuses on SQL (Structured Query Language) and involves writing SQL scripts to perform various tasks on a MySQL database. The tasks include creating databases, tables, and performing operations such as inserting, updating, and querying data.

## Setup Instructions
### Installing MySQL 8.0 on Ubuntu 20.04 LTS
1. Update the package list:
   ```bash
   sudo apt update
   ```

2. Install MySQL Server:
   ```bash
   sudo apt install mysql-server
   ```

3. Check the installed MySQL version:
   ```bash
   mysql --version
   ```

4. Connect to MySQL:
   ```bash
   sudo mysql
   ```

5. Exit MySQL:
   ```bash
   quit
   ```

### Using Container-on-Demand to Run MySQL
- In the container, credentials are root/root.
- Ask for a container with Ubuntu 20.04.
- Connect via SSH or use the Web terminal.
- Start MySQL in the container:
   ```bash
   service mysql start
   ```

### Running the Scripts
- Execute SQL scripts using the following format:
   ```bash
   cat script_file.sql | mysql -hlocalhost -uroot -p
   ```

## Project Tasks

### Task 0: List Databases
Write a script that lists all databases on your MySQL server.

**Script:** [0-list_databases.sql](./0-list_databases.sql)

### Task 1: Create a Database
Write a script that creates the database `hbtn_0c_0` in your MySQL server. If the database already exists, the script should not fail.

**Script:** [1-create_database_if_missing.sql](./1-create_database_if_missing.sql)

### Task 2: Delete a Database
Write a script that deletes the database `hbtn_0c_0` in your MySQL server. If the database doesn’t exist, the script should not fail.

**Script:** [2-remove_database.sql](./2-remove_database.sql)

### Task 3: List Tables
Write a script that lists all the tables of a specified database in your MySQL server.

**Script:** [3-list_tables.sql](./3-list_tables.sql)

### Task 4: Create First Table
Write a script that creates a table called `first_table` in the specified database. If the table already exists, the script should not fail.

**Script:** [4-first_table.sql](./4-first_table.sql)

### Task 5: Full Table Description
Write a script that prints the full description of the table `first_table` from the specified database.

**Script:** [5-full_table.sql](./5-full_table.sql)

### Task 6: List All in Table
Write a script that lists all rows of the table `first_table` from the specified database.

**Script:** [6-list_values.sql](./6-list_values.sql)

### Task 7: Insert a Value
Write a script that inserts a new row in the table `first_table` of the specified database.

**Script:** [7-insert_value.sql](./7-insert_value.sql)

### Task 8: Count 89
Write a script that displays the number of records with `id = 89` in the table `first_table` of the specified database.

**Script:** [8-count_89.sql](./8-count_89.sql)

### Task 9: Full Creation
Write a script that creates a table called `second_table` in the specified database and adds multiple rows.

**Script:** [9-full_creation.sql](./9-full_creation.sql)

### Task 10: List by Best
Write a script that lists all records of the table `second_table` of the specified database, ordering them by score.

**Script:** [10-top_score.sql](./10-top_score.sql)

### Task 11: Select the Best
Write a script that lists all records with a score >= 10 in the table `second_table` of the specified database, ordering them by score.

**Script:** [11-best_score.sql](./11-best_score.sql)

### Task 12: No Cheating
Write a script that updates the score of a specific record in the table `second_table` without using the id value.

**Script:** [12-no_cheating.sql](./12-no_cheating.sql)

### Task 13: Change Class
Write a script that removes all records with a score <= 5 in the table `second_table` of the specified database.

**Script:** [13-change_class.sql](./13-change_class.sql)

### Task 14: Average
Write a script that computes the score average of all records in the table `second_table` of the specified database.

**Script:** [14-average.sql](./14-average.sql)

### Task 15: Number by Score
Write a script that lists the number of records with the same score in the table `second_table` of the specified database.

**Script:** [15-groups.sql](./15-groups.sql)

###

 Task 16: Say My Name
Write a script that lists all records of the table `second_table` of the specified database, excluding rows without a name value.

**Script:** [16-no_link.sql](./16-no_link.sql)

### Task 17: Go to UTF8 (Advanced)
Write a script that converts the specified database, table, and field to UTF8.

**Script:** [100-move_to_utf8.sql](./100-move_to_utf8.sql)

### Task 18: Temperatures #0 (Advanced)
Import a table dump and write a script that displays the average temperature (Fahrenheit) by city ordered by temperature.

**Script:** [101-avg_temperatures.sql](./101-avg_temperatures.sql)

### Task 19: Temperatures #1 (Advanced)
Import a table dump and write a script that displays the top 3 cities' temperature during July and August ordered by temperature.

**Script:** [102-top_city.sql](./102-top_city.sql)

### Task 20: Temperatures #2 (Advanced)
Import a table dump and write a script that displays the max temperature of each state ordered by state name.

**Script:** [103-max_state.sql](./103-max_state.sql)

## Conclusion
This project provides a hands-on introduction to SQL and MySQL, covering essential concepts such as database and table creation, data manipulation, and querying. Each task is designed to reinforce understanding and skills in working with databases using SQL.
