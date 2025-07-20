def vertaal_emoji(zin, emoji_list):
    split_zin = zin.split()
    for index in range(0,len(split_zin)):
        for word, emoji in emoji_list:
            if word == split_zin[index]:
                split_zin[index] = emoji
    return " ".join(split_zin)
            
        