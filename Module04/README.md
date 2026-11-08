# Module 4

Module description

## Learning Goals

<a id="lg1"></a>
### LG1 — `Creation`

Create tables with the full constraint toolkit: NOT NULL, UNIQUE, CHECK, PRIMARY, KEYFOREIGN, KEYSTRICT and typing.

**Evidence:** [LG1](#task-creation)

<a id="lg2"></a>
### LG2 — `Deriviation`

Use generated columns to derive values at the engine instead of in application code.

**Evidence:** [LG2](#task-deriviation)

<a id="lg3"></a>
### LG3 — `Triggers`

Write triggers that enforce domain rules and maintain audit/rollup tables automatically.

**Evidence:** [LG3](#task-triggers)

<a id="lg4"></a>
### LG4 — `DML Using`

Use DML correctly — including (UPSERT ON CONFLICT) for idempotent edge ingestion.

**Evidence:** [LG4](#task-using)

<a id="task-creation"></a>
## Task Creation

- The file integrity-notes.md was [created](https://github.com/Asckord/HSBI-Databases/blob/main/Module04/integrity-notes.md)

- The [first](https://github.com/Asckord/HSBI-Databases/blob/main/Module04/pictures/Task%20A%20(First%20Run).png) and the [second](https://github.com/Asckord/HSBI-Databases/blob/main/Module04/pictures/Task%20A%20(Second%20Run).png) tables were developed and checked

**Proves:** [LG1](#lg1) - Was made by my own

<a id="task-deriviation"></a>
## Task Deriviation

- The [SQL run](https://github.com/Asckord/HSBI-Databases/blob/main/Module04/pictures/Task%202%20SQL%20run.png) and [python run](https://github.com/Asckord/HSBI-Databases/blob/main/Module04/pictures/Task%202%20python%20run.png) are done

**Proves:** [LG2](#lg2) - Was made by my own

<a id="task-triggers"></a>
## Task Triggers

- The triggers were developed and [checked](https://github.com/Asckord/HSBI-Databases/blob/main/Module04/pictures/Task%203%20run.png)

- The execution of trigger's time was [received](https://github.com/Asckord/HSBI-Databases/blob/main/Module04/pictures/Time%20of%20Trigger.png) through written python file [time_trigger.py](https://github.com/Asckord/HSBI-Databases/blob/main/Module04/time_trigger.py) 

**Proves:** [LG3](#lg3) - Was made by my own

<a id="task-using"></a>
## Task DML Using

- The access was successfully [checked](https://github.com/Asckord/HSBI-Databases/blob/main/Module04/pictures/Task%204.png)

- PostgreSQL has users and roles, so you can decide who can read or change specific tables. SQLite works differently because it doesn't have its own user management — access is controlled through file permissions, read-only mode and views. This works fine for a local database where usually one application accesses the file. But for a web app with many users, it's not enough, because each user may need different permissions (even on the computer of the developer himself)

**Proves:** [LG4](#lg4) - Was made by my own

## Reflection 4

[Reflection 4](../Reflections/ref04.md)

