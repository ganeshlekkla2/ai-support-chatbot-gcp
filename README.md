# AI-Powered Customer Support Ecosystem

Building a smarter, more empathetic way to bridge the gap between businesses and their customers.

---
**🔗 [Live Demo](https://storage.googleapis.com/gk_chatbot27/index.html)** | **📁 [Documentation](https://github.com/ganeshlekkla2/ai-support-chatbot-gcp)**

---

## 🚀 Project Overview
In modern commerce, customer support is often either too rigid (basic bots) or too slow (overwhelmed human agents). I developed this project to demonstrate a **Hybrid Intelligence** approach: a system that can handle structured data tasks like order tracking with 100% accuracy, while using Generative AI to manage complex, high-emotion complaints with genuine empathy.

By leveraging a serverless architecture on Google Cloud Platform, this ecosystem is designed to be highly scalable, cost-effective, and production-ready from day one.

---

## 🏗️ System Architecture
This diagram illustrates the flow of data from the user interface through the cloud logic layers and into the AI/Database engines.

```text
┌──────────┐      ┌──────────────────────────┐      ┌──────────────────────────────────────────────────┐
│          │      │                          │      │                                                  │
│   User   ├─────►│     Website (Frontend)   ├─────►│                Dialogflow CX (AI Brain)          │
│   👤     │      │       (HTML/CSS)         │      │                                                  │
└──────────┘      └──────────────────────────┘      └───────────────────────┬──────────────────────────┘
                                                                            │
                                                                            │ Webhook Call
                                                                            │
                                                                            ▼
                                                      ┌──────────────────────────────────────────────────┐
                                                      │                                                  │
                                                      │        Cloud Function (Python Backend Logic)     │
                                                      │                                                  │
                                                      └───────────────────────┬──────────────────────────┘
                                                                            │
                                                       ┌────────────────────┴────────────────────┐
                                                       │                                         │
                                                       ▼                                         ▼
                                             ┌───────────────┐                         ┌───────────────────┐
                                             │               │                         │                   │
                                             │   Firestore   │                         │    Gemini API     │
                                             │   (Database)  │                         │ (For Complaints)  │
                                             │               │                         │                   │
                                             └───────────────┘                         └───────────────────┘
```
---

## ✨ Key Features
Real-Time Order Tracking: Seamlessly integrates with a Firestore NoSQL database to provide live shipping updates.

Empathetic Complaint Handling: Uses the Gemini API to analyze user frustration and generate human-like, professional responses.

Intelligent Intent Recognition: Built with Dialogflow CX, utilizing advanced entity extraction to identify Order IDs and user needs accurately.

Serverless & Scalable: The backend is hosted on GCP Cloud Functions, ensuring zero idle costs and the ability to scale to thousands of concurrent users.

---

## 🛠️ Tech Stack
Cloud Platform: Google Cloud Platform (GCP)

Conversational AI: Dialogflow CX

Large Language Model: Gemini Pro (via API)

Backend: Python 3.9 (Cloud Functions)

Database: Firestore (NoSQL)

Frontend: HTML5, CSS3, JavaScript

---

## 🚀 Setup & Installation
To deploy this project, ensure the following APIs are enabled in your Google Cloud Console:

Dialogflow API

Cloud Functions API

Cloud Build API

Firestore API

Generative AI API (for Gemini)

---

## Backend Requirements
Ensure your requirements.txt includes:

functions-framework

google-cloud-firestore

google-generativeai
