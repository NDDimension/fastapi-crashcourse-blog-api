# ⚡ FastAPI Crash Course – Blog API (Simple Project)

> 🚀 A beginner-friendly blog API built with **FastAPI**, covering routing, request handling, schemas, authentication, and password hashing — without a full-fledged database setup.

---

## 📋 Project Description

This project is a **crash course implementation of a blog API using FastAPI**. It demonstrates how to build clean, modular, production-style APIs using **Python 3**, **FastAPI**, and Pydantic, with **dummy in-memory data** instead of a database.

This is ideal for learners who want to understand the **core FastAPI concepts** before diving into database integration and deployment.

---

## 📌 Topics Covered

✅ FastAPI Basics (routing, path/query params)  
✅ Request Body Handling with Pydantic  
✅ Schema Design (Request & Response Models)  
✅ Modular project structure using routers & repository layers  
✅ User creation & password hashing  
✅ Simple authentication using OAuth2 & JWT  
✅ Token validation & route protection  
✅ Clean file organization with reusable modules

---

## 🏗️ Folder Structure

```
📦 your-project/
├── CodeFiles/                 # Practice/demo files
│   ├── main.py
│   ├── query_param.py
│   ├── request_body.py
│   └── tea_crud_fastapi.py
├── blog/                      # Core Module (Main App)
│   ├── __init__.py
│   ├── authentication.py
│   ├── blog.py                # Blog logic/handlers
│   ├── user.py                # User APIs
│   ├── database.py            # Simulated in-memory DB (no SQL used)
│   ├── hashing.py             # Password hashing using passlib
│   ├── models.py              # Pydantic models (not ORM models)
│   ├── oauth2.py              # Token verification
│   ├── schemas.py             # Request/Response Schemas
│   └── token.py               # Token schema
├── repository/                # Logic layer for blog & user
│   ├── blog.py
│   ├── user.py
├── routers/                   # API route splitting
│   ├── blog.py
│   ├── user.py
│   └── authentication.py
├── Notes/                     # Course notes (optional)
├── blog.db                    # Placeholder DB file (unused)
├── main.py                    # Main app entry point
├── requirements.txt           # Dependencies
```

---

## 🧑‍💻 Getting Started

### ✅ Prerequisites

- Python 3.8+
- pip / venv
- FastAPI & Uvicorn

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Start the App

```bash
uvicorn main:app --reload
```

### 🔗 API Docs

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## 🔐 Auth & Security (Simplified)

- 🧂 Passwords are hashed using **Passlib (`bcrypt`)**
- 🔒 JWT tokens issued using **OAuth2 password flow**
- 🔑 Protected routes require valid `Bearer` token in headers

---

## 🧰 Tech Stack

- ⚙️ Python 3
- ⚡ FastAPI
- 🔐 OAuth2 + JWT
- 💡 Pydantic
- 🧂 Passlib (for passwords)
- 🧪 Uvicorn (app server)

> 📌 **Note**: No actual SQL/ORM/DB is used. Data is simulated for learning purposes.

---

## 📘 Resources

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Uvicorn Docs](https://www.uvicorn.org/)
- [Passlib Docs](https://passlib.readthedocs.io/)

---

## 🤝 Contributing

Feel free to fork this repo and customize it:
- Add SQLite/PostgreSQL support
- Implement full CRUD for users/blogs
- Create a frontend in React/Vue/HTMX

---

## 📣 Stay Connected

I'll also be sharing regular updates on **LinkedIn** to track my progress and connect with other learners. Feel free to follow or reach out!

🔗 GitHub: [NDDimension](https://github.com/NDDimension)  
🔗 LinkedIn: [DHANRAJ SHARMA](https://www.linkedin.com/in/dhanraj-sharma-nddimension/)

---

## 📄 License

MIT — Free to use, modify, and share.

---

## ⭐️ Follow-Up

> If this helped you learn FastAPI better, give the repo a ⭐ on GitHub and share it with others!
