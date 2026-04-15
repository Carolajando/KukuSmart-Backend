\#  KukuSmart — AI-Based Advisory System for Smallholder Poultry Farmers



> Empowering smallholder poultry farmers in East Africa with real-time AI-powered disease diagnosis and agricultural guidance.



\---



\## Problem Statement



Poultry farming is one of the most accessible livestock activities for smallholder farmers in sub-Saharan Africa, yet it remains highly vulnerable to preventable losses caused by disease, poor management practices, and delayed treatment. Many small-scale farmers in Kenya and across East Africa lack timely access to veterinary services, disease diagnosis expertise, and structured agricultural education — leading to high mortality rates and financial loss.



KukuSmart bridges this gap by providing an affordable, always-available, and easy-to-use digital tool that delivers real-time poultry health guidance tailored to the East African context.



\---



\## What KukuSmart Does



\- ?? \*\*Image-based disease detection\*\* — Upload a photo of your chicken and get an instant AI diagnosis

\- ?? \*\*AI Chatbot\*\* — Ask questions about symptoms, treatment, and vaccination schedules in English or Swahili

\- ?? \*\*Treatment Guidance\*\* — Receive simple, actionable recommendations based on the diagnosis

\- ?? \*\*Built for East Africa\*\* — Designed with smallholder farmers in Kenya and the wider East African region in mind



\---



\## ??? Project Structure



```

KukuSmart/

+-- KukuSmart-Backend/        # FastAPI backend + ML model

¦   +-- main.py               # API entry point

¦   +-- class\\\_labels.json     # Disease classification labels

¦   +-- Requirementst.txt     # Python dependencies

¦   +-- .gitignore

¦

+-- KukuSmart-Frontend/       # Frontend interface (coming soon)

```



\---



\## ??? Tech Stack



| Layer | Technology |

|---|---|

| Backend | FastAPI (Python) |

| ML Model | Convolutional Neural Network (CNN) |

| Image Dataset | Chicken Health Images — Kaggle |

| AI Chatbot | LLM via API (e.g. OpenAI / open-source transformer) |

| Frontend | Coming soon |



\---



\## ?? Dataset



\*\*A. Image Classification\*\*

The Chicken Health Images dataset from Kaggle contains labeled images of healthy and diseased chickens, used to train and evaluate a computer vision model for disease classification.



\*\*B. Language Model\*\*

The system integrates a Large Language Model (LLM) through an API or local deployment to retrieve, summarize, and generate poultry health recommendations based on user queries.



\---



\## ?? Approach



1\. \*\*Data Preprocessing\*\* — Images are cleaned, resized, normalized, and split into training, validation, and test sets. Augmentation is applied to improve model performance.

2\. \*\*Model Training\*\* — A CNN model is trained to classify poultry diseases from images.

3\. \*\*Chatbot Integration\*\* — An AI chatbot handles farmer questions about symptoms, treatment, and vaccination.

4\. \*\*User Flow\*\* — Farmer uploads image ? receives disease prediction ? gets treatment guidance in English or Swahili.

5\. \*\*User Testing\*\*



\---



\## ?? Getting Started (Backend)



\### Prerequisites

\- Python 3.8+

\- pip



\### Installation



```bash

git clone https://github.com/Carolajando/KukuSmart-Backend.git

cd KukuSmart-Backend

pip install -r Requirementst.txt

```



\### Run the API



```bash

uvicorn main:app --reload

```



The API will be available at `http://localhost:8000`



\---



\## ?? Expected Outcomes



\- ? A working prototype of an AI-based poultry advisory system

\- ? A trained disease classification model

\- ? A chatbot providing simple poultry health advice

\- ? Demonstrated reduction in poultry mortality through accessible, smartphone-based veterinary guidance



\---





\## ?? License



This project is licensed under the MIT License — see the \[LICENSE](LICENSE) file for details.

