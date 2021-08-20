import vk_api, os, sys, time
from vk_api import VkUpload
from python_json_config import ConfigBuilder
from colorama import init, Fore
init()

a = 1
banner = """
╭━━━╮╱╱╱╱╭╮╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱┃┃╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╭╯╰╮
┃┃╱┃┣╮╭┳━╯┣┳━━╮┃╰━━┳━━┳━┳┳━┻╮╭╯
┃╰━╯┃┃┃┃╭╮┣┫╭╮┃╰━━╮┃╭━┫╭╋┫╭╮┃┃
┃╭━╮┃╰╯┃╰╯┃┃╰╯┣┫╰━╯┃╰━┫┃┃┃╰╯┃╰╮
╰╯╱╰┻━━┻━━┻┻━━┻┻━━━┻━━┻╯╰┫╭━┻━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯\n"""

builder = ConfigBuilder()
config = builder.parse_config('config.json')


vks = vk_api.VkApi(token=config.token)
vk = vks.get_api()
upload = VkUpload(vks)

while True:
	try:
		upload.audio(
			audio="audio.mp3",
			artist=config.artist,
			title=config.title)
		os.system('clear||cls')
		print(Fore.MAGENTA + banner + Fore.BLUE + "Author: Klimenko\n")
		print(Fore.GREEN + "Загруженно музыки: " + str(a))
		a += 1
	except Exception as e:
		os.system('clear||cls')
		print(Fore.RED + banner + f"[{str(a)}] Err! " + str(e))
		a += 1
		time.sleep(30)