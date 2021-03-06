from django.http import HttpResponseRedirect, Http404
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html')

def prediction(request, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q):
    new_input = [[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q]]
    data_path = 'heart_2020_cleaned.csv'
    healthData = pd.read_csv(data_path)

    #healthData.drop('HeartDisease')
    healthData['AgeCategory'] = healthData['AgeCategory'].replace({'18-24':0,'25-29':1,'30-34':2,'35-39':3,'40-44':4,'45-49':5,'50-54':6,'55-59':7,'60-64':8,'65-69':9,'70-74':10,'75-79':11,'80 or older':12})
    healthData['Race'] = healthData['Race'].replace({'White':0, 'Black':1, 'Hispanic':2,'Other':3,'Asian':4,'American Indian/Alaskan Native':5})
    healthData['Smoking'] = healthData['Smoking'].replace({'No':0, 'Yes':1})
    healthData['AlcoholDrinking'] = healthData['AlcoholDrinking'].replace({'No':0, 'Yes':1})
    healthData['Stroke'] = healthData['Stroke'].replace({'No':0, 'Yes':1})
    healthData['DiffWalking'] = healthData['DiffWalking'].replace({'No':0, 'Yes':1})
    healthData['Sex'] = healthData['Sex'].replace({'Male':0, 'Female':1})
    healthData['PhysicalActivity'] = healthData['PhysicalActivity'].replace({'No':0, 'Yes':1})
    healthData['GenHealth'] = healthData['GenHealth'].replace({'Poor':0, 'Fair':1, 'Good': 2, 'Very good': 3, 'Excellent': 4})
    healthData['Asthma'] = healthData['Asthma'].replace({'No':0, 'Yes':1})
    healthData['KidneyDisease'] = healthData['KidneyDisease'].replace({'No':0, 'Yes':1})
    healthData['SkinCancer'] = healthData['SkinCancer'].replace({'No':0, 'Yes':1})
    healthData['Diabetic'] = healthData['Diabetic'].replace({'No':0, 'No, borderline diabetes': 1, 'Yes (during pregnancy)':2, 'Yes':3})
    healthData['HeartDisease'] = healthData['HeartDisease'].replace({'No':0, 'Yes': 1})
    feature_cols = ['BMI','Smoking', 'AlcoholDrinking', 'Stroke','PhysicalHealth', 'MentalHealth', 'DiffWalking',  'Sex','AgeCategory', 'Race', 'Diabetic', 'PhysicalActivity', 'GenHealth', 'SleepTime', 'Asthma', 'KidneyDisease', 'SkinCancer']
    X = healthData.loc[:, feature_cols]
    y = healthData.HeartDisease
    model = LogisticRegression(max_iter=10000)
    # fit model
    X_train , X_test, y_train, y_test = train_test_split(X,y,test_size=0.9,random_state=0)
    model.fit(X_train, y_train)
    result = ""
    new_output = model.predict(new_input)
    # summarize input and output
    if(new_output == 1):
        result = "According to our data, you ARE likely to get heart disease."
    else:
        result = "According to our data, you ARE NOT likely to get heart disease."
    context = {
        'result': result
    }
    #print(result)
    #print(model.score(X_test, y_test))
    print(result)
    return render(request, 'prediction.html', context)
