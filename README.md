# 📌Smart-HealthCare-Condition-Monitoring-and-Motion-Analysis
## Human posture recognition, MediaPipe, OpenCV, machine learning 

## 🧾 Overview  
This project is a **prototype healthcare system** that detects and corrects human posture in real time using **computer vision** and **machine learning**. Unlike wearable-based solutions, this system works **only with a camera feed**, making it **low-cost, non-intrusive, and practical** for daily use.  

Maintaining correct posture is essential for spinal health and overall well-being. Poor posture leads to back pain, neck strain, reduced flexibility, and even long-term injuries. This project provides **real-time monitoring, activity recognition, and feedback (text/speech)** to help users maintain proper posture.  

---

## 🚀 Features  
- 📷 **Camera-only detection** (no sensors or wearables required)  
- 🧍 **Pose Estimation with MediaPipe (33 landmarks)**  
- ⏱ **Real-time feedback for posture correction** (text & speech using `pyttsx3`)  
- 📐 **Symmetry & angle analysis** for head, neck, torso, and limbs  
- 📊 **Custom dataset** of sitting, standing, bending poses  
- 🤖 **Machine learning models tested & compared**  
  - Logistic Regression  
  - Linear Discriminant Analysis  
  - KNN  
  - Naive Bayes  
  - SVM  
  - Decision Tree  
  - Random Forest  
- ✅ **High accuracy (up to 100%)** in classification  
- 💻 **Lightweight and runs on laptops/PCs with low resource usage**  

---

## 🛠️ Tech Stack  
- **Language:** Python  
- **Libraries/Frameworks:**  
  - [OpenCV](https://opencv.org/) – image processing  
  - [MediaPipe](https://developers.google.com/mediapipe) – pose landmark detection  
  - [scikit-learn](https://scikit-learn.org/) – ML models  
  - [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/) – data preprocessing & visualization  
  - [pyttsx3](https://pypi.org/project/pyttsx3/) – text-to-speech feedback  

---

## ⚙️ Installation & Setup  

1. **Clone this repository:**  
   ```bash
   git clone https://github.com/nikitansg/Smart-Healthcare-Posture-Correction.git
   cd Smart-Healthcare-Posture-Correction

2. **Create and activate conda environment:**
   ```bash
   conda create -n posture_env python=3.9
   conda activate posture_env

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Run the system:**
   ```bash
   python src/body_data.py
   python src/human.py
   python src/main.py
   python src/merged.py
   
## 📊 Results

- Logistic Regression: 99.5% accuracy
- Decision Tree: 99.7% accuracy
- Random Forest: 100% accuracy
- Overall performance: Highly reliable real-time posture detection & correction


## 📸 Demo
- 🪑 Sitting & standing posture correction in real-time
- 🔊 Feedback provided via text & speech (alerts for incorrect posture)
- 🌙 Works even in low-light conditions

## 🔮 Future Scope
- Expand dataset with more diverse poses & activities
- Deploy on edge devices / IoT cameras
- Integrate with wearables & healthcare IoT systems
- Use deep learning (CNN, LSTM) for enhanced accuracy

## 👨‍💻 Author
**Nikita Sharma**
- 📍 Machine Learning & Computer Vision Engineer

