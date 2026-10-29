# Module 2

> **Example module** from the IoT introduction class. Adjust the headings and tasks to match your actual course content.

We are going to show here notes for Task 1, 2, 3, 4, and 5 to prove

## Learning Goals

> Copy the module's learning goals from the course workbook. Keep the `LG1`, `LG2`, … IDs and a one-word keyword; under each goal, link to the task that proves it.

<a id="lg1"></a>
### LG1 — `Reconstruction`

**Evidence:** [LG1](#task-reconstruction)

<a id="lg2"></a>
### LG2 — `Identification`

**Evidence:** [LG2](#task-identification)

<a id="lg3"></a>
### LG3 — `Relationship`

**Evidence:** [LG3](#task-relationship)

<a id="task-reconstruction"></a>
## Task Reconstruction

**Proves:** [LG1](#lg1) - Was made by my own

- Preparations were done in the file [study-log.db]()

- List the entities primary keys are [here]()

- The made ER-diagram can be found [here]()

- The determination of the cardinalities is [here]()

- 1:1: The legacy schema does not explicitly model a one-to-one relationship because it contains no separate Nameplate entity or uniqueness constraints to enforce such a relationship (doesn't exist in our situation)

- 1:N: The schema implicitly represents one-to-many relationships between Machine and MaintenanceJob, and between Technician and MaintenanceJob, through the machine_name and technician columns, but it does not enforce these relationships with foreign keys

- M:N: The relationship between MaintenanceJob and Part is hidden in the parts_used text column, which stores multiple part numbers in a single field instead of using a junction table

<a id="task-identification"></a>
## Task Identification

**Proves:** [LG2](#lg2) - Was made by my own

All the [defects]():

- Maintenance work for machine cnc-05 may be omitted from machine-specific maintenance reports, causing required service work to be overlooked

- Duplicate part number P-1003 may cause incorrect inventory counts, duplicate join results, and inaccurate maintenance cost calculations

- Text-based price comparisons may return incorrect results, leading to inaccurate cost reports and purchasing decisions

- The invalid installation date for RANDOM-NAME prevents reliable calculation of machine age and may distort maintenance planning

- Maintenance job 1 is omitted from the join because it lists two parts in one text field, resulting in incomplete records of parts used and potentially inaccurate maintenance reports

<a id="task-relationship"></a>
## Task Relationship

**Proves:** [LG3](#lg3) - Was made by my own

- The [file]() was successfully made and the [result was received]()

- Pydantic validates that machine_id is at least 1 and serial_no starts with SN-, providing immediate feedback on invalid input. The database enforces primary keys, foreign keys, non-null constraints, and unique serial numbers to protect data integrity, even when data bypasses Pydantic validation. This separates input validation from database-level integrity guarantees

## Reflection 2

[Reflection 2](../Reflections/ref02.md)

