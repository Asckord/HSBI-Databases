https://pressbooks.uiowa.edu/fundamentalsofdatabasemanagement/chapter/chapter-2/?utm_source=chatgpt.com - how to represent entities, attributes, and relationships; one-to-one (1:1), one-to-many (1:N) and optional versus mandatory relationships; how to represent real-world constraints in a data model; how to determine how many instances of one entity can be associated with another

https://courses.ischool.berkeley.edu/i202/f97/Lecture8/Lecture8.html?utm_source=chatgpt.com - how to organize tables to reduce unnecessary data duplication; including first, second, and third normal forms; problems that can occur when inserting, updating, or deleting records; why many-to-many relationships require an intermediate table.

Questions:
1:
Explain shortly but completely - what is the difference between 1:1, 1:N and M:N relationships; how are they represented in a relational database?
2:
Explain shortly but completely - does storing multiple part numbers in one column violate normalization? If yes, how should it be fixed?
3:
Explain shortly but completely - what is the particular difference between a natural key and a surrogate key? When should each be used?
4:
Explain shortly but completely - what problems can occur when a database table is not properly normalized?

Answers:
1:
- 1:1: one machine is associated with one nameplate. A foreign key with a UNIQUE constraint can enforce this relationship.
- 1:N: one machine can have many sensors. The foreign key is stored in the SENSOR table.
- M:N: one work order can use multiple parts, and one part can be used in multiple work orders. An intermediate table, such as job_part, stores the relationships.
2:
A value such as P-1001,P-1002 contains multiple values in one field and therefore violates the first normal form (1NF). It makes searching for individual parts, enforcing foreign keys, and joining tables more difficult. The solution is to create a separate job_part table, where each job–part combination is stored in its own row. - 
3:
A natural key is based on a real-world property, such as a machine's serial number. A surrogate key is an artificial identifier created for database use, such as an automatically generated integer.

Natural keys have real-world meaning, while surrogate keys provide identifiers that are independent of business data. A database can use a surrogate primary key while enforcing the uniqueness of a natural key with a UNIQUE constraint.
4:
Poor normalization can cause data duplication and three common types of anomalies:
- Insertion anomaly: information cannot be added without also adding unrelated information.
- Update anomaly: the same fact must be changed in multiple rows, which can lead to inconsistencies.
- Deletion anomaly: deleting one record unintentionally removes other important information.
Normalization separates data into related tables and reduces these problems.

Verifying:
1: 
I understood the meanings by using such an example - a sensor belongs to one machine, so the relationship is 1 but part can be used in many different work orders, while each work order can contain many parts, so the relationship is M.
2:
The problem became clear when I understood would happen if I wanted to find all work orders containing part P-1001. If several part numbers are stored together in one field, I cannot treat each part as an independent value. By storing each work order–part combination in a separate row, I can represent the relationship clearly and work with individual parts.
3:
I understood the difference by considering that a machine already has a serial number before it is entered into a database, so it is a natural identifier. If the serial number changes or is entered incorrectly, using it as the only identifier can cause difficulties but an artificial ID can remain stable even if the machine's descriptive information changes.
4:
I considered an example in which a part's description is repeated in many maintenance-job records and understood that separating parts into their own table would make everything much simpler.

The found ER-diagrams are: 
[1 - here](), which was taken from [here](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model?utm_source=chatgpt.com#/media/File:ER_Diagram_MMORPG.svg) - it taught that  ER diagrams help identify entities, their attributes, and relationship cardinalities. They can also model the difference between a general type and individual instances, which is useful when designing databases for more complex systems.
[2 - here](), which was taken from [here](https://lucid.co/diagram/erd/symbols-and-notation?utm_source=chatgpt.com) - it taught that freign keys may connect related tables, lookup tables store reusable values, and a self-referencing foreign key can represent relationships between records of the same entity type

The made 4 tables are:

[Table 1-1]() Machine and Nameplate:
Description: Each machine has exactly one nameplate containing its serial number and manufacturer. Each nameplate belongs to exactly one machine.
Entities: Machine, Nameplate.
Attributes:
-Machine: machine_id (primary key), machine_name.
-Nameplate: machine_id (primary key and foreign key), serial_number, manufacturer.
Relationship: One-to-one (1:1).

[Table 1-N]() Machine and Sensor:
Entities: Machine, Sensor.
Attributes:
-Machine: machine_id (primary key), machine_name.
-Sensor: sensor_id (primary key), machine_id (foreign key), sensor_type.
Relationship: One-to-many (1). One machine can have multiple sensors, while each sensor belongs to exactly one machine.

[Table M-N]() Work Order and Part:
Description: A work order can use multiple parts, and a part can be used in multiple work orders. The same part can appear only once in a given work order.
Entities: Work_Order, Part, Work_Order_Part.
Attributes:
-Work_Order: order_id (primary key), order_date.
-Part: part_id (primary key), part_name.
-Work_Order_Part: order_id and part_id (composite primary key and foreign keys), quantity.
Relationship: Many-to-many (M) between Work_Order and Part, implemented using the junction table Work_Order_Part.

[Table vs]() Entity vs. Attribute vs. Relationship Maintenance Job:
Entities: Machine, Technician, Maintenance_Job.
Attributes:
-Machine: machine_id (primary key), machine_name.
-Technician: technician_id (primary key), technician_name.
-Maintenance_Job: job_id (primary key), machine_id (foreign key), technician_id (foreign key), done_on (date).
Relationships:
-One machine can have multiple maintenance jobs (1).
-One technician can perform multiple maintenance jobs (1).
-Each maintenance job refers to exactly one machine and one technician.

[Prove]() for Table 1-N Machine and Sensor:

CREATE TABLE Machine (machine_id INTEGER PRIMARY KEY, machine_name TEXT NOT NULL);
CREATE TABLE Sensor (sensor_id INTEGER PRIMARY KEY, machine_id INTEGER NOT NULL, sensor_type TEXT NOT NULL, FOREIGN KEY (machine_id) REFERENCES Machine(machine_id));

INSERT INTO Machine (machine_id, machine_name) VALUES (1, 'CNC-01');
INSERT INTO Sensor (sensor_id, machine_id, sensor_type) VALUES (101, 1, 'Temperature'), (102, 1, 'Vibration');

SELECT m.machine_name, COUNT(s.sensor_id) AS sensor_count FROM Machine AS m LEFT JOIN Sensor AS s ON m.machine_id = s.machine_id GROUP BY m.machine_id, m.machine_name;