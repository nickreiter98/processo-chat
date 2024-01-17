import json
from openai import OpenAI
from pydantic_classes import RequestDetails
from process_concepts.process_visualization import visualize_process

if __name__ == "__main__":
    client = OpenAI()

    while True:
        user_input = input("Give me a prompt: ")
        print("+++REQUEST STARTED+++")

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            functions=[RequestDetails.openai_schema],
            messages=[
                {"role": "user", "content": user_input},
            ]
        ) 

        response = completion.choices[0].message.function_call.arguments
        dict_response = json.loads(response)

        if dict_response["request_type"] == "process_visualization":
            print("+++START PROCESS VISUALIZATION+++")
            visualize_process(dict_response["underlying_data"])
            print("+++END PROCESS VISUALIZATION+++")

        print("+++REQUEST ENDED+++")

