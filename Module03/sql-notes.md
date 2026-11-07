https://www.sqlite.org/eqp.html?utm_source=chatgpt.com - official documentation. Explains SCAN, SEARCH, the use of indexes, covering indexes, and temporary sorting structures

https://en.wikipedia.org/wiki/Relational_algebra?utm_source=chatgpt.com - explains SELECTION, PROJECTION, JOIN, UNION, DIFFERENCE and the mathematical foundation of relational queries

https://use-the-index-luke.com/?utm_source=chatgpt.com - a guide to indexes, their usage, and the reasons why the optimizer might ignore them

https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html?utm_source=chatgpt.com - a guide to securing SQL queries, parameterization and handling user input safely

Questions:
1:
I am a student in a 3rd-semester database class - explain very briefly relational algebra with simple examples, highlight the main concepts and tell me how to explain it best to a peer.
2:
Here is a query plan:
SCAN orders
SEARCH customer USING INTEGER PRIMARY KEY (rowid=?)

What is the engine doing, line by line? What would make it choose a different plan?

SCAN orders — SQLite reads the records of the 'orders' table sequentially.

SEARCH customer USING INTEGER PRIMARY KEY — for each matching order record, SQLite finds the corresponding customer using the primary key.
3:
When does SQLite use a covering index and when does it still have to visit the table?

4:
Why can't an index help "WHERE" technician LIKE '%ei%'?
What could?

5:
Why does SQL evaluate FROM before SELECT?
Give me a query that fails because someone assumed the written order.

Answers:
1:
Relational algebra is the mathematical foundation of relational databases. It defines the operations that can be performed on relations (tables) to produce new relations.

Key operations:
- Selection (σ) — selecting rows.
- Projection (π) — selecting columns.
- Join (⋈) — combining related tables.
- Union (∪) — combining compatible results.
- Difference (−) — obtaining records present only in the first relation.
- Grouping (γ) — grouping records and applying aggregate functions.

2:
- SCAN orders — SQLite performs a sequential scan of the records in the 'orders' table.
- SEARCH customer USING INTEGER PRIMARY KEY — for each matching order record, SQLite locates the corresponding customer using their primary key.
The plan should be interpreted as a set of nested loops:
1. First, the outer table, 'orders', is processed.
2. For each matching record, a lookup for the customer is performed in the 'customer' table.
The plan may change if:
- an appropriate index is added;
- the filtering conditions are modified;
- the join order of the tables is altered;
- the data statistics are updated;
- the version of SQLite is changed.
Important: This is an example of how to analyze a hypothetical query plan; it does not represent the actual output from running a query on the specific database used in the assignment.

3:
A covering index is used when the index contains all the columns required to execute a query. The fewer additional columns that need to be read from a table, the higher the likelihood that a covering index can be used effectively.

4:
A standard B-tree index orders values ​​based on their beginning.

For example, in the query 'WHERE technician LIKE 'Bei%'', SQLite can—under the right conditions—utilize an index because the prefix 'Bei' is known. However, for a query like 'WHERE technician LIKE '%ei%'', the beginning of the target string is unknown.

A match could occur anywhere within the string; therefore, a standard B-tree index cannot effectively narrow down the search range.

Possible alternatives include:
- FTS5 (full-text search), provided the use case aligns with its search model;
- A trigram index or a specialized extension designed for substring searching;
- An alternative storage and retrieval method tailored to the application's specific requirements.
For the purpose of a brief demonstration in this task, comparing 'LIKE 'Bei%'' with 'LIKE '%ei%'' is sufficient.

5:
This is because the database must first identify the data source, retrieve the rows, and perform filtering. Only then can it construct the resulting columns.

Example of an incorrect query:
SELECT price * qty AS total FROM order_line WHERE total > 100;

The problem: 'total' is an alias created during the 'SELECT' phase, but the 'WHERE' clause is processed earlier.

The fix:
SELECT price * qty AS total FROM order_line WHERE price * qty > 100;

Thus, the order in which SQL code is written does not correspond to the logical order of execution.

The Task 1 request:
SQLite schema:
customer(customer_id, name, city),
product(product_id, sku, price),
orders(order_id, customer_id, ordered_on, status),
order_line(order_id, product_id, qty).

Write a query that returns, for each city, the number of distinct customers and the total revenue (sum of qty*price) of orders placed in 2025, ordered by revenue descending.

Task 1 prediction:
- There is no index for searching by order_id, so the first one is SCAN o1
- Then to campare ol.order_id and o.order_id it should get o.order_id, so the second one is SEARCH o USING INTEGER PRIMARY KEY (rowid=?)
- Then it is going from the beginning and to campare o.customer_id and c.customer_id it should get c.customer_id, so the third one is SEARCH c USING INTEGER PRIMARY KEY (rowid=?)
- Then it is going to the end and to campare ol.product_id and p.product_id it should get p.product_id, so the fourth one is SEARCH p USING INTEGER PRIMARY KEY (rowid=?)
- Then after the beginning it has c.customer_id and it must be DISTINCT, so the sixth one is USE TEMP B-TREE FOR count(DISTINCT)
- Then by the end it has revenue and it must be ORDERED BY, so the seventh one is USE TEMP B-TREE FOR ORDER BY

The Task 1 answer:
SELECT
    c.city,
    COUNT(DISTINCT c.customer_id) AS customers,
    SUM(ol.qty * p.price) AS revenue
FROM customer c
JOIN orders o
    ON o.customer_id = c.customer_id
JOIN order_line ol
    ON ol.order_id = o.order_id
JOIN product p
    ON p.product_id = ol.product_id
WHERE o.ordered_on >= '2025-01-01'
  AND o.ordered_on < '2026-01-01'
GROUP BY c.city
ORDER BY revenue DESC;

The Task 2 request:
I have the following SQLite query: 
SELECT
    c.city,
    COUNT(DISTINCT c.customer_id) AS customers,
    SUM(ol.qty * p.price) AS revenue
FROM customer c
JOIN orders o
    ON o.customer_id = c.customer_id
JOIN order_line ol
    ON ol.order_id = o.order_id
JOIN product p
    ON p.product_id = ol.product_id
WHERE o.ordered_on >= '2025-01-01'
  AND o.ordered_on < '2026-01-01'
GROUP BY c.city
ORDER BY revenue DESC;

Analyze this query and suggest which SQLite indexes could improve its performance. For each suggested index:
- Provide the exact CREATE INDEX statement
-  Explain which part of the query it is intended to optimize
- Explain why it might improve performance
- Mention any potential trade-offs or cases where it might not help

Do not rewrite the SQL query. Prioritize a small number of useful indexes and explain your reasoning

The Task 2 answer:
CREATE INDEX ix_orders_ordered_on
ON orders(ordered_on);

CREATE INDEX ix_orderline_order
ON order_line(order_id);

CREATE INDEX ix_orderline_product
ON order_line(product_id);