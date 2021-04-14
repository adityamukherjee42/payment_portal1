import streamlit as st
from bokeh.models.widgets import Div
import pandas as pd
from PIL import Image
import SessionState
import pymongo
from instamojo_wrapper import Instamojo
API_KEY = "test_2f83fb338bea7ea58020bb8b50f"

AUTH_TOKEN = "test_5d2e8cf45646124ef084e81ad36"

api = Instamojo(api_key="test_2f83fb338bea7ea58020bb8b50f", auth_token="test_5d2e8cf45646124ef084e81ad36", endpoint='https://test.instamojo.com/api/1.1/')

st.set_page_config(layout="wide")
col1, col2 = st.beta_columns([1, 1])
f_order=[]
final_order=SessionState.get(State=[],amo=0,amo1=0,update="False")
st.sidebar.image('./Images/logo.jpg')
try:
    conn = pymongo.MongoClient('mongodb+srv://aditya:12345@cluster0.rutst.mongodb.net/test')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

def order_colone(a,k,m,d,z,p):
    image = Image.open(k)
    col1.image(image,width=200)
    if col1.button(a):
        z.append((m,p))
    my_expander = col1.beta_expander("Description")
    my_expander.write(d)
    return z
def order_coltwo(a,k,m,d,z,p):
    image = Image.open(k)
    col2.image(image,width=200)
    if col2.button(a):
        z.append((m,p))
    my_expander = col2.beta_expander("Description")
    my_expander.write(d)
    return z
tableno=st.sidebar.text_input("Type Your Table Number")
db = conn.Restaurent1
if tableno:
    collection=db[tableno]
cusine=st.sidebar.selectbox("Select Choice",['None','Indian','Continental','Bread','Dessert','Order Confirmation'])

if cusine=='Indian':


    final_order.State = order_colone('Add Shahi Paneer', './Images/5.jpeg', 'Shahi Paneer',
                                     'Cottage cheese mixed with creamy tomato and cashew gravy',
                                     final_order.State,110)
    final_order.State = order_colone('Add Mix Vegetable', './Images/4.jpeg', 'Mix Vegetable',
                                      'A subtle mixture of potato and cauliflower accompanied with chopped tomato and diced onion',
                                     final_order.State,210)
    final_order.State = order_coltwo('Add Dal Makhani:', './Images/3.jpeg', 'Dal Makhani:',
                                     'A mixture of Kidney beans and Black Lentils served with a whole bunch of cream and butter',
                                     final_order.State,220)
    final_order.State = order_coltwo('Add Chana Masala', './Images/1.jpg', 'Chana Masala',
                                     'Combination of chickpeas and innumerable Indian spices topped with chopped onion and corriander',
                                     final_order.State,400)
    if st.sidebar.button('Clear order'):
        final_order.State=[]
    st.sidebar.title("Your Order")
    freq = {}
    for item in final_order.State:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    for key, value in freq.items():
        st.sidebar.write("{} -Rs {} : {}".format(key[0], key[1], value))
if cusine=='None':
    st.markdown("<h1>Welcome to Wriggle n Giggle!</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p align='justify' style='font-size:20px;font-family:arial;'><br> This restaurant is a one-stop shop for all amazing delicacies from a range of cuisines that will leave your appetites wanting more. From a veritable repository of mouth-watering dishes, you now have the option of dining-in, ordering online and take-away. You can now place, modify your order  with our newly launched website all from the comfort of your device. Join us for a time of delectable dining and precious moments..</p>",
        unsafe_allow_html=True)
    st.markdown("<h3>Developed by </h3>",unsafe_allow_html=True)
    col1, col2, col3 = st.beta_columns((1, 1, 1))
    col1.image("./Images/p3.jpeg", width=150)
    col1.markdown("<h4>Aditya Mukherjee</h4>",unsafe_allow_html=True)
    col1.markdown("<h5>Designation : </h5> Technical Lead", unsafe_allow_html=True)
    col2.image("./Images/p1.jpeg", width=150)
    col2.markdown("<h4>Sumedha Banthia</h4>",unsafe_allow_html=True)
    col2.markdown("<h5>Designation : </h5>Business Analyst",unsafe_allow_html=True)
    col3.image("./Images/p2.jpeg", width=150)
    col3.markdown("<h4>Anand Iyer</h4>",unsafe_allow_html=True)
    col3.markdown("<h5>Designation : </h5> Project Manager", unsafe_allow_html=True)

if cusine=='Continental':
    final_order.State = order_colone('Add Farmhouse Pizza', './Images/6.jpeg', 'Farmhouse Pizza',
                                     ' A heavenly cheesy pizza combined with fresh vegetables like tomato, onion, bell pepper, corn and toppings of mushroom and jalapenos',
                                     final_order.State,200)
    final_order.State = order_colone('Add Quesadilla', './Images/8.jpeg', 'Quesadilla',
                                     'Mexican tortillas filled with cheese, spices, corn and other seasonal vegetables served with mayonnaise',
                                     final_order.State,300)
    final_order.State = order_coltwo('Add Gratin:', './Images/7.jpeg', 'Gratin',
                                     'Baked vegetables like potato, cauliflower, beans, broccoli and golden corn topped with grated cheese, butter and breadcrumbs',
                                     final_order.State,450)
    final_order.State = order_coltwo('Add Taco', './Images/9.jpeg', 'Taco',
                                     'Wheat tortillas topped with tomatoes, onions, lettuce, cheese and garnished with salsa sauce, guacamole and sour cream',
                                     final_order.State,350)
    if st.sidebar.button('Clear order'):
        final_order.State = []
    st.sidebar.title("Your Order")
    freq = {}
    for item in final_order.State:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    for key, value in freq.items():
        st.sidebar.write("{} -Rs {} : {}".format(key[0],key[1], value))
if cusine=='Bread':


    final_order.State = order_colone('Add Butter Naan', './Images/10.jpeg', 'Butter Naan',
                                     '',final_order.State,30)
    final_order.State = order_colone('Add Garlic Kulcha', './Images/11.jpeg', 'Garlic Kulcha','',final_order.State,50)
    final_order.State = order_coltwo('Add Missi Roti', './Images/12.jpeg', 'Missi Roti',
                                     '',
                                     final_order.State,40)
    final_order.State = order_coltwo('Add Tandoori Roti', './Images/13.jpeg', 'Tandoori Roti',
                                     '',
                                     final_order.State,50)
    if st.sidebar.button('Clear order'):
        final_order.State=[]
    st.sidebar.title("Your Order")
    freq = {}
    for item in final_order.State:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    for key, value in freq.items():
        st.sidebar.write("{} -Rs {} : {}".format(key[0], key[1], value))

if cusine=='Dessert':


    final_order.State = order_colone('Add Nutella Waffle', './Images/14.jpeg', 'Nutella Waffle',
                                     'An overload of Nutella between freshly cooked waffles topped with chocolate sauce and ice cream',
                                     final_order.State,110)
    final_order.State = order_colone('Add Sizzling Brownie', './Images/16.jpeg', 'Sizzling Brownie','Heavenly Brownies served as sizzlers with vanilla ice cream and a dash of chocolate syrup',final_order.State,180)
    final_order.State = order_coltwo('Add Strawberry Mousse', './Images/15.jpeg', 'Strawberry Mousse',
                                     'Airy, Fluffy and light whipped cream mixed with wholesome strawberry syrup with chunks of strawberry and a spoonful of strawberry ice cream',final_order.State,150)
    final_order.State = order_coltwo('Add Blueberry Cheesecake','./Images/17.jpeg', 'Blueberry Cheesecake',
                                     'A mixture of whipping cream and cream cheese on a biscotti crust of crush cookies served with freshly prepared blueberry sauce topped with sweetened blueberries',final_order.State,170)
    if st.sidebar.button('Clear order'):
        final_order.State=[]
    st.sidebar.title("Your Order")
    freq = {}
    for item in final_order.State:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    for key, value in freq.items():
        st.sidebar.write("{} -Rs {} : {}".format(key[0], key[1], value))
if cusine=='Order Confirmation':
        col1.title("Details for payment")
        freq = {}
        amount=0
        final_order.amo=0
        for item in final_order.State:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        for key, value in freq.items():
            final_order.amo=final_order.amo+(key[1]*value)
        amount = final_order.amo+final_order.amo1
        col1.markdown("<h3>The final amount is {}</h3>".format(amount),unsafe_allow_html=True)
        purpose ="Food"
        name = col1.text_input("Enter Name")
        email = col1.text_input("Enter email")
        response = api.payment_request_create(
            amount=amount,
            purpose=purpose,
            buyer_name=name,
            send_email=True,
            email=email,
            redirect_url="https://share.streamlit.io/adityamukherjee42/payment_portal1/main/feeedback.py"
        )
        order = 0
        cusine="None"
        result=[]
        col2.title("Your Order")
        freq = {}
        for item in final_order.State:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        for key, value in freq.items():
            col2.write("{} -Rs {} : {}".format(key[0], key[1], value))
            result.append(
                {
                    'Dish': key[0],
                    'Price': key[1],
                    'Quantity': value
                }
            )
        if final_order.update=='False':
            col1.markdown("<h4>Please place order to pay</h4>",unsafe_allow_html=True)
        if col2.button("Place order"):
            collection.insert_many(result)
            final_order.update="True"
        if final_order.update=='True':
            if col2.button("Please press here if you want to continue ordering or else please click pay"):
                col2.write("Please continue ordering more food")
                final_order.amo1 = final_order.amo
                final_order.State = []
                final_order.update = "False"
            if (col1.button("Pay") and final_order.update=='True'):
                js ="window.open('{}')".format(response['payment_request']['longurl'])  # New tab or window
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)
                order=order+1
                final_order.update = "False"
        else:
            st.write("")


