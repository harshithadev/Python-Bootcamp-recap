# Project 25 : Practice what we learned : Story Generator. 
story_line = ""                                                                              
story = ""
while(True):
    story_line = input("Whar is on your mind? ")
    if story_line == "the end" :
        break
    story += story_line.rstrip()+". "
print(story)
    
