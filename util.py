import json
from string import Template



def ParseAID(AIDString):
    AIDString = AIDString.replace("(","")
    AIDString = AIDString.replace(")","")
    AIDString = AIDString.strip()
    AIDList = AIDString.split()
    aid = AIDList[0]
    board = AIDList[1]
    return aid, board

def SaveUserJson(id, password, board, aid):
    aidInfo = aid + " (" + board + ")"
    data = {
        "id": id,
        "password": password,
        "aid": aidInfo
    }
    with open("user.json", "w") as f:
        json.dump(data, f)
        f.close()
    
def SetPushFormat(floor, pushType, author, time, content):
    t = Template('<font color="white"> $floor </font> <font color="white"> $pushType </font> <font color="yellow"> $author </font>                       <font color="white"> $time </font>\n <font color="yellow"> $content </font>')
    t.substitute(floor = str(floor), pushType = pushType, author = author, time = str(time), content = content)
    return str(t)
