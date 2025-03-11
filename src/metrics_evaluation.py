import numpy as np

def extract_call_kpis(segments, customer_text, agent_text, customer_sentiment, agent_sentiment, response_time):
    """Extracts key performance indicators from the call."""
    call_duration = segments[-1]['end'] - segments[0]['start'] if segments else 0
    agent_talk_time = sum([s['end'] - s['start'] for s in segments if s.get('speaker_role') == 'agent'])
    customer_talk_time = sum([s['end'] - s['start'] for s in segments if s.get('speaker_role') == 'customer'])
    total_talk_time = agent_talk_time + customer_talk_time
    agent_talk_ratio = agent_talk_time / total_talk_time if total_talk_time > 0 else 0
    silence_ratio = (call_duration - total_talk_time) / call_duration if call_duration > 0 else 0
    
    return {
        "call_duration": call_duration,
        "agent_talk_ratio": agent_talk_ratio,
        "silence_ratio": silence_ratio,
        "response_time": response_time
    }

def evaluate_performance(segments):
    """Calculates response times between speakers."""
    response_times = []
    for i in range(1, len(segments)):
        if segments[i-1]['speaker_role'] == 'customer' and segments[i]['speaker_role'] == 'agent':
            response_times.append(segments[i]['start'] - segments[i-1]['end'])
    return np.mean(response_times) if response_times else 0, response_times
