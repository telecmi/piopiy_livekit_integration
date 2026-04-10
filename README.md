# PIOPIY SIP Trunk with LiveKit Cloud Agent

This repository provides an example of how to integrate **PIOPIY SIP Trunks** with **LiveKit Cloud Agents** to create AI-powered voice assistants that can handle outbound PSTN calls.

## Features
- **Outbound Calling**: Automatically initiate calls to any phone number using PIOPIY SIP Trunks.
- **AI Voice Agent**: A Python-based LiveKit agent using OpenAI (LLM/TTS) and Deepgram (STT).
- **SIP Participant Integration**: Modern LiveKit SIP API usage to connect telephony with WebRTC rooms.
- **Room Dispatch**: Automatically dispatches the agent to the room when the call starts.

## Prerequisites
- [LiveKit Cloud](https://cloud.livekit.io/) account.
- [PIOPIY](https://dashboard.piopiy.com) SIP Trunk credentials.
- OpenAI API Key.
- Deepgram API Key.

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

## Usage

### 1. Start the Agent
The agent needs to be running to handle the voice interaction.
```bash
python3 agent.py dev
```

### 2. Initiate an Outbound Call
Run the call script to connect a phone number to your agent.
```bash
python3 call.py
```

## How it works
1. **`agent.py`**: Defines the LiveKit worker that listens for jobs. It uses Silero for VAD, Deepgram for STT, and OpenAI for LLM/TTS.
2. **`call.py`**: Uses the LiveKit API to:
   - Create a room.
   - Dispatch the agent to that room.
   - Initiate a SIP call through the PIOPIY trunk and join it to the room as a participant.
