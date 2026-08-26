# Background

SQL sublanguage: DDL (Data Definition Language)

Before we can store or retrieve any data, we need to define the format in which it is stored. The syntax for
creating a table is as follows:

CREATE TABLE table_name(
    variable_name1 datatype constraint,
    variable_name2 datatype constraint
);

## Problem 1

Create a new table in `problem1.sql`, called `song` with 2 columns `title` and `artist`. Both columns should have
the datatype varchar(100).

| title | artist |
|-------|--------|
| Let it be | Beatles |
| Hotel California | Eagles |
| Kashmir | Led Zeppelin |
