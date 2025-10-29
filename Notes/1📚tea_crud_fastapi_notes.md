
---
## Tea CRUD API with FastAPI 🍵🚀

### 🌟 FastAPI

- **Definition**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on type hints.
    
- **Why FastAPI?**
    
    - 🚀 Extremely fast due to Starlette + Pydantic
        
    - 🛠 Auto-generated **Swagger UI** and **ReDoc** documentation
        
    - ✅ Type checking with Python type hints
        
- **Applications**:
    
    - REST APIs
        
    - Microservices
        
    - Backend for web & mobile apps
        
    - ML model deployment
        

---

### 🧾 Pydantic & BaseModel

- **Definition**: Pydantic is a data validation library that ensures input data matches the defined schema.
    
- **BaseModel**: A class you inherit from to define structured models.
    
- **Example**:
    
    ```python
    class Tea(BaseModel):
        id: int
        name: str
        origin: str
    ```
    
- **Applications**:
    
    - Input validation
        
    - Response serialization
        
    - Ensuring API data integrity
        

---

### 🛠 CRUD Operations

- **Definition**: Basic operations to interact with data:
    
    - **C**reate → Add new data (`POST`)
        
    - **R**ead → Retrieve data (`GET`)
        
    - **U**pdate → Modify existing data (`PUT`)
        
    - **D**elete → Remove data (`DELETE`)
        
- **Example**:
    
    - `POST /teas` → Add new tea
        
    - `GET /teas` → Get all teas
        
    - `PUT /teas/{id}` → Update tea
        
    - `DELETE /teas/{id}` → Delete tea
        

---

### 🔗 Path & Query Parameters

- **Path parameter**: `/{tea_id}` → part of the URL  
    Example: `/teas/1` fetches tea with ID 1
    
- **Query parameter**: `?origin=India` → filter teas from India (not yet used in your code, but possible).
    

---

### 📦 In-memory Database

- Right now, you’re using a simple Python list (`teas: List[Tea] = []`) to store data.
    
- **Pros**: Easy, fast for learning.
    
- **Cons**: Data is lost when the server restarts.
    
- **Next step**: Use a real database like SQLite, PostgreSQL, or MongoDB.
    

---

### 🌍 Real-world Applications of CRUD APIs

- 📱 Social Media Apps (posts, comments, users)
    
- 🛒 E-commerce (products, orders, customers)
    
- 📚 Libraries (books, authors, borrowers)
    
- 🍵 Tea House (your app 😉)
    

---

