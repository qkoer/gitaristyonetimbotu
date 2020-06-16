# @qkoer tarafindan sevdiklerinize sunulmuştur.

from telethon import events

import asyncio

from userbot.events import register

@register(outgoing=True, pattern="^!seviyorum")

async def merkurkedissa(event):

    if event.fwd_from:

        return

    animation_interval = 0.8

    animation_ttl = range(0, 14)

    await event.edit("kralicem")

    animation_chars = [
        
            "💕S💕",
            "💕Se💕",
            "💕Sen💕",
            "💕Seni💕",
            "💕Seni 💕",
            "💕Seni s💕",
            "💕Seni se💕",
            "💕Seni sev💕",
            "💕Seni sevi💕",
            "💕Seni seviy💕",
            "💕Seni seviyo💕",
            "💕Seni seviyor💕",
            "💕Seni seviyoru💕",
            "💕Seni seviyorum💕"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 14])