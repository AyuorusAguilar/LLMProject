import json
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function
import argparse
from openai.types import Completion, CompletionChoice, CompletionUsage
def main():
    load_dotenv()
    

    parser = argparse.ArgumentParser(description='Chatbot', add_help='Arguments for the chatbot app I guess')
    parser.add_argument("user_prompt", help='Promt for the chatbot app', type=str)
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages=[{"role": "system", "content": system_prompt},
              {"role":"user", "content": args.user_prompt}]
    #Main loop:
    for _ in range(20):
        #Calling the model 
        response = calling_llm_api(messages, args.user_prompt, verbose=args.verbose)

        #Handling Responses
        message = response.choices[0].message
        messages.append(message)   
        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, verbose=True)
                if not result_message["content"]:
                    raise Exception("Error: The result message from the called function is empty")
                if args.verbose:
                    print(f"-> {result_message['content']}")
                messages.append(result_message)
        else:
            print(message.content)
            sys.exit(0)
            break
    print("Error: The agent exceded its iteration number limit")
    sys.exit(1)


def calling_llm_api(messages : list[object], user_prompt: str, verbose: bool = False):
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key == None:
        raise RuntimeError("API key not found, please get a OpenRouter API key")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions
    )

    #validation
    if response.usage.completion_tokens == None:
        raise RuntimeError("Bad API response")
    if verbose:
        print(f"""
|----------------------------------------------------------------------------------------------------------------------------------|
User prompt: {user_prompt}
Prompt tokens: {response.usage.prompt_tokens}
Response tokens: {response.usage.completion_tokens}""")
    return response
    

if __name__ == "__main__":
    main()