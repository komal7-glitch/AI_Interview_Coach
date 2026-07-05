# AI Interview Coach

## Overview

AI Interview Coach is a Streamlit-based application that helps users practice technical interviews using AI-generated questions and automated answer evaluation. The application leverages Ollama's local Large Language Models (LLMs) to generate interview questions, assess responses, and provide detailed feedback.

## Features

* Generate interview questions on multiple technical topics
* Evaluate user answers using AI
* Score answers out of 10
* Identify strengths and weaknesses
* Suggest improvements
* Provide ideal answers for learning
* Track interview history
* Display performance dashboard with:

  * Total Questions Attempted
  * Average Score
  * Highest Score
  * Lowest Score

## Supported Topics

* Python
* SQL
* Machine Learning
* Deep Learning
* Generative AI (GenAI)

## Tech Stack

* Python
* Streamlit
* Ollama
* Llama 3.2 (3B Model)
* Regular Expressions (re)

## Project Structure

```text
AI_Interview_Coach/
│
├── app.py
├── check_models.py
├── screenshots
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI_Interview_Coach.git
cd AI_Interview_Coach
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2:3b
```

Verify installation:

```bash
ollama list
```

## Run the Application

Start Ollama:

```bash
ollama serve
```

Run the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## How It Works

### Question Generation

The application sends a prompt to the Llama 3.2 model to generate a technical interview question based on the selected topic.

### Answer Evaluation

After the user submits an answer, the AI evaluates it and provides:

* Score (/10)
* Strengths
* Weaknesses
* Improvement Suggestions
* Ideal Answer

### Performance Dashboard

The dashboard tracks:

* Number of questions attempted
* Average score
* Highest score
* Lowest score

### Interview History

All interview attempts are stored in the session and displayed for review.

## Sample Workflow

1. Select a topic.
2. Click "Generate Question".
3. Read the generated question.
4. Enter your answer.
5. Click "Evaluate Answer".
6. Review feedback and score.
7. Track progress through the dashboard.

## Future Enhancements

* User authentication
* Question difficulty levels
* Voice-based interview simulation
* PDF report generation
* Progress tracking database
* Multiple LLM support
* Coding interview mode
* Behavioral interview questions

## Requirements

```text
streamlit
ollama
```

Install manually:

```bash
pip install streamlit ollama
```

## Author

Komal Yadav

AI & Data Science Enthusiast | Python Developer | Machine Learning Practitioner

## License

This project is open-source and available under the MIT License.
