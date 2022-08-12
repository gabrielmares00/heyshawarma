import discord
import os
import traceback

from discord.ext import commands


def list_module(directory):
    return (f for f in os.listdir(directory) if f.endswith('.py'))


class HeyShawarma(commands.Bot):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="hs.", intents=intents, *args, **kwargs)

    async def setup_hook(self) -> None:
        moduleFolders = ['commands']
        for module in moduleFolders:
            for extension in list_module(module):
                extensionToLoad = f'{module}.{os.path.splitext(extension)[0]}'
                try:
                    await self.load_extension(extensionToLoad)
                    print(f'Loaded module extension {extensionToLoad}')
                except Exception:
                    print(f'Failed to load module {extensionToLoad}', file=sys.stderr)
                    traceback.print_exc()
