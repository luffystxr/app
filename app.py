import streamlit as st
from huggingface_hub import hf_hub_download
from tensorflow.keras.models import load_model
from streamlit_lottie import st_lottie
import json
import base64
from PIL import Image
import numpy as np
from io import BytesIO

# Page config

st.set_page_config(page_title="Forest Fire Detection", layout="wide", page_icon="🔥")

@st.cache_resource
def loadmodel():
    model_path = hf_hub_download(
        repo_id="Sridharsri098/ffdkeras",  # Your model repo name
        filename="src/model/FFD.keras",
        repo_type="space"  # Explicitly specify model repo
    )
    return model_path

model = load_model(loadmodel())

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0px;  
        padding-bottom: 0px;     
    }
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet"><style>
        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif !important;
        }
    </style>
    """, unsafe_allow_html=True)


# Load Lottie
def load_lottie_animation(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_hello = load_lottie_animation("lotties/hello.json")
lottie_pulze = load_lottie_animation("lotties/pulze.json")
lottie_work = load_lottie_animation("lotties/work.json")

# --- Title Section ---
st.markdown("""
    <h1 style='text-align: center; font-size: 35px;'>
        Forest Fire Detection Using Deep Learning 🔥
    </h1>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Block 1: Intro ---
col1, col2= st.columns([2.5, 2])

with col1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h4>Hi, I am Sridharan 👋</h3>", unsafe_allow_html=True)
    st.markdown("## A Machine Learning Engineer From India")
    st.markdown("<p style='font-size:20px;'>Passionate Machine Learning Engineer with a strong interest in building intelligent, real-world AI applications that make a positive impact.</p>", unsafe_allow_html=True)    

with col2:
    st.markdown("<div class='lottie-container'>", unsafe_allow_html=True)
    st_lottie(lottie_hello, height=350, key="hello")
    st.markdown("</div>", unsafe_allow_html=True)


st.markdown("<hr style='border-top: 2px solid; margin: 1rem 0;'>", unsafe_allow_html=True)

col1, col2= st.columns([1, 1.5])

with col1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🔍 Project Description:")
    st.markdown("""
        <ul style="font-size: 18px; line-height: 1.8; padding-left: 20px;">
            <li>Uses deep learning techniques to identify forest fires in satellite imagery.</li>
            <li>Trained on high-resolution datasets with annotated fire zones.</li>
            <li>Real-time prediction and alert capabilities.</li>
            <li>Helps in early detection to prevent large-scale destruction.</li>
            <li>Designed to be lightweight and scalable.</li>
        </ul>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<div class='lottie-container'>", unsafe_allow_html=True)
    st_lottie(lottie_pulze, height=280, key="pulze")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr style='border-top: 2px solid; margin: 1rem 0;'>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1.5])
with col1:
    st.markdown("## 📺 What I do")

    # Model highlights

    st.markdown("#### ✅ Model Highlights:")
    st.markdown("""
        <ul style="font-size: 18px; line-height: 1.8; padding-left: 20px;">
    <li>Preprocessed data with resizing and data augmentation for better generalization </li> 
    <li>Built a custom <b style="color: yellow;">CNN model</b> with efficient layers  </li>
    <li>Included <b style="color: yellow;">Dropout layers</b> to prevent overfitting </li> 
    <li>Trained using the best optimizer and tuned learning rate  </li>
    <li>Applied <b style="color: yellow;">EarlyStopping</b> and <b style="color: yellow;">L2 regularization</B> to optimize training  </li>
        </ul>
    """, unsafe_allow_html=True)
    
    # Accuracy summary
    st.markdown("""
<h3 style='color: green;'>📈 Final Accuracy: <b>83.4%</b></h4>
<h3 style='color: red;'>📉 Final Loss: <b>3.875</b></h4>
""", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='lottie-container'>", unsafe_allow_html=True)
    st_lottie(lottie_work, height=350, key="work")
    st.markdown("</div>", unsafe_allow_html=True)


st.markdown("<hr style='border-top: 2px solid; margin: 1rem 0;'>", unsafe_allow_html=True)


col1, col2 = st.columns([1, 1])
fire = False
nofire = False
with col1:
    st.markdown("###  🔎 Upload Image To Detect Forest Fire")
    st.markdown("**Note** : this Model Trained to Predict Fire in Forest")
    st.markdown("<br>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("upload an image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    if uploaded_file:
        image = Image.open(uploaded_file)

        st.markdown("""
        <style>
        .stButton > button {
            background-color: transparent;
            color: #ccc;
            font-size: 18px;
            font-weight: bold;
            padding: 12px 24px;
            border: 2px solid #ccc;
            border-radius: 8px;
            text-decoration: none;
            transition: all 0.3s ease;
            box-shadow: none;
            display: block;
            margin: auto;
        }
        .stButton > button:hover {
            color: white;
            box-shadow: 0 0 15px red;
            transform: scale(1.05);
        }
        </style>
    """, unsafe_allow_html=True)
        
        predictnow = st.button("🚀 Predict Now")

        if predictnow:

            def predict_image(img):
                img = img.resize((224, 224))
                img_array = np.array(img) / 255.0
                img_array = img_array.reshape((1, 224, 224, 3))
                prediction = model.predict(img_array)
                return prediction
            with st.spinner("Analyzing Image..."):
                prediction = predict_image(image)

            if prediction[0][0]>=0.5:
                nofire = True
                st.success("✅ No Forest Fire Detected!")
                confidence = prediction[0][0]*100
                st.markdown(f"<h3 style='color: green;'>📈 Confidence: <b>{confidence:.2f}%</b></h3>", unsafe_allow_html=True)
            if prediction[0]<0.5:
                fire = True
                st.error("🔥 Forest Fire Detected!")
                confidence = 100 - prediction[0][0]*100
                st.markdown(f"<h3 style='color: red;'>📉 Confidence: <b>{confidence:.2f}%</b></h3>", unsafe_allow_html=True)   
                
with col2:
    if uploaded_file:       
        img = Image.open(uploaded_file)

        # --- 3. Detect the format and encode image to base64 ---
        buffer = BytesIO()
        img_format = img.format if img.format else "PNG"
        img.save(buffer, format=img_format)
        img_b64 = base64.b64encode(buffer.getvalue()).decode()

        # --- 4. Get correct MIME type ---
        mime_type = f"image/{img_format.lower()}"

        # --- 5. Style for scrollable container ---
        # --- 5. Style for scrollable container ---
        st.markdown("""
        <style>
        .image-scroll-container {
            width: 100%;
            max-width: 600px;
            height: 400px;
            overflow: auto;
            border: 2px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
            margin: auto;

            display: flex;
            justify-content: center;
            align-items: center;
        }
        .image-scroll-container img {
            max-width: none; /* allow scrolling if image is large */
            max-height: none;
        }
        </style>
        """, unsafe_allow_html=True)


        # --- 6. Inject image via base64 inside HTML ---
        st.write("**Note** : scroll if image is not full viewed")
        st.markdown(f"""
            <div class="image-scroll-container">
                <img src="data:{mime_type};base64,{img_b64}" alt="Uploaded Image" />
            </div>
        """, unsafe_allow_html=True)




col1,col2,col3 = st.columns([1,2,1])
with col1:
    with open("gifs/plant.gif", "rb") as f:
                    data = f.read()
                    b50 = base64.b64encode(data).decode()
    with open("gifs/treeonfire.gif", "rb") as f:
                    data = f.read()
                    b51 = base64.b64encode(data).decode()
    if(fire):
        st.markdown(f"""<img src="data:image/gif;base64,{b51}" alt="Link" width="1600" height="320" >""", unsafe_allow_html=True)
    
    if(nofire):
        st.markdown(f"""<img src="data:image/gif;base64,{b50}" alt="Link" width="1000" height="320" >""", unsafe_allow_html=True)

with col2:
    with open("gifs/angry.gif", "rb") as f:
                    data = f.read()
                    b60 = base64.b64encode(data).decode()
    with open("gifs/safe.gif", "rb") as f:
                    data = f.read()
                    b61 = base64.b64encode(data).decode()
    if(fire):
        st.markdown(f"""<img src="data:image/gif;base64,{b60}" alt="Link" width="1600" height="320" >""", unsafe_allow_html=True)
        st.markdown("""
<div style="margin-left: 150px;">
    <h1>Hurry Up Save Forest.</h1>
</div>
""", unsafe_allow_html=True)
    
    if(nofire):
        st.markdown(f"""<img src="data:image/gif;base64,{b61}" alt="Link" width="1000" height="320" >""", unsafe_allow_html=True)
        st.markdown("""
<div style="margin-left: 150px;">
    <h1>No worries its safe.</h1>
</div>
""", unsafe_allow_html=True)

with col3:
    with open("gifs/plant.gif", "rb") as f:
                    data = f.read()
                    b50 = base64.b64encode(data).decode()
    with open("gifs/treeonfire.gif", "rb") as f:
                    data = f.read()
                    b51 = base64.b64encode(data).decode()
    if(fire):
        st.markdown(f"""<img src="data:image/gif;base64,{b51}" alt="Link" width="1600" height="320" >""", unsafe_allow_html=True)
    
    if(nofire):
        st.markdown(f"""<img src="data:image/gif;base64,{b50}" alt="Link" width="1000" height="320" >""", unsafe_allow_html=True)



st.markdown("<hr style='border-top: 2px solid; margin: 1rem 0;'>", unsafe_allow_html=True)





st.markdown("#### 📬 Connect With Me")



with open("gifs/huggy.gif", "rb") as f:
    data = f.read()
    b64 = base64.b64encode(data).decode()

with open("gifs/linked.gif", "rb") as f:
    data = f.read()
    b65 = base64.b64encode(data).decode()

with open("gifs/git.gif", "rb") as f:
    data = f.read()
    b66 = base64.b64encode(data).decode()


st.markdown(f"""
    <style>
        a.hover-link, a.hover-link:visited {{
            text-decoration: none !important;
            color: #ccc !important;
        }}

        a.hover-link:hover {{
            text-decoration: none !important;
            color: white !important;
            box-shadow: 0 0 15px white;
            transform: scale(1.05);
        }}

        .hover-link {{
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 16px;
            font-size: 20px;
            border-radius: 8px;
            background-color: transparent;
            transition: all 0.3s ease;
        }}
    </style>
            
    <a href="https://www.linkedin.com/in/sridharan-s-4635442a9" class="hover-link" target="_blank">
        <img src="data:image/gif;base64,{b65}" alt="Link" width="45">   
        Visit My LinkedIn Profile
    </a>

    <a href="https://github.com/luffystxr" class="hover-link" target="_blank">
        <img src="data:image/gif;base64,{b66}" alt="Link" width="45">   
        Visit My Github
    </a>

    <a href="https://huggingface.co/Sridharsri098" class="hover-link" target="_blank">
        <img src="data:image/gif;base64,{b64}" alt="Link" width="45">
        Vist My Hugging Face
    </a>

""", unsafe_allow_html=True)

st.markdown("<hr style='border-top: 1px solid; margin: 1rem 0;'>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666; font-size:1rem;'>© 2025 Forest Fire Detection AI | Developed with ❤️ for environmental protection  By Sridharan :)</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
