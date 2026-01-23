## 1\. basic query structure

* select  
* column aliasing (as)  
* from  
* where  
* order by  
* limit / offset  
* distinct

## 2\. filtering & boolean logic

* comparison operators (=, \!=, \<, \>, \<=, \>=)  
* and, or, not  
* operator precedence  
* in  
* between  
* like / pattern matching  
* case sensitivity behavior

## 3\. aggregation & grouping

* count(\*) vs count(column)  
* sum, avg, min, max  
* group by  
* having  
* aggregate functions with expressions  
* conditional aggregation using case when

## 4\. joins

* inner join  
* left join  
* right join  
* full outer join  
* join conditions (on)  
* multi-table joins  
* self joins  
* join order  
* handling duplicate rows after joins

## 5\. subqueries

* scalar subqueries  
* subqueries in where  
* subqueries in select  
* correlated subqueries  
* exists / not exists  
* in vs exists

## 6\. common table expressions (ctes)

* with clause  
* multiple ctes  
* recursive ctes (conceptual understanding)  
* ctes vs subqueries

## 7\. window (analytic) functions

* over()  
* partition by  
* order by in windows  
* row\_number()  
* rank()  
* dense\_rank()  
* lag()  
* lead()  
* running aggregates (sum() over)  
* window frame clauses (rows, range)

## 8\. case expressions

* case when ... then ... end  
* nested case statements  
* case inside aggregates  
* case for bucketing / segmentation

## 9\. null handling

* null behavior in comparisons  
* is null / is not null  
* coalesce  
* nullif  
* impact of nulls on aggregates

## 10\. date & time functions

* date vs timestamp  
* date arithmetic  
* extracting date parts  
* truncating dates  
* time-based comparisons  
* timezone awareness (conceptual)

## 11\. set operations

* union  
* union all  
* intersect  
* except / minus

## 12\. deduplication techniques

* distinct  
* row\_number() \+ filtering  
* grouping-based deduplication  
* choosing a survivor row

## 13\. string functions

* concat  
* substring  
* length  
* trim  
* upper / lower  
* string pattern functions

## 14\. type casting & conversions

* implicit vs explicit casting  
* cast()  
* handling type mismatch errors

## 15\. query performance fundamentals

* select \* vs column selection  
* filter pushdown  
* join order impact  
* indexes (read-level understanding)  
* reading execution plans (basic)

## 16\. database objects (read-only analyst level)

* tables vs views  
* materialized views (conceptual)  
* temporary tables

## 17\. data integrity & constraints (conceptual)

* primary keys  
* foreign keys  
* uniqueness  
* referential integrity

## 18\. transaction basics (awareness)

* begin  
* commit  
* rollback  
* isolation levels (high-level)

## 19\. vendor differences (awareness)

* postgres vs mysql vs sql server differences  
* date functions variance  
* window function support  
* syntax portability

## 20\. query formatting & readability

* alias naming conventions  
* indentation  
* ordering clauses logically

