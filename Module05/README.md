# Module 5

Module description

## Learning Goals

<a id="lg1"></a>
### LG1 — `Dependencies and keys`

Derive functional dependencies from a relation and identify candidate keys.

**Evidence:** [LG1](#task-dependencies-keys)

<a id="lg2"></a>
### LG2 — `Normalization`

Normalize a relation to 1NF, 2NF, and 3NF, explaining the anomaly each step removes.

**Evidence:** [LG2](#task-normalization)

<a id="lg3"></a>
### LG3 — `Denormalization`

Denormalize deliberately to speed up a hot read path, and predict what it costs on writes and storage.

**Evidence:** [LG3](#task-denormalization)

<a id="lg4"></a>
### LG4 — `Measurement`

Measure the trade-off: query latency, write cost, and database size — before and after.

**Evidence:** [LG4](#task-measurement)

<a id="lg5"></a>
### LG5 — `Decidion`

Decide, and defend, where a schema should sit on the normalization spectrum for a given workload.

**Evidence:** [LG5](#task-decidion)

<a id="task-reconstruction"></a>
## Task Dependencies and keys

**Proves:** [LG1](#lg1) - The dependencies were done by myself, identification was done by [Arisha](https://github.com/Arshia-zi)

- Functional Dependencies:
    job_id → technician (each job has one technician).
    job_id → machine_id (each job is assigned to one machine).
    machine_id → site (each machine belongs to one site).
    part_no → part_price (each part has one fixed price).
Candidate Key: (job_id, part_no), because together they uniquely identify each row.

After normalization, machine_id → site is moved to a separate machine table, and part_no → part_price is moved to a separate part table. This reduces data redundancy and prevents update anomalies.

- The Arisha's part is presented in pictures [1](https://github.com/Asckord/HSBI-Databases/blob/main/Module05/pictures/Arisha%201.png), [2](https://github.com/Asckord/HSBI-Databases/blob/main/Module05/pictures/Arisha%202.png), [3](https://github.com/Asckord/HSBI-Databases/blob/main/Module05/pictures/Arisha%203.png)

<a id="task-identification"></a>
## Task Normalization

**Proves:** [LG2](#lg2) - Was made [Arisha](https://github.com/Arshia-zi)(2) and by myself (3)

- The Arisha's part is presented in pictures [4](https://github.com/Asckord/HSBI-Databases/blob/main/Module05/pictures/Arisha%204.png), [5](https://github.com/Asckord/HSBI-Databases/blob/main/Module05/pictures/Arisha%205.png), [6](https://github.com/Asckord/HSBI-Databases/blob/main/Module05/pictures/Arisha%206.png), [7](https://github.com/Asckord/HSBI-Databases/blob/main/Module05/pictures/Arisha%207.png)

- The result of the round 3 can be seen [here](https://github.com/Asckord/HSBI-Databases/blob/main/Module05/pictures/Round%203.png)

<a id="task-relationship"></a>
## Task Denormalization

**Proves:** [LG3](#lg3) - Was made by my own

- The result of the round 4 can be seen [here](https://github.com/Asckord/HSBI-Databases/blob/main/Module05/pictures/Round%204.png)

<a id="task-measurement"></a>
## Task Measurement

**Proves:** [LG4](#lg4) - Was made by my own

- The result of the round 5 can be seen [here](https://github.com/Asckord/HSBI-Databases/blob/main/Module05/pictures/Round%205.png)

<a id="task-decidion"></a>
## Task Decidion

**Proves:** [LG5](#lg5) - Was made by [Arisha](https://github.com/Arshia-zi)(6) and by myself(7)

- I recommend maintaining a normalized version of the operational database (in 3NF) and using a separate, denormalized table (report_jobpart) for the equipment status dashboard. A normalized data structure is better suited for day-to-day operations, as it reduces data redundancy and prevents anomalies during updates, insertions, and deletions.

A denormalized architecture can improve dashboard performance by requiring fewer JOIN operations.

However, it demands more storage space and creates a risk of data becoming outdated or inconsistent.

To avoid this, I would implement a scheduled rebuild of the reporting table, ensuring it is regularly updated with the latest information from the normalized tables.

According to our tests, a query on the dashboard using a normalized structure took [0.860 seconds], while a query using a denormalized structure took [0.934 seconds].

The denormalized schema consumed [10,832.0] KB of memory, compared to [3,976.0] KB for the normalized schema.

Therefore, I would employ both approaches: 3NF for robust daily operations, and denormalization for faster analytical queries.

- Normalization reduces data redundancy and prevents update, insert, and delete anomalies.

- Denormalization improves read performance by reducing the need for JOIN operations.
    
- Denormalization increases storage requirements and makes data synchronization more complex.

- Indexes can significantly improve query performance but add storage and write overhead.

- The best database design depends on the workload: normalized schemas are suitable for transactional systems, while denormalized schemas are often better for read-intensive reporting.

Optionally compare performance with DuckDB.

## Reflection 5Measurement

[Reflection 5](../Reflections/ref05.md)

