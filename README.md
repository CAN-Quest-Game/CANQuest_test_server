# CANQuest Testing Server

To make development easier, we’ve provided a simple testing server that you can use to connect to the CANQuest game while building your own levels.
The server is a lightweight Python script that communicates with the game by sending and receiving commands.

## ⚙️ Setup

- Edit line 6 of the script to set your IP address.

   - Use '' for localhost (default).

## 🚀 Usage

- Run the script using Python 3:

```bash
  python test_server.py
```
- **Important:** After every connection, make sure to stop and restart the server to avoid issues with connectivity, sending, or receiving data.
