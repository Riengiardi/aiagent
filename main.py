import os, argparse, prompts, sys
from dotenv import load_dotenv
from openai import OpenAI
from call_function import available_functions
from functions.call_function import call_function

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
        {"role": "system", "content": prompts.system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    for _ in range(20):

        # Creating ChatCompletion object
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        # Monitoring token usage for ChatCompletion (--verbose)
        if response.usage == None:
            raise RuntimeError("Usage details not found. Possible failed API request.")
        if args.verbose == True:
            print("-------------------------------------------")
            print(f"User prompt: {messages[1]["content"]}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
            print("-------------------------------------------")

        # Extracting message for later use and adding to message list
        message = response.choices[0].message
        messages.append(message)

        # Check for the end of the agent reasoning
        if message.tool_calls == None:
            print(f"Response: {message.content}")
            return "Successfuly finished the calls"

        # Printing tool calls from ChatCompletion
        for tool_call in message.tool_calls:
            tool_message = call_function(tool_call)
            messages.append(tool_message)
            if args.verbose == True:
                print(f"-> {tool_message['content']}")

    # if loop time exceeded
    print("Error: Amount of allowed time exceeded.")
    sys.exit('1')

if __name__ == "__main__":
    main()
