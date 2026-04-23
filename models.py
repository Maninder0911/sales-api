from pydantic import BaseModel


class SalesSummary(BaseModel):
    total_sales: float
    total_orders: int


class Product(BaseModel):
    product: str
    total: float


class MonthlySales(BaseModel):
    month: str
    total: float


class CustomerSales(BaseModel):
    customer_name: str
    total: float
