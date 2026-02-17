import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERATIONS

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
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)

    prompt = " ".join(user_text)

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)]),]

    for _ in range(MAX_ITERATIONS):
        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print(f"Final Response: {final_response}")
                return
        except Exception as e:
            print(f"Error generating content: {e}")
    
    print(f"Max number of iterations reached ({MAX_ITERATIONS})! Cancelling prompt to conserve tokens...")
    sys.exit(1)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.5-flash", # gemini-2.0-flash-001 (old model to be phased out)
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
        )

    if not response.usage_metadata:
        raise RuntimeError("API request appears to have failed")

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.candidates:
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)

    if not response.function_calls:
        return response.text

    function_responses = []
    for call in response.function_calls:
        function_call_result = call_function(call, verbose)
        if not function_call_result.parts or not function_call_result.parts[0].function_response or not function_call_result.parts[0].function_response.response:
            raise Exception(f"Empty function response for {call.name}")
        function_responses.append(function_call_result.parts[0])
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

    messages.append(types.Content(role="user", parts=function_responses))



if __name__ == "__main__":
    main()