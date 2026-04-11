import asyncio
import os
import uuid
import json
from dotenv import load_dotenv

from livekit import api

load_dotenv()

async def main():
    livekit_api = api.LiveKitAPI()

    room_name = os.getenv("ROOM_NAME", "demo-room")
    trunk_id = os.getenv("SIP_TRUNK_ID")
    to_number = os.getenv("TO_NUMBER")
    agent_name = os.getenv("AGENT_NAME", "my-agent")

    print(f"🚀 Initiating outbound call to {to_number} in room {room_name}")

    # 1. Dispatch the agent to the room first
    # Since you created the agent in the LiveKit UI, this command tells 
    # LiveKit Cloud to send that agent into the room.
    try:
        dispatch = await livekit_api.agent_dispatch.create_dispatch(
            api.CreateAgentDispatchRequest(
                agent_name=agent_name,
                room=room_name,
            )
        )
        print(f"✅ Cloud Agent '{agent_name}' dispatched (ID: {dispatch.id})")
    except Exception as e:
        print(f"⚠️ Agent dispatch failed: {e}")
        print("   Make sure the Agent Name in the UI matches AGENT_NAME in .env")

    # 2. Create the SIP participant
    try:
        resp = await livekit_api.sip.create_sip_participant(
            api.CreateSIPParticipantRequest(
                sip_trunk_id=trunk_id,
                sip_call_to=to_number,
                room_name=room_name,
                participant_identity=f"sip_{uuid.uuid4().hex[:6]}",
                participant_name="Outbound Call",
                wait_until_answered=True,
            )
        )
        print("✅ SIP Call initiated")
        print(resp)
    except Exception as e:
        print(f"❌ SIP Call failed: {e}")

    await livekit_api.aclose()

if __name__ == "__main__":
    asyncio.run(main())