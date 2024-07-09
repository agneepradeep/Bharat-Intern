from flask import Flask, request, render_template
import joblib
import json
import pandas as pd

app = Flask(__name__, static_url_path='/static')

# Load the trained model and category mappings
model = joblib.load('model/random_forest_regressor.pkl')
with open('categorical_mappings.json', 'r') as file:
    category_mapping = json.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = None
    if request.method == 'POST':
        # Get form data
        lot_area = float(request.form['LotArea'])
        overall_qual = int(request.form['OverallQual'])
        age_of_house = float(request.form['age_of_house'])
        exter_qual = int(request.form['ExterQual'])
        first_flr_sf = float(request.form['1stFlrSF'])
        garage_cars = int(request.form['GarageCars'])
        tot_rms_abv_grd = int(request.form['TotRmsAbvGrd'])
        kitchen_qual = int(request.form['KitchenQual'])

        # Prepare the input data
        input_data = pd.DataFrame([[lot_area, overall_qual, age_of_house, exter_qual, first_flr_sf, garage_cars, tot_rms_abv_grd, kitchen_qual]],columns=['LotArea', 'OverallQual', 'age_of_house', 'ExterQual', '1stFlrSF', 'GarageCars', 'TotRmsAbvGrd', 'KitchenQual'])
        # Make prediction
        prediction = model.predict(input_data)
        prediction_text = f'Predicted House Price: ${prediction[0]:,.2f}'

    return render_template('index.html', categories=category_mapping, prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)

