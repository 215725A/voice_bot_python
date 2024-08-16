import asyncio
import discord

z_digit = '１２３４５６７８９０'
h_digit = '1234567890'
z2h_digit = str.maketrans(z_digit, h_digit)
h2z_digit = str.maketrans(h_digit, z_digit)

async def join_voice_channel(client, message):
    if message.content == '!join':
        if message.author.voice is None:
            await message.reply("Please Join Voice Channel")
            return
        else:
            await message.author.voice.channel.connect()
            return

async def leave_voice_channel(client, message):
    if message.content == '!leave':
        if message.author.voice is None:
            await message.reply("Please Jon Voice Channel")
            return
        else:
            await message.guild.voice_client.disconnect()
            return

async def change_voice_speaker(client, voice_vox, message, process_message_command, speakers):
    if message.content == '!change':
        process_message_command[0] = True
        await message.reply("Please Type random or select")

        def check(m):
            return m.content in ['random', 'select'] and m.channel == message.channel

        try:
            msg = await client.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError:
            await message.reply(f"{message.author.mention} Operation Timed Out")
        else:
            if msg.content == 'select':
                speakers_info_text = f"Speakers Info: \n" + "\n".join([f"ID: {key}, Speaker: {value}" for key, value in speakers.items()])
                await message.reply(f"""
Please select one of the numbers below and enter the number.
{speakers_info_text}
""")
                def check_num(num):
                    try:
                        input_num = num.content
                        h_num = input_num.translate(z2h_digit)
                        return int(h_num) in voice_vox.speaker_ids and num.channel == message.channel
                    except:
                        return False
                
                try:
                    num_msg = await client.wait_for('message', check=check_num, timeout=30)
                    voice_vox.change_voice(msg.content, num_msg.content)
                    await message.reply('Changed Voice Vox Speaker')
                    await play_sound(client, message, process_message_command)
                except asyncio.TimeoutError:
                    await message.reply(f"{message.author.mention} Operation Timed Out")

            elif msg.content == 'random':
                voice_vox.change_voice(msg.content)
                await message.reply('Changed Voice Vox Speaker')
                await play_sound(client, message, process_message_command)
        
        process_message_command[0] = False

async def play_sound(client, message, process_message_command):
    wave_path = "../outputs/out.wav"
    process_message_command[0] = True
    voice_channel = message.guild.voice_client

    if voice_channel.is_playing():
        await message.channel.send("Already playing audio. Please wait for the current audio to finish.")
        process_message_command[0] = False
        return

    voice_channel.play(discord.FFmpegOpusAudio(wave_path), after=lambda e: print(f'Error: {e}') if e else None)
    process_message_command[0] = False