from fmsdb import *

open_db('geo.json')
from_rows = sql_from('zipcodes')
where_rows = where(from_rows, 'Place Name', 'Springfield')
select_rows = select(where_rows, ['State'])
distinct_rows = distinct(select_rows)
orderby_rows = orderby(distinct_rows, 'State')

for row in orderby_rows:
    print(row['State'])
    
close_db()