# 🪐 Planets & Moons — Data Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![JupyterLab](https://img.shields.io/badge/JupyterLab-Notebook-orange)
![Data Science](https://img.shields.io/badge/Project-Beginner%20Data%20Science-green)

## 📌 Project Overview

This is a beginner-level **Data Science and Scientific Data Analysis** project based on the public **Planets & Moons** dataset from Kaggle.

The aim is to understand how Python can be used to explore, clean, preprocess and visualize real scientific data. Because the dataset contains physical and orbital properties of planets, the project also connects a **Physics background with Data Science**.

## 🎯 Objectives

- Load and understand a scientific dataset using Python.
- Explore the structure and basic statistics.
- Check missing values and duplicate records.
- Identify possible outliers using the IQR method.
- Apply simple physics-based validation.
- Standardize numerical features.
- Create scientific visualizations.
- Save cleaned and preprocessed data.

## 🛠️ Tools & Libraries

- Python
- JupyterLab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## 🔬 Dataset

**Planets & Moons — Kaggle**

https://www.kaggle.com/datasets/joebeachcapital/planets-and-moons

The dataset contains planetary information such as mass, diameter, distance from the Sun, orbital period and other physical properties.

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Initial Exploration
   ↓
Missing Value Check
   ↓
Duplicate Check
   ↓
Outlier Detection
   ↓
Physics-Based Validation
   ↓
Data Cleaning
   ↓
Feature Standardization
   ↓
Visualization
   ↓
Processed Dataset
```

## 📊 Visualizations

### 1. Planetary Mass Comparison
Compares the masses of the planets and demonstrates their large range of values.

### 2. Planetary Diameter vs Mass
Shows the relationship between planetary size and mass.

### 3. Distance from Sun vs Orbital Period
Shows how orbital period changes with distance from the Sun, connecting the analysis with basic orbital mechanics.

## 🧹 Data Preprocessing

The project includes:

- Standardized column names.
- Missing-value checking.
- Duplicate checking.
- IQR-based outlier screening.
- Basic physical validity checks.
- Numerical feature standardization using `StandardScaler`.

> **Note:** Statistical outliers were not automatically treated as errors because extreme planetary properties can be physically meaningful.

## 📁 Project Files

```text
planets-and-moons-data-analysis/
│
├── Week_1_Planets_and_Moons_JupyterLab.ipynb
├── Week_1_Planets_and_Moons_Final_Precise_Report.docx
└── README.md
```

If permitted by the dataset license, `planets.csv` can also be included. Otherwise, download it from the Kaggle link above.

## 📈 Key Learning Outcomes

This project helped me learn the basic Data Science workflow:

**Load → Explore → Clean → Validate → Preprocess → Visualize → Save**

It also helped me understand how a **Physics background can be combined with Data Science** to analyze scientific datasets.

## 🚀 Future Scope

The dataset can be extended for:

- Correlation analysis
- Planet classification
- Regression models
- Prediction of planetary properties
- More advanced astronomical data analysis

## 👨‍💻 Author

**Yasir Arafat**  
M.Sc. Physics | Beginner Data Science Learner
