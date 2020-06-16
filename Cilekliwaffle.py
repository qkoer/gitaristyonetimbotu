# @qkoer tarafindan can sıkıntısı nedeniyle cikekliwaffle’ye yapilmistir.

from telethon import events

import asyncio
from userbot.events import register

@register(outgoing=True, pattern="^.cilekliwaffle")

async def cilekliwaffle(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 12)
    animation_chars = [
            "❤️cilekliwaffle mukemmel biridir❤️",
            "💕❤️cilekliwaffle dokunulmazdir",
            "💙💕❤️cilekliwaffle cooook tatliii❤️💙💕",
            "💚💙💕❤️cilekliwaffle cok guzeeel❤️💕💙💚", 
            "💛💚💙💕❤️Kimse bir cilekliwaffle edemez❤️💕💙💚💛",
            "🧡💛💚💙💕❤️cilekliwaffle gitaristbey seni seviyor❤️💕💙💚💛🧡",
            "🖤🧡💛💚💙💕❤️cilekliwaffle seni yeriim❤️💕💙💚💛🧡🖤",
            "❤️, 
            "❤️💕", 
            "❤️💕💙",
            "❤️💕💙💚", 
            "💚💙💕❤️Asırı tatlısın💚💙💕❤️"

    ]
    for i in animation_ttl:
        
        await asyncio.sleep(animation_interval)
        
        await event.edit(animation_chars[i % 12])