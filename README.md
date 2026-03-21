\# 🤖 Mistral AI Chatbot



A conversational AI chatbot built with Mistral's API and FastAPI backend. This project demonstrates real-world integration of large language models into a full-stack web application.



\## 🚀 Features



\- Real-time AI responses powered by Mistral API

\- Clean and responsive chat UI

\- FastAPI backend with REST API endpoint

\- Secure API key management with environment variables

\- Lightweight and fast



\## 🛠️ Tech Stack



\- \*\*Backend:\*\* Python, FastAPI, Uvicorn

\- \*\*Frontend:\*\* HTML, CSS, JavaScript

\- \*\*AI:\*\* Mistral AI API (mistral-small-latest)

\- \*\*Security:\*\* python-dotenv for environment variables



\## ⚙️ Installation \& Setup



1\. Clone the repository

&nbsp;  git clone https://github.com/shubhamdsj/mistral-chatbot.git

&nbsp;  cd mistral-chatbot



2\. Create a virtual environment

&nbsp;  python -m venv venv

&nbsp;  venv\\Scripts\\activate



3\. Install dependencies

&nbsp;  pip install fastapi uvicorn mistralai python-dotenv



4\. Create a .env file in the root folder

&nbsp;  MISTRAL\_API\_KEY=your\_mistral\_api\_key\_here



5\. Run the server

&nbsp;  uvicorn main:app --reload



6\. Open your browser and go to

&nbsp;  http://127.0.0.1:8000/static/index.html



\## 📁 Project Structure



mistral-chatbot/

├── main.py          → FastAPI backend

├── static/

│   └── index.html   → Chat frontend

├── .env             → API key (not uploaded)

├── .gitignore       → Ignored files

└── README.md        → Project documentation



\## 🔒 Security



The .env file is excluded from version control via .gitignore to keep the API key safe.



\## 👨‍💻 Author



Shubham Mishra

MS Computer Science – ESILV Paris

https://www.linkedin.com/in/shubhammishra-78a151197

