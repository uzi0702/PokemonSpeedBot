import discord
from jaconv import hira2kata
from split_text import split_text

from pokemon import (
    resolve_pokemon_name,
    calc_speed,
    get_dict_id_of_pokemon
)
from api import get_speed

class PokeClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.poke_dict = get_dict_id_of_pokemon()

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if not message.content.startswith("!p"):
            return

        await message.channel.send("ポケモン名 [フォルム] 性格 を入力してください")

        def check(m):
            return m.channel == message.channel

        while True:
            msg = await self.wait_for("message", check=check)

            try:
                name, option, condition = self.parse_message(msg.content)
                api_name = resolve_pokemon_name(name, option, self.poke_dict)

                speed = get_speed(api_name)
                result = calc_speed(speed, condition)

                await message.channel.send(f"{name}:{condition}:{result}")

            except Exception:
                await message.channel.send("入力エラー")

    def parse_message(self, text):
        tokens = split_text(text)

        name = hira2kata(tokens[0])

        if len(tokens) >= 3:
            return name, tokens[1], tokens[2]
        return name, "", tokens[1]