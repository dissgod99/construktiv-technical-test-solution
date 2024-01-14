from openai import OpenAI

# It is prefered to add the openai key as an environment variable!
# Since the assignment requires the direct insertion of the api key, I will do it this way

OPENAI_API_KEY = "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"

TASK = "You are a gentleman and your task is to answer the question in the most kind, gentle and funny way."

client = OpenAI(api_key=OPENAI_API_KEY)
def generate_chat_gpt(user_input, final_prompt=TASK):
    client.api_key = OPENAI_API_KEY
    completion = client.chat.completions.create(  #The documentation got updated, see https://github.com/openai/openai-python
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": str(final_prompt)},
            {"role": "user", "content": str(user_input)}
            ],
    max_tokens=400,
    temperature=0.6
    )
    #completion = str(response)

    return completion


if __name__=="__main__":
    print("Setup works!")

    res = generate_chat_gpt(user_input="Am I good enough to achieve my dreams?")

    #Access the reponse
    print(res.choices[0].message.content)

