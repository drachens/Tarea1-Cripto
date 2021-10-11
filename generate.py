text_i = "aAA@@@33"
text_r = ""
k = open("generate.txt","w")
while(len(text_r)<64*32):
    text_r = text_r+text_i
k.write(text_r)
k.close()