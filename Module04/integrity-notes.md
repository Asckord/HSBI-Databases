https://www.sqlite.org/lang_createtable.html - all restrictions

https://www.sqlite.org/stricttables.html - data types and strong typing

https://www.sqlite.org/foreignkeys.html - referential integrity and PRAGMA

https://www.sqlite.org/gencol.html - Calculated columns

https://www.sqlite.org/lang_createtrigger.html - triggers, OLD, NEW, BEFORE, AFTER

https://www.sqlite.org/lang_upsert.html - INSERT ON CONFLICT

https://www.w3schools.com/sql/sql_constraints.asp - simple explanations of SQL constraints

Questions:
1:
Explain entity, referential and domain integrity, with one SQL example each — and tell me which one a CHECK constraint can never cover

2:
Here is my CREATE TABLE: Which of the three layers is unguarded, and what concrete bad row gets through?

3:
Give me a rule a CHECK constraint cannot express but a trigger can

4:
What is the difference between BEFORE and AFTER triggers, and which one can reject a row?

5:
Why is PRAGMA foreign_keys per connection? What silently breaks when a tool forgets it?

6:
What is the difference between PRIMARY KEY and UNIQUE?

7:
Why can’t we always use CHECK instead of TRIGGER?

8:
What is the difference between VIRTUAL and STORED?

9:
What happens if you delete a record referenced by FOREIGN KEY?

Answers:
1:
There are three levels of integrity:
- Entity Integrity — the uniqueness and identification of records. For example, a PRIMARY KEY.
- Referential Integrity — the validity of relationships between tables. For example, a FOREIGN KEY.
- Domain Integrity — the validity of values. For example, CHECK(value > 0).
A CHECK constraint cannot replace a FOREIGN KEY, as it is not designed to verify the existence of a record in another table.

2:
None of the three levels of integrity are enforced here:
- Entity: no PRIMARY KEY or UNIQUE constraints.
- Referential: no FOREIGN KEY constraints.
- Domain: no CHECK or NOT NULL constraints.
Examples of invalid records:
INSERT INTO t VALUES (1, 'temp_c', 9000);
INSERT INTO t VALUES (1, 'temp_c', 'hot');
INSERT INTO t VALUES (2, 'bogus', -500);


All three records can be inserted into a standard SQLite table.

3:
For example, consider the following rule:

"Every time a sensor reading changes, both the old and new values ​​must be recorded in a separate audit table."

A `CHECK` constraint cannot, on its own, create entries in other tables.

A `TRIGGER` is suitable for this purpose:
CREATE TRIGGER audit_update
AFTER UPDATE OF value ON reading
FOR EACH ROW
BEGIN
INSERT INTO audit (
reading_id,
old_value,
new_value
)
VALUES (
NEW.reading_id,
OLD.value,
NEW.value
);
END;


In this way, the trigger automatically maintains a history of changes.

4:
- BEFORE triggers before a row is modified.
- AFTER triggers after a row is modified.
You can use BEFORE in conjunction with RAISE(ABORT) to validate and reject a record.

5:
In SQLite, foreign key enforcement must be enabled separately for each database connection:
PRAGMA foreign_keys = ON;


If an application creates a new connection and fails to execute this command, SQLite will not enforce foreign key constraints for that connection.

As a result, records may be created that reference non-existent objects.

6:
Both ensure uniqueness.

However:
- PRIMARY KEY is the main identifier for a row. A table can have only one PRIMARY KEY.
- UNIQUE is an additional uniqueness constraint. There can be multiple such constraints.

7:
A CHECK constraint is designed to validate an expression, typically based on the values ​​in the current row.

A TRIGGER can perform more complex actions, such as:
- checking other tables;
- inserting records into other tables;
- maintaining a history;
- automatically triggering additional operations when data is modified.
For example, while CHECK(value > 0) validates a value, a trigger could record information about a threshold being exceeded by inserting an entry into an "alarm" table.

8:
- VIRTUAL: Calculated upon reading, does not occupy storage space for the result, may require more computation during read operations. 
- STORED: Calculated upon writing, occupies storage space, generally faster to read.

9:
The behavior depends on the ON DELETE clause.

For example:
FOREIGN KEY (sensor_id)
REFERENCES sensor(id)
ON DELETE CASCADE


When a sensor is deleted, the associated readings are automatically deleted as well.

Other options include:
- RESTRICT — prevents deletion if there are associated records.
- SET NULL — sets the foreign key to NULL.
- SET DEFAULT — sets the value to the default.