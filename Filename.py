filename=input("Input the filename :")
filist=filename.split(".")
if(len(filist)==2):
    if(filist[1]=="py"):
       print("The extension of the file is : 'Python'")
    elif(filist[1]=="java"):
        print("The extension of the file is :'Java'")
    elif(filist[1]=="wbpj"):
        print("The extension of the file is :'Ansys'")
else:
    print("Invalid filename")
    

