/* 
    To print some random quotes from the table.
    Note. If you have changes the table name replace it accordingly.
*/

SELECT * FROM quote_db OFFSET floor(random() * (SELECT COUNT(*) FROM quote_db)) LIMIT 1
