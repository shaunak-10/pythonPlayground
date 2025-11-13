# 📦 Python APM Playground

A **multi-framework Python project** demonstrating **FastAPI**, **Django**, and **Flask** — each instrumented with **Postgres**, **MySQL**, **Kafka** & **external API calls**.

This repository contains **three standalone Python web applications**:

- **FastAPI App** (async, modern API server)  
- **Django App** (DRF + multi-DB routing)  
- **Flask App** (RESTX + SQLAlchemy + Kafka)  

---

All three apps **share**:

- Kafka producer + sample consumer script  
- Postgres (**User** models)  
- MySQL (**Product** models)  
- External API proxy example  
- Docker-based infra for DBs + Kafka  
- Swagger / API docs  

> **Each app is fully independent and can be run separately.**

---

## 🚀 1. Clone the Repository

```bash
git clone https://github.com/shaunak-10/python-apm-playground.git
cd python-apm-playground
