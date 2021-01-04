
def ParseAID(AIDString):
    AIDString = AIDString.replace("(","")
    AIDString = AIDString.replace(")","")
    AIDString = AIDString.strip()
    AIDList = AIDString.split()
    aid = AIDList[0]
    board = AIDList[1]
    return aid, board