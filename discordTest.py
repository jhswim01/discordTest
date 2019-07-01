import discord
import asyncio

TOKEN_AUTH = "NTQzNDg3NjU4NTc2MzE0Mzc4.XQYW_g.59rk3zToDpqrunfUTFq0OvAl41Q"

client = discord.Client()

@client.event
async def on_ready():
    print(client.servers)
    print('connected to discord!')

@client.event
async def on_message(message):
    print('message has been arrived')
    print('message: '+message.content)
    print(message.channel.id)

    ch_id = message.channel.id

    if message.attachments:
      print('message has attachments')
      print(message.attachments)
      if message.author == client.user:
        print('message form myself')
        return
      elif message.author != client.user:
        if ch_id == "569181269603254288" or ch_id == "570075116059492367" or ch_id == "570772988656484402":
          print('Ignored: useless message')
          await client.send_message(client.get_channel("591641163812044817"), message.attachments[0]['url'])
          await client.send_message(client.get_channel("591641163812044817"), message.content)
          return
        elif ch_id == "526357317361336330":
          print('message from 내용업데이트-불고랩용')
          await client.send_message(client.get_channel("594223385236603025"), message.attachments[0]['url'])
          await client.send_message(client.get_channel("594223385236603025"), message.content)
          return
        elif ch_id == "569244221240770566":
          print('message from new-membership-only-global')
          await client.send_message(client.get_channel("594223526848757765"), message.attachments[0]['url'])
          await client.send_message(client.get_channel("594223526848757765"), message.content)
          return
        elif ch_id == "526348924840312832":
          print('message from announcement-public')
          await client.send_message(client.get_channel("594223877710938123"), message.attachments[0]['url'])
          await client.send_message(client.get_channel("594223877710938123"), message.content)
          return
        elif ch_id == "591641163812044817":
          print('message from channel-self')
          await client.send_message(client.get_channel("591641163812044817"), message.attachments[0]['url'])
          await client.send_message(client.get_channel("591641163812044817"), message.content)
          return
        else:
          print('meesage from nowhere')
          await client.send_message(client.get_channel("591641163812044817"), message.attachments[0]['url'])
          await client.send_message(client.get_channel("591641163812044817"), message.content)
          return
        return



    if message.author == client.user:
        print('message form myself')
        return
    elif message.author != client.user:
      if ch_id == "569181269603254288" or ch_id == "570075116059492367" or ch_id == "570772988656484402":
        print('Ignored: useless message')
        await client.send_message(client.get_channel("591641163812044817"), message.content)
        return
      elif ch_id == "526357317361336330":
        print('message from 내용업데이트-불고랩용')
        await client.send_message(client.get_channel("594223385236603025"), message.content)
        return
      elif ch_id == "569244221240770566":
        print('message from new-membership-only-global')
        await client.send_message(client.get_channel("594223526848757765"), message.content)
        return
      elif ch_id == "526348924840312832":
        print('message from announcement-public')
        await client.send_message(client.get_channel("594223877710938123"), message.content)
        return
      elif ch_id == "591641163812044817":
        print('message from channel-self')
        await client.send_message(client.get_channel("591641163812044817"), message.content)
        return
      else:
        print('meesage from nowhere')
        await client.send_message(client.get_channel("591641163812044817"), message.content)
        return
      return



client.run(TOKEN_AUTH, bot=False)





