# Dentology: Topological Data Analysis for Dentists 🦷

![header image showing a robot dentist](figs/header_image.png)

Dentology applies cutting-edge mathematical tools to dental imaging, offering innovative methods for cavity detection and analysis.

## Cavity Detection Pipeline

The main feature of Dentology is the Cavity Detection Pipeline (CDP). It is a state-of-the-art tool for identifying cavities in dental X-ray images. It uses Topological Data Analysis (TDA) to detect cavities in a patient's teeth. More specifically, it uses the Mapper algorithm.

The workflow of the CDP is as follows:

1. **Feature Extraction**: Extract the patient's tooth to be analyzed and 3D scan it to create a point cloud.
2. **Mapper Algorithm**: Apply the Mapper algorithm to generate a graph representation of the point cloud.
3. **Cavity Detection**: Identify cavities in the patient's tooth based on the topological features of the Mapper graph.

---

## Upcoming Features

### Teeth Counting Pipeline

We are currently developing the Teeth Counting Pipeline (TCP). TCP is a cutting-edge tool for counting the number of teeth in a patient's mouth. It uses Persistent Homology to analyze the topological features of the patient's dental X-ray image. The TCP will also be able to inform the dentist if the patient has teeth at all, saving valuable time and resources in these cases.

---

## Installation
Clone the repository:
```bash
git clone https://github.com/odinhg/Dentology-TDA-for-Dentists 
cd Dentology-TDA-for-Dentists
pip install -r requirements.txt
```

## Usage
1. Upload a dental X-ray image.
2. Run the Dentology pipeline.
3. Interpret the results with our cutting-edge `ToothMapper` function.

**Example:**
```python
from dentology import analyze_xray

diagram = analyze_xray("dental_xray.png")
diagram.plot()
```

## Disclaimer
This tool is intended for research purposes only and should not replace professional dental care. Please visit your dentist regularly.

---

By the way, happy 1st of April! 


