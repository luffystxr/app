
# 🌲 Forest Fire Detection Using Deep Learning 🔥

Developed by: **Sridharan S**  
AICTE Student ID: `STU67bafc13b02e31740307475`  
AICTE Internship ID: `INTERNSHIP_174099535967c57b1f336c3`  

Live App 👉 [forestfiredetect.streamlit.app](https://forestfiredetect.streamlit.app)  
Source Code 👉 [GitHub Repository](https://github.com/luffystxr/app.git)

---

## 📌 Problem Statement

Forest fires are increasingly devastating due to climate change, leading to massive loss of biodiversity, human displacement, and ecological damage. Traditional detection methods (satellites, patrols) are delayed and expensive.

---

## ✅ Solution

A **deep learning-based system** was created using a **custom Convolutional Neural Network (CNN)** to detect forest fires from images in real-time. This system:
- Classifies images into **"fire"** or **"no fire"**
- Achieved **83% accuracy**
- Was deployed using **Streamlit** for user-friendly interaction

---

## 🎯 Learning Objectives
- Gather and structure image datasets for forest fire detection
- Preprocess data via resizing and augmentation
- Design CNN models from scratch
- Apply regularization (Dropout, L2, EarlyStopping)
- Train & evaluate models with optimizers and validation datasets
- Deploy models via interactive apps for real-world testing

---

## 🛠 Tools & Technologies
- **Python** – Core development language  
- **TensorFlow/Keras** – Model building and training  
- **CNN** – Custom deep learning architecture  
- **Google Colab** – Training environment  
- **Kaggle** – Dataset source  
- **NumPy, Pandas** – Data handling  
- **Matplotlib, Seaborn** – Visualization  
- **Streamlit** – Frontend for deployment  
- **streamlit-lottie** – UI animation support

---

## ⚙️ Methodology

1. **Data Collection** from Kaggle: Fire vs. No-Fire images  
2. **Preprocessing**: Resizing, augmentation  
3. **Model Design**:
   - 3 Conv2D layers
   - 3 MaxPooling layers
   - 1 Dropout
   - 1 Flatten
   - 2 Dense layers  
4. **Training**:
   - Adam optimizer
   - Binary Crossentropy
   - Accuracy as metric
   - Early stopping + L2 regularization  
5. **Evaluation**:
   - Achieved **83% test accuracy**
   - Real-time image predictions tested
6. **Deployment**:
   - Streamlit app with image uploader
   - Predicts fire/no fire
   - Includes alert sounds & downloadable PDF reports

---

## 📈 Results

| Prediction Set | Total Images | Correct Predictions | Accuracy |
|----------------|--------------|----------------------|----------|
| Fire Images    | 9            | 8                    | ~89%     |
| No Fire Images | 9            | 8                    | ~89%     |

Overall test accuracy: **83.4%**

---

## 📸 App Features

- 🔍 Upload image to detect fire
- 🧠 Get prediction & confidence score
- 🔊 Fire alert audio for fire images
- 🧾 Download prediction report
- ✨ Animated UI using Lottie

---

## 🚀 How to Open the App

### 🔗 Web Version (Recommended)
i hosted my model in streamlit cloud u can just click on the below link to view my streamlit app
link:  
👉 **[Open the App](https://forestfiredetect.streamlit.app)**

### 🖥️ Run Locally (Advanced)
if u want to view the source code and run it locally follow below instructions:

1. **Clone the repo**  
   ```bash
   git clone https://github.com/luffystxr/app.git
   cd app
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Streamlit app**  
   ```bash
   streamlit run app.py
   ```

---

## 🧠 Conclusion

This project proves how AI and deep learning can be applied to critical real-world problems like wildfire detection. With an 83% accuracy model, real-time predictions, and user-friendly deployment, this system enables quick action and scalable forest monitoring.

### 🔮 Future Enhancements
- Real-time video classification
- Drone integration for aerial analysis
- IoT sensor fusion for multi-modal alerting

---
