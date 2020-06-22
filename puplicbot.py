import discord
import asyncio
from discord import Guild, message, Member, User

import os
import sys

client = discord.Client()

###############################################################################################

# DEFAULT: 0,
# AQUA: 1752220,
# GREEN: 3066993,
# BLUE: 3447003,
# PURPLE: 10181046,
# GOLD: 15844367,
# ORANGE: 15105570,
# RED: 15158332,
# GREY: 9807270,
# DARKER_GREY: 8359053,
# NAVY: 3426654,
# DARK_AQUA: 1146986,
# DARK_GREEN: 2067276,
# DARK_BLUE: 2123412,
# DARK_PURPLE: 7419530,
# DARK_GOLD: 12745742,
# DARK_ORANGE: 11027200,
# DARK_RED: 10038562,
# DARK_GREY: 9936031,
# LIGHT_GREY: 12370112,
# DARK_NAVY: 2899536,
# LUMINOUS_VIVID_PINK: 16580705,
# DARK_VIVID_PINK: 12320855

################################################################################################

autoroles = {
    718493315405840495: {'memberroles': [719112492881674260], 'botroles': [718793348688773220]}

}


@client.event
async def on_ready():
    print('Der Bot ist eingeloggt als User -> {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('⋙ Vision Crapter ⋘'), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game('》+help《'), status=discord.Status.online)
        await asyncio.sleep(5)


@client.event
async def on_member_join(member):
    guild: Guild = member.guild
    if not member.bot:
        channel = discord.utils.get(member.guild.channels, name="")  # <--- Channel-Name
        embed = discord.Embed(title="⋙ Form-Writer ⋘", color=1752220)

        embed.set_footer(text="[]")
        embed.set_thumbnail(url=f"{member.avatar_url}")
        mess = await channel.send(embed=embed)
        guild: Guild = member.guild

        autoguild = autoroles.get(member.guild.id)
        if autoguild and autoguild['memberroles']:
            for roleId in autoguild['memberroles']:
                role = guild.get_role(roleId)
                if role:
                    await member.add_roles(role, reason='AutoRoles', atomic=True)
    else:
        autoguild = autoroles.get(member.guild.id)
        if autoguild and autoguild['botroles']:
            for roleId in autoguild['botroles']:
                role = guild.get_role(roleId)
                if role:
                    await member.add_roles(role, reason='AutoRoles', atomic=True)

@client.event
async def on_message(message):
    if message.content.startswith('!userinfo'):
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                                      description='Dies ist eine Userinfo für den User {}'.format(member.mention),
                                      color=0x22a7f0)
                embed.add_field(name='Server beigetreten', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                embed.add_field(name='Discord beigetreten', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                rollen = ''
                for role in member.roles:
                    if not role.is_default():
                        rollen += '{} \r\n'.format(role.mention)
                if rollen:
                    embed.add_field(name='Rollen', value=rollen, inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text='Ich bin ein EmbedFooter.')
                mess = await message.channel.send(embed=embed)



client.run("NzI0NjA4OTc2MjU1MzIwMTI1.XvCqxg.guGIfv2NjQBuNpsOzaW-exwtAcM")
