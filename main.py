import os
import ctypes
from time import sleep
def clearscreen():
    os.system('cls & title HelinChecker')
def main():
    clearscreen()
    try:
        print('HELIN PROJECT')
        print("""
        1. Открыть папки (recent/appdata/temp и т.д)
        2. Программы для проверки
        """)
        ans = input("Выбрано: ")
        if ans == '1':
            path = 'C:/HelinChecker/assets'
            os.startfile(path + '/fileopenner.bat')
            return main()
        elif ans == '2':
            appscheck()
        else:
            clearscreen()
            for i in range(5):
                print('[ERROR] НАПИШИТЕ ЦИФРУ! (1-2)')
            sleep(3)
            clearscreen()
            main()
    except KeyboardInterrupt:
        os._exit(1)
def appscheck():
    path = 'C:/HelinChecker/assets'
    apps = {
        '1': 'Lastactivityview/LastActivityView',
        '2': 'Everything/Everything',
        '3': 'Openedfilesview/Openedfilesview',
        '4': 'ExecutedProgramms/ExecutedProgramsList',
        '5': 'HxD/HxD',
        '6': 'Userassistview/Userassistview',
        '7': 'Usbdeview/UsbDeview',
        '8': 'Shellbags/Shellbags'
    }
    clearscreen()
    print('HELIN PROJECT')
    print("""
    1. Lastactivityview
    2. Everything
    3. Openedfilesview
    4. ExecutedProgramms
    5. HxD
    6. Userassistview
    7. Usbdeview
    8. ShellbagsAnalyzer
    ----------------------
    9. <- ВЕРНУТЬСЯ НАЗАД!
    """)
    ans = input("Выбрано: ")
    if ans == '9':
        main()
    elif ans in apps:
        os.startfile(os.path.join(path, apps[ans]))
        sleep(1)
        clearscreen()
        appscheck()
    else:
        for _ in range(5):
            print('[ERROR] НАПИШИТЕ ЦИФРУ! (1-7)')
        sleep(3)
        clearscreen()
        appscheck()
def is_admin():
   try:
     return os.getuid() == 0
   except AttributeError:
     return ctypes.windll.shell32.IsUserAnAdmin() != 0
if __name__ == "__main__":
    if is_admin() == True:
        main()
    else:
        for i in range(5):
            print("[ERROR] ЗАПУСТИТЕ ФАЙЛ С ПРАВАМИ АДМИНИСТРАТОРА")
        sleep(3)
        os._exit(1)
