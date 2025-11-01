import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()

    verbose = False
    user_text = sys.argv[1:]

    if not user_text:
        print('Error: Missing prompt!\nExpected format: python3 main.py "Enter prompt here"')
        sys.exit(1)
    
    if "--verbose" in user_text:
        user_text.remove("--verbose")
        verbose = True

    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    prompt = " ".join(user_text)

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)]),]

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Response:\n{response.text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(f"Response:\n{response.text}")

if __name__ == "__main__":
    main()