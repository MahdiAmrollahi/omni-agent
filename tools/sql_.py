import sqlite3
from langchain.tools import tool


@tool
def sql_database(query: str) -> str:
    """Execute a SQL query against a SQLite database.
    
    Args:
        query: The SQL query to execute.
    Returns:
        The result of the SQL query.
    Example:
        - sql_database("SELECT * FROM users")
        Returns:
        The result of the SQL query "SELECT * FROM users".
    Example:
        - sql_database("INSERT INTO users (name, age) VALUES ('John', 20)")
        Returns:
        The result of the SQL query "INSERT INTO users (name, age) VALUES ('John', 20)".
    Example:
        - sql_database("UPDATE users SET age = 21 WHERE name = 'John'")
        Returns:
        The result of the SQL query "UPDATE users SET age = 21 WHERE name = 'John'".
    Example:
        - sql_database("DELETE FROM users WHERE name = 'John'")
        Returns:
        The result of the SQL query "DELETE FROM users WHERE name = 'John'".


    """
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    if query.strip().upper().startswith("SELECT"):
        result = cursor.fetchall()
        result =  {"result": result,"query": query,"number of rows": len(result)}
    else:
        result = {"result": f"{cursor.rowcount} rows affected","query": query,"number of rows": cursor.rowcount}
    conn.close()
    return result
