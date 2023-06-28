
def extract_Image_from_Html(img,target_folder="images",filename="test"):
    
    

    
    filetypes=["png","jpg","jpeg","pdf","svg"]
    
    if img[:4]=="data":
        
        filetype,img=img.split(",",1)
        filetype=filetype.split(";")
        filetype=filetype[0].replace("data:image/","").replace("svg+xml","svg")
        if filetype in filetypes:
            print(filetype)                
            import base64
            img=base64.b64decode(img)
            print(filename)
            with open(f"{target_folder}/{filename}.{filetype}", "wb") as fh:
                fh.write(img)
                
            print("image generated.")
        else:
            print(filetype)
        return 
    


def removeIMGs(Content,write_img=False, targetFolder="images",IMG_filename="test"):
    tags=Content.findAll('img')
    
    for count, match in enumerate(tags):
        img=match["src"]
        filename=IMG_filename+"_"+str(count)
        
        if write_img==True:
            extract_Image_from_Html(img,target_folder=targetFolder,filename=filename) 
        
        match['src']=f'deleted: {filename}'
       # print(f"image removed: {filename}")
    return Content