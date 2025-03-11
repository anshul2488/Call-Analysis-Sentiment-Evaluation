# Call-Analysis-Sentiment-Evaluation

## Overview
This project is a real-time call analysis and agent performance evaluator built using Streamlit. It processes customer service calls to extract key insights, including:
- **Speech Transcription**: Converts speech to text using Whisper AI.
- **Speaker Identification**: Differentiates between customer and agent.
- **Sentiment Analysis**: Determines the emotional tone of the conversation.
- **Performance Metrics**: Evaluates agent response time, talk ratio, and silence percentage.
- **Chatbot Assistant**: Allows querying insights from the call.

## Features
- Real-time transcription and speaker recognition.
- Interactive dashboard with sentiment trends and performance indicators.
- Call segmentation and speaker labeling.
- Customizable alert system for negative trigger words.
- Visual KPI charts for talk time distribution and response efficiency.

## Installation
### Prerequisites
Ensure you have Python 3.8+ and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application
```bash
streamlit run app.py
```

Upload a call recording (`.wav`, `.mp3`) to start the analysis.

## Project Structure
```
/your_project_name
│── /src
│   │── __init__.py
│   │── audio_processing.py
│   │── speaker_identification.py
│   │── sentiment_analysis.py
│   │── metrics_evaluation.py
│   │── chatbot_assistant.py
│── app.py
│── requirements.txt
│── README.md
```

- **`app.py`**: Main Streamlit app.
- **`src/audio_processing.py`**: Handles audio transcription and processing.
- **`src/speaker_identification.py`**: Identifies and segments speakers.
- **`src/sentiment_analysis.py`**: Analyzes conversation sentiment.
- **`src/metrics_evaluation.py`**: Extracts key performance indicators.
- **`src/chatbot_assistant.py`**: Implements a chatbot for call analysis.

## Contributions
Feel free to fork the repo and submit pull requests for enhancements.

## License
MIT License

