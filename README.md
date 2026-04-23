A RESTful API built using Python and FastAPI to generate dynamic sales insights from a MySQL database. The project demonstrates real-world backend development concepts including API design, database integration, layered architecture, and production-ready practices like environment-based configuration and logging.

This project is an extension of a CLI-based reporting tool, upgraded into a scalable API service.

🚀 Features
📊 Sales Summary (Total Sales & Orders)
🏆 Top-N Products (Dynamic query parameter)
📅 Monthly Sales Trends
👥 Sales by Customer (JOIN operations)
⚙️ Query parameter validation
🧱 Layered architecture (API → Service → DB)
🌐 REST API with JSON responses
🔐 Environment-based configuration (.env)
📝 Logging middleware for request tracking
⚠️ Global exception handling
🛠️ Tech Stack
Language: Python
Framework: FastAPI
Database: MySQL
Server: Uvicorn
Libraries:
mysql-connector-python
python-dotenv
pydantic

📂 Project Structure
sales-api/
│
├── app.py              # FastAPI application
├── db.py               # Database connection (dependency)
├── services.py         # Business logic layer
├── queries.py          # SQL queries
├── models.py           # Pydantic response models
├── config.py           # Environment-based configuration
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1. Clone Repository
git clone <your-repo-url>
cd sales-api

2. Install Dependencies
pip install -r requirements.txt

3. Configure Environment Variables
Create a .env file in the root directory:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=sales_dashboard

4. Run the API
uvicorn app:app --reload

5. Access API Docs

Open in browser:

http://127.0.0.1:8000/docs

👉 Interactive Swagger UI to test endpoints

▶️ API Endpoints

🔹 Sales Summary
GET /sales-summary

🔹 Top Products
GET /top-products?limit=3

🔹 Monthly Sales
GET /monthly-sales

🔹 Sales by Customer
GET /sales-by-customer

🧠 Key Concepts Demonstrated
REST API development using FastAPI
Dependency injection for DB connections
Layered architecture (API → Service → DB)
SQL aggregations, JOINs, and date-based queries
Pydantic models for response validation
Global exception handling
Middleware for logging
Secure configuration using environment variables

📊 Example Response
[
  {
    "product": "Laptop",
    "total": 105000.0
  },
  {
    "product": "Phone",
    "total": 42000.0
  }
]
🚀 Future Enhancements
Add authentication (JWT-based)
Introduce pagination and filtering improvements
Deploy using Docker
Add unit and integration tests
Integrate caching (Redis)

👨‍💻 Author
Maninder Singh
Independent Project (Python Backend & API Development)