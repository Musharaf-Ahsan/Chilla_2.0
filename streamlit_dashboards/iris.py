from gettext import install
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from PIL import Image


#st.title("Easy Iris Flower Prediction App")

html_temp = """
    <div style="background-color:black;padding:10px">
    <h2 style="color:red;text-align:center;">Easy Iris Flower Prediction App</h2>
    <h2 style="color:red;text-align:center;">BaBa g sb sikhatey hai, Bs Chilla join kro </h2>
    <p style="color:red;text-align:center;" >This is a <b>Streamlit</b> app use for prediction of the <b>Iris flower</b> type.</p>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

#st.write("""This is a **Streamlit** app use for prediction of the **Iris flower** type.""")

# image = Image.open('iris-image.png')

# st.image(image, use_column_width=True,format='PNG')

def user_input_features():
    sepal_length = st.slider('Sepal length', 4.3, 7.9, 4.5)
    sepal_width = st.slider('Sepal width', 2.0, 4.4, 4.3)
    petal_length = st.slider('Petal length', 1.0, 6.9, 3.1)
    petal_width = st.slider('Petal width', 0.1, 2.5, 2.0)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

st.subheader('Enter Input Through Slider')
df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Prediction Probability')
st.write('**Setosa**:',prediction_proba[0][0])
st.write('**Versicolor**:',prediction_proba[0][1])
st.write('**Virginica**:',prediction_proba[0][2])

st.subheader('Final Prediction')
st.error(iris.target_names[prediction][0])

html_temp1 = """
    <div style="background-color:#f63366">
    <p style="color:green;text-align:center;" >Edited By: <b>Musharaf Ahsan</b> </p>
    </div>
    """
st.markdown(html_temp1,unsafe_allow_html=True)