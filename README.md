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

We are currently developing the Teeth Counting Pipeline (TCP). TCP is a cutting-edge tool for counting the number of teeth in a patient's mouth. It uses Persistent Homology to analyze the topological features of the patient's dental X-ray image. The TCP will also be able to inform the dentist if the patient has any teeth at all, saving valuable time and resources in these cases.

---

## Installation and Usage

### Clone the repository:

```bash
git clone https://github.com/odinhg/Dentology-TDA-for-Dentists 
cd Dentology-TDA-for-Dentists
pip install -r requirements.txt
```

To run the Cavity Detection Pipeline, you can use the `cavity_detection.py` script. For example:

```bash
python cavity_detection.py --filename data/premolar_normal.stl
```

This will generate a filtered simplicial complex and output a persistence diagram showing the topological features of the tooth. To visualize the 3D model, use the `--plot_mesh` flag:

```bash
python cavity_detection.py --filename data/premolar_normal.stl --plot_mesh
```

We demonstrate the Cavity Detection Pipeline on a healthy tooth and a tooth with two cavities. We use the following 3D model of a healthy premolar tooth:

![3d tooth model](figs/premolar_3d_model_normal.png)

Running the CDP on the healthy and cavity-infected teeth, we obtain the following persistence diagrams:

| PD Healthy Tooth | PD Cavities | 
|:-----------------:|:-------------------:|
| ![point cloud normal](figs/persistence_diagram_normal.png)  | ![point cavity](figs/persistence_diagram_cavities.png) |

We can clearly see the two persistence pairs in the upper right corner of the diagram for the tooth with cavities. These pairs correspond to the cavities in the tooth.

---

## Disclaimer
This tool is intended for research purposes only and should not replace professional dental care. Please visit your dentist regularly. Also, happy 1st of April! 


