from fastapi import FastAPI
from fastapi import Depends
from db import get_connection
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse

from models import SalesSummary, MonthlySales, Product, CustomerSales
from typing import List
from services import (
    get_sales_summary,
    get_top_products,
    get_monthly_sales,
    get_sales_by_customer,
)

import queries

app = FastAPI()


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500, 
        content={"error": "Internal Server Error", "detail": str(exc)}
    )


@app.get("/")
def home():
    return {"message": "API is running"}


@app.get("/sales-summary", response_model=SalesSummary)
def sales_summary(db_conn=Depends(get_connection)):

    sales, orders = get_sales_summary(db_conn)

    return {-
            "total_sales": float(sales or 0), 
            "total_orders": orders
            }


@app.get("/top-products", response_model=List[Product])
def top_products(limit: int = 1, db_conn=Depends(get_connection)):

    results = get_top_products(db_conn, limit)

    return [{"product": row[0], "total": float(row[1])} for row in results]


@app.get("/monthly-sales", response_model=List[MonthlySales])
def monthly_sales(db_conn=Depends(get_connection)):

    results = get_monthly_sales(db_conn)

    return [{"month": row[0], "total": float(row[1])} for row in results]


@app.get("/sales-by-customer", response_model=List[CustomerSales])
def sales_by_customer(db_conn=Depends(get_connection)):

    results = get_sales_by_customer(db_conn)

    return [{"customer_name": row[0], "total": float(row[1])} for row in results]
