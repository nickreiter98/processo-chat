from openai import OpenAI

if __name__ == "__main__":
    client = OpenAI()

    while True:
        user_input = input("Give me a prompt: ")
        print("+++REQUEST STARTED+++")

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input},
            ]
        ) 

        print(completion.choices[0].message.content)
        print("+++REQUEST ENDED+++")

