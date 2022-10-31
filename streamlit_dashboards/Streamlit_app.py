import numpy as np
import pandas as pd
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import os
import glob
from tensorflow import keras 
import tensorflow as tf
import cv2



col1, col2, col3 = st.columns(3)

with col1:
    st.write("")

with col2:
    image1=Image.open('App logo.png')
    st.image(image1)

with col3:
    st.write("")







st.markdown("<h1 style='text-align: center; color: blue;'>Drawing Detection app</h1>", unsafe_allow_html=True)
video1= open('Team Faseeh.gif.mp4', 'rb')
st.video(video1)



st.markdown("<h4 style=padding: 300px 5px; color: blue;'>Draw on board</h4>", unsafe_allow_html=True)
stroke_width = st.sidebar.slider("Stroke width: ", 5, 20, 10)
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect",
                      "circle", "polygon")
)


language_selection = st.sidebar.selectbox(
    "Select Language:", ("Urdu", "English")
)



model = keras.models.load_model(r'model_doodles_v3.h5')

if language_selection == "Urdu":
    df = {1:'ہوائی جہاز' , 2:'کتاب',3:'ٹوکری',4:'چمکادڑ',
               5:'دماغ',6:'روٹی',7:'سیب',8:' پل',
               9:' سائیکل',10:'کیلا',
               11:'ایفل ٹاور',12:'بس',13:'کیک', 
               14:'گھنٹہ گلاس',15:'اونٹ',  16:'گھر', 
               17:'آئس کریم',18:'موم بتی',19:'جیکٹ',
               20:'کار',21:'بھیڑ',
               22:'چابی',23:'جوتا',24: 'محل',
               25:'بلی',26:'چھری',27:'سیڑھی', 
               28:'سیل فون',29: 'کرسی',30: 'پتہ',
               31:'مسکراہٹ والا چہرہ',32: 'گھڑی',33: 'بادل',  
               34:'کافی کپ',35: ' شیر', 36: 'سنو مین',
               37:'لالی پاپ',38:'چمچ',  
               39:'تاج',40:'ستارہ' , 41:'کپ',42: 'بندر',
               43:'ہیرا', 44:'موٹر بائیک',45:'کتا',
               46:'پہاڑ', 47: 'چوہا', 48:'اسٹرابیری',
               49:'کھمبی',50:'دھول',51:'سورج', 
               52:'تلوار',
               53:'لفافہ',54:'میز',55:'چشمے',
               56:'آنکھ',57:'چہرہ',58:'چیتا',59:'انگلی',
               60:'مچھلی', 61:'ناشپاتی' ,62:'پھول',
               63:'درخت',64:'کانٹا',65:'پیزا', 
               66:'چھتری',67:'قلفی', 68:'انگور',
               69:'خرگوش',70:'ہاتھ',
               71:'قوس قزح'  ,72:'زگ زیگ'}

    df = pd.DataFrame(list(df.items()),columns = ['Id','Name']) 


else:
    df = {1:'airplane' , 2:'book',3:'basket',4:'bat',
               5:'brain',6:'bread',7:'apple',8:'bridge',
               9:'bicycle',10:'banana',
               11:'Eiffel Tower',12:'bus',13:'cake', 
               14:'hourglass',15:'camel',  16:'house', 
               17:'ice cream',18:'candle',19:'jacket',
               20:'car',21:'sheep',
               22:'key',23:'shoe',24: 'castle',
               25:'cat',26:'knife',27:'ladder', 
               28:'cell phone',29: 'chair',30: 'leaf',
               31:'smiley face',32: 'clock',33: 'cloud',  
               34:'coffee cup',35: 'lion', 36: 'snowman',
               37:'lollipop',38:'spoon',  
               39:'crown',40:'star' , 41:'cup',42: 'monkey',
               43:'diamond', 44:'motorbike',45:'dog',
               46:'mountain', 47: 'mouse', 48:'strawberry',
               49:'mushroom',50:'drums',51:'sun', 
               52:'sword',
               53:'envelope',54:'table',55:'eyeglasses',
               56:'eye',57:'face',58:'tiger',59:'finger',
               60:'fish', 61:'pear' ,62:'flower',
               63:'tree',64:'fork',65:'pizza', 
               66:'umbrella',67:'popsicle', 68:'grapes',
               69:'rabbit',70:'hand',
               71:'rainbow'  ,72:'zigzag'}

    df = pd.DataFrame(list(df.items()),columns = ['Id','Name'])



stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")

realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=None,
    update_streamlit=realtime_update,
    height=300,
    drawing_mode=drawing_mode,
    display_toolbar=st.sidebar.checkbox("Display toolbar", True),
    key="canvas",
)



# col1, col2, col3 = st.columns(3)


# with col1:
a = 1
if canvas_result.image_data is not None:
        image = canvas_result.image_data
        image1 = image.copy()
        image1 = image1.astype('uint8')
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        #image2 = cv2.resize(image1, (90, 90))
        image1 = cv2.resize(image1, (28, 28))
        #st.image(image2)
        image1.resize(1,28,28,1)
  
  
# with col2:
        st.markdown("<h1 style='text-align: left; color: red;'>Result</h1>", 
                    unsafe_allow_html=True)
        


# with col3:
        a=(np.argmax(model.predict(image1)))
        st.header(df.loc[a,'Name'])
        
        
        


page_bg_img = '''
<style>
.css-10trblm {
    color: #ffbf00;
}

</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)





st.header(":mailbox: Comments")


contact_form = """
<form action="https://formsubmit.co/faseehteam@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")



# image=Image.open('photo.jpg')
# st.image(image, width = 120)



col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.write("")

with col3:
    image2=Image.open('photo.jpg')
    st.image(image2, width = 120)