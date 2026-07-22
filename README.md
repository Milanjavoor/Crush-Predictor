# ❤️ Crush Compatibility Predictor (Machine Learning)

## Overview

Crush Compatibility Predictor is a fun machine learning desktop application built with Python and Tkinter. The application predicts a compatibility score between two people based on three simple factors:

* Common Interests
* Daily Chats
* Personality Match

The prediction is made using a **Random Forest Regressor** trained on a synthetic dataset created specifically for learning machine learning concepts. The project is intended for educational purposes and entertainment only—it does **not** measure real human emotions or relationships.

---

## Features

* ❤️ Predicts a compatibility score from 0–100%
* 🤖 Machine Learning model using Random Forest Regression
* 📊 Synthetic dataset generation
* 💾 Trained model saved using Joblib
* 🖥️ Simple and interactive Tkinter GUI
* 🎨 Purple and black themed interface
* ⚠️ Input validation and error handling
* 💬 Fun compatibility messages based on prediction

---

## Technologies Used

* Python 3
* Tkinter
* Pandas
* NumPy
* Scikit-learn
* Joblib

---

## Machine Learning Workflow

1. Generate a synthetic dataset.
2. Store the dataset as a CSV file.
3. Load the dataset using Pandas.
4. Split the data into training and testing sets.
5. Train a Random Forest Regression model.
6. Evaluate the model using the R² score.
7. Save the trained model using Joblib.
8. Load the model inside the Tkinter application.
9. Predict compatibility based on user inputs.

---

## Project Structure

```text
Crush Compatibility Predictor/
│
├── dataset_generator.py
├── dataset.csv
├── train_model.py
├── compatibility_model.pkl
├── app.py
└── README.md
```

---

## Input Parameters

The application accepts the following inputs:

* Common Interests (0–10)
* Daily Chats
* Personality Match (0–100)

These values are passed to the trained machine learning model to predict the compatibility percentage.

---

## Example

**Input**

* Common Interests: 8
* Daily Chats: 10
* Personality Match: 85

**Output**

```
Compatibility: 88%

❤️ Perfect Match!
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project folder:

```bash
cd Crush-Compatibility-Predictor
```

Install the required libraries:

```bash
pip install pandas numpy scikit-learn joblib
```

Generate the dataset:

```bash
python dataset_generator.py
```

Train the machine learning model:

```bash
python train_model.py
```

Run the application:

```bash
python app.py
```

---

## Learning Outcomes

This project demonstrates the complete workflow of a classical machine learning application, including:

* Dataset creation
* Data preprocessing
* Feature selection
* Model training
* Model evaluation
* Model serialization
* Desktop GUI development
* Machine learning deployment using Tkinter

---

## Future Improvements

* Improved GUI with animations
* Feature importance visualization
* Dark/Light mode
* Web version using Flask or FastAPI
* User authentication
* Better compatibility algorithms
* Data visualization charts
* Multiple machine learning model comparison

---

---

## License

This project is licensed under the MIT License.

---

## Author

**Milan Javoor**

If you found this project useful, consider giving the repository a ⭐ on GitHub!

