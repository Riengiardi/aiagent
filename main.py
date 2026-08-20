import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse



def main():

    # loading .env and checking for api key
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key == None:
        raise RuntimeError("API key not found!")
    
    # creating with client and conecting with API
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    )

    # parser here
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
        

    # message storage

    messages= [ {"role": "user", "content": args.user_prompt,}, ]

    # getting a response array
    response = client.chat.completions.create(model = "openrouter/free", messages=messages)

    # getting usage data and checking it
    usage = response.usage
    if usage == None:
        raise RuntimeError("Usage data is empty!")
    p_tokens = usage.prompt_tokens
    c_tokens = usage.completion_tokens

    print(response.choices[0].message.content)
    if args.verbose == True:
        print(f"User prompt: {args.user_prompt}\nPrompt tokens: {p_tokens}\nResponse tokens: {c_tokens}")
    
    


if __name__ == "__main__":
    main()
