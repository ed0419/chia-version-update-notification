import requests,time
from bs4 import BeautifulSoup
def notify(id,gotinfo):
    if id==1:
        message = "Chia Updated LINK:\n"
    else:
        message = "OK"
    token = "your line notify token"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"}
    payload = {'message': message + gotinfo}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
while 1:
    try:
        r = requests.get("https://github.com/Chia-Network/chia-blockchain/releases/latest", allow_redirects=False) #將網頁資料GET下來
        soup = BeautifulSoup(r.text,"html.parser") 
        sel = soup.select("a") 
        for s in sel:
            gotinfo=s["href"]

        file1 = open("lastVer.txt","r+") 
        if file1.read() != gotinfo:
            print("No, sending message to LINE.",time.ctime())
            notify(1,gotinfo)
            file1.close()
            file1 = open("lastVer.txt","w")
            file1.write(gotinfo)
        elif file1.read() == gotinfo:
            print("YES")
        else:
            print("ok",time.ctime())
        time.sleep(3600)
    except:
        break


