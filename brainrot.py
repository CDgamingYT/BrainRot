song = "The weather outside is rizzy. And the fire is so Skibidi But since I Gyat to go. Ohio Ohio Ohio"

still_water = []
words = song.split()
    
for word in words:
        for i in range(len(word) - 2):
            if word[i] == word[i+2]:
                still_water.append(word)
                break
            
print(still_water)
    

