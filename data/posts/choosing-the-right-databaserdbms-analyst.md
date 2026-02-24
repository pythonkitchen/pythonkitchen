title: Choosing the right database(RDBMS) for Data analyst?
slug: choosing-the-right-databaserdbms-analyst
pub: 2022-11-27 10:21:19
authors: abdulkhan
tags: databases, sql, system design
category: data engineering
related_posts: packaging-an-sqlite-db-included-crud-pyqt5-app-using-pyinstaller,why-choose-flask-over-fastapi,python-engineering-articles


> 
> **Which database is best? The question, obviously, depends on what you want to use it for.**
> 

[![](https://raw.githubusercontent.com/Abdullium/Data_Analysis/main/Screenshot%202022-11-27%20134023.png)](https://raw.githubusercontent.com/Abdullium/Data_Analysis/main/Screenshot%202022-11-27%20134023.png)



I, like most Data analysts, want to use a database to warehouse, process, and manipulate data—and there's no shortage of thoughtful commentary outlining the types of databases I should prefer. But these evaluations, which typically discuss databases in terms of architecture, cost, scalability, and speed, rarely address one other key consideration: how hard is it for a beginner data analyst to write queries against these databases.![](https://raw.githubusercontent.com/Vertica/Vertica-Python/master/examples/vertica_error_rates.png)

Relative to factors like processing speed and scalability, the essentials of a database's query language may seem trivial. Regardless of how hard it is to write a query against it?

When you work with a database day in and day out, the annoyances that hinder every quick project—how do I get the current time in Redshift? `NOW()`? `CURDATE()`? `CURDATE`? `SYSDATE`? `WHATDAYISIT?`—often slow you down more than a lower top speed.

I looked into the question as any analyst would—by using data. Data Analysts write thousands of queries in SQL using various RDBMS. My analysis focused on the eight most popular: MySQL, PostgreSQL, Redshift, SQL Server, BigQuery, Vertica, Hive, and Impala



[![im_3](https://images.ctfassets.net/fi0zmnwlsnja/110MlzPLetri6azOQ0AyhU/2c4f2845e52736f0cb8ce80b9eacb239/best-database-chart-4.png?w=1740&h=724&q=50&fm=webp "im_3")](https://images.ctfassets.net/fi0zmnwlsnja/110MlzPLetri6azOQ0AyhU/2c4f2845e52736f0cb8ce80b9eacb239/best-database-chart-4.png?w=1740&h=724&q=50&fm=webp "im_3")

Table of contents
=================


1. A basic measure of difficulty
2. Controlling for query complexity
3. Scale vs Speed
4. Flavour of SQL
5. Head-to-head comparisons
6. The winners


A basic measure of difficulty
=============================



The most basic indicator that an analyst is having trouble with a query is when it fails. These error messages, (constantly) rejecting bad syntax, misnamed functions, or a misplaced comma, probably provide the truest indication of how much a language frustrates a Data analyst.

I started simple, looking at how often queries fail. As it turns out, Vertica and SQL Server have the highest error rates, and MySQL and Impala have the lowest. The chart below shows the error rates for each database.

[![im_2](https://mode.com/blog-assets/images/post-images/best-database-chart-1.png "im_2")](https://mode.com/blog-assets/images/post-images/best-database-chart-1.png "im_2")

Unfortunately for our wallets (Impala, MySQL, and Hive are all open-source and free, while Vertica, SQL Server, and BigQuery are decidedly not), rates like these are probably too crude to be conclusive.

People use databases for different things. Vertica and SQL Server are proprietary databases provided by major vendors, and most likely used by large businesses with deeper analytical budgets. The high error rates from these languages may come from a more ambitious use of the language rather than the language being “harder.”



Controlling for query complexity
================================



Can we then adjust for how complex a query is? Unfortunately, controlling for query complexity is hard.

Query length could be a decent proxy, but it's not perfect.
 [![im_4](https://mode.com/blog-assets/images/post-images/best-database-chart-2.png "im_4")](https://mode.com/blog-assets/images/post-images/best-database-chart-2.png "im_4")



An easy language may be easy because it's concise. Or, as anyone who's attempted to parse a string of seemingly random brackets, backslashes, and periods in a regular expression will tell you, a language may be hard because it's concise.

While there are clear differences in query lengths across different languages, the relationships between query length, query complexity, and language difficulty are all intertwined. Figuring out these relationships sounds even more daunting than parsing regex.

But we may be able to control for complexity in other ways. Queries often evolve over the course of an analysis. They start as simple explorations and become more complex as analysts add layers. You can see this evolution in the chart below, which shows how the median query doubles in length after 20 or so edits, and triples after 100 edits.

[![im_5](https://mode.com/blog-assets/images/post-images/best-database-chart-3.png "im_5")](https://mode.com/blog-assets/images/post-images/best-database-chart-3.png "im_5")

Rather than comparing queries of similar lengths, we could instead compare queries at the same stage in the analytical process. How often does the first query run result in an error? The fifth? The 20th?

The chart below shows the error rates for queries by the number of times analysts have edited them. After five or so runs, a few clear patterns emerge. PostgreSQL, MySQL, and Redshift have consistently low error rates. Impala, BigQuery, and SQL Server have high error rates. And as before, Vertica consistently outpaces the rest with the highest error rate.

[![im_6](https://mode.com/blog-assets/images/post-images/best-database-chart-4.png "im_6")](https://mode.com/blog-assets/images/post-images/best-database-chart-4.png "im_6")

Scale vs. Speed
---------------


When you need speed, consider Postgres: Under 1TB, Postgres is quite fast for loading and querying. Plus, it’s affordable. As you get closer to their limit of 6TB (inherited by Amazon RDS), your queries will slow down.

Flavor of SQL
-------------


Redshift is built on a variation of Postgres, and both support good ol’ SQL. Redshift doesn’t support every single data type and function that postgres does, but it’s much closer to the industry standard than BigQuery, which has its own flavor of SQL.

Unlike many other SQL-based systems, BigQuery uses the comma syntax to indicate table unions, not joins according to their docs. This means that without being careful regular SQL queries might error out or produce unexpected results. Therefore, many teams have trouble convincing their analysts to learn BigQuery’s SQL.

Head-to-head comparisons
------------------------



Query complexity, however, isn't the only factor affecting error rates. If you've seen me bulldoze through 15 syntax errors in a row, you know the skill of the analyst also matters.

Twenty percent of analysts using online compilers write queries against more than one type of database. Personally, I regularly use PostgreSQL and Pandas

These multi-lingual analysts offer us an opportunity. Among people who use different languages, which are they most comfortable with? Does an analyst who uses PostgreSQL and BigQuery tend to have higher error rates in one language or another? If we could pit SQL languages against each other (in what would surely be the nerdiest gladiator round), which one would win?


> 
>  I used a method of **pairwise comparisons** to aggregate together these head-to-head matchups:
> 


* I found all the analysts who've run a minimum of 10 queries per database for multiple databases.
* I calculated the query error rates for each analyst for each database.
* I averaged the differences in error rates for every database pair to construct the matrix below.



The matrix shows the difference in error rates of the database on the top row compared to the database on the left. Here, a higher number is worse than a lower number. For example, the “20.2” at the intersection of Hive and BigQuery indicates that, among analysts who use both of those databases, the error rate tends to be 20.2% higher for Hive than BigQuery.

[![im_7](https://mode.com/blog-assets/images/post-images/best-database-chart-5.png "im_7")](https://mode.com/blog-assets/images/post-images/best-database-chart-5.png "im_7")

The total score line on the bottom sums the differences for each database. The result provides a similar conclusion to the error-by-run analysis: MySQL and PostgreSQL are the easiest versions of SQL to write. Redshift also jumps up a couple of spots, from the fourth easiest to the second easiest.

Vertica gains the most ground. It moves from being the most difficult language to somewhere near the middle of the pack, beating out SQL Server and Hive. This suggests that Vertica's high error rate may be more indicative of the type of analyst that uses it than it is of the language itself.

The winners
===========



Overall, these numbers point to MySQL and PostgreSQL as the easiest versions of SQL to write. Intuitively, this makes sense. Among the eight languages analyzed, these two are the most widely used in online SQL compiler likes **(** **SQL Fiddle,** **SQL Mode,** **SQL Online,** **and** **Hackkerank** **)** Unfortunately for analysts, they're also poorer in features—and often slower—than languages like Vertica and SQL Server.
