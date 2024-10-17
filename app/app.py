import chainlit as cl
#chainlit is a python frontend library especially designed for building with LLM
from langchain.chat_models import ChatOpenAI
#langchain is a frameowrk to work with LLM
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.llms import HuggingFaceInterference
from langchain.chains import LLMChain
from langchain.schema import StrOutputParser

template = ChatPromptTemplate.from_messages(
  [
    SystemMessagePromptTemplate.from_template(
        content = ("You are a helpful assistant that translates {input_language} to {output_language}.")
        ),
    HumanMessagePromptTemplate.from_template("{text}"),
  ]
)

llm = HuggingFaceInterference(model_id="meta-llama/Llama-3.2-1B", max_new_tokens=1024)
llm(template.format(text="Hello", input_language="en", output_language="ne"))


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message.content}",
    ).send()
