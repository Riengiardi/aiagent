import os, argparse
from dotenv import load_dotenv
from openai import OpenAI

def main():

    # Loading local env
    load_dotenv()

    # Fetching API key
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key == None:
        raise RuntimeError("API key is missing.")

    # Choosing client (OperRouter)
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )  

    # Parsing user input with argparse
    parser = argparse.ArgumentParser(description="This a chatbot based on the free Openrouter client.")
    parser.add_argument("user_prompt", type=str, help="Prompt given by a user.")
    parser.add_argument("--verbose", '-v', action="store_true", help="More verbose output for additional details.")
    args = parser.parse_args()

    # Storing conversation
    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    # Creating ChatCompletion object
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    # Monitoring token usage for ChatCompletion (--verbose)
    if response.usage == None:
        raise RuntimeError("Usage details not found. Possible failed API request.")
    if args.verbose == True:
        print(f"User prompt: {messages[0]["content"]}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    # Printing message content from ChatCompletion
    print(f"Response: {response.choices[0].message.content}")
    


if __name__ == "__main__":
    main()
