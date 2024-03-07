# Mesh-AI Technical Challenge

The objective of this challenge is to gain insights on problem-solving approaches to software development tasks. Therefore, although completing the task is desirable, it is equaly important *how* you go about it. Also note that there is more than one way to achieve the desired outcome!

## Background

A client receives sales data in a text file (CSV format). Each row in this file contains item_id, order_id, product_name, quantity, unit_price.

The client wants to keep this information in a more accessible storage solution (e.g. a database). Therefore they have created a small python ETL tool to store this data in SQLite. On the back of this, they have created a revenue report with the top 2 products that looks like this:

```
Top 2 Products by Revenue:
1. ProductX: £XXX.XX
2. ProductY: £XX.XX
```

## Task No. 1

After the success of the initial reporting solution, the client provides you with their orderbook and wants you to create a second report that shows the daily revenue for the first business week of January 2024. Note that for this particular client business weeks run from *Tuesday to Monday* (both inclusive).

## Task No. 2
You are also provided with a basic test suite in the *test/* folder which you can run using the pytest testing framework (although tests are written using unittest). The client asks that you provide appropriate testing for their data pipeline.

## Solution considerations

You are provided with scaffolding code necessary to solve this task:
* sample data in the *resources/* folder
* dependency management via *requirements.txt* file
* skeleton implementation in *etl.py* file

There are many ways of solving the task so don't be afraid of being creative. Feel free to use additional libraries and code as needed.

**Happy coding!**