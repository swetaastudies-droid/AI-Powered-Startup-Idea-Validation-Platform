# 🚀 AI-Powered Startup Idea Validation Platform – IronHub

An AI-assisted startup validation platform developed to evaluate the feasibility of **IronHub**, a Chennai-based doorstep ironing and garment care service.

The platform combines **market analysis, customer research, competitor analysis, financial feasibility, machine learning, and an interactive Streamlit dashboard** to provide a structured assessment of a startup idea before full-scale implementation.

---

## 📌 Project Overview

Starting a business involves uncertainty around market demand, customer acceptance, competition, pricing, and financial sustainability.

This project develops a structured validation framework that evaluates a startup idea across four major dimensions:

1. 📊 Market Size & Growth
2. 👥 Customer Demand
3. 🏆 Competition
4. 💰 Financial Feasibility

The framework was applied to **IronHub**, a proposed Chennai-based doorstep ironing service.

The project also includes a prototype **AI Startup Idea Validator** built using Python and Streamlit.

---

## 🎯 Project Objective

The primary objective is:

> **To validate the market demand, customer acceptance, competitive position, and financial feasibility of IronHub using a structured AI-assisted startup validation framework before full-scale implementation.**

The project focuses on converting startup assumptions into measurable indicators and identifying areas that require further validation.

---

# 🧩 Startup Being Validated – IronHub

**IronHub** is a proposed Chennai-based doorstep ironing and garment care service.

### Core Service

IronHub aims to provide:

- Doorstep pickup and delivery
- Ironing of office formals
- School and college uniforms
- Sarees
- Blazers
- General garments
- Online service booking
- Same-day / fast turnaround service

The proposed service model focuses on convenience, transparent pricing, localized operations, and doorstep delivery.

---

# 🔍 Validation Framework

The startup is evaluated through four major validation dimensions.

## 1. 📊 Market Size & Growth

Market research was conducted using:

- Industry market reports
- Google Trends
- TAM–SAM–SOM analysis
- Python-based visualization

The analysis helps understand the broader market opportunity and the potential market base relevant to IronHub.

---

## 2. 👥 Customer Demand

A customer survey was conducted to understand:

- Current ironing habits
- Frequency of ironing usage
- Existing service providers
- Monthly spending
- Customer difficulties
- Interest in doorstep pickup and delivery
- Interest in fast turnaround
- Price preferences
- Likelihood of trying IronHub

### Survey Size

**25 respondents**

The results indicate positive stated interest in doorstep ironing services.

However, the survey sample is limited and therefore the results should be interpreted as **initial validation evidence rather than proof of actual market demand**.

---

## 3. 🏆 Competition Analysis

Competitor research was conducted using publicly available information from ironing and laundry service providers.

The analysis considered:

- Service offerings
- Pricing
- Pickup and delivery
- Turnaround time
- Online booking
- Service areas
- Competitive positioning

Competitor information was collected and organized using Python, Excel, Requests, and BeautifulSoup.

### Competitors Analyzed

- LaundryBus
- Presso
- Wash & Dry
- The Salavai Laundry
- Elite Cleaners
- Madras Ironing Company

Where a competitor's website did not specify a particular feature, it was recorded as **"Not specified"** rather than assuming that the feature was unavailable.

---

# 💰 Financial Feasibility Analysis

The project evaluates the financial assumptions of IronHub using:

- Revenue analysis
- Unit economics
- Sensitivity analysis
- Capital requirement analysis
- ROI
- NPV

### Key Financial Assumptions

The proposed business model includes:

- Average Order Value: ₹100
- IronHub commission: 35%
- Proposed daily orders: 120
- Proposed monthly orders: 3,600
- Proposed initial capital: ₹15 lakh

The analysis also evaluates lower and higher order-volume scenarios to understand how changes in demand can affect profitability.

### Important Note

Financial results in the platform are **projections based on assumptions** and should not be interpreted as actual realized business results.

---

# 📈 TAM – SAM – SOM Analysis

The project includes a structured TAM–SAM–SOM analysis.

### TAM

The Total Addressable Market uses the broader **India laundry service market** as the market reference.

### SAM

The Serviceable Available Market uses the **Chennai household base** as the geographic market base.

### SOM

The Serviceable Obtainable Market is represented using IronHub's proposed operating assumptions, including:

- Daily order capacity
- Monthly order volume
- Annual order volume
- Average order value
- Commission revenue

The SOM represents a **proposed business scenario**, not a validated market share.

---

# 🤖 Machine Learning

A **Random Forest Classifier** was developed as a prototype machine-learning component.

### Input Features

The model uses:

- Market Size
- Customer Interest
- Competition Level
- Profit Margin

### Validation Labels

The demonstration dataset contains validation categories such as:

- High
- Medium
- Low

The model generates a startup validation prediction based on the supplied input scores.

### Important Limitation

The Random Forest model uses a **demonstration dataset** created for the academic prototype.

Therefore, model predictions should **not be interpreted as statistically validated proof of startup success**.

The machine-learning component demonstrates how startup validation can be incorporated into a data-driven decision-support system.

---

# 🖥️ Streamlit Application

The project includes an interactive Streamlit dashboard called:

## AI Startup Idea Validator

The application provides three major modules.

### 🎯 1. Idea Validation

Users can enter:

- Startup idea
- Market size score
- Customer interest score
- Competition level
- Profit margin score

The application provides a structured validation result.

---

### 💰 2. Financial Projection

Users can enter:

- Initial investment
- Projection period
- Annual net cash flow
- Discount rate

The application calculates:

- Net Present Value (NPV)
- Annual ROI
- Projected cash flows

The tool also indicates whether the selected assumptions result in a positive or negative NPV.

---

### 🤖 3. Idea Feedback Assistant

The feedback assistant allows users to enter a startup idea and receive structured feedback based on:

- Market Size
- Customer Demand
- Competition
- Financial Feasibility

Example:

**IronHub – Doorstep Ironing and Garment Care Service**

The assistant then provides a structured validation-oriented assessment.

---

# 🧪 Testing & Improvement

The platform was tested using multiple startup scenarios and validation inputs.

Testing focused on:

- Validation score generation
- Financial calculations
- NPV calculation
- ROI calculation
- Machine-learning predictions
- Idea feedback generation
- Dashboard usability

The testing process helped identify areas where assumptions require stronger evidence and where the platform can be improved.

---

# 📂 Project Structure

```text
AI-Powered-Startup-Idea-Validation-Platform/
│
├── app_step7.py
│
├── random_forest_validation.py
├── startup_validation_dataset.csv
│
├── tam_sam_som_analysis.py
├── IronHub_TAM_Bar_Chart.png
├── IronHub_SAM_Bar_Chart.png
├── IronHub_SOM_Bar_Chart.png
├── IronHub_TAM_SAM_SOM_Summary.csv
│
├── competitor_scraper.py
├── elitecleaners_scraped_data.xlsx
├── laundrybus_complete_scraped_data.xlsx
├── madras_ironing_scraped_data.xlsx
├── salavai_scraped_data.xlsx
├── washanddry_scraped_data.xlsx
│
├── IronHub_Random_Forest_Confusion_Matrix.png
├── IronHub_Random_Forest_Feature_Importance.png
│
├── screenshots/
│   ├── idea_validation.png
│   ├── financial_projection.png
│   └── idea_feedback_assistant.png
│
├── requirements.txt
└── README.md
