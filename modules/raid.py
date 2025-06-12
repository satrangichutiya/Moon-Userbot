from pyrogram import Client, filters
import random
import asyncio

GALIS = [
    "Teri maa ka bhosda 💥",
    "Behen ke l*** 🤬",
    "Madarch*d tu to ultimate gandu nikla 😎",
    "BSDK tere jaise chutiye kam milte hain 😂",
    "Tere baap ki chaddi chura li re! 😜",
    "Tere ghar mein WiFi se zyada galiyan chalti hain! 📶",
    "Abey chup bc, tu rehne de! 🙄",
    "Ghar ja aur maa se seekh kaise baat karte hain 😤",
    "Tu paida hua ya system error se nikla be? 🧠",
    "Tere jaisa emoji bhi na aaye 😒",
    "Tere jaise toh public toilet mein likhe milte hain 🚽",
    "Aukaat se baat kar nalayak 🫵",
    "Mummy se permission leke gali dena be 👶",
    "Abe chirkut! Gandu detected 🤖",
    "Tera toh chaddi bhi duplicate nikla 🩲",
    "Tu 4G nahi, gandu hai fast wala 💨",
    "Maa ka broadband bandh kar de 📴",
    "Behen ki chut mein bomb daal dunga 💣",
    "Apni aukaat WhatsApp DP se kam mat dikhana 📱",
    "Tu toh iPhone mein bhi hang kare re 🤡",
    "Tere jaise log ke liye condoms free mein milte hain 😐",
    "Abe nalayak, tere jaise emoji bhi kaand karte hain 😂",
    "Baba Ramdev bhi tere muh se galiyan na nikaale 🧘",
    "Abe tu toh Google pe bhi nahi milta be 🫢",
    "Tu aur tera content dono hi bhakwas 🤮",
    "Bheekh maang ke paida hua tha kya? 🥴",
    "Tu log out ho ja, tera time khatam 💀",
    "Tere jaise logon se toh corona bhi darta tha 😷",
    "Teri maa ka front camera off hai kya? 📸",
    "Abe phuddu, tu zameen pe bojh hai! 🪨",
    "Teri aukaat toh YouTube ad ke skip button se kam hai ⏩",
    "Tu toh free fire mein bhi revive ke laayak nahi 😶",
    "Tera muh dekh ke chappal bhi mooh mod le 😂",
    "Tu toh chutiyaon ka chutiya nikla 🙈",
    "Tere jaisa bekaar aadmi toh khud Modi bhi chhod de 🙄",
    "Oye halli ke ande! 🥚",
    "Teri maa ki chut mein network nahi aata 📴",
    "Tera dimaag toh Airtel ke tower se bhi weak hai 📶",
    "Tu toh harami logon ka boss hai 😎",
    "Bhosdike tu toh Google Meet mein bhi fail hai 🤓",
    "Tu MC-BC ki dictionary hai kya? 📚",
    "Teri maa ka jigra dekh, tujhe janm diya 🤧",
    "Gandu! Tujhe toh delete kar dena chahiye 🤐",
    "Tu kaunsa virus hai be? Har jagah spread hota hai 😵",
    "Tu insaan nahi chirkut hai 😆",
    "Tere dimaag mein chawal ugte hain kya? 🌾",
    "Abe bhadwe, chup chap raid kha le 😤",
    "Behen ke lawde, tu baar baar milta kyu hai? 🤨",
    "Oye tere ko system format karna padega 🧽",
    "Tere jaisa banda toh recycle bin bhi reject kare 🗑️",
    "Tu online toh hai, par kaam ka nahi 🤷",
    "Tera IP address gaand mein ghusa dunga 💻",
    "Teri maa ki chut khule bazar mein 😏",
    "Tu toh software update se bhi thik nahi hoga ⚙️",
    "Tu gaali sun ke bhi pighal jaata hai 🧊",
    "Tera muh dekh ke toh mirror toot jaye 🪞",
    "Abe lund, tu toh emoji bhi na ban paaye 🫥",
    "Tujhe toh Roadies bhi reject kar de 🚫",
    "Tu reality show ka blooper hai 📺",
    "Bhosdike, apne muh mein gand daal aur chup reh 🤐",
    "Tu toh chutiyo ka bhi competition fail kare 🏆",
    "Teri maa ka USB port loose hai kya? 🔌",
    "Tu kaunsa error hai be? 404: Logic Not Found 🤖",
    "Tu hai ya Xerox copy ka failed printout 📄",
    "Abey chutiyon ke raja, kaise ho? 👑",
    "Teri maa ki chut mein router daal ke dekha kya? 🤔",
    "Tera password 'gandu123' hoga pakka 🔑",
    "Tu toh TED Talk mein bhi bakchodi kare 🗣️",
    "Tere jaisa banda toh Gaana pe bhi mute sunta hai 🎧",
    "Tu chutiyo ke WhatsApp group ka admin hai kya? 👨‍💻",
    "Tujh jaise logon pe toh God bhi facepalm kar le 🙏",
    "Tu insult proof hai kya? Ab tak zinda kaise hai 😵‍💫",
    "Tu toh toh chutiyo ka final form hai 💥",
    "Abe gaand mara hua meme hai tu 😆",
    "Behen ke lund! tu har jagah laanat hai 🌪️",
    "Tere muh se toh Hitler bhi pighal jaye 🙃",
    "MC BC ABCD... sab teri maa ki chut se aaye 🤯",
    "Oye teri aukaat Recycle Bin ke andhar bhi nahi 🚮",
    "Tujhe toh captcha bhi na pehchaane 😵",
    "Tu toh chutiyo ka version update hai 2.0 😜",
    "Tera career toh gand me chala gaya bhai 😭",
    "Tu toh overacting ka Oscar hai 🎭",
    "Tu jitna likhta hai usse accha gand maraata hai 💩",
    "Tu gaand mein calculator leke baitha hai kya? ➕",
    "Tu Windows XP jaisa outdated hai 💻",
    "Tere jaise chutiye dekh ke aliens bhi bhaag jaate hain 👽",
    "Tu bina gaali ke adhura hai 💔"
]

@Client.on_message(filters.command("raid", prefixes=".") & filters.me)
async def raid_gali(client, message):
    if len(message.command) > 1:
        target = " ".join(message.command[1:])
    else:
        target = "Gandu"

    await message.edit(f"🔫 Raiding {target}...\n🔥 Get ready for GALI ATTACK!")
    await asyncio.sleep(2)

    for i in range(15):
        await message.reply(random.choice(GALIS))
        await asyncio.sleep(1.2)
