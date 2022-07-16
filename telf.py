
from telethon import TelegramClient
from time import sleep


# Get api ID/Hash From:
# https://my.telegram.org                
api_id = 111111111111111
api_hash = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

# Message ID
from_msgid = 1
to_msgid = 1000

# Channel
from_c = -1111111111
to_c = -222222222

#################################
#################################

async def main():
    counter,final,sec=[0,from_msgid,100]
    while final <= to_msgid:
        try :
            await client.forward_messages(to_c,list(range(from_msgid+counter, from_msgid+sec)),from_c)
            counter += 100
            sec += 100
            final += 100
            sleep(20)
        except Exception as e:
            print(e)
            stm=int(str(e).split(" ")[3])
            print(stm)
            sleep(stm)
        print(final)
    print("\n[+]Done!\n")

print("\n[#]Running...")
with TelegramClient('Eric', api_id, api_hash) as client:
    client.loop.run_until_complete(main())

#Enjoy :)
