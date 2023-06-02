from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# from pymongo import MongoClient
import math


def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")


# Client = MongoClient('mongodb+srv://sohamjadhav0130:finalyearproject@obesitydetection.eojavmg.mongodb.net/?retryWrites=true&w=majority')
# db = Client.get_database('test')

def result(request):
    data = pd.read_csv(
        r"C:\Users\Alfija Sayyad\Desktop\Prediction\prediction\prediction\Survey.csv")
    print(data.head())
    print("CSV file loaded successfully")

    # Add a new column to the data DataFrame that contains the addiction level based on the time thresholds
    def categorize_addiction_level(row):

        total_time = int(row['hours_online_games']) + int(
            row['hours_social_media'])

        if total_time >= 8 :
            return 'Highly addicted'
        elif total_time >= 4 and total_time < 8:
            return 'Moderately addicted'
        else:
            return 'Less addicted'

    data['addiction_level'] = data.apply(categorize_addiction_level, axis=1)

    x = data[["hours_online_games", "hours_social_media"]]

    y = data['addiction_level']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

    # Train a logistic regression model
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)

    val1 = int(request.GET['n1'])
    val2 = int(request.GET['n2'])
    val3 = str(request.GET['n3'])
    val4 = int(request.GET['n4'])
    val5 = int(request.GET['n5'])
    val6 = str(request.GET['n6'])
    val7 = int(request.GET['n7'])
    val8 = str(request.GET['n8'])
    val9 = str(request.GET['n9'])
    val10 = int(request.GET['n10'])

    new_data = pd.DataFrame({
        "hours_online_games": [val7],
        "hours_social_media": [val10],
    })

    pred = model.predict(new_data)

    # Categorize the predicted addiction level into one of the three levels
    if pred == 'Highly addicted':
        result1 = "Highly Addicted"
        template_name = 'highaddicted1.html'
    elif pred == 'Moderately addicted':
        result1 = "Moderately Addicted"
        template_name = 'moderate_addiction.html'
    else:
        result1 = "Less Addicted"
        template_name = 'low_addiction.html'

    print(result1)
    # Render the result template with the predicted addiction level
    return render(request, template_name, {"result2": result1})

import pandas as pd