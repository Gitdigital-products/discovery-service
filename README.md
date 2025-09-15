# discovery-service
# Discovery Service  Search &amp; discovery engine for the **Gitdigital Products** ecosystem.   Lets users find products, content, and other entities via keyword queries.  ## 🚀 Features - `GET /search?q=keyword` → search across titles, descriptions, tags - 
# Discovery Service

Search & discovery engine for the **Gitdigital Products** ecosystem.  
Lets users find products, content, and other entities via keyword queries.

## 🚀 Features
- `GET /search?q=keyword` → search across titles, descriptions, tags
- Simple in-memory index (for now)
- Easy to expand with more searchable fields

## 🛠️ Setup
```bash
cargo run
# Discovery Service

A lightweight service registry and discovery system for the HustleGPT microservices platform.  
It allows services to **register, deregister, heartbeat, and be discovered** by other components.  
Includes a simple **search layer** for querying services by name, tags, or metadata.

---

## 🚀 Features
- Register and deregister services
- Heartbeat monitoring for availability
- Service discovery API
- Keyword-based search for metadata
- REST API for easy integration
- Dockerized for deployment

---

## 🛠️ Tech Stack
- Python 3.11+
- FastAPI
- Uvicorn
- SQLite (default, pluggable for Postgres)
- Docker

---

## 📂 Project Structure
