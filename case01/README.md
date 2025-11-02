

# SSS Assistant - README

## Overview

The **Protel FAQ Assistant** is an intelligent, Django-based question-answering system designed to provide accurate and fast responses to user queries.
It uses a **hybrid approach** that combines a predefined FAQ database with the power of **Large Language Models (LLMs)**.
This ensures that users always receive the best possible answer — whether the question already exists in the database or must be generated dynamically.

---

## Features

### 1. **FAQ Database Querying**

* The system maintains a structured database of frequently asked questions and their corresponding answers.
  (More than 190 Protel-related Q&A pairs stored in `sample_faqs.json`).
* When a user submits a question, the system first searches for a semantically similar question in the database.
* If the similarity score is **90% or higher**, the related answer is returned to the user.

### 2. **LLM Integration**

* If no suitable FAQ is found (similarity below 90%), the system dynamically generates an answer using an **LLM**.
* This allows the system to respond accurately even to questions not present in the database.
* The LLM can handle complex, open-ended, or domain-specific questions.

### 3. **search_in_urls (Searches within Protel-related links)**

* When the LLM cannot provide a sufficient answer, the system retrieves related information from the Protel website.
* This improves accuracy for up-to-date or external information needs.

### 4. **Enhanced Similarity Scoring Mechanism**

* The system now uses a more advanced **NLP-based similarity scoring algorithm**.
* It considers semantic relationships rather than just keyword matching, resulting in higher accuracy.

### 5. **Dynamic Knowledge Base**

* Administrators can easily add, edit, or delete FAQ entries.
* The FAQ database is designed to continuously evolve based on user needs.

### 6. **LLM Fallback for Unanswered Queries**

* If a question does not exist in the database, the system automatically switches to the LLM for context-aware answers.
* If the LLM fails, a Protel web search is triggered.
* If still no answer is found, the system politely replies with “Sorry, no answer available” and suggests three similar topics/questions.

### 7. **Advanced Query Logging**

* Every query and its response source (FAQ database, LLM, or web) are logged.
* This allows administrators to evaluate and improve system performance and coverage over time.

### 8. **Interactive Front-End**

* A simple and user-friendly interface allows users to type questions and view responses easily.
* If no answer is found, similar question suggestions are offered.
* The responsive design ensures smooth operation across all devices.

### 9. **Scalable Architecture**

* The project is designed to scale from small setups to enterprise-level deployments.

### 10. **Customizable Thresholds**

* Administrators can adjust the similarity threshold (default: 90%) to balance precision and coverage.

### 11. **Static File Support**

* Static files like CSS, JavaScript, and images are integrated to enrich user experience.

---

## System Workflow

1. **User Query Submission**

   * Users submit questions via the front-end interface.
2. **Database Search**

   * The system calculates the similarity score between the submitted question and all FAQ entries.
   * If the similarity is 90% or higher, the corresponding answer is returned.
3. **LLM Fallback**

   * If no match is found, the query is sent to the LLM for real-time response generation.
4. **Answer Display**

   * The best answer (from database or LLM) is displayed to the user.
5. **Query Logging**

   * Each query is stored for later analysis and system improvement.

---

## Advantages

* **Efficiency**: Quickly answers frequent questions using pre-recorded FAQs.
* **Flexibility**: Handles unique or unexpected questions via LLM integration.
* **Scalability**: Adapts easily to growing databases and user bases.
* **User-Centric**: Provides an intuitive and seamless experience.
* **Customizable**: Administrators can fine-tune the system easily.

---

## User Guide

### For Users

* Type your question in the input box and click **"Ask Question"**.
* If the question is recognized, the answer appears instantly.
* If not recognized, please wait a few seconds while the LLM generates a response.
* If no answer is found, similar questions will be shown — click one if relevant.
  Otherwise, click **"Ask Another Question"** to rephrase and try again.

### For Administrators

* Use Django’s admin panel to manage the FAQ database.
* Regularly review query logs to identify frequently asked or unanswered questions.
* Update the database to improve accuracy and coverage.

---

## Running the Project Locally

### Requirements

* Python (3.8 or higher)
* Django (4.x or higher)
* SQLite (default, pre-configured)
* Optional: LLM API key (e.g., OpenAI or equivalent)

### Steps

> These steps can also be executed in **Anaconda Prompt**.

1. **Clone the Project:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   *(Already included in the project)*

   * Create a `.env` file in the root directory and add:

     ```env
     SECRET_KEY=<your-django-secret-key>
     DEBUG=True
     LLM_API_KEY=<your-llm-api-key>
     ```

5. **Run Database Migrations:**
   *(If manage.py isn’t accessible, specify the full file path)*

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Load Sample FAQ Data:**

   ```bash
   python manage.py loaddata sample_faqs.json
   ```

7. **Start the Development Server:**

   ```bash
   python C:\Users\yasme\Desktop\FQA\smart_FAQ\manage.py runserver
   ```

   Access the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

8. **Access the Admin Panel:**

   * You can find login credentials in the “super user.txt” file or create a new one:

     ```bash
     python manage.py createsuperuser
     ```
   * Then visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

---

## Future Improvements

* **Multilingual Support**: Process queries in multiple languages.
* **Advanced Analytics**: Provide detailed reports on user behavior and system performance.
* **Improved NLP Techniques**: Integrate newer models for better similarity scoring.
* **Voice Query Integration**: Enable voice-based question input.
* **Google Search API Integration**:

  * The ready-to-use function in `google_search.py` can be reactivated in the `views.py` file.
  * However, keyword-based filtering is recommended to avoid irrelevant, non-Protel answers.

---

## Installation & Startup

1. **Clone the Repository**
2. **Install Dependencies** (from `requirements.txt`)
3. **Run Migrations** to set up the database
4. **Load Initial FAQ Data**
5. **Start the Development Server**
6. **Access the Application** via `http://127.0.0.1:8000`

---

## Folder Structure

```
smart_FAQ/
│-- db.sqlite3              # SQLite database
│-- manage.py               # Django management script
│-- .env                    # Environment variables
│-- .gitignore              # Git ignore file
│-- README.md               # Project documentation
│-- super user              # Admin credentials for 'http://127.0.0.1:8000/admin'
├── faq/                    # Main application
│   ├── helper/             # Utility functions
│   ├── migrations/         # Database migrations
│   ├── admin.py            # Admin panel config
│   ├── apps.py             # App config
│   ├── models.py           # Database models
│   ├── views.py            # App logic
│
├── smart_FAQ/              # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing
│   ├── asgi.py, wsgi.py    # Deployment configs
│
├── static/                 # Static files (CSS, JS, etc.)
│   ├── styles.css
│
├── templates/              # HTML templates
│   ├── ask.html
│   ├── home.html
│
├── requirements.txt        # Dependency list
├── Verified FAQ.py         # Script for verified FAQs
```


