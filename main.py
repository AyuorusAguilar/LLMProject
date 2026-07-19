import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function
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
    messages=[{"role": "system", "content": system_prompt},
              {"role":"user", "content": args.user_prompt}]
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions
    )
    print('we got here, so the model actually answered')
    if response.usage.completion_tokens == None:
        raise RuntimeError("Bad API response")
    if args.verbose:
        print(f"""
|----------------------------------------------------------------------------------------------------------------------------------|
User prompt: {args.user_prompt}
Prompt tokens: {response.usage.prompt_tokens}
Response tokens: {response.usage.completion_tokens}""")
    message = response.choices[0].message    
    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose=True)
            if not result_message["content"]:
                raise Exception("The result message from the called function is empty")
            if args.verbose:
                print(f"-> {result_message['content']}")
    else:
        print(message.content)
if __name__ == "__main__":
    main()
