# Abyat

## Description

**تحليل الأبيات الشعرية** من حيث البحر، القافية، والعصر، الموضوع

**توليد** الأبيات والقصائد محددة الأهداف عن طريق (الفكرة، البحر، طول القصيدة)

**مساعدة** الشاعر عن طريق التدرب مع النموذج على **الإجازة الشعرية**

**طريقة إلقاء** البيت الشعري عن طريق تقسيم البيت تقسيما **عروضيا** 
## Demo
![Project demo](./images/Demo.gif)


This is a Python project that requires Python 3.11. Follow the steps below to set up the environment and run the application.
## Prerequisites

- Python 3.11 or later
- `pip` (Python package installer)

## Setup Instructions

### 1. Install Python 3.11
Ensure that Python 3.11 is installed on your machine. You can download it from the official Python website:

- [Download Python 3.11](https://www.python.org/downloads/release/python-3110/)

Verify that Python is installed correctly by running the following command in your terminal or command prompt:

```bash
python --version
```
This should return Python 3.11.x.

### 2. Create a Virtual Environment
Once Python 3.11 is installed, navigate to your project directory and create a virtual environment:

```bash
python -m venv venv
```
This will create a venv folder in your project directory containing the virtual environment.

### 3. Install Requirements
Activate the virtual environment and install the necessary dependencies.

On macOS/Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```
After activating the virtual environment, install the required Python packages:

```bash
pip install -r requirements.txt
```
### 4. Set Up the .env File
Create a .env file in the root directory of your project to store environment variables. This file may contain sensitive data such as API keys, database credentials, or configuration settings.

Example .env file:

```env
OPENAI_API_KEY=API-KEY
ALLAM_ACCESS_TOKEN=ALLAM-TOKEN
ALLAM_ORIGINAL_URL=URL
ALLAM_FINTUNED_URL=URL
```
Make sure to replace the values with your actual configuration.

### 5. Run the Application
Once everything is set up, you can run the application using the following command:

```bash
python app.py
```
This will start the application. Ensure that any necessary services (e.g., a database or web server) are running if required by the project.

### Additional Information
If you need to deactivate the virtual environment, run:

```bash
deactivate
```

To update your dependencies, modify the requirements.txt file and run:
```bash
pip install -r requirements.txt
```
## License
Include licensing information here (MIT License).
