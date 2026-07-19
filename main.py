import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from openai.types import Completion, CompletionChoice, CompletionUsage
def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key == None:
        raise RuntimeError("API key not found, please get a OpenRouter API key")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    parser = argparse.ArgumentParser(description='Chatbot', add_help='Arguments for the chatbot app I guess')
    parser.add_argument("user_prompt", help='Promt for the chatbot app', type=str)
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages=[{"role":"user", "content": args.user_prompt}]
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages
    )

    if response.usage.completion_tokens == None:
        raise RuntimeError("Bad API response")
    if args.verbose:
        print(f"""
|----------------------------------------------------------------------------------------------------------------------------------|
User prompt: {args.user_prompt}
Prompt tokens: {response.usage.prompt_tokens}
Response tokens: {response.usage.completion_tokens}""")
    print(response.choices[0].message.content)
if __name__ == "__main__":
    main()
