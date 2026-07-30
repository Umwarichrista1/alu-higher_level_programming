# SQL - More queries

This project builds on SQL basics: creating MySQL users and managing
their privileges, table constraints (NOT NULL, UNIQUE, DEFAULT,
PRIMARY KEY, FOREIGN KEY), and combining data from multiple tables
with subqueries and JOINs.

## Learning Objectives
- How to create a new MySQL user
- How to manage privileges for a user on a database or table
- What's a PRIMARY KEY, and what's a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- What are subqueries, and what are JOIN and UNION

## Requirements
- Ubuntu 20.04 LTS, MySQL 8.0 (8.0.25)
- All files end with a new line
- Every file starts with a comment describing the task
- Every SQL query has a comment directly above it
- All SQL keywords are uppercase (SELECT, WHERE, etc.)

## Files
| File | Description |
|------|-------------|
| 0-privileges.sql | Show grants for user_0d_1 and user_0d_2 |
| 1-create_user.sql | Create user_0d_1 with all privileges |
| 2-create_read_user.sql | Create hbtn_0d_2 and a read-only user |
| 3-force_name.sql | Create force_name with a required name |
| 4-never_empty.sql | Create id_not_null with a default id |
| 5-unique_id.sql | Create unique_id with a unique default id |
| 6-states.sql | Create hbtn_0d_usa and a states table |
| 7-cities.sql | Create a cities table linked to states |
| 8-cities_of_california_subquery.sql | Cities of California, via subquery |
| 9-cities_by_state_join.sql | Cities joined with their state name |
| 10-genre_id_by_show.sql | Shows that have at least one genre |
| 11-genre_id_all_shows.sql | All shows, NULL genre if none |
| 12-no_genre.sql | Shows with no genre linked |
| 13-count_shows_by_genre.sql | Number of shows per genre |
| 14-my_genres.sql | All genres of the show Dexter |
| 15-comedy_only.sql | All Comedy shows |
| 16-shows_by_genre.sql | All shows with their linked genres |
