# Stroke Risk Analysis System
## Healthcare Data Analytics Application

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Grade](https://img.shields.io/badge/Grade-71%25-success)](https://github.com/henriettainobeme/stroke-risk-analysis)

A comprehensive data analytics application for analyzing stroke risk factors in patients using clinical data. This project was developed as part of my MSc Big Data Analytics program at Sheffield Hallam University.

## **Important Project Context**

A key requirement for this assignment was to demonstrate core Python fundamentals **without** using any high-level data libraries like Pandas, NumPy, or CSV. All data loading, parsing, and statistical calculations were built from scratch using only standard Python file I/O and custom-built modules.


##  Achievement
- **Grade**: 71% (Distinction level)
- **Feedback**: "Professional level use of programming concepts for the implementation, robust application delivered"

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technical Implementation](#technical-implementation)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Insights](#key-insights)
- [Skills Demonstrated](#skills-demonstrated)
- [Future Improvements](#future-improvements)

##  Overview

This application analyzes a dataset of 172,000 simulated patient records to identify patterns and risk factors associated with stroke occurrence. The system provides healthcare professionals with insights into how various factors like hypertension, smoking habits, and lifestyle choices correlate with stroke risk.

### Problem Statement
Cardiovascular disease is one of the leading causes of death in the UK. This application aims to help healthcare providers:
- Monitor patient vital signs and lifestyle factors
- Predict likelihood of stroke occurrence
- Make data-driven clinical decisions
- Prevent avoidable health complications

## Features

The application provides comprehensive analytics including:

1. **Demographic Analysis**
   - Average, median, and modal age calculations for various patient groups
   - Gender-based risk analysis
   - Urban vs rural residence impact

2. **Risk Factor Analysis**
   - Hypertension and stroke correlation
   - Smoking habits impact assessment
   - Heart disease relationship with stroke
   - Glucose level analysis

3. **Lifestyle Factors**
   - Sleep patterns analysis
   - Dietary habits correlation
   - Physical activity impact

4. **Statistical Analysis**
   - Descriptive statistics for all features
   - Mean, standard deviation, min/max values
   - Quartile analysis (25%, 50%, 75%)

##  Technical Implementation

### Core Modules

1. **`dataset_module.py`**
   - Loads CSV data without using high-level libraries (Pandas/NumPy)
   - Implements custom file parsing using Python file objects
   - Returns data in nested dictionary structure

2. **`query_module.py`**
   - Contains 12+ analytical functions
   - Implements custom statistical calculations
   - Exports results to CSV format
   - Object-oriented design with QueryModule class

3. **`ui_module.py`**
   - Interactive text-based user interface
   - Menu-driven system for easy navigation
   - Input validation and error handling
   - Seamless integration of all modules

### Key Programming Concepts Demonstrated
- **Object-Oriented Programming**: Class-based module design
- **File I/O**: Custom CSV parsing without external libraries
- **Data Structures**: Nested dictionaries for data management
- **Algorithm Design**: Custom implementations of statistical functions
- **Error Handling**: Robust input validation
- **Modular Programming**: Clean separation of concerns

##  Installation

### Prerequisites
- Python 3.8 or higher
- No external dependencies required (pure Python implementation)

### Setup
```bash
# Clone the repository
git clone https://github.com/henriettainobeme/stroke-risk-analysis.git

# Navigate to project directory
cd stroke-risk-analysis

# Ensure data.csv is in the same directory
# Run the application
python ui_module.py
```

## Usage

1. **Start the Application**
   ```bash
   python ui_module.py
   ```

2. **Enter Your Name**
   The system will prompt for your name for personalization

3. **Select Analysis Option**
   Choose from options A-L:
   - A: Smokers with hypertension analysis
   - B: Heart disease and stroke correlation
   - C: Gender-based hypertension analysis
   - D: Smoking habits impact
   - E: Geographic area analysis
   - F: Dietary habits correlation
   - G: Hypertension-stroke relationship
   - H: Detailed patient records
   - I: Heart disease patient details
   - J: Feature descriptive statistics
   - K: Sleep pattern analysis
   - L: Exit application

4. **View Results**
   Results are displayed on screen and can be exported to CSV

5. **Continue or Exit**
   Choose to perform another analysis or exit

##  Project Structure

```
stroke-risk-analysis/
│
├── dataset_module.py       # Data loading functionality
├── query_module.py         # Analytics and calculations
├── ui_module.py           # User interface
├── Main-python_project.ipynb  # Jupyter notebook demonstration
├── data.csv               # Dataset (172,000 records)
├── README.md              # Project documentation
└── examples/              # Sample outputs
    └── sample_results.csv # Example analysis results
```

## Key Insights

From the analysis of 172,000 patient records:

1. **Hypertension** is a significant risk factor, especially when combined with smoking
2. **Age** shows strong correlation with stroke occurrence
3. **Urban vs Rural** residence impacts stroke rates
4. **Sleep patterns** vary significantly between stroke and non-stroke patients
5. **Gender differences** exist in hypertension-related stroke risk

##  Skills Demonstrated

- **Data Analysis**: Processing and analyzing large healthcare datasets
- **Statistical Computing**: Implementing statistical measures from scratch
- **Software Engineering**: Modular design and clean code practices
- **Problem Solving**: Addressing real-world healthcare challenges
- **Documentation**: Clear code comments and user documentation
- **Testing**: Robust error handling and input validation

##  Future Improvements

Potential enhancements for this project:
- Implement machine learning models for predictive analytics
- Add data visualization using matplotlib/seaborn
- Create a web-based dashboard interface
- Integrate real-time data processing capabilities
- Add database support for larger datasets
- Implement parallel processing for performance optimization

##  Academic Context

This project was completed as Assignment 1 for the Programming Concepts and Practice module in my MSc Big Data Analytics program at Sheffield Hallam University (2024-25).

### Learning Outcomes Achieved
- Problem analysis and solution requirements elicitation
- Program development using design concepts
- Implementation using relevant programming concepts
- Professional documentation and demonstration skills

##  Contact

**Henrietta Inobeme**
- Email: henriettainobeme@gmail.com
- LinkedIn: [linkedin.com/in/henrietta-inobeme](https://linkedin.com/in/henrietta-inobeme)
- GitHub: [github.com/henriettainobeme](https://github.com/henriettainobeme)

## License

This project is available for educational purposes. Please contact me for usage permissions.

---

*Note: The dataset used in this project contains simulated patient data and is not from real patients, ensuring privacy and ethical compliance.*
