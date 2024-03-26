import os
import webbrowser
import keyboard
import pydirectinput as pyd
from time import sleep
current_working_directory = os.getcwd()
def greetings():
    os.system('cls & title ANChecker')
    print("""
 ▄▄▄      ███▄    █  ▄████▄   ██░ ██ ▓█████ ▄████▄  ▀██ ▄█▀▓█████ ██▀███  
▒████▄    ██ ▀█   █ ▒██▀ ▀█ ▒▓██░ ██ ▓█   ▀▒██▀ ▀█   ██▄█▒ ▓█   ▀▓██ ▒ ██▒
▒██  ▀█▄ ▓██  ▀█ ██▒▒▓█    ▄░▒██▀▀██ ▒███  ▒▓█    ▄ ▓███▄░ ▒███  ▓██ ░▄█ ▒
░██▄▄▄▄██▓██▒  ▐▌██▒▒▓▓▄ ▄██ ░▓█ ░██ ▒▓█  ▄▒▓▓▄ ▄██ ▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
 ▓█   ▓██▒██░   ▓██░▒ ▓███▀  ░▓█▒░██▓░▒████▒ ▓███▀  ▒██▒ █▄░▒████░██▓ ▒██▒
 ▒▒   ▓▒█░ ▒░   ▒ ▒ ░ ░▒ ▒    ▒ ░░▒░▒░░ ▒░ ░ ░▒ ▒   ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓ ░▒▓░
  ░   ▒▒ ░ ░░   ░ ▒░  ░  ▒    ▒ ░▒░ ░ ░ ░    ░  ▒   ░ ░▒ ▒░ ░ ░    ░▒ ░ ▒░
  ░   ▒     ░   ░ ░ ░         ░  ░░ ░   ░  ░        ░ ░░ ░    ░     ░   ░ 
      ░           ░ ░ ░       ░  ░  ░   ░  ░ ░      ░  ░      ░     ░     
    Actually build v1.0.3 (26.03.2024)
    offical github - https://github.com/Anarchowitz/ANChecker
    """)
    sleep(2.6)
    os.system('pause')
    main()

def main():
    os.system('cls')
    try:
        print('Main Menu')
        print("""
        1. Проверка в игре. (авто-прожатие INSERT и т.д)
        2. Открыть папки (recent/appdata/temp и т.д)
        3. Программы для проверки (LastActivity и т.д)
        4. Открытие популярных сайтов
        [5]. Update Logs
        """)
        ans = input("Выбрано: ")
        if ans == '1':
            gamecheck()
        elif ans == '2':
            script_dir = os.path.dirname(os.path.abspath(__file__))
            print(script_dir)
            file_path = os.path.join(script_dir, 'assets', 'fileopenner.bat')
            print(file_path)
            os.startfile(file_path)
        elif ans == '3':
            appscheck()
        elif ans == '4':
            os.system('cls')
            print('Открываю сайты... \n УСПЕШНО!')
            webbrowser.open('http://oplata.info')
            webbrowser.open('http://midnight.im')
            webbrowser.open('http://neverlose.cc')
            webbrowser.open('http://xone.fun')
            print('[Сообщение проверяющему]: Проверьте почту/вк у подозреваемого!')
            os.system('pause & cls'); main()
        elif ans == '5':
            os.system('cls')
            print('UPDATE LOG!')
            print("""
        Update season 1:
            07.03.2024 -> Release version!
            08.03.2024 -> Remove useless function and false detection virus.
            09.03.2024 -> 
                  [V] Fixing path to assets folder.
                  [V] Add new signatures for finding cheats
                  [V] Added new CheatCheck function
                  [V] Some minor fixes...
        Update season 2:
            26.03.2024  ->
                  [V] Added new checker - "REGSCANNER".
                  [V] Fixed my mentality health 
        (гуи не будет)
(что бы вернуться назад нажмите любую кнопку)
        """)
            sleep(1.3)
            os.system('pause & cls') 
            main()
        else:
            os.system('cls') 
            for i in range(5):
                print('[ERROR] НАПИШИТЕ ЦИФРУ! (1-2)')
            sleep(3)
            os.system('cls') 
            main()
    except KeyboardInterrupt:
        os._exit(1)
active=False
def gamecheck():  # нажатие клавиш в игре  - ПОЛНЫЙ ГОВНОКОД НА КОСТЫЛЯХ
    os.system('cls')
    print('Pressing keys in game')
    def toggle_activation():
        global active
        active = not active
        if active:
            print('Начинаем цикл прожатия.')
        else:
            print('Цикл остановлен/Завершен!')
            os.system('pause & cls')
            main()
    keyboard.add_hotkey('insert', toggle_activation)
    keys_to_press = [
        ('decimal', 'del'),
        'fn',
        'home',
        ('ctrlleft', 'ctrlright'),
        'end',
        'pagedown',
        'pageup',
        'shiftright',
        'shiftleft',
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'insert'
    ]
    def keyspressing():
        if active:
                for key in keys_to_press:
                    if isinstance(key, str):
                        pyd.press(key)
                        print(f'Нажата клавиша: {key}')
                    else:
                        pyd.press(key[0])
                        print(f'Нажата клавиша: {key[1]}')
    while True:
        sleep(1)
        keyspressing()
def appscheck():
    path = 'assets'
    apps = {
        '1': 'Lastactivityview/LastActivityView',
        '2': 'Everything/Everything',
        '3': 'Openedfilesview/Openedfilesview',
        '4': 'ExecutedProgramms/ExecutedProgramsList',
        '5': 'HxD/HxD',
        '6': 'Userassistview/Userassistview',
        '7': 'Usbdeview/UsbDeview',
        '8': 'Shellbags/Shellbags',
        '9': 'BrowserDownloadsView/BrowserDownloadsView',
        '10': 'Regscanner/Regscanner'
    }
    os.system('cls') 
    print('Programs Menu')
    print("""
    1. Lastactivityview
    2. Everything
    3. Openedfilesview
    4. ExecutedProgramms
    5. HxD
    6. Userassistview
    7. Usbdeview
    8. ShellbagsAnalyzer
    9. BrowserDownloadsView
    10. RegScanner (Может быть распознан вирусом потому-что получает доступ к registry editor)
    ----------------------
    11. <- ВЕРНУТЬСЯ НАЗАД!
    """)
    ans = input("Выбрано: ")
    if ans == '11':
        main()
    elif ans in apps:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', apps[ans])
        os.startfile(program_path)
        sleep(1)
        os.system('cls') 
        appscheck()
    else:
        for _ in range(5):
            print('[ERROR] НАПИШИТЕ ЦИФРУ! (1-11)')
        sleep(3)
        os.system('cls') 
        appscheck()
if __name__ == "__main__":
        greetings()
