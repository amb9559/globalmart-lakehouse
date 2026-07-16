# 🛒 GlobalMart Enterprise Retail Lakehouse Platform

> Production-grade end-to-end Azure Databricks Lakehouse implementation following enterprise data engineering best practices.

![Azure](https://img.shields.io/badge/Azure-Cloud-blue)
![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-red)
![Python](https://img.shields.io/badge/Python-3.11+-yellow)
![PySpark](https://img.shields.io/badge/PySpark-Enterprise-orange)
![Delta Lake](https://img.shields.io/badge/Delta-Lake-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# Project Overview

GlobalMart is a fictional multinational retail organization operating:

- 🏬 2,500+ Stores
- 🌍 30+ Countries
- 👥 150 Million Customers
- 📦 25 Warehouses
- 🛍️ Online Marketplace
- 📱 Mobile Application
- 🚚 Supply Chain
- 💳 Finance
- 📈 Marketing
- ❤️ Customer Service

This project demonstrates how to build a **production-grade Azure Databricks Lakehouse** using modern Data Engineering practices.

---

# Objectives

- Build a scalable enterprise Lakehouse
- Implement Medallion Architecture
- Build reusable ETL framework
- Generate realistic enterprise datasets
- Implement Delta Lake best practices
- Build batch and streaming pipelines
- Apply enterprise coding standards
- Implement monitoring and logging
- CI/CD using Azure DevOps
- Portfolio-ready implementation

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Cloud | Microsoft Azure |
| Compute | Azure Databricks |
| Storage | ADLS Gen2 |
| Language | Python |
| Big Data | PySpark |
| SQL | Databricks SQL |
| Streaming | Azure Event Hub |
| API | FastAPI |
| ETL | Azure Data Factory |
| Governance | Unity Catalog |
| Security | Azure Key Vault |
| DevOps | Azure DevOps |
| Reporting | Power BI |

---

# Architecture

```
                    Source Systems

 CSV      JSON      APIs      Azure SQL

             Azure Data Factory

                     │

             Azure Data Lake Storage

                     │

            Bronze Delta Tables

                     │

            Silver Delta Tables

                     │

             Gold Business Layer

                     │

        Power BI / Machine Learning
```

---

# Medallion Architecture

```
Landing

   │

Bronze

   │

Silver

   │

Gold
```

---

# Project Structure

```
globalmart-lakehouse/

│
├── configs/
│
├── data/
│
├── docs/
│
├── notebooks/
│
├── src/
│   ├── generators/
│   ├── ingestion/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   ├── api/
│   ├── streaming/
│   ├── common/
│   └── tests/
│
├── infrastructure/
│
├── deployment/
│
├── monitoring/
│
├── cicd/
│
├── sql/
│
├── requirements.txt
│
└── README.md
```

---

# Completed Modules

## Infrastructure

- Azure Subscription
- Resource Group
- Azure Databricks Workspace
- Azure Storage Account (ADLS Gen2)
- GitHub Repository

---

## Enterprise Framework

Implemented reusable enterprise modules:

```
config.py

logger.py

common.py

faker_utils.py
```

These modules provide:

- Centralized Configuration
- Enterprise Logging
- Common Utility Functions
- Synthetic Data Generation Framework

---

# Enterprise Coding Standards

This project follows:

- PEP-8
- SOLID Principles
- DRY Principle
- Modular Design
- Type Hinting
- Exception Handling
- Centralized Logging
- Configuration Driven Development
- Reusable Components

---

# Data Sources

The platform supports:

- CSV
- JSON
- Parquet
- Azure SQL Database
- REST APIs
- Azure Event Hub

---

# Enterprise Features

- Medallion Architecture
- Delta Lake
- Auto Loader
- Structured Streaming
- Change Data Capture (CDC)
- MERGE
- Time Travel
- OPTIMIZE
- ZORDER
- VACUUM
- Unity Catalog
- Workflows
- Secret Management
- Monitoring
- CI/CD

---

# Project Roadmap

| Phase | Status |
|---------|--------|
| Infrastructure Setup | ✅ |
| Shared Generator Framework | ✅ |
| Category Generator | ⏳ |
| Supplier Generator | ⏳ |
| Product Generator | ⏳ |
| Warehouse Generator | ⏳ |
| Customer Generator | ⏳ |
| Batch Ingestion | ⏳ |
| Bronze Layer | ⏳ |
| Silver Layer | ⏳ |
| Gold Layer | ⏳ |
| Streaming | ⏳ |
| Unity Catalog | ⏳ |
| Security | ⏳ |
| Monitoring | ⏳ |
| CI/CD | ⏳ |
| Performance Optimization | ⏳ |

---

# Running the Project

## Clone Repository

```bash
git clone https://github.com/<your-github-username>/globalmart-lakehouse.git

cd globalmart-lakehouse
```

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Author

**Ambuj Kumar**

Senior Data Engineer

Enterprise Azure Databricks Lakehouse Project

---

# License

This project is intended for learning, portfolio demonstration, and interview preparation.