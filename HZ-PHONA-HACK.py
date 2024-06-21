"""

Author:Gheris :)

"""
#!/usr/bin/python3
from pystyle import Colors, Colorate, Write #pip install pystyle
import requests # pip install requests
import os
from colorama import init, Fore # pip install colorama


os.system('cls' if os.name == 'nt' else 'clear')

# colors
init()
RED = Fore.BLACK
RED = Fore.GREEN

print(f"{RED} UYARI : {RED}Bunu başkalarına zarar vermek için kullanmayın! Bu script yalnızca eğitim amaçlıdır, şaka amaçlı değildir")
Write.Print("""
                                        HOŞGELDİNİZ.
    ARACIMIZA HOŞGELDİNİZ BU ARAÇ HZ.MAHOYA AİTTİR. KEYİFİNİZE BAKIN :)       
\n""",Colors.black_to_red, interval=0.01)
RED = Fore.RED
print(f"{RED} uyarı eğer bit hata varsa discorddan ulaşınız discord hz.maho.") 

def main():
    phone = Write.Input("[*] Mağdurun numarasını giriniz : ",Colors.green_to_black)
    print(f">>> {phone}")
    message = Write.Input("[*] MESAJINIZI GİRİP ENTERE BASINIZ. :",Colors.blue_to_black)
    print(f">>> {message}")
    resp = requests.post('https://textbelt.com/text', {
    'phone': f'{phone}',
    'message': f'{message}',
    'key': 'textbelt',
    })
    print("\n")
    print(f"{RED} {resp.json()}")


if __name__ == "__main__":
    main()
