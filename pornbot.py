from re import sub
import discord, json, aiohttp, random, discord.ext
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import praw

client = commands.Bot(command_prefix=".",help_command=None, case_insensitive=True)

reddit = praw.Reddit(client_id='faXrkys5czbn-A',
                     client_secret='059OT4n2oYlDj8jwPqGPhFlmGEKsEQ',
                     user_agent="Chrome: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36")

@client.event
async def on_ready():
    print("Bot running with:")
    print("Username: ", client.user.name)
    print("User ID: ", client.user.id)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Type : .nudes help"))



@client.command(pass_context=True)
async def nudes(ctx, arg=None):
    if arg is None:
        memes_submissions = reddit.subreddit('porn').new()
        post_to_pick = random.randint(1, 100)
        for _ in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await ctx.send(submission.url)
    elif arg == "ass":
        memes_submissions = reddit.subreddit('ass').new()
        post_to_pick = random.randint(1, 100)
        for _ in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await ctx.send(submission.url)
    elif arg == "tits":
        memes_submissions = reddit.subreddit('tits').new()
        post_to_pick = random.randint(1, 100)
        for _ in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await ctx.send(submission.url)
    elif arg == "gif":
        memes_submissions = reddit.subreddit('sexgifs').new()
        post_to_pick = random.randint(1, 100)
        for _ in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await ctx.send(submission.url)
    elif arg == "help":
        em = discord.Embed(Title="PornBOT")
        em.add_field(name="Categorys", value="ass\ntits\ngif\nvideo\nHelp : .nudes help")
        em.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=em)
    elif arg == "video":
        memes_submissions = reddit.subreddit('nsfwvideos').new()
        post_to_pick = random.randint(1, 100)
        for _ in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await ctx.send(submission.url)





@client.command()
@has_permissions(administrator=True)
async def msg(ctx, *, args = None):
    await client.wait_until_ready()
    if args is None:
        message_content = "Please wait, we will be with you shortly!"

    else:
        message_content = "".join(args)

        em = discord.Embed(title="PornBOT", description=f"{message_content}")
        await ctx.send(embed=em)
        await ctx.message.delete()











client.run("")