from app.config.settings import settings
import openai

def test_openai_connection():
    openai.api_key = settings.OPENAI_API_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10,
        )
        print("✅ OpenAI test successful:", response['choices'][0]['message']['content'])
    except Exception as e:
        print("❌ OpenAI test failed:", str(e))

test_openai_connection()