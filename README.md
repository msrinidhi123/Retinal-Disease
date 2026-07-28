# 👁️ Retinal Disease Classification System

A web-based Deep Learning application for **real-time retinal disease classification** using a **VGG19 Convolutional Neural Network**. The system enables users to upload retinal fundus images through a web interface and receive instant disease predictions.

---

## 📌 Overview

This project integrates **Artificial Intelligence** with **Web Technologies** to assist in the early detection of retinal diseases.

The model classifies retinal fundus images into the following four categories:

- 👁️ Cataract
- 🩸 Diabetic Retinopathy
- 🔍 Glaucoma
- ✅ Normal (Healthy Retina)

The application combines:

- HTML/CSS frontend
- PHP backend
- Python inference engine
- TensorFlow VGG19 model

to provide a seamless real-time prediction system.

---

## ✨ Features

- Real-time retinal disease prediction
- Deep Learning model based on VGG19
- User-friendly web interface
- Automatic image preprocessing
- Supports JPG and PNG images
- Local deployment using Apache (XAMPP/WAMP)
- Modular architecture for future cloud deployment

---

## 🏗️ System Architecture

```
User
   │
   ▼
HTML/CSS Web Interface
   │
   ▼
PHP Backend
   │
   ▼
Python Inference Script (app.py)
   │
   ▼
VGG19 Deep Learning Model (.keras)
   │
   ▼
Prediction Result
```

---

## 🧠 Deep Learning Model

**Base Model:** VGG19 (Transfer Learning)

### Input

- RGB Retinal Fundus Images
- Image Size: **224 × 224 pixels**

### Output Classes

- Cataract
- Diabetic Retinopathy
- Glaucoma
- Normal

The model was trained offline using labeled retinal image datasets and exported as a `.keras` model for inference.

---

## 💻 Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming Languages | Python, PHP |
| AI Framework | TensorFlow, Keras |
| Image Processing | Pillow, NumPy |
| Frontend | HTML, CSS |
| Web Server | Apache (XAMPP/WAMP) |
| Deep Learning | VGG19 Transfer Learning |

---

## 📂 Project Structure

```
Retinal-Disease-Classification/
│
├── index.html
├── style.css
├── upload.php
├── app.py
├── retinal_model.keras
├── upload/
├── README.md
└── requirements.txt
```

---

## ⚙️ Prerequisites

### Software

- Python 3.10+
- XAMPP or WAMP
- Apache Server
- Google Chrome / Firefox

### Python Libraries

Install the required dependencies:

```bash
pip install tensorflow numpy pillow
```

---

## 🚀 How to Run

### Step 1

Install **XAMPP** or **WAMP**.

Copy the project into:

```
xampp/htdocs/
```

or

```
wamp/www/
```

---

### Step 2

Start **Apache Server**.

---

### Step 3

Open the application in your browser:

```
http://localhost/index.html
```

---

### Step 4

Upload a retinal image.

Supported formats:

- JPG
- PNG

---

### Step 5

The system will:

1. Save the uploaded image.
2. Execute the Python inference script.
3. Load the trained VGG19 model.
4. Predict the disease.
5. Display the prediction on the webpage.

---

## 🔄 Workflow

1. User uploads retinal image.
2. PHP stores the image in the **upload/** folder.
3. PHP invokes **app.py**.
4. Python preprocesses the image.
5. VGG19 performs classification.
6. Prediction is returned to PHP.
7. Result is displayed to the user.

---

## 🎯 Applications

- Early retinal disease screening
- Telemedicine
- Clinical decision support
- Academic research
- AI-assisted diagnostics

---

## 📈 Future Enhancements

- Cloud deployment (Google Cloud, AWS)
- Mobile application integration
- Electronic Medical Record (EMR) integration
- Multi-disease classification
- Explainable AI using **Grad-CAM**
- Performance optimization and scalability

---

## 📷 Sample Output

*(Add screenshots of your application interface and prediction results here.)*

---

## 👨‍💻 Author

**Medari Srinidhi**

- 📧 Email: medarisrinidhi@gmail.com
- 💼 LinkedIn: *(Add LinkedIn URL)*
- 💻 GitHub: *(Add GitHub URL)*

---

⭐ If you found this project useful, consider giving the repository a **Star**.
