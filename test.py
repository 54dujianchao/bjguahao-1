from mysqlSingle import mysqlSingle

mysql_single = mysqlSingle()
conn, cursor = mysql_single.get_conn()
sql = "select * from guahao;"
print(mysql_single.execute_sql_one(sql))