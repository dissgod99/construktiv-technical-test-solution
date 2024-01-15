from openai import OpenAI

# It is prefered to add the openai key as an environment variable!
# Since the assignment requires the direct insertion of the api key, I will do it this way

OPENAI_API_KEY = "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"
HISTORY = []
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

    #res = generate_chat_gpt(user_input="Am I good enough to achieve my dreams?")
    #res = generate_chat_gpt(user_input="What is my name?")

    #Access the reponse
    #print(res.choices[0].message.content)
    #print(res)
    print("Hello, how can I assist you?")
    history_prompt = ""
    i=0
    while True:
        print(i)
        user_input = input('User: ')
        if history_prompt == "":
            completion = generate_chat_gpt(user_input=user_input)
            history_prompt = f"Here's the last conversation with the user:\n User: {user_input}\n Chatbot: {completion.choices[0].message.content} \n {TASK}"
            #print("history EMPTY")
        else:
            completion = generate_chat_gpt(user_input=user_input, final_prompt=history_prompt)
            print(history_prompt+ "\n\n")
            history_prompt = f"Here's the last conversation with the user:\n User: {user_input}\n Chatbot: {completion.choices[0].message.content} \n {TASK}"
            #print("HISTORY ELSE")
        print(completion.choices[0].message.content)
        i += 1

