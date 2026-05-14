# RAG Chat Agent (FastAPI + LangChain + Qdrant)

A **Retrieval-Augmented Generation (RAG)** based chat agent that answers user questions using **contextual knowledge stored in a vector database**.  
This project uses **FastAPI** as the backend API, **LangChain** for RAG orchestration, and **Qdrant** for embedding storage and similarity search.

The application is fully **Docker** and **Docker Compose** enabled for easy deployment.

The context data contains sample pdf file for Company policies and the agent answers based on the content from this file and does not answer other questions.

---

## 🚀 Features

- **Chat API** powered by FastAPI
- **RAG pipeline** using LangChain
- **Vector database** support via Qdrant
- Stores and retrieves knowledge using **embeddings**
- Supports **document ingestion** (optional depending on implementation)
- Fully containerized using **Docker**
- One-command startup using **docker-compose**

---

## 🏗️ Tech Stack

- **Python**
- **FastAPI**
- **LangChain**
- **Qdrant**
- **Docker / Docker Compose**

---

## ⚙️ Setup and Installation

### Prerequisites

Make sure you have the following installed:
- 🐍 Python 3.10+
- 🐳 Docker (optional, for deployment)



### OpenAI API Key 🔑

To integrate the OpenAI language model into your RAG system, you’ll need to provide your OpenAI API key. Follow these steps to set it up:
Get your API key and add it to the .env file.
   ```bash
   OPENAI_API_KEY="your openai api key"
   ```

### Huggingface API Key

For embedding context data, huggingface api used. Add your 
   ```bash
   HF_TOKEN="your openai api key"
   ```

### Qdrant storage path 
To persist embedded data in vector database, storage path is required.

   ```bash
   QDRANT_STORAGE_PATH="/your/storage/path"
   ```

## 🚀 Deployment

### Docker Deployment
If you want to deploy and run your RAG system using Docker, simply run the following command. Before that just update
the docker-compose file with your environment parameters:

```bash
docker-compose up
```

This command creates the docker image and deploy and run it.
