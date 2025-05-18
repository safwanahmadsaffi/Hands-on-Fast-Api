# FastAPI Iris Species Prediction

This project is a simple web application and API for predicting the species of an Iris flower based on its sepal and petal dimensions. It uses a pre-trained scikit-learn model served with FastAPI.






FAST_API_ML_MODEL/
├── ML_Model/
│ └── iris_model.joblib
├── static/
│ └── css/
│ └── styles.css
├── templates/
│ └── index.html
├── main.py
└── README.md


## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Anaconda (optional but recommended for creating virtual environments)

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/jitender-insights/FAST_API_ML_MODEL.git
   cd FAST_API_ML_MODEL

2. **Create a virtual environment**

   
   Using Anaconda
   
   conda create -n iris_env python=3.8
   
   conda activate iris_env

   or using 'venv'
   python -m venv venv
   
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

4. **Install dependencies**
   pip install -r requirements.txt

5.  **Run the Application**
   uvicorn main:app --reload

   Open your browser and go to http://127.0.0.1:8000 to see the web form.

   The API documentation and Swagger UI are available at http://127.0.0.1:8000/docs

   

   


