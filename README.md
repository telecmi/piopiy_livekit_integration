# PIOPIY SIP Trunk with LiveKit Cloud Agent

This repository provides an example of how to integrate **PIOPIY SIP Trunks** with **LiveKit Cloud Agents** (Voice Pipeline) to create AI-powered voice assistants that can handle outbound PSTN calls.

## Features
- **Outbound Calling**: Automatically initiate calls to any phone number using PIOPIY SIP Trunks.
- **Cloud-Hosted Agent**: Managed via LiveKit Cloud Dashboard (No local worker required).
- **SIP Participant Integration**: Modern LiveKit SIP API usage to connect telephony with WebRTC rooms.
- **Room Dispatch**: Automatically dispatches your pre-configured Cloud Agent to the room when the call starts.

## Prerequisites
- [LiveKit Cloud](https://cloud.livekit.io/) account.
- [PIOPIY](https://dashboard.piopiy.com) SIP Trunk credentials.
- A **Voice Pipeline Agent** created in the LiveKit Cloud dashboard.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/telecmi/piopiy_livekit_integration.git
   cd piopiy_livekit_integration
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Copy `.env.example` to `.env` and fill in your credentials:
   ```bash
   cp .env.example .env
   ```
   > [!IMPORTANT] 
   > Ensure the `AGENT_NAME` matches the name of the agent you created in the LiveKit Cloud UI.

## Usage

### 1. Configure your Agent in UI
Go to your [LiveKit Cloud Dashboard](https://cloud.livekit.io/), navigate to **Agents**, and create a new **Voice Pipeline** agent. This allows you to configure instructions, LLM, and voice settings without managing any local code.

### 2. Initiate an Outbound Call
Run the call script to connect a phone number to your Cloud Agent.
```bash
python3 call.py
```

## How it works
1. **`call.py`**: Uses the LiveKit API to:
   - Create a room.
   - **Dispatch** your Cloud-hosted agent to that room by name.
   - Initiate a SIP call through the PIOPIY trunk and join it to the room as a participant.
2. The agent handles the audio processing (STT, LLM, TTS) entirely in the cloud, requiring zero local compute or complex worker infrastructure.
