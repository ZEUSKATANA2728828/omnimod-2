import discord
from discord.ext import commands
from discord import app_commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    await tree.sync()
    print(f"🤖 OmniMod online como {bot.user}")

@tree.command(name="ping", description="Ver latência do bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"🏓 Pong! {round(bot.latency * 1000)}ms")

@tree.command(name="clear", description="Apagar mensagens")
async def clear(interaction: discord.Interaction, quantidade: int):
    if not interaction.user.guild_permissions.manage_messages:
        return await interaction.response.send_message("❌ Sem permissão!", ephemeral=True)

    await interaction.channel.purge(limit=quantidade)
    await interaction.response.send_message(f"🧹 {quantidade} mensagens apagadas!", ephemeral=True)

@tree.command(name="ban", description="Banir usuário")
async def ban(interaction: discord.Interaction, user: discord.Member, motivo: str = "Sem motivo"):
    if not interaction.user.guild_permissions.ban_members:
        return await interaction.response.send_message("❌ Sem permissão!", ephemeral=True)

    await user.ban(reason=motivo)
    await interaction.response.send_message(f"🔨 {user} foi banido. Motivo: {motivo}")

@tree.command(name="kick", description="Expulsar usuário")
async def kick(interaction: discord.Interaction, user: discord.Member, motivo: str = "Sem motivo"):
    if not interaction.user.guild_permissions.kick_members:
        return await interaction.response.send_message("❌ Sem permissão!", ephemeral=True)

    await user.kick(reason=motivo)
    await interaction.response.send_message(f"👢 {user} foi expulso. Motivo: {motivo}")

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
