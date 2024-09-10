import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DB_USERNAME=root
# DB_PASSWORD=09169805227mM
# DB_HOST=localhost:3306
# DB_NAME=employees

DATABASE_URL = "mysql+mysqlconnector://root:09169805227mM@localhost/employees"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

select_query = "SELECT (SELECT DISTINCT salary FROM salaries ORDER BY salary DESC LIMIT 1 OFFSET 1) as SecondHighestSalary"
df_result = pd.read_sql_query(select_query, engine)
print(df_result)

session.close()




