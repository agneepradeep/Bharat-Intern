# House Price Prediction

## Overview

The House Price Prediction model utilizes machine learning techniques to estimate the sale prices of houses based on various features. It aims to provide accurate predictions that can assist homeowners, real estate professionals, and investors in making informed decisions.

## Model Architecture

The model employs RandomForestRegressor from scikit-learn, an ensemble learning method consisting of multiple decision trees. Each tree is trained on a random subset of the data to predict house prices based on input features.

## Data Preprocessing

### Data Cleaning

- Handled missing values in numerical and categorical features.
- Addressed outliers that could impact model performance.

### Feature Engineering

- Created new features such as the age of the house derived from the year built and remodel year.
- Converted categorical variables into numerical representations using label encoding.

### Normalization/Scaling

- Applied Min-Max scaling to numerical features to normalize their ranges.
- Ensured categorical features were appropriately encoded for model compatibility.

## Model Training

### Training Algorithm

- Trained using RandomForestRegressor for its ability to capture complex relationships in data.

### Hyperparameters Used

- `n_estimators`: Number of trees in the forest.
- `max_depth`: Maximum depth of each tree to control overfitting.
- Tuned other parameters like `min_samples_split` and `min_samples_leaf` through cross-validation.

### Training/Validation Split

- Split data into training and validation sets (80% training, 20% validation) using `train_test_split` from scikit-learn.

### Training Metrics

- Evaluated model performance using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared (R2) score.

## Model Evaluation

### Evaluation Metrics Used

- MAE, MSE, RMSE: Measures of prediction accuracy.
- R2 Score: Indicates the proportion of variance explained by the model.

### Test Dataset Used

- Assessed model generalization using a separate test dataset not included in training/validation.

### Results and Analysis

- Achieved an MAE of $20,907.07, MSE of $1.05e+09, RMSE of $32,460.37, and R2 score of 0.843045 on the test set.
- Analyzed feature importances to understand key predictors of house prices.

## Model Deployment

### Deployment Process

- Deployed the model as a Flask application, providing REST API endpoints for predictions.
- Hosted on a cloud platform (e.g., Github) for accessibility.

### Testing After Deployment

- Conducted integration tests to ensure API endpoints functioned correctly.
- Monitored performance post-deployment to address any operational issues.

## Conclusion

The House Price Prediction model demonstrates robust performance in estimating house prices based on provided features. Insights gained include the importance of features such as overall quality, lot area, and number of rooms in determining house values.

## References

- [Housing Prices Competition for Kaggle Learn Users](https://www.kaggle.com/competitions/home-data-for-ml-course/data)
- Scikit-learn Documentation
- Flask Documentation

## Appendix

### Additional Information
- Data preprocessing scripts.
- Sample API requests and responses.

### Dependencies
- Python 3.8+
- Flask
- Pandas
- Numpy
- Joblib
- Requests
- Scikit-learn

### Installation:
```
pip install flask pandas numpy scikit-learn joblib requests
```
### How to Run:

To run the House Price Prediction website locally on your machine, follow these steps:

1. **Clone the Repository:**
   ```
   git clone https://github.com/agneepradeep/Bharat-Intern.git
   ```
   
2. **Navigate to the Project Directory:**
   ```
   cd Bharat-Intern
   ```

3. **Set up virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```
4. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Run the Flask Application:**
   ```
   python app.py
   ```

6. **Access the Website:**
   Open a web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

7. **Use the Website:**
   Enter house features, submit the form, and view the predicted house price.
