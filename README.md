
# 🧭 Bookmark Management Backend — FastAPI + PostgreSQL + JWT

## 🚀 Overview

This project is a backend API built with **FastAPI**, designed to manage **user authentication** and **personal bookmarks**.
It follows a **microservices architecture** with modular components and **JWT-based authentication** to ensure secure user sessions.

---


## ⚙️ Core Features

### 🧑‍💻 User Authentication

* Implements **JWT (JSON Web Token)** authentication.
* Users can:

  * **Register** with email and password.
  * **Login** and receive a JWT access token.
  * **Refresh** expired access tokens using refresh tokens.
* Tokens have an **expiry time of 1 hour** for enhanced security.

---

### 🔖 Bookmark Management

Authenticated users can:

* **Create** a new bookmark (URL, title, description, category).
* **View** all their saved bookmarks.
* **Find** a specific bookmark by its ID.
* **Update** a bookmark’s title or description.
* **Delete** a bookmark.
* **Categorize** bookmarks (e.g., “Work”, “Personal”, etc.).

---

### 🗄️ Database

* Uses **PostgreSQL** for storing:

  * User credentials (with securely hashed passwords)
  * Bookmark data (linked to each user)
* ORM: **SQLAlchemy**

---

## 🧩 API Endpoints

### 🔐 Authentication Routes (`/api/v1/auth/auth/`)

| Method   | Endpoint                    | Description            |
| -------- | --------------------------- | ---------------------- |
| **POST** | `/api/v1/auth/auth/`        | Register a new user    |
| **POST** | `/api/v1/auth/auth/token`   | Login to get JWT token |
| **POST** | `/api/v1/auth/auth/refresh` | Refresh access token   |

---

### 🔖 Bookmark Routes (`/api/v1/bookmarker/`)

| Method     | Endpoint                  | Description                    |
| ---------- | ------------------------- | ------------------------------ |
| **GET**    | `/api/v1/bookmarker/`     | Get all bookmarks              |
| **POST**   | `/api/v1/bookmarker/`     | Create a new bookmark          |
| **GET**    | `/api/v1/bookmarker/{id}` | Find bookmark by ID            |
| **PATCH**  | `/api/v1/bookmarker/{id}` | Update a bookmark (title/desc) |
| **DELETE** | `/api/v1/bookmarker/{id}` | Delete a bookmark              |

---

## 🔐 JWT Security

* Tokens expire after **1 hour**.
* Secured endpoints require a valid token in the **Authorization header**:

  ```
  Authorization: Bearer <your_token>
  ```
* Refresh tokens can be used to generate new access tokens without re-login.

---

## 🧱 Tech Stack

* **FastAPI** — Web Framework
* **SQLAlchemy** — ORM
* **PostgreSQL** — Database
* **Uvicorn** — ASGI Server
* **Docker & Docker Compose** — Containerization
* **Python 3.11**

---

## 🐳 Running with Docker

To start all services (Auth + Bookmark + DB):

```bash
docker-compose up --build
```

---

## 🧰 Local Development Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/AlankrithaS/Assignment_Copy.git
   cd Assignment_Copy
   ```

2. **Create virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   uvicorn src.main:app --reload
   ```

---

## 🧪 Testing

Once the app is running, test the endpoints using:

* **Postman**
* **cURL**
* Or visit `http://127.0.0.1:8000/docs` for an interactive Swagger UI.

---

## ✨ Author

**Alankritha S**
📂 [Project Drive Link](https://drive.google.com/drive/u/0/folders/17VtxfgBIb0hVggFEe3SUcMkwM0ZHyzO3)

---

