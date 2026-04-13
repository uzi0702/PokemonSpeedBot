import discord
import bot_token as token
from client import PokeClient

def main():
    intents = discord.Intents.default()
    intents.message_content = True

    client = PokeClient(intents=intents)
    client.run(token.token)

if __name__ == "__main__":
    main()