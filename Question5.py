def f(Mainstream, must_watch):
    common = []
    not_common = []
    for i in Mainstream:
        if i in must_watch:
            common.append(i)
            must_watch.remove(i)
        else:
            not_common.append(i)
    
    for i in must_watch:
        not_common.append(i)
            
    return common, not_common


Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]

common, not_common = f(Mainstream, must_watch)

print(common)
print(not_common)
