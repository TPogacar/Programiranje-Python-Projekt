import re
import requests


# sm dav class, ka se mi zdi, da bo za vnaprej najbolj primerno, sam za enkrat še ni tok...
# imena splemenljivk bi mogoče lahko ble bolše...
class SteamData:

    def __init__(self, userid):
        """
            initializira...
            dobi ID uporabnika, s katerim lahko pridemo do njegovih podatkov (njegovo stran)
        """
        self.steamUserID = userid
        self.steamProfileLink = requests.get("https://steamcommunity.com/profiles/" + userid)
        self.steamProfileText = self.steamProfileLink.text

        # ime uporabnika
        self.steamUserName = re.findall(r'<title>Steam Community :: .+</title>', self.steamProfileText)
        self.steamUserName = re.sub(r'<[^>]+>', "", self.steamUserName[0])
        self.steamUserName = re.sub(r'.+ :: ', "", self.steamUserName)
        print(self.steamUserName)

        # izpiše koliko iger ima uporabnik
        self.numberOfGamesOwned = re.findall(r"\d+ games owned", self.steamProfileText)
        self.numberOfGamesOwned = self.numberOfGamesOwned[0].split(" ")[0]
        print(self.numberOfGamesOwned)

    # mogoče posebi metoda da bi koda zgledala "bol urejena"
    #def getFriends(self):

        # gre na stran uporabnika, kjer so prikazani vsi njegovi prijatelji
        # poleg imen so bi lahko še dobila podatke za njihov ID, Profilno sliko,
        self.steamFriendsLink = requests.get("https://steamcommunity.com/profiles/" + userid + "/friends/")
        self.steamFriendsText = self.steamFriendsLink.text

        # dobi imena vseh prijateljev in jih shrani v tabelo
        self.steamFriendNames = re.findall(r'<div class="friend_block_content">.+<br>', self.steamFriendsText)
        self.steamFriendNames = [re.sub(r'<[^>]+>', "", name) for name in self.steamFriendNames]
        print(self.steamFriendNames, len(self.steamFriendNames))

        # dobi ID
        self.steamFriendIDs = re.findall(r'data-steamid="\d+"', self.steamFriendsText)
        self.steamFriendIDs = [re.sub(r'[^0-9]+', "", ID) for ID in self.steamFriendIDs]
        print(self.steamFriendIDs, len(self.steamFriendIDs))

        # zdej ka mava ID od vseh bi lahko za vsakega
        #for ID in self.steamFriendIDs:
            #SteamData(ID)
        # sam morva še dodat, da se enkrat prekine



# ID mojga Steam Accounta ("Ajax")
userID = "76561198069577640"
SteamData(userID)

# tko za enkrat neki malga narejenga
# dela:D
