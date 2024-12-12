# FastAPI Boilerplate 🚀

A modern, fast (high-performance) web framework for building APIs with Python 3.7+.

## 🛠️ Prerequisites

- Python 3.7 or higher
- MongoDB installed locally or a remote MongoDB instance
- Git (optional)

## 🚀 Getting Started

### 1. Get the Code

```bash
# Clone the repository
git clone <repository-url>
cd fastapi-boilerplate
```

### 2. Set Up Virtual Environment 🔧

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies 📦

```bash
# Install all dependencies at once
pip install -r requirements.txt

# Or install packages individually
pip install fastapi==0.104.1 uvicorn==0.24.0 motor==3.3.1 pymongo==4.5.0 \
    pydantic==2.5.2 python-jose==3.3.0 "passlib[bcrypt]"==1.7.4 \
    python-multipart==0.0.6 python-dotenv==1.0.0 email-validator==2.1.0.post1
```

### 4. Configure Environment ⚙️

Create a `.env` file in the root directory:

```bash
echo "MONGODB_URL=mongodb://localhost:27017
DB_NAME=fastapi_db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256" > .env
```

### 5. Launch the Application 🎯

```bash
uvicorn app.main:app --reload
```

## 🔗 API Endpoints

### Users 👥

- `POST /api/users/` - Create new user
- `GET /api/users/` - List all users
- `GET /api/users/{user_id}` - Get specific user
- `PUT /api/users/{user_id}` - Update user
- `DELETE /api/users/{user_id}` - Delete user

### Orders 📦

- `POST /api/orders/` - Create new order
- `GET /api/orders/` - List all orders
- `GET /api/orders/{order_id}` - Get specific order
- `PUT /api/orders/{order_id}` - Update order
- `DELETE /api/orders/{order_id}` - Delete order

## 🛠️ Development Commands

```bash
# Install new package
pip install package_name

# Update requirements.txt
pip freeze > requirements.txt

# Deactivate virtual environment
deactivate
```

## 📚 Documentation

Access your API and its documentation at:

- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 💡 Need Help?

Check out the [FastAPI documentation](https://fastapi.tiangolo.com/) for detailed information about the framework.
