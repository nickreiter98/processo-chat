import json
import logging

from openai import OpenAI
from colorama import Fore, Back, Style

from pydantic_classes import RequestDetails
from process_concepts.process_visualization import visualize_process


if __name__ == "__main__":
    #logging.basicConfig(level=logging.INFO)
    client = OpenAI()

    INSTRUCTION = "What Would you like to know today?"
    messages = [{"role": "system", "content": INSTRUCTION}]

    previous_question_answer = []

    while True:
        prompt = input(Fore.GREEN + Style.BRIGHT + INSTRUCTION + Style.RESET_ALL)

        for question, answer in previous_question_answer:
            messages.append({"role": "user", "content": question})
            messages.append({"role": "assistant", "content": answer})
        messages.append({"role": "user", "content": prompt})

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            functions=[RequestDetails.openai_schema],
            messages=messages
        )

        response = completion.choices[0].message
        if response.content == None:
            previous_question_answer.append((prompt, "extracted and passed information to inner functionalities"))
        else:
            previous_question_answer.append((prompt, response.content))

        if len(previous_question_answer) > 10:
            previous_question_answer = previous_question_answer.pop(0)

        response = completion.choices[0].message

        try:
            dict_response = json.loads(response.function_call.arguments)
            
            if dict_response["request_type"] == "process_visualization":
                logging.info("+++START PROCESS VISUALIZATION+++")
                visualize_process(dict_response["underlying_data"])
                logging.info("+++END PROCESS VISUALIZATION+++")

        except AttributeError:
            print(response.content)

        

        logging.info("+++REQUEST ENDED+++")

