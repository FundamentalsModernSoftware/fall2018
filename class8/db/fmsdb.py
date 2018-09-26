import csv
import json
import operator

# Global variable db_filname is the name of the schema file
db_filename = None


### Internal functions ####

# Read the database schema
def read_schema():
    f = open(db_filename)
    schema = json.load(f)
    f.close()
    return schema
    
# Write a database schema
def write_schema(schema):
    f = open(db_filename, 'w')
    json.dump(schema, f)
    f.close()

# Read the rows in table_name
def read_table(table_name):
    schema = read_schema()
    f = open(schema[table_name]['filename'])
    reader = csv.DictReader(f, fieldnames=schema[table_name]['fields'])
    rows = list(reader)
    f.close()
    return rows

# Write the specified rows into table_name
def write_table(table_name, rows):
    schema = read_schema()
    f = open(schema[table_name]['filename'], 'w')
    writer = csv.DictWriter(f, schema[table_name]['fields'])
    writer.writerows(rows)
    f.close()



### Database commands ###

# Create a new empty database
# SQL: CREATE DATABASE
def create_db(filename):
    global db_filename 
    db_filename = filename
    schema = {}
    write_schema(schema)

# Open a database from filename
def open_db(filename):
    global db_filename 
    db_filename = filename

# Close the database
def close_db():
    global db_filename 
    db_filename = None


### Table commands ###

# Creates an empty table with the specified fields
# SQL: CREATE TABLE table_name (fields);
def create_table(table_name, fields):
    filename = table_name + '.csv'
    table_schema = {'filename': filename, 'fields': fields}
    schema = read_schema()
    schema[table_name] = table_schema
    write_schema(schema)
    write_table(table_name,[])
    
# Removes the specified table from the database
# SQL: DROP TABLE table_name;
def drop_table(table_name):
    schema = read_schema()
    del schema[table_name]
    write_schema(schema)

# Add specified row to table_name
# SQL: INSERT INTO table_name VALUES row;
def insert(table_name, row):
    rows = read_table(table_name)
    rows.append(row)
    write_table(table_name, rows)

# Delete specified row from table_name
# SQL: DELETE FROM table_name WHERE field=value;
def delete(table_name, field, value):
    rows = read_table(table_name)
    new_rows = []
    for row in rows:
        if row[field] != value:
            new_rows.append(row)
    write_table(table_name, new_rows)




### Rowset commands ###

# Returns all the rows from table_name
# SQL: ... FROM table_name;
def sql_from(table_name):
    rows = read_table(table_name)
    return rows

# Restricts rows to the specified fields
# SQL: SELECT field1, field2, ... 
def select(rows, fields):
    new_rows = []
    for row in rows:
        new_row = {}
        for field in fields:
            new_row[field] = row[field]
        new_rows.append(new_row)
    return new_rows

# Return list of only the rows where field == value
# SQL: ... WHERE field=value
def where(rows, field, value):
    new_rows = []
    for row in rows:
        if row[field] == value:
            new_rows.append(row)
    return new_rows

# Returns only the distinct rows in a list
# SQL [SELECT] DISTINCT
def distinct(rows):
	new_rows = []
	for row in rows:
	    if row not in new_rows:
	        new_rows.append(row)
	return new_rows

# Sort a list of rows based on their value in field
# SQL: ... ORDERBY field
def orderby(rows, field):
    return sorted(rows, key = operator.itemgetter(field))

# Counts the number of rows
# SQL: COUNT()
def count(rows):
    return len(rows)
    
# Totals the values in field
# SQL: SUM(field)
def sum(rows, field):
    total = 0
    for row in rows:
        total = total + float(row[field])
    return total


# Combine rows which have the same value in field in both tables
# SQL: ... FROM table_name1 INNER JOIN table_name2 ON table_name1.field = table_name2.field
def join(table_name1, table_name2, field):
    new_rows = []
    for row1 in read_table(table_name1):
        for row2 in read_table(table_name2):
            if row1[field] == row2[field]:
                new_row = {}
                new_row.update(row1)
                new_row.update(row2)
                new_rows.append(new_row)
    return new_rows



