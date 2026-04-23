import queries


def get_sales_summary(db_conn):

    cursor = db_conn.cursor()
    cursor.execute(queries.total_sales())
    sales = cursor.fetchone()[0]

    cursor.execute(queries.total_orders())
    orders = cursor.fetchone()[0]

    return sales, orders


def get_top_products(db_conn, limit):

    cursor = db_conn.cursor()
    cursor.execute(queries.top_products(), (limit,))
    results = cursor.fetchall()
    return results


def get_monthly_sales(db_conn):

    cursor = db_conn.cursor()
    cursor.execute(queries.monthly_sales())
    results = cursor.fetchall()
    return results


def get_sales_by_customer(db_conn):

    cursor = db_conn.cursor()
    cursor.execute(queries.sales_by_customer())
    results = cursor.fetchall()
    return results
