# Medical Diagnosis Tool
This repository contains a command-line program that prompts the user for their age, gender, symptoms, duration of symptoms, and underlying medical conditions, and then uses the OpenAI API to generate a medical diagnosis based on this information. The generated diagnosis includes information on possible causes of the diagnosis and suggested treatment options or medications.

# Prerequisites
You will need to have a valid API key for the OpenAI API. You can sign up for an API key at https://beta.openai.com/signup/.

# Installation
1. Clone the repository:
```
git clone https://github.com/your-username/medical-diagnosis-tool.git
```
2. Navigate to the repository directory:
```
cd medical-diagnosis-tool
```
3. Install the required packages:
```
pip install -r requirements.txt
```

#Usage
1.Replace "YOUR_API_KEY" with your own API key in the code:
```
openai.api_key = "YOUR_API_KEY"
```
2. Run the program:
```
python main.py
```
3. Follow the prompts to enter your age, gender, symptoms, duration of symptoms, and underlying medical conditions.

4. The program will use the OpenAI API to generate a medical diagnosis based on the information you provided.

#Notes
>The OpenAI API should not be used as a substitute for professional medical advice. It is always important to seek appropriate medical care and to follow the advice of your healthcare provider.

>The model used by the OpenAI API may not be able to generate accurate or complete diagnoses in all cases. Use the generated diagnosis only as a starting point for further research and discussion with a qualified healthcare professiona





