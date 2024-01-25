if __name__ == "__main__":
    from openai import OpenAI
    client = OpenAI()

    INSTRUCTION = "What Would you like to know today?"
    messages = [{"role": "system", "content": INSTRUCTION}]

    previous_question_answer = []


    while True:
        print("+++++++++++++++")
        prompt = input(INSTRUCTION)

        for question, answer in previous_question_answer:
            messages.append({"role": "user", "content": question})
            messages.append({"role": "assistant", "content": answer})
        messages.append({"role": "user", "content": prompt})

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            #functions=[RequestDetails.openai_schema],
            messages=messages
        )

        answer = completion.choices[0].message.content
        previous_question_answer.append((prompt, answer))

        if len(previous_question_answer) > 10:
            previous_question_answer = previous_question_answer.pop(0)

        print(answer)
        print("+++++++++++++++ /n/n")