# FastAPI MongoDB Starter 🚀

A modern, production-ready FastAPI starter template with MongoDB integration.

## 🌟 Features

- **FastAPI** - Modern, fast web framework for building APIs
- **MongoDB** with Motor - Async MongoDB driver
- **JWT Authentication** - Secure authentication system
- **Pydantic Models** - Data validation using Pydantic
- **Dependency Injection** - Clean and testable code
- **CORS Middleware** - Cross-Origin Resource Sharing
- **Environment Variables** - Configuration using environment variables
- **Pagination** - Built-in pagination support
- **Error Handling** - Comprehensive error handling
- **Security Utilities** - Password hashing, token generation
- **API Documentation** - Automatic API documentation with Swagger/ReDoc

## 🛠️ Prerequisites

- Python 3.7+
- MongoDB
- Git (optional)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd fastapi-mongodb-starter
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
# App Settings
APP_NAME="FastAPI MongoDB Starter"
DEBUG=True

# MongoDB Settings
MONGODB_URL="mongodb://localhost:27017"
DB_NAME="fastapi_db"

# JWT Settings
SECRET_KEY="your-secret-key-here"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS Settings
CORS_ORIGINS=["*"]
CORS_CREDENTIALS=true
```

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

## 📚 API Documentation

Once the application is running, you can access:

- API Documentation (Swagger UI): <http://localhost:8000/docs>
- Alternative Documentation (ReDoc): <http://localhost:8000/redoc>
- API Base URL: <http://localhost:8000/api>

## 🔗 API Endpoints

### Authentication

- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration

### Users

- `GET /api/users/` - List users (paginated)
- `GET /api/users/me` - Get current user
- `GET /api/users/{user_id}` - Get user by ID
- `PUT /api/users/{user_id}` - Update user
- `DELETE /api/users/{user_id}` - Delete user

### Orders

- `GET /api/orders/` - List orders (paginated)
- `GET /api/orders/{order_id}` - Get specific order
- `POST /api/orders/` - Create new order
- `PUT /api/orders/{order_id}` - Update order
- `DELETE /api/orders/{order_id}` - Delete order

## 📁 Project Structure

```json
fastapi-mongodb-starter/
├── app/
│   ├── core/
│   │   ├── config.py      # Configuration settings
│   │   ├── security.py    # Security utilities
│   │   └── deps.py        # Dependencies
│   ├── database/
│   │   └── mongodb.py     # MongoDB connection
│   ├── models/
│   │   ├── user.py        # User models
│   │   └── token.py       # Token models
│   │   └── order.py       # Order models
│   ├── routes/
│   │   ├── api.py         # API router
│   │   └── endpoints/     # API endpoints
│   ├── utils/
│   │   └── helper.py     # General utilities
│   └── main.py           # Application entry point
├── .env                  # Environment variables
├── .env.example         # Example environment variables
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## 🔧 Development Commands

```bash
# Install new package
pip install package_name

# Update requirements
pip freeze > requirements.txt

# Run tests (when implemented)
pytest

# Format code
black app/

# Check types
mypy app/
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💡 Support

If you have any questions or need help, please open an issue in the repository.
