# ***WHAT IS API?***

- A MECHANISM  THAT ENABLES TWO SOFTWARE COMPONENTS- SUCH AS FRONTEND AND BACKEND- TO COMMUNICATE WITH EACH OTHER USING DEFINED PROTOCOLS AND DATA FORMATS.
- IT IS A SET OF ENDPOINTS. FUNCTION IS AVAILABLE PUBLICLY.
- API RETURN THE DATA BACK IN `JASON`.
- JSON CAN INTERACT WITH AND IS CAPABLE OF UNDERSTANDING PYTHON. PHP.

'''

## ***API - ML PERSPECTIVE***

- ML MODEL

→APPLICATION PROGRAMMING INTERFACE

→TALE REQUEST AND RETURNS RESPONSE

---


# CLIENT-SERVER ARCHITECTURE

## The Client (REQUEST-INITIATOR)

- The client is typically a device or software that initiates a request for a service or resource. It's the user-facing component that asks for something.
- DEVICE CONNECTED TO INTERNET→ CLIENT

Web browsers (Chrome, Safari, Firefox)
Mobile apps (Instagram, banking applications)
Desktop applications (Email clients)

## The Server- (RESPOND)

- The server is a powerful computer or program that provides services and resources in response to client requests. It processes requests and sends back data.
- PROGRAM THAT PROVIDES SERVICE→ SERVER

Web servers hosting websites (Apache, Nginx)
Database servers storing information (SQL, MongoDB)
Application servers running business logic

***CLIENT→request to server→SERVER PROCESS→SERVER RESPOND→HTML,IMAGES TO BROWSER OR CLIENT***

---

# REST API’S

### CLIENT-SERVER

### STATELESS

### UNIFORM INTERFACE

### CACHEABLE

---

## ***FASTAPI***

- PYTHON WEB FRAMEWORK FOR BUILDING API WITH PYTHON
- FASTAPI MADE ON :
- STARLETTE → API RECEIVES AND SENDS RESPONSE
- PEDANTIC  → CHECK DATA IN YOUR API IS CORRECT AND IN THE RIGHT FORMAT
- unicorn for server
- FLASK: `WEB SERVER ( GUVICORN ) → WSGI SERVER GATEWAY INTERFACE → API CODE`
- **FAST API: `WEB SERVER  ( UVICON ) →   ASGI STARLETTE → API CODE  ( ASYNCHRONOUS ENDPOINT )`**

---

## UV

PACKAGE INSTALLER → FAST

- PIP INSTALL UV
- UV INIT PROJECT-NAME
- uv run [main.py](http://main.py/) - Creating virtual environment at: .venv
- add dependencies and library by writing command in terminal - uv add fast API in .toml
- uv build
- unicorn for server
- for specific dependencies  - uv run --with 'flask' [chaiexample.py](http://chaiexample.py/)

---

**$—EXAMPLE—$**

`CUSTOMER—WAITER—CHEF`

`REQUEST—PROCESS—RESPONSE` 

![image.png](attachment:93284037-955a-4f68-b6bc-86bb3f178766:image.png)

API—Application Programming Interface

You→→API→Server.

Request

served

Waiter

KITCHEN

Customer

Response back.

You (the customer): Want to order fooo (ask for data) Action.

Waiter (API): Takes your order to kitchen (server)

Kitchen (Server): Prepare food (Process the reg)

Wattor (APT) Brings food back (retum data).

You req: what's the weather in New York

API: Take it to server.

Server Process: tind weather data.

APT: brings back The weather is sury.

API has its own pros and cons.

---

## → INTERACTIONS

SERVER → DYNAMIC →  CONTAINS CRUD OPRATION

- TO RETRIEVE (GET) : HTTPS → VERB → GET →
- TO SEND (POST): HTTPS → VERB → POST   → CREATE
- TO UPDATE (PUT) : HT   TPS → VERB → PUT → UPDATE
- TO DELETE (DELETE) : HTTPS → VERB → GET → DELETE

### HOW IT WORKS

## HTTP REQUEST

- START LINE (WHICH METHOD)
- HEADERS (TOKENS)
- BODY (DATA)

## HTTP RESPONSE
