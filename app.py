import streamlit as st
from src.audio_processing import process_audio_segment
from src.speaker_identification import identify_speakers_by_pitch
from src.sentiment_analysis import analyze_sentiment
from src.metrics_evaluation import extract_call_kpis, evaluate_performance
from src.chatbot_assistant import process_chatbot_query
import tempfile
import os

# Initialize Streamlit app
st.title("📊 Call Analysis & Sentiment Evaluation")
st.write("Upload customer service call recordings to evaluate agent performance and customer satisfaction.")

# File uploader
uploaded_file = st.file_uploader("Upload Call Recording", type=['mp3', 'wav', 'ogg'])

if uploaded_file:
    st.audio(uploaded_file, format="audio/wav")
    if st.button("🚀 Start Analysis"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_file_path = temp_file.name

        with st.spinner("Processing audio..."):
            text_segments, customer_text, agent_text, customer_sentiment, agent_sentiment, \
            customer_triggers, agent_triggers, customer_metadata, agent_metadata = \
                process_audio_segment(temp_file_path)

        avg_response_time, response_times = evaluate_performance(text_segments)
        kpis = extract_call_kpis(text_segments, customer_text, agent_text, customer_sentiment, agent_sentiment, avg_response_time)

        st.subheader("Call Analysis Overview")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Customer")
            st.write(f"Sentiment: {customer_sentiment['label']} ({customer_sentiment['score']:.2f})")
            st.write(f"Key Concerns: {', '.join(customer_triggers) if customer_triggers else 'None detected'}")

        with col2:
            st.subheader("Agent")
            st.write(f"Sentiment: {agent_sentiment['label']} ({agent_sentiment['score']:.2f})")
            st.write(f"Response Time: {avg_response_time:.2f} seconds")

        st.subheader("Overall Performance")
        st.write(f"Resolution: {kpis['resolution_achieved']}")
        st.write(f"Response Efficiency: {kpis['avg_response_time']:.2f}s")

        os.unlink(temp_file_path)
