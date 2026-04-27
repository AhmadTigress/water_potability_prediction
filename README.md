# Water Potability Prediction Project

**Access** to safe drinking water is a fundamental requirement for public health and a major factor in preventing waterborne diseases. This project implements a professional machine learning pipeline to analyze water quality parameters and predict whether a water source is potable (safe to drink) or non potable.

## Project Overview

The core objective of this system is to automate the diagnostic process of water quality assessment. By utilizing chemical properties and physical measurements, the system provides a rapid classification tool that can support environmental health decision making.

## Water Quality Parameters

The model evaluates nine critical factors found in the dataset to determine safety:

**ph**: The acid base balance of the water. Most potable water falls between 6.5 and 8.5.

**Hardness**: The concentration of calcium and magnesium salts, which affects how water interacts with pipes and soap.

**Solids**: The total dissolved solids (TDS) indicating the mineral content in the water.

**Chloramines**: The concentration of chlorine and ammonia used for disinfection.

**Sulfate**: Naturally occurring minerals; high levels can affect the taste and safety of the water.

**Conductivity**: A measure of the ability of water to pass an electrical current, indicating the presence of dissolved salts.

**Organic Carbon**: The total amount of carbon found in organic compounds, often used as a measure of water purity.

**Trihalomethanes**: Chemicals that can result from water treatment processes.

    
**Turbidity**: The measure of light scattering properties of the water, which indicates the presence of suspended particles.

## Detailed Project Structure

The repository is organized following MLOps best practices to ensure that data, code, and model versions are strictly managed.

```txt
mlops-water-potability/
├── .dvc/                   # DVC configuration and cache (Internal)
├── .github/                # GitHub Actions for CI/CD (Optional)
├── data/                   # Data directory (Ignored by Git, tracked by DVC)
│   ├── raw/                # Original, immutable data (train.csv, test.csv)
│   └── processed/          # Data after cleaning/feature engineering
├── models/                 # Saved model artifacts (.pkl files)
├── reports/                # Metrics and plots (metrics.json)
├── src/                    # Source code directory
│   ├── __init__.py         # Makes 'src' a Python package
│   ├── data/               # Scripts related to data handling
│   │   ├── __init__.py
│   │   ├── data_collection.py
│   │   └── data_prep.py
│   └── model/              # Scripts related to ML logic
│       ├── __init__.py
│       ├── model_building.py
│       └── model_eval.py
├── .gitignore              # Tells Git what to ignore (data, .venv, models)
├── dvc.lock                # DVC state file (Crucial: Keep in Git)
├── dvc.yaml                # DVC pipeline definition
├── params.yaml             # Hyperparameters and configurations
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and instructions
```

## Installation and Setup

This project is optimized for Ubuntu. To ensure a clean environment, follow these steps:

    - Create a virtual environment to isolate the project dependencies:
```bash
    python3 -m venv .venv
```

    - Activate the virtual environment:
```bash
    source .venv/bin/activate
```

    - Install the required libraries (Pandas, Scikit Learn, FastAPI, and DVC):
```bash
    pip install -r requirements.txt
```

## Running the Pipeline

This project uses Data Version Control (DVC) to automate the workflow. Instead of running each script manually, you can execute the entire pipeline with a single command:

```bash
dvc repro
```

This command checks which parts of your code or data have changed and only runs the necessary steps to update your model and metrics.
Prediction Service

The project includes a web service that allows you to interact with the model through an API.

    Launch the service:
```bash
    uvicorn src.main:app --host 0.0.0.0 --port $PORT
```

    Access the documentation:
    Once the server is running, you can visit http://127.0.0.1:8000/docs in your browser to see the interactive API dashboard.

**Submit a test**:
    Use the test script to send a sample of water data to the server:
```bash
    python3 src/test.py
```

## Model Evaluation

The model's performance is measured using several medical and statistical benchmarks:

**Accuracy**: Overall correctness of the model.

**Precision**: The ability to avoid false positives (labeling unsafe water as safe).

**Recall**: The ability to identify all truly potable water sources.

**F1 Score**: The balance between precision and recall.

These values are updated automatically in the metrics.json file every time the model is retrained.

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software for educational or professional purposes. See the **LICENSE** file for more details.