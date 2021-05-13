import discord

client = discord.Client()

emojis = ["🚫","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","⬆️"]

@client.event
async def on_message(message):
    
    if message.author == client.user:
        for emoji in emojis:
            await message.add_reaction(emoji)
    else:

        if message.content == "test":
            await message.channel.send("Tested successfully")

        if message.content.startswith(".sc"):
            botName = message.content[4:]
            embed = discord.Embed(title=(botName + " Stock Check"), description="Please react with the number of copies you are holding.")
            await message.channel.send(embed=embed)

client.run("KEY")
