# 🚀 FastAPI Learning Guide

A comprehensive guide to understanding APIs, REST architecture, and FastAPI framework.

---

## 📖 Table of Contents

- [What is API?](#what-is-api)
- [Client-Server Architecture](#client-server-architecture)
- [REST APIs](#rest-apis)
- [FastAPI Framework](#fastapi-framework)
- [UV Package Manager](#uv-package-manager)
- [HTTP Methods (CRUD)](#http-methods-crud)
- [HTTP Request & Response](#http-request--response)

---

## 🔌 What is API?

**API (Application Programming Interface)** is a mechanism that enables two software components—such as frontend and backend—to communicate with each other using defined protocols and data formats.

### Key Points:
- ✅ A set of endpoints with publicly available functions
- ✅ Returns data in **JSON** format
- ✅ JSON is compatible with Python, PHP, JavaScript, and more

### 🤖 API from ML Perspective

```
ML Model → Application Programming Interface → Takes Request → Returns Response
```

### 🍽️ Real-World Analogy

| Role | Component | Action |
|------|-----------|--------|
| **Customer** | You (Client) | Want to order food (ask for data) |
| **Waiter** | API | Takes your order to kitchen (server) |
| **Chef/Kitchen** | Server | Prepares food (processes the request) |
| **Waiter** | API | Brings food back (returns data) |

**Example:**
```
You request: "What's the weather in New York?"
    ↓
API: Takes it to server
    ↓
Server: Finds weather data
    ↓
API: Returns "The weather is sunny"
```

---

## 🖥️ Client-Server Architecture

### The Client (Request Initiator)

The client is typically a device or software that **initiates a request** for a service or resource. It's the user-facing component that asks for something.

> 📱 Device connected to Internet → **CLIENT**

**Examples:**
- Web browsers (Chrome, Safari, Firefox)
- Mobile apps (Instagram, banking applications)
- Desktop applications (Email clients)

### The Server (Responder)

The server is a powerful computer or program that **provides services and resources** in response to client requests. It processes requests and sends back data.

> 💻 Program that provides service → **SERVER**

**Examples:**
- Web servers hosting websites (Apache, Nginx)
- Database servers storing information (SQL, MongoDB)
- Application servers running business logic

### Flow Diagram

```
CLIENT → Request to Server → SERVER PROCESSES → SERVER RESPONDS → HTML/Images to Browser
```

---

## 🌐 REST APIs

**REST (Representational State Transfer)** APIs follow these principles:

| Principle | Description |
|-----------|-------------|
| **Client-Server** | Separation of concerns between client and server |
| **Stateless** | Each request contains all necessary information |
| **Uniform Interface** | Consistent way to interact with resources |
| **Cacheable** | Responses can be cached for performance |

---

## ⚡ FastAPI Framework

**FastAPI** is a modern, fast Python web framework for building APIs.

### Built On:

| Component | Purpose |
|-----------|---------|
| **Starlette** | Handles API requests and sends responses |
| **Pydantic** | Validates data in your API (correct format) |
| **Uvicorn** | ASGI server to run the application |

### Flask vs FastAPI

```
┌─────────────────────────────────────────────────────────────────┐
│ FLASK:                                                          │
│ Web Server (Gunicorn) → WSGI (Server Gateway Interface) → API   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ FASTAPI:                                                        │
│ Web Server (Uvicorn) → ASGI (Starlette) → API (Async Endpoints) │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 UV Package Manager

**UV** is a fast Python package installer and resolver.

### Installation & Commands

```bash
# Install UV
pip install uv

# Initialize a new project
uv init project-name

# Run a Python file (auto-creates .venv)
uv run main.py

# Add dependencies (updates pyproject.toml)
uv add fastapi

# Build the project
uv build

# Run with temporary dependency
uv run --with 'flask' example.py
```

### Check Virtual Environments

```powershell
# Find all .venv folders
Get-ChildItem -Path "." -Recurse -Directory -Filter ".venv"

# Find all pyvenv.cfg files (venv indicator)
Get-ChildItem -Path "." -Recurse -Filter "pyvenv.cfg"
```

---

## 🔄 HTTP Methods (CRUD)

| Operation | HTTP Method | Description |
|-----------|-------------|-------------|
| **Create** | `POST` | Send/create new data |
| **Read** | `GET` | Retrieve/fetch data |
| **Update** | `PUT` / `PATCH` | Modify existing data |
| **Delete** | `DELETE` | Remove data |

---

## 📨 HTTP Request & Response

### HTTP Request Structure

```
┌────────────────────────────────┐
│ 1. START LINE (Method + URL)   │
│ 2. HEADERS (Auth tokens, etc.) │
│ 3. BODY (Request data/payload) │
└────────────────────────────────┘
```

### HTTP Response Structure

```
┌────────────────────────────────┐
│ 1. STATUS LINE (Status code)   │
│ 2. HEADERS (Content-type, etc.)│
│ 3. BODY (Response data)        │
└────────────────────────────────┘
```

### Common Status Codes

| Code | Meaning |
|------|---------|
| `200` | OK - Success |
| `201` | Created |
| `400` | Bad Request |
| `401` | Unauthorized |
| `404` | Not Found |
| `500` | Internal Server Error |

---

## 🚀 Quick Start with FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

Run with:
```bash
uvicorn main:app --reload
```

---

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

*Happy Coding! 🐍*
