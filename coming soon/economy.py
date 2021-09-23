async def open_account(user):
    with open("bank.json", "r") as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 100 

    with open("bank.json", "w") as f:
        json.dump(users,f) 
    return True         


async def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)

    return users  

async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()   

    users[str(user.id)][mode] += change 
    
    with open("bank.json", "w") as f:
        json.dump(users,f) 
    
    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal      


@client.command(name="withdraw", aliases=["with"])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Hey Dumbo You Gotta WithDraw An Amount Duh")
        return
        
    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[1]:
        await ctx.send("Ayo You Poor ASF MAN!")
        return

    if amount<bal[0]:
        await ctx.send("You Want 0 Man stfu")
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount, "bank")

    await ctx.send(f"You Withdrew ${amount}!")

@client.command(name="deposit", aliases=["dep"])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Hey Dumbo You Gotta Deposit An Amount Duh")
        return
        
    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("Ayo You Poor ASF MAN!")
        return

    if amount<bal[0]:
        await ctx.send("You Want To Deposit $0 Man stfu")
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount, "bank")

    await ctx.send(f"You Deposited ${amount}!")


@client.event
async def on_ready():
    print("Economy Is Working Fine :EpicFace:")

@client.command(name="balance", aliases=["bal"])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]  
##Make Embeds More Cool lmao
    em = nextcord.Embed(title = f"{ctx.author.name}'s Balance", color = nextcord.Color.blue())
    em.add_field(name = "Wallet",value = wallet_amt)
    em.add_field(name = "Bank",value = bank_amt)
    await ctx.send(embed = em)


@client.command()
async def beg(ctx):
    await open_account(ctx.author)

    user = ctx.author
    
    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f"Someone Gave You ${earnings}!")
    
    users[str(user.id)]["wallet"] += earnings

    with open("bank.json", "w") as f:
        json.dump(users,f) 