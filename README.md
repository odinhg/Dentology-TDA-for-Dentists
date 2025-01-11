# Dentology: Topological Data Analysis for Dentists 🦷

Dentology applies cutting-edge mathematical tools to dental imaging, offering innovative methods for cavity detection and analysis.

## Key Features
- **Cavity Detection**: Automatically maps dental X-rays to persistence diagrams for advanced analysis.
- **Tooth Stability Analysis**: Quantifies the structural integrity of each tooth.
- **Gum Topology Visualization**: Provides insights into dental health with state-of-the-art topological methods.

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

Example:
```python
from dentology import analyze_xray

diagram = analyze_xray("dental_xray.png")
diagram.plot()
```

## Disclaimer
This tool is intended for research purposes only and should not replace professional dental care. Please visit your dentist regularly.

---

By the way, happy 1st of April! 


