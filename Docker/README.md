# 🐳 TuteDude – Docker Learning Projects

Welcome to **TuteDude**, a collection of beginner-friendly Docker projects.  
This repo is designed as a step-by-step journey—from a simple “Hello World” to a multi-service app using Docker Compose.  

It’s a humble tribute to learning by doing: honoring the basics, yet paving the way toward building production-ready systems.

---

## 📚 Table of Contents

- [📂 Project Structure](#-project-structure)  
- [🚀 Projects Overview](#-project-overview)
- [⚙️ Requirementsk](#-requirements)  
- [✨ Why this repo?](#-why-this-repo)  
- [📄 License](#-license)  
- [🌟 Final Thought](#-final-thought)

---

## 📂 Project Structure

```bash
Docker/
├── python-hello-world/ # Simple Python Hello World with Docker
├── nodejs-hello/ # Node.js Hello World with Docker
├── python-read/ # Python app reading from a text file
└── completeDockerApp/ # Flask backend + Express frontend (Docker + Compose)
```

---

## 🚀 Projects Overview

### 1️⃣ Python Hello World
- A minimal Python script that prints **Hello, World!**
- Dockerized with a lightweight Python image.
**Run:**
```bash
docker build -t python-hello ./Docker/python-hello-world
docker run python-hello
```

### 2️⃣ Node.js Hello World
- Basic Node.js app returning a Hello World message.
- Perfect starting point for learning Node + Docker.
**Run:**
```bash
docker build -t node-hello ./Docker/nodejs-hello
docker run -p 3000:3000 node-hello
```
Visit: http://localhost:3000

### 3️⃣ Python Read App
- A Python app that reads data from a text file and displays it.
- Includes a Dockerfile for easy containerization.
**Run:**
```bash
docker build -t python-read ./Docker/python-read
docker run python-read
```

### 4️⃣ Complete Docker App – Flask + Express
- Backend: Flask reads data from a text file and exposes an API.
- Frontend: Express consumes the API and displays the data.
- Uses Docker Compose for multi-container orchestration.
- Demonstrates port mappings & service-to-service communication.
**Run:**
```bash
cd Docker/completeDockerApp
docker-compose up --build
```


## ⚙️ Requirements
- Docker
- Docker Compose (for the full app)

## ✨ Why this repo?
- To learn Docker the practical way—not just theory.
- To move from single container apps → multi-service apps.
- To serve as a reference for beginners practicing Docker basics.

## 📜 License

This project is open-sourced.
Feel free to learn, tinker, and build upon it.

## 🌟 Final Thought
Like a ship learning to sail calm waters before braving the ocean,
this repo takes you from the gentlest “Hello World” to a fleet of containers
sailing together in harmony.

---
