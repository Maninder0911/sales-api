import logging
from fastapi import FastAPI
from fastapi import Depends
from db import get_connection
from fastapi import HTTPException
from fastapi import Request
from fastapi import Query
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from models import SalesSummary, MonthlySales, Product, CustomerSales
from typing import List
from services import (
    get_sales_summary,
    get_top_products,
    get_monthly_sales,
    get_sales_by_customer,
)

import queries

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    logger.info("API started successfully")

    yield

    #Shutdown logic
    logger.info("API shutting down")

app = FastAPI(lifespan=lifespan) 


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")

    response = await call_next(request)

    logger.info(f"Response Status: {response.status_code}")

    return response

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logger.error(f"Validation error: {exc}")

    return JSONResponse(
        status_code=400,
        content={
            "error": "Invalid input",
            "detail": exc.errors()
        }
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error on {request.method} {request.url}: {exc}")

    return JSONResponse(
        status_code=500, 
        content={
            "error": "Internal Server Error", 
            "detail": str(exc)
        }
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
def top_products(limit: int = Query(1,ge=1,le=10), db_conn=Depends(get_connection)):

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
