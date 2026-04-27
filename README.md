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