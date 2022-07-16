
try:
    from telethon import TelegramClient
except:
    from os import system
    system("pip install telethon")
finally:
    from telethon import TelegramClient
from time import sleep


# Get api ID/Hash From:
# https://my.telegram.org                
api_id = 111111111111               
api_hash = 'aaaaaaaaaaaaaaaaaaaa'

# Message ID
from_msgid = 1
to_msgid = 1000

# Channel
from_c = -111111111111111
to_c = -111111111111111

#Code
async def main():
    counter,final,sec=[0,from_msgid,100]
    while final <= to_msgid:
        try :
            await client.forward_messages(to_c,list(range(from_msgid+counter, from_msgid+sec)),from_c)
            counter += 100
            sec += 100
            final += 100
            sleep(5)
        except Exception as e:
            print(e)
            stm=int(str(e).split(" ")[3])
            print(f"\n[!]Banned From Server For: {stm} sec. plz w8.\n")
            sleep(stm)
        print(final)
    print("\n[+]Done!\n")

if __name__=="__main__":
    print("\n[#]Running...")
    with TelegramClient('session', api_id, api_hash) as client:
        client.loop.run_until_complete(main())

