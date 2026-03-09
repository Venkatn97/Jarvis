# core/brain.py
import json
import ollama

def think(user_input):
    """Send your command to Llama and get a response"""
    
    system_prompt = """
    You are Jarvis, a helpful browser AI assistant.
    You help the user control their browser, check emails, 
    search jobs, play YouTube videos and more.
    Keep responses short and clear.
    Always confirm before taking important actions.
    """
    
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        options={
            "num_predict": 100,
            "temperature": 0.7,
            "num_thread": 8
        }
    )
    
    return response['message']['content']

def extract_intent(user_input):
    """Use AI to understand the command and extract key info"""
    
    prompt = f"""
    Analyze this voice command and respond in JSON only, no explanation:
    
    Command: "{user_input}"
    
    Respond with exactly this format:
    {{
        "action": "search_google" or "search_youtube" or "open_website" or "play_youtube" or "chat",
        "query": "the actual search term only, no filler words"
    }}
    
    Examples:
    "can you search temperature in chicago" -> {{"action": "search_google", "query": "temperature in chicago"}}
    "search latest songs on youtube" -> {{"action": "search_youtube", "query": "latest songs"}}
    "play lofi music" -> {{"action": "play_youtube", "query": "lofi music"}}
    "open gmail" -> {{"action": "open_website", "query": "gmail"}}
    "how are you" -> {{"action": "chat", "query": ""}}
    """
    
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
        options={"num_predict": 50, "temperature": 0}
    )
    
    try:
        result = json.loads(response['message']['content'])
        return result
    except:
        return {"action": "chat", "query": ""}