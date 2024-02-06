# Project AFER: Advancements in Facial Emotion Detection

Welcome to Project AFER, a venture aimed at advancements in Facial Emotion Detection. This project utilizes various techniques and models to enhance the accuracy of recognizing emotions from facial expressions.

## Folder Structure
  
- **Code:** This directory contains all training documents and supporting materials.

## Data Used

[FER2013 - CSV](https://www.kaggle.com/datasets/nicolejyt/facialexpressionrecognition)

[FER2013 - Image Data](https://www.kaggle.com/datasets/msambare/fer2013)
## Running the Detector

To run the facial emotion detection, use the notebook named `FacialAudioEmotionDetection.ipynb`. Make sure to speak during the recording section, as there may be an issue with empty buffers while processing audio.

## Installation
### Anaconda Environment
This project utilizes an Anaconda environment to manage dependencies and ensure reproducibility. The environment.yml file contains a list of all required packages and their versions. To create the environment, 

```bash
conda env create --file environment.yml
```
Activate the environment before running the code:
```bash
conda activate fer
```

### Remarks
Installing LFS and enabling it is essential, as there are large files in the repository that necessitate this feature.

