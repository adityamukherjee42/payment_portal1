import pymongo
import streamlit as st


st.title("Feedback Form")
try:
    conn = pymongo.MongoClient('mongodb+srv://aditya:12345@cluster0.rutst.mongodb.net/test')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = conn.Restaurent1
collection=db['Feedback']

tableno = st.text_input("Enter Table Number","1")
feedback = st.text_area("Enter your valuebale  Feedback"," ")
result=[]
result.append(
                {
                    'Table no ': tableno,
                    'Feedback': feedback
                }
            )
if st.button("Done"):
    collection.insert_many(result)
    st.markdown("<h3>Thank you , Hope you had a good experience</h3>")
