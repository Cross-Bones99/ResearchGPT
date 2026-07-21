# 🔬 ResearchGPT

> An AI-powered multi-agent research assistant that automates the process of researching, analyzing, and generating professional research reports using autonomous AI agents.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

ResearchGPT is a multi-agent AI research platform built using **LangGraph** and **FastAPI**. Instead of relying on a single AI model, the system coordinates multiple specialized AI agents to collaboratively research a topic, gather relevant information, analyze findings, and generate comprehensive research reports.

The application provides a modern web interface with real-time agent activity streaming, allowing users to monitor each stage of the research process as it happens.

---

## ✨ Features

- 🤖 Multi-Agent Research Workflow
- 🔍 Intelligent Web Search
- 📑 Automated Research Report Generation
- ⚡ Real-Time Agent Progress Streaming (SSE)
- 🌗 Dark / Light Theme
- 🎨 Modern Responsive UI
- 🔄 LangGraph State Management
- 📡 FastAPI Backend
- 📝 Markdown Report Rendering

---

## 🏗️ Architecture

```
                User Query
                     │
                     ▼
              Planner Agent
                     │
                     ▼
              Search Agent
                     │
                     ▼
            Research Agent
                     │
                     ▼
              Writer Agent
                     │
                     ▼
           Final Research Report
```

---

## ⚙️ Tech Stack

### Backend

- Python
- FastAPI
- LangGraph
- LangChain
- Groq LLM
- Tavily Search API

### Frontend

- HTML5
- CSS3
- JavaScript
- Server-Sent Events (SSE)

---

## 🚀 Current Workflow

1. User submits a research query.
2. Planner Agent breaks the task into research objectives.
3. Search Agent gathers relevant information from the web.
4. Research Agent analyzes and synthesizes the collected data.
5. Writer Agent generates a structured research report.
6. Results are streamed live to the frontend.

---

## 📂 Project Structure

```
ResearchGPT
│
├── backend
│   ├── agents
│   ├── graphs
│   ├── routers
│   ├── services
│   ├── utils
│   └── main.py
│
├── frontend
│   ├── assets
│   │   ├── css
│   │   ├── js
│   │   └── images
│   └── index.html
│
├── tests
├── requirements.txt
└── README.md
```

---

## 🌟 Key Highlights

- Multi-agent orchestration using LangGraph
- Modular backend architecture
- Event-driven communication using Server-Sent Events
- Clean and responsive user interface
- Scalable architecture for adding new AI agents and tools
- Separation of frontend and backend

---




