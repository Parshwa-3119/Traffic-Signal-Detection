# 🚦 Traffic Signal Identifier using CNN with Voice Alerts

This project is a deep learning-based system that detects and classifies traffic signals (Red, Yellow, Green) from images or real-time video feeds and **provides voice-based alerts** using text-to-speech. It is developed using **Python**, **YOLOv5**, **OpenCV**, and **pyttsx3** for voice output.

---

## 🧠 Overview

In modern traffic systems, visual signal detection alone may not be sufficient — especially for visually impaired individuals or autonomous systems needing audio feedback. This project enhances traditional traffic signal recognition by integrating **Convolutional Neural Networks (CNNs)** with **voice alerts** that announce the detected signal state.

---

## 🔍 Key Features

- ✅ Real-time detection of traffic lights (Red, Yellow, Green)
- 🧠 Deep learning-based image classification using CNN (e.g., YOLOv5)
- 🗣️ Voice output using `pyttsx3` to announce the current signal
- 🌤️ Handles varying lighting/weather conditions and occlusions
- 📷 Works with webcam or pre-recorded video input

---

## 📌 Project Goals

- Improve traffic safety with both visual and auditory signal detection
- Assist autonomous systems and visually impaired users
- Create an intelligent, adaptable traffic light identifier for real-world deployment

---

## 🛠️ Tools & Technologies

| Category         | Technology                     |
|------------------|--------------------------------|
| Language         | Python                         |
| Deep Learning    | TensorFlow / PyTorch, YOLOv5   |
| Computer Vision  | OpenCV                         |
| Text-to-Speech   | Pyttsx3                        |
| IDE              | Visual Studio Code             |
| OS               | Windows 11                     |

---

## 🧪 Testing & Results

| Test Scenario                         | Result      | Accuracy   |
|--------------------------------------|-------------|------------|
| Standard signal in clear image       | ✅ Pass     | > 95%      |
| Low light or nighttime scenes        | ✅ Pass     | > 85%      |
| Occluded or partially hidden signal  | ⚠️ Partial  | > 70%      |
| Heavy occlusion or unknown designs   | ❌ Fail     | < 50%      |
| Video with moving objects & light    | ⚠️ Partial  | ~65%       |

Voice output examples:
- `"Red signal ahead, please stop."`
- `"Yellow signal detected, be ready."`
- `"Green signal, proceed with caution."`

---

## 🚀 Future Scope

- 📱 Mobile version with voice alerts
- 🧠 Integration with ADAS and autonomous systems
- 📡 IoT support for connected traffic systems
- 🎙️ Multilingual voice output

---

## 👨‍💻 Contributors

- Parshwa Dedhia  
- Kajal Jagtap 

Supervised by: *Assistant Prof. Seema Bhuravane*

---

## 📚 References

1. YOLOv5 for real-time object detection  
2. OpenCV for computer vision  
3. Pyttsx3 for offline text-to-speech in Python  
4. Research papers on CNNs and traffic signal recognition

---

> 📁 This repository includes all code, dataset references, and test cases for the Traffic Signal Identifier project with voice alerts.

