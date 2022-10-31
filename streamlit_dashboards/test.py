import streamlit as st
import seaborn as sns

st.header("I'm learning Streamlit with Baba_Aammar in Python ka chilla")
st.text(" streamlit is amaizinng Maza aa rha hai Boss.")
st.header("Minu v nhi pta ki likhna.")
st.header("-----------------------------------------------------")

st.header("Iris Dataset")
Phool = sns.load_dataset("iris")
st.write(Phool.head(5))

st.header(" Select Some Columns from Iris")
st.write(Phool[["species","sepal_length", "sepal_width"]].head(5))
st.header("BarChart")
st.text("Bar Chart sirf continous value ka bnta hai.")
st.bar_chart(Phool["sepal_length"   ])

st.header("LineChart")
st.line_chart(Phool["sepal_length"   ])



