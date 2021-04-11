import streamlit as st
import pymongo

try:
    conn = pymongo.MongoClient('mongodb+srv://aditya:12345@cluster0.rutst.mongodb.net/test')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = conn.Restaurent1

st.title("Current Orders")

liveorder=st.multiselect("The cuurent tables with live orders are ",db.list_collection_names())

st.title("Dishes to be made are ")

for i in liveorder:
    st.markdown("<h3>Table {} </h3>".format(i),unsafe_allow_html=True)
    collection = db[i]
    cursor = collection.find()
    for record in cursor:
        st.write("Dish name : "+str(record['Dish']) +' X ' + str(record['Quantity']))
    if st.button('Clear Final order {} '.format(i)):
        collection.delete_many({})
        st.write("Order cleared refresh to complete")

