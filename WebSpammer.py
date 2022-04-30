import requests
from discord import Webhook, RequestsWebhookAdapter
import colorama
from colorama import Fore
import threading


colorama.init()
def WebHook():
 url = input("WebHook: \n")
 print(f" ")
 mensagem = input("Mensagem: ")
 threading.Thread(target=WebHook).start()
 while True:
  webhook = Webhook.from_url(f"{url}", adapter=RequestsWebhookAdapter())
  webhook.send(f"{mensagem}")
  print(f"{Fore.GREEN}[+] Web-Spammer")
print(f"""

{Fore.MAGENTA} ██████╗  █████╗ ██████╗ ██╗  ██╗███╗   ███╗ ██████╗ ██████╗ ███████╗
{Fore.MAGENTA} ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝████╗ ████║██╔═══██╗██╔══██╗██╔════╝
{Fore.MAGENTA} ██║  ██║███████║██████╔╝█████╔╝ ██╔████╔██║██║   ██║██║  ██║█████╗  
{Fore.MAGENTA} ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  
{Fore.MAGENTA} ██████╔╝██║  ██║██║  ██║██║  ██╗██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗
{Fore.MAGENTA} ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                                                                                                                                                        
{Fore.MAGENTA} ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗
{Fore.MAGENTA} ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
{Fore.MAGENTA} ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
{Fore.MAGENTA} ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
{Fore.MAGENTA} ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
{Fore.MAGENTA} ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
{Fore.WHITE}
                                                                """)
WebHook()
