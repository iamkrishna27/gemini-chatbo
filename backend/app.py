import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

# 🔐 Replace with your actual API key (the one you provided)
API_KEY = "AIzaSyDaPp7GaqwVPjPNgqkd3oZK659odsl-_R8"
genai.configure(api_key=API_KEY)

app = Flask(__name__)
CORS(app)  # This allows your frontend to talk to the backend

# Environmental system prompt to restrict the bot
ENVIRONMENTAL_SYSTEM_PROMPT = """You are EcoGuide, a specialized AI assistant focused ONLY on environmental topics.
Your expertise includes:
- Climate change and global warming
- Renewable energy (solar, wind, hydro, geothermal)
- Pollution (air, water, soil, plastic)
- Conservation and biodiversity
- Sustainable living and green practices
- Environmental policies and regulations
- Recycling and waste management
- Carbon footprint and emissions
- Environmental science and ecology
- Weather and climate patterns
- Environmental technology (green tech)

IMPORTANT RULES:
1. ONLY answer questions related to environmental topics listed above
2. If a question is NOT about the environment, respond with: "I'm specialized in environmental topics only. Please ask me about climate change, sustainability, pollution, renewable energy, or other environmental subjects."
3. Keep responses factual, helpful, and educational
4. If a question is vaguely related to environment, focus on the environmental aspects
5. Be friendly and use relevant emojis in your responses (🌍, 🌱, ♻️, ☀️, etc.)

Remember: You are an environmental expert, not a general assistant."""

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the message from the request
        data = request.get_json()
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Use Gemini model with system prompt
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Combine system prompt with user message
        full_prompt = f"{ENVIRONMENTAL_SYSTEM_PROMPT}\n\nUser Question: {user_message}\n\nEcoGuide:"
        
        response = model.generate_content(full_prompt)

        # Extract the text from Gemini's response
        bot_reply = response.text

        return jsonify({'reply': bot_reply})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'status': 'Environmental Chatbot is running!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)