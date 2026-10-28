# Module 1

Module description

## Learning Goals

> **How to use the learning goals.** Copy the module's learning goals from the course workbook into the block below. Keep the `LG1`, `LG2`, … IDs and a one-word keyword. In each task, write `Proves: LG2` (or link to `[LG2](#lg2)`) so you can find the evidence quickly at checkpoint time. In the **Evidence** line under each goal, link to the task that proves it.

<a id="lg1"></a>
### LG1 — `Class`

Explain how this class works — the CBL/PBL philosophy, the portfolio-based project work assessment, and the "moving bar" of a first-time course

**Evidence:** [Task Inspirations](#task-inspirations)

<a id="lg2"></a>
### LG2 — `Creating`

Set up your personal GitHub portfolio from the course template, with a clean first commit and a that keeps databases and secrets out of Git

**Evidence:** [Task Personal Profile](#task-personal-profile)

<a id="lg3"></a>
### LG3 — `Toolchain`

Set up the entire toolchain reproducibly with uv — one fixed Python plus SQLite, DuckDB, Datasette, and more — on Windows, macOS, or Linux, and verify it

**Evidence:** [Task What is IoT](#task-what-is-iot)

<a id="lg4"></a>
### LG4 — `Difference`

Explain — with a measurement, not a slide — the difference between an embedded database and a client/server database, and why most local apps should not run a server

**Evidence:** [Task Differences of Databases](#task-differences)

<a id="lg5"></a>
### LG5 — `SQLite`

Load real rows into SQLite and query them from Python using bound parameters

**Evidence:** [Task Loading Rows](#task-loading-rows)

<a id="lg6"></a>
### LG6 — `Query`

Take a first LLM-generated query, run it, and begin the habit that defines this course: verify before you trust

**Evidence:** [Task LLM-Generated Query](#task-query)

<a id="task-inspirations"></a>
## Task Inspirations

**Proves:** [LG1](#lg1) - Was made by my own

- Inspiration 1 — Challenge-/Project-Based Learning (CBL/PBL): Learning through practical challenges and projects rather than theory alone

- Inspiration 2 — Portfolio-Based Assessment and the Moving Bar: Demonstrating learning through portfolio evidence, with expectations evolving as the course develops

<a id="task-personal-profile"></a>
## Task Personal Profile

**Proves:** [LG2](#lg2) - Was made by my own

- My personal [portfolio](https://github.com/Asckord/HSBI-Databases)

- The instructor was added as a repository collaborator (prove is at the [picture](https://github.com/Asckord/HSBI-Databases/blob/main/Module01/pictures/The%20instructor's%20addition.png))

- The first [commit](https://github.com/Asckord/HSBI-Databases/commit/23c088ed6c0ef61068c60f48a93e2472bc61ecdf)

- The file '.gitignore' was successfully [created](https://github.com/Asckord/HSBI-Databases/blob/main/Module01/.gitignore)

- All the commits can be seem [here](https://github.com/Asckord/HSBI-Databases/commits/main/) 

- The description of the personal portfolio was [updated](https://github.com/Asckord/HSBI-Databases/blob/main/README.md)

<a id="task-what-is-iot"></a>
## Task What is IoT

**Proves:** [LG3](#lg3) - Was made by my own

- The proves of toolchain installation is [here]()

<a id="#task-differences"></a>
## Task Differences

**Proves:** [LG4](#lg4) - Was made by my own

- The needed files [shell-tour.txt](https://github.com/Asckord/HSBI-Databases/blob/main/Module01/shell-tour.txt) and [toursql](https://github.com/Asckord/HSBI-Databases/blob/main/Module01/tour.sql)

- Difference 1: SQLite runs directly in an application; client-server databases require a separate server

- Difference 2: SQLite requires minimal administration; client-server databases need more configuration and maintenance

- Difference 3: Both are reliable; client-server databases often offer more advanced recovery and replication features

- Difference 4: SQLite allows only one writer at a time; client-server databases generally support multiple concurrent writers

- Difference 5: SQLite is free and requires minimal infrastructure; client-server databases may involve server and maintenance costs

- The run time: real 0.002831 user 0.000000 sys 0.000000

<a id="#task-loading-rows"></a>
## Task Loading Rows

- The game SQL Island was [passed](https://github.com/Asckord/HSBI-Databases/blob/main/Module01/pictures/End%20of%20SQL%20Island.png) and the code is [here](https://github.com/Asckord/HSBI-Databases/blob/main/Module01/SQL%20Island.txt)

- The needed files: [generate_telemetry.py](https://github.com/Asckord/HSBI-Databases/blob/main/Module01/generate_telemetry.py) and [load_telemetry.py](https://github.com/Asckord/HSBI-Databases/blob/main/Module01/load_telemetry.py)

- The size of telemetry.db is 172800 and ammount of lines of telemetry.db is 10526720

- The needed [results of requests](https://github.com/Asckord/HSBI-Databases/blob/main/Module01/pictures/Results%20of%20Requests.png)

- Storing this telemetry data in the cloud would incur storage and database service costs depending on the data volume and usage, which would be paid by the company operating the application

**Proves:** [LG5](#lg5) - Was made by my own

<a id="task-query"></a>
## Task LLM-Generated Query

**Proves:** [LG6](#lg6) - Was made by my own

Domains and included areas:

-
-

Commonly used (data) protocols:

-
-

Typical devices (appliance or micro controller):

-
-

Challenges:

-
-

## Reflection 1

[Reflection 1](../Reflections/ref01.md)
