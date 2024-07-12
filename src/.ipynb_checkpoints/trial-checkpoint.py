import numpy as np
import pandas as pd
import gradio as gr
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('https://raw.githubusercontent.com/EdemGold/gradio_project/main/diabetes.csv')
data.head()
print (data.columns)

x = data.drop(['Outcome'], axis=1)

y = data['Outcome']
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y)
from sklearn.preprocessing import StandardScaler

#instantiate StandardScaler object
scaler = StandardScaler()

#scale data
x_train_scaled = scaler.fit_transform(x_train)

x_test_scaled = scaler.fit_transform(x_test)
#import model object
from sklearn.neural_network import MLPClassifier
model =  MLPClassifier(max_iter=1000,  alpha=1)

#train model on training data
model.fit(x_train_scaled, y_train)

#getting model performance on test data
print("accuracy:", model.score(x_test_scaled, y_test))
#geting our columns

print(data.columns)
def diabetes(Pregnancies, Glucose, Blood_Pressure, SkinThickness, Insulin, BMI, Diabetes_Pedigree, Age):
#turning the arguments into a numpy array  
    x = np.array([Pregnancies,Glucose,Blood_Pressure,SkinThickness,Insulin,BMI,Diabetes_Pedigree,Age])
    prediction = model.predict(x.reshape(1, -1))
    return prediction
outputs = gr.outputs.Textbox()

app = gr.Interface(fn=diabetes, inputs=['number','number','number','number','number','number','number','number'], outputs=outputs,description="This is a diabetes model")
app.launch()