from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from gradio_tools.tools import BarkTextToSpeechTool, StableDiffusionTool, StableDiffusionPromptGeneratorTool
from langchain.memory import ConversationBufferMemory
from time import sleep

import os
os.environ["OPENAI_API_KEY"] = 'PASTE YOUR OPEN API KEY HERE'

sleep(10)
llm = OpenAI(temperature=0)
sleep(10)
memory = ConversationBufferMemory(memory_key='chat_history')
sleep(10)
tools = [BarkTextToSpeechTool().langchain,
         StableDiffusionTool().langchain,
         StableDiffusionPromptGeneratorTool().langchain]
sleep(10)

agent = initialize_agent(tools, llm, memory=memory, agent="conversational-react-description", verbose = True)
sleep(10)
output = agent.run(input=("Create a jingle for an south african company called 'Fatal Sweets' that makes tasty sweets."
                          "The tune must be and catch the audience of all the age groups"
                          "Save the file in .mp3 format or any other formats, if possible"
                          ))
sleep(10)
output = agent.run(input=("Create a logo from this company. Please improve"))
sleep(10)
output = agent.run(input=("Create a slogan from this company. Please improve"))