# Rising Waters: Flood Prediction System 🌊

Rising Waters is a Machine Learning-powered web application that analyzes meteorological data to predict the likelihood of flood events. By examining factors such as annual rainfall, seasonal precipitation patterns, humidity, and cloud cover, the system provides authorities and residents with early warnings to aid in disaster response and evacuation planning.

## 🚀 Features

- **Machine Learning Models**: Trained and evaluated multiple classification algorithms (Decision Tree, Random Forest, K-Nearest Neighbors, XGBoost) on historical weather data to determine the most accurate model for flood prediction.
- **Dynamic Frontend UI**: A premium, "glassmorphism" styled web interface built with HTML, CSS, and JS that is fully responsive and interactive.
- **Instant Weather Analysis**: Input live or historical meteorological data to instantly receive a Flood Probability Score.
- **Smart Data Auto-Fill**: A dynamic test-data generator that automatically populates the form with realistic boundaries to demonstrate functionality instantly.
- **Contextual Insights**: The model doesn't just output a percentage; it provides dynamic, human-readable insights explaining *why* the prediction was made (e.g., "Excessive annual precipitation detected") and recommends actionable protocols based on severity.

## 🛠️ Technologies Used

- **Backend / Web Framework**: Python 3, Flask
- **Machine Learning**: Scikit-Learn, XGBoost, Pandas, NumPy
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism design), JavaScript
- **Model Serialization**: Joblib

## ⚙️ Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/raising-waters.git
cd raising-waters
```

**2. Install dependencies**
Ensure you have Python 3.8+ installed, then install the required Python packages:
```bash
pip install -r requirements.txt
# Note: If requirements.txt is missing, run:
# pip install pandas scikit-learn xgboost flask joblib
```

**3. Train the Model (Optional)**
If you want to re-train the models on the dataset or if the saved `.joblib` files are missing, run the training script:
```bash
python train.py
```
This will process `data/flood_prediction.csv`, evaluate multiple models, and save the best performer (along with the data scaler) into the `models/` directory.

**4. Run the Application**
Start the Flask development server:
```bash
python app.py
```

**5. Access the Web App**
Open your web browser and navigate to:
`http://127.0.0.1:5000`

## 🧪 Usage Instructions

1. Upon opening the application, you will see a beautifully designed weather parameter input grid.
2. You can manually enter data for fields like Temperature, Humidity, Annual Rainfall, etc.
3. Alternatively, click the **Auto Fill** button at the top to dynamically generate a realistic, randomized dataset for testing.
4. Click **Analyze Flood Risk** to view the results. 
5. The system will display the Flood Probability, a Severity Classification (Severe, Elevated, or Normal), and dynamic insights explaining the reasoning behind the prediction.

## 📝 Disclaimer
This prediction application is generated using a machine learning model trained on historical weather data and is intended for educational and demonstrative purposes only. It should not replace official meteorological and governmental weather advisory systems.
