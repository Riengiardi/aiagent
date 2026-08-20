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
    args = parser.parse_args()

    # getting a response array
    response = client.chat.completions.create(model = "openrouter/free", messages=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ])

    # getting usage data and checking it
    usage = response.usage
    if usage == None:
        raise RuntimeError("Usage data is empty!")
    p_tokens = usage.prompt_tokens
    c_tokens = usage.completion_tokens

    print(response.choices[0].message.content)
    print(f"Prompt tokens: {p_tokens}\nResponse tokens: {c_tokens}")
    
    


if __name__ == "__main__":
    main()
