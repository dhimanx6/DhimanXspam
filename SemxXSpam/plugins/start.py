from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from .. import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, OWNER_ID
from SemxXSpam.plugins.help import *


RYAN_IMG = "https://te.legra.ph/file/91d82bf74b7a75468f5ef.jpg"

Ryan_Button = [
        [
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/AcR_ChaTTinG")
        ],
        [
        Button.inline("⚡ ᴄᴏᴍᴍᴀɴᴅs ⚡", data="help_back")
        ]
        ]
               
RyanX_Button = [
        [
        Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/ABOUT_DHIMAN_X"),
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/w_o_d_x")
        ],
        [
        Button.url("🔥 ʀᴇᴘᴏ 🔥", "https://telegra.ph/file/ce8efab574dd85199b3f3.jpg")
        ]
        ]
        
        
#USERS 


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RyanBot = await event.client.get_me()
       bot_name = RyanBot.first_name
       bot_id = RyanBot.id
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRyan = event.chat_id
       firstname = replied_user.user.first_name
       userid = replied_user.user.id
       ownermsg = f"**Hello Boss !!, It's Me {bot_name}, Your Spam Bot !! \n\n Click Below Buttons For Help. 🌚**"
       usermsg = f"**Hello !! [{firstname}](tg://user?id={userid})\nNice To Meet You, Well I Am [{bot_name}](tg://user?id={bot_id}), A Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From The Button Given Below.** \n\n**Powered By : [𝘿𝙃𝙄𝙈𝘼𝙉 𝙓 𝙎𝙋𝘼𝙈](https://t.me/Dhiman_xx)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheRyan,
                  RYAN_IMG,
                  caption=ownermsg, 
                  buttons=Ryan_Button)
       else:
            await event.client.send_file(TheRyan,
                  RYAN_IMG,
                  caption=usermsg, 
                  buttons=RyanX_Button)
                

