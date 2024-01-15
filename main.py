from openai import OpenAI
import streamlit as st

# It is prefered to add the openai key as an environment variable!
# Since the assignment requires the direct insertion of the api key, I will do it this way
OPENAI_API_KEY = "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"
TASK = "You are a gentleman and your task is to answer the question in the most kind, gentle and funny way."

client = OpenAI(api_key=OPENAI_API_KEY)

"""Added final_prompt as parameter to pass the final prompt of the last conversation + the actual task
final_prompt is initialized to TASK when there are no previous conversations"""
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

    return completion

"""The main user interface function that creates a streamlit application"""
def run_chatbot_ui():
    #Setup the page configurations
    st.set_page_config(
    page_title="Gentle Chatbot",
    layout="wide",
    page_icon="🤵"
)
    #setup the title and the sidebar
    st.title("Chat with Gentle Chatbot 🤵🤖")

    st.sidebar.text("Instructions:")
    st.sidebar.markdown("- Type your message in the input box.")
    st.sidebar.markdown("- The chatbot will respond kindly and gently.")

    #Use session states to keep track of the messages
    #The following line of code initializes the meassges with the hello, feel free ... messages by the system
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role": "system",
            "content": "Hello, feel free to ask anything!"}
        ]
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    #Store user input if it is not None
    user_prompt = st.chat_input()

    if user_prompt is not None:
        st.session_state.messages.append(
            {"role": "user",
            "content": user_prompt}
        )
        with st.chat_message("user"):
            st.write(user_prompt)

        #This block is reponsible for teh spinner effect and most imporatantly the passing of the right propmt (with last conversation) to the gpt model
        if st.session_state.messages[-1]["role"] != "system":
            with st.chat_message("system"):
                with st.spinner("Loading ..."):
                    user_input = st.session_state.messages[-1]["content"]
                    history_prompt = f"Here's the last conversation with the user:\n User: {user_input}\n Chatbot: {st.session_state.messages[-2]['content']} \n {TASK}"
                    ai_response = generate_chat_gpt(user_input=user_prompt, final_prompt=history_prompt).choices[0].message.content
                    st.write(ai_response)
            #Add the system response to teh messages 
            new_ai_message = {"role": "system",
                            "content": ai_response}

            st.session_state.messages.append(new_ai_message)

if __name__=="__main__":
    
    run_chatbot_ui()

