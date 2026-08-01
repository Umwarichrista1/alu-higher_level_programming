# Python - Object-relational mapping

This project links Python to MySQL: first with the raw `MySQLdb`
module (writing SQL by hand, and seeing why unsanitized queries are
vulnerable to SQL injection), then with the `SQLAlchemy` ORM, which
lets you work with Python objects instead of SQL queries.

## Learning Objectives
- How to connect to a MySQL database from a Python script
- How to SELECT and INSERT rows in a MySQL table from Python
- What ORM means
- How to map a Python class to a MySQL table

## Requirements
- Ubuntu 20.04 LTS, python3 (3.8.5)
- MySQLdb 2.0.x, SQLAlchemy 1.4.x
- All files start with `#!/usr/bin/python3`
- All files end with a new line and are executable
- Code follows pycodestyle 2.7.*
- Every module, class, and function has a real docstring
- No `.execute()` calls when using SQLAlchemy

## Files
| File | Description |
|------|-------------|
| 0-select_states.py | List all states (MySQLdb) |
| 1-filter_states.py | States starting with N (MySQLdb) |
| 2-my_filter_states.py | Filter by name, unsafe (MySQLdb) |
| 3-my_safe_filter_states.py | Filter by name, injection-safe |
| 4-cities_by_state.py | Cities joined with their state |
| 5-filter_cities.py | Cities of one state, injection-safe |
| model_state.py | SQLAlchemy State model |
| 6-model_state.py | Create the states table from the model |
| 7-model_state_fetch_all.py | List all states (SQLAlchemy) |
| 8-model_state_fetch_first.py | First state only (SQLAlchemy) |
| 9-model_state_filter_a.py | States containing "a" |
| 10-model_state_my_get.py | Get a state's id by name |
| 11-model_state_insert.py | Insert a new state (Louisiana) |
| 12-model_state_update_id_2.py | Rename the state with id = 2 |
| 13-model_state_delete_a.py | Delete states containing "a" |
| model_city.py | SQLAlchemy City model |
| 14-model_city_fetch_by_state.py | List cities with their state |
