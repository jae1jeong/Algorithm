ML, MR, TL, TR = ('SPR'.index(i) for i in input().split())
'''
0 2
1 0
2 1
'''
if ML == MR and (ML+2) % 3 in [TL, TR]:
    print("TK")

elif TL == TR and (TL+2) % 3 in [ML, MR]:
    print("MS")

else:
    print("?")
