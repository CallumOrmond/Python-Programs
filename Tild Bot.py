import discord
#Ashdra#2712

client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if msg.startswith("£save"):
        fileSave(msg[6:])
        

    if msg.startswith("£show"):
        
        for i in fileRead():
            if "www" in i:
                await message.channel.send("<" + i[:-1] + ">") 
            else:
                await message.channel.send(i[:-1]) 

    if msg.startswith("£deleteall"):
        fileClear()
        await message.channel.send("Cleared") 
        return

    if msg.startswith("£help"):
        await message.channel.send("£save - saves the text after the command") 
        await message.channel.send("£show - shows all the saved text")
        await message.channel.send("£delete - deletes the line according the number beside the command, e.g £delete 1") 
        await message.channel.send("£deleteall - clears the all the saved text")   


    if msg.startswith("£delete"):

        delint = int(msg[8:]) - 1
        counter = 0
        saves = fileRead()
        fileClear()

        for i in saves:
            if counter != delint:
                fileSave(i[:-1])
                counter = counter + 1

            else:
                counter = counter + 1


    
def fileSave(msg):
    f = open("saves.txt", "a")
    f.write(msg + "\n")
    f.close()
    

def fileClear():
    f = open("saves.txt", "w")
    f.write("")
    f.close()

def fileRead():
    f = open("saves.txt", "r")
    values = f.readlines()
    return values
     
    





client.run('ODU1OTQ3NTIxNjk0ODkyMDQy.YM55Pw.XeISt8dc9f6MQrC0cstO32jlFfE')