import pickle
import streamlit as st
from os import path
import numpy as np

st.title("Flower Classification App")

filename="lr_model.pkl"
with open(path.join(filename),'rb') as f:
    lr_model = pickle.load(f)
    
sl = st.number_input("Insert a sepal length")
sw = st.number_input("Insert a sepal width") 
pl = st.number_input("Insert a petal length") 
pw = st.number_input("Insert a petal width") 


if st.button("Predict"):
    pred = lr_model.predict(np.array([[sl,sw,pl,pw]]))
    st.write("The Flower is :",pred[0])
