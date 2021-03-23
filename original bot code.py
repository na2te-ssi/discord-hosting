import discord
import random

client = discord.Client()
hianswer = ["ㅎㅇ", "안녕", "반가워♪(^∇^*)", "ㅎㅇㅎㅇ", "하이~", "나도 ㅎㅇ~:wave:", "하이하이"]
byeanswer = ["잘있어", "또 올게~", "난 아직 여기 있다...<(＿　＿)>"]

@client.event
async def on_ready():
    print(client.user.id)
    print("Program is ready")


@client.event
async def on_message(message):
    if message.content.startswith("$안녕"):
        await message.channel.send(random.choice(hianswer))
    if message.content.startswith("$ㅎㅇ"):
        await message.channel.send(random.choice(hianswer))
    if message.content.startswith("$반가워"):
        await message.channel.send(random.choice(hianswer))
    if message.content.startswith("$하이"):
        await message.channel.send(random.choice(hianswer))
    if message.content.startswith("$하위"):
        await message.channel.send(random.choice(hianswer))
    if message.content.startswith("$안뇽"):
        await message.channel.send(random.choice(hianswer))
    if message.content.startswith("$얄로"):
        await message.channel.send(random.choice(hianswer))

    if message.content.startswith("$잘가"):
        await message.channel.send(random.choice(byeanswer))


client.run("NzI0NDY4MDk1Nzc4ODE2MDIw.XvAnfg.0uy9sMgEDcszRsLPwn8HGdtyftI")
