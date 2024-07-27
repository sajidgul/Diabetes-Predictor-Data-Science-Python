{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccfe68f4-b217-44e9-8542-665a784ebf68",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "import joblib\n",
    "\n",
    "# Load the trained model\n",
    "model = joblib.load('random_forest_model.pkl')\n",
    "\n",
    "# Initialize Flask app\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    data = request.get_json()\n",
    "    input_data = [\n",
    "        data['Pregnancies'], \n",
    "        data['Glucose'], \n",
    "        data['BloodPressure'], \n",
    "        data['SkinThickness'], \n",
    "        data['Insulin'], \n",
    "        data['BMI'], \n",
    "        data['DiabetesPedigreeFunction'], \n",
    "        data['Age']\n",
    "    ]\n",
    "    prediction = model.predict([input_data])\n",
    "    return jsonify({'Prediction': int(prediction[0])})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
