def process_chatbot_query(query, call_summary, text_segments, customer_text, agent_text, kpis, performance_metrics):
    """Processes user queries about the call and generates responses."""
    query = query.lower()
    
    if "summary" in query:
        return f"This call lasted {kpis['call_duration']} seconds. Resolution: {'Resolved' if kpis['resolution_achieved'] else 'Unresolved'}."
    elif "customer" in query and "sentiment" in query:
        return f"Customer sentiment was {performance_metrics['Customer Sentiment']} with a score of {performance_metrics['Customer Sentiment Score']:.2f}."
    elif "agent" in query and "performance" in query:
        return f"Agent talk ratio: {kpis['agent_talk_ratio']*100:.1f}%, Response efficiency: {performance_metrics['Response Efficiency']}."
    else:
        return "I'm not sure about that. Try asking about the summary, sentiment, or agent performance."
