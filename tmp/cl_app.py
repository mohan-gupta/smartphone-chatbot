import chainlit as cl

from agent import smartphone_assistant

@cl.on_chat_start
async def main():
    await cl.Message(content="Hello, How can I assit you!").send()
    
@cl.on_message
async def recieve_message(message: cl.Message):
    try:
        ai_response = await smartphone_assistant(query=message.content)
        await cl.Message(ai_response).send()
    except Exception:
        await cl.Message("Please try again.").send()