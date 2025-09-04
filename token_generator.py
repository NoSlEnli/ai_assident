import requests

SANDBOX_ID = "your livekit sandbox key"
API_URL = "your Livekit URL"

def get_sandbox_token(room_name: str = None, participant_name: str = None) -> dict:
    payload = {}

    if room_name:
        payload["roomName"] = room_name
    if participant_name:
        payload["participantName"] = participant_name

    headers = {
        "X-Sandbox-ID": SANDBOX_ID,
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.ok:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    room = input("Enter room name (optional): ").strip()
    name = input("Enter participant name (optional): ").strip()

    try:
        result = get_sandbox_token(
            room_name=room if room else None,
            participant_name=name if name else None
        )

        print("\n✅ Paste this info into LiveKit Playground (Manual tab):")
        print("WebSocket URL:", result["serverUrl"])
        print("Room Name    :", result["roomName"])
        print("Participant  :", result["participantName"])
        print("Token        :", result["participantToken"])

    except Exception as e:
        print("❌ Failed to get token:", e)

