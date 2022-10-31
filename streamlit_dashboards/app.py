import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# make containers
header = st.container()
datasts = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Kshti ki app BaBa g de nal")
    st.text("In this projectct we'll work on kashti data")
with datasts:
    st.header("kashti doob gaye, Oh Hoye ch ch")
    st.text("In this project we'll work on 'Titanic' data")
# Importing data
    df = sns.load_dataset('titanic')
    df = df.dropna()
    st.write(df.head(10))
    st.subheader("kitny Admi thy?")
    st.bar_chart(df['sex'].value_counts())

#Other plot
    st.subheader("Class ke hisab se farq")
    st.bar_chart(df['class'].value_counts())
    st.subheader("khichri paki pai kuch samjh ni aa rai")
    st.bar_chart(df['age'])
    st.subheader("ye thik hai.")
    st.bar_chart(df['age'].sample(10))


with features:
    st.header("These are our app features")
    st.text("Me ne itney features add kr dene hain ap dekhtey reh jana hai.")
    st.markdown("**Feature 1:**abhi nhi pta")
    st.markdown("**Feature 2:**kaha na bhi nhi pta")
    st.markdown("**Feature 1:**baad me likhu ga abhi time km hai")


with model_training:
    st.header("Kashti walo ka kia bana?-Model training")
    st.text("In this projecct we'll change our parameters.")
# Making columns
    input, display = st.columns(2)

    # pehly column me ap k selection point ho
    max_depth = input.slider("Kiny bandiyan nu janda tu?", min_value=10, max_value=100, value=20, step=5)

# n_estimators
n_estimators = input.selectbox("How many trees should be in random forest?", [ 50, 100, 200, 300,'No limit'])

#adding list of features
input.write(df.columns)

# input features from user

input_features = input.text_input('Which feature we should use?')

# Machine learning Model
model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

# Define x and y
x= df[[input_features]]
y= df[['fare']]

# fit a model
model.fit(x,y)
prediction = model.predict(y)

# Display Metrics

display.subheader("Mean absolute error of the model is:")
display.write(mean_absolute_error(y, prediction))
display.subheader("Mean squared error of the model is:")
display.write(mean_squared_error(y, prediction))
display.subheader("r squared error of the model is:")
display.write(r2_score(y, prediction))