# 🛒 E-Commerce Microservices Application

This project is a full-stack **E-Commerce system** built using a **microservices architecture** with **FastAPI (Backend)** and **React.js (Frontend)**.
It supports authentication, product management, cart handling, and order processing using scalable services.

The goal of this project is to demonstrate real-world backend design, API communication, JWT authentication, caching, and frontend integration.

---

## 🚀 Tech Stack

### Backend

* FastAPI
* PostgreSQL (Auth, Users, Orders)
* MongoDB (Products, Cart)
* Redis (Caching)
* JWT Authentication
* Pydantic Validation

### Frontend

* React.js
* Axios
* React Router
* Context API

### Tools

* Git & GitHub
* Postman
* Docker (optional)

---

## 🧩 Microservices Architecture

The backend is divided into 4 independent services:

| Service         | Description                                  | Port |
| --------------- | -------------------------------------------- | ---- |
| Auth Service    | User registration, login, JWT authentication | 8000 |
| Product Service | Product catalog, pagination, caching         | 8001 |
| Cart Service    | Add, update, remove cart items               | 8002 |
| Order Service   | Checkout, order creation, history            | 8003 |

Each service runs independently and communicates via REST APIs.

---

## 🔐 Features

* User Registration & Login
* JWT Token Authentication
* Role-based access (User/Admin)
* Product listing with pagination
* Redis caching for fast product fetch
* Cart management
* Order checkout flow
* React frontend integration
* Protected routes

---

## 📁 Project Structure

```
ecommerce-project/
│
├── auth-service/
├── product-service/
├── cart-service/
├── order-service/
│
└── frontend/
    ├── src/
    ├── pages/
    ├── components/
    ├── context/
```

---

## ⚙️ Backend Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pymongo redis passlib python-jose
```

### 3️⃣ Run Services

```bash
uvicorn main:app --reload --port 8000
uvicorn main:app --reload --port 8001
uvicorn main:app --reload --port 8002
uvicorn main:app --reload --port 8003
```

---

## ⚙️ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Open browser:

```
http://localhost:3000
```

---

## 🔄 API Flow

1. User registers/logs in
2. Auth service generates JWT
3. React stores token
4. Token is sent with API calls
5. Product service fetches cached data
6. Cart service manages items
7. Order service completes checkout

---

## 🧪 Testing

* APIs tested using Postman
* Frontend tested via browser
* JWT validated on each request

---

## 🎯 Learning Outcomes

* Microservices architecture
* JWT authentication
* API communication
* Redis caching
* MongoDB integration
* React frontend integration
* Clean project structure

---

## 👨‍💻 Author

**Rajeev Kumar**
Backend / Full Stack Developer
Python | FastAPI | React | PostgreSQL | MongoDB

---

## 📌 Future Enhancements

* Payment gateway integration
* Admin dashboard
* Docker deployment
* Kubernetes orchestration
* CI/CD pipeline

---


