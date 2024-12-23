from django.shortcuts import render, redirect
import joblib

MODEL_PATH = 'diagnosis/ml_models/heart_disease_model.pkl'

def predict_heart_disease(request):
    if request.method == 'POST':
        try:
            # Extract height and weight inputs
            height = request.POST.get('height')  # Get height as a string like 5'4"
            feet, inches = map(float, height.split('.'))  # Split into feet and inches
            height_in_meters = (feet * 0.3048) + (inches * 0.0254)  # Convert to meters

            weight = float(request.POST.get('weight'))  # Get weight input

            # Check the weight metric
            weight_metric = request.POST.get('weight_metric')
            if weight_metric == 'lbs':  # Convert pounds to kilograms
                weight = weight * 0.453592

            # Calculate BMI
            bmi = weight / (height_in_meters ** 2)  # BMI calculation using height in meters

            # Extract other features from the form
            features = [
                bmi,  # Calculated BMI
                int(request.POST.get('smoking')),
                int(request.POST.get('alcohol')),
                int(request.POST.get('stroke')),
                float(request.POST.get('physical_health')),
                float(request.POST.get('mental_health')),
                int(request.POST.get('diff_walking')),
                int(request.POST.get('sex')),
                int(request.POST.get('age_category')),
                int(request.POST.get('diabetic')),
                int(request.POST.get('physical_activity')),
                int(request.POST.get('gen_health')),
                float(request.POST.get('sleep_time')),
                int(request.POST.get('kidney_disease')),
            ]

            # Load the model
            model = joblib.load(MODEL_PATH)

            # Make a prediction
            prediction = model.predict([features])[0]

            # Redirect to the results page with the prediction
            return redirect(f'/diagnose/results/?prediction={prediction}')

        except Exception as e:
            # Redirect with an error message
            return redirect(f'/diagnose/results/?error={str(e)}')

    return render(request, 'prediction_form.html')


def results(request):
    # Extract query parameters
    prediction = request.GET.get('prediction')
    error = request.GET.get('error')

    # Pass them to the template
    return render(request, 'results.html', {'prediction': prediction, 'error': error})
