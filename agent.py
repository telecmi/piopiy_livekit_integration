import logging
import os

from dotenv import load_dotenv
from livekit.agents import JobContext, WorkerOptions, cli, voice, llm
from livekit.plugins import openai, deepgram, silero

load_dotenv()

logger = logging.getLogger("voice-agent")
logger.setLevel(logging.INFO)

async def entrypoint(ctx: JobContext):
    # This will be triggered when the agent is dispatched to a room.
    # We connect to the room first.
    await ctx.connect()

    # Define the assistant's workflow.
    # In livekit-agents 1.x, we use voice.Agent and voice.AgentSession.
    instructions = (
        "You are a helpful voice assistant for TeleCMI. "
        "Your goal is to assist users with their telephony needs. "
        "When the call connects, greet the user briefly and ask how you can help."
    )

    chat_ctx = llm.ChatContext()
    chat_ctx.add_message(
        role="system",
        content=instructions,
    )

    assistant = voice.Agent(
        vad=silero.VAD.load(),
        stt=deepgram.STT(),
        llm=openai.LLM(),
        tts=openai.TTS(),
        chat_ctx=chat_ctx,
        instructions=instructions,
    )

    # Start the assistant session in the room.
    # In 1.x, we use AgentSession to manage the agent's interaction with the room.
    session = voice.AgentSession()
    await session.start(assistant, room=ctx.room)

    # A simple greeting when the agent starts the session.
    await session.say("Hello, this is the TeleCMI AI voice assistant. How can I help you today?", allow_interruptions=True)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(
        entrypoint_fnc=entrypoint,
        agent_name=os.getenv("AGENT_NAME", "my-agent"),
    ))