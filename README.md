
# Medicine Information Extraction System

## Overview

The Medicine Information Extraction System is designed to extract and provide detailed information about medicines from images and a pre-defined CSV database. This system utilizes Optical Character Recognition (OCR) to extract text from images and integrates a language model for generating informative descriptions about medicines.

## Features

- **Image Preprocessing**: Enhances the quality of images for better text extraction.
- **Text Extraction**: Uses Tesseract OCR to extract text from images of medicine labels.
- **Medicine Identification**: Identifies the main medicine name and retrieves relevant information from a CSV database.
- **Information Generation**: Creates user-friendly descriptions for medicines, including potential substitutes, key uses, benefits, side effects, precautions, and expiry information.

## Technologies Used

- **Python**
- **OpenCV**
- **Tesseract OCR**
- **Pandas**
- **Matplotlib**
- **Ollama for LLaMA models**

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7 or higher**
- **Ollama**: Install it following the instructions on the [Ollama website](https://ollama.com/docs/getting-started).
- **LLaMA 3.2 model**: Pull the model using the command:

  ```bash
  ollama pull llama3.2
  ```

## Requirements

To run this project, you will need the following Python packages:

```plaintext
pytesseract==0.3.10
opencv-python==4.5.3.20210920
pandas==1.3.3
matplotlib==3.4.3
gdown==4.2.0
```

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/Chaitu5210/Tablet-Insight-Engine.git
   cd Tablet-Insight-Engine
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:

```bash
python main.py
```

1. The script will prompt you to enter the path to your medicine image (e.g., `Dataset/TestImg.jpg`).
2. The system will process the image, extract the text, and identify the medicine name.
3. You will then be prompted to enter the ID of the medicine to retrieve detailed information.
4. The system will display a user-friendly description of the selected medicine, including its:
   - **Name**
   - **Potential Substitutes**
   - **Key Uses**
   - **Benefits**
   - **Side Effects**
   - **Precautions**
   - **Expiry Information**

---

**Note**: This system is intended for educational purposes only and should not replace professional medical advice.
