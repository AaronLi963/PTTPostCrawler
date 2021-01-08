import json

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