from docx import Document
import os
import shutil
#making destination directory
try:
    os.mkdir(os.environ['UserProfile']+'//desktop'+'//'+'Merage')
except:
    print("Directory exit")


def move_file(source_path,destination_path):
    try:
        for root,directory,file in os.walk(source_path):
    #     print(file)
            for i in file:
                if i.startswith("Assignment") or i.endswith(".docx"):

                    shutil.copy(os.path.join(root, i),destination_path)
    except: 
        print("Files exit")               
                
#Merge operation
def combine_word_documents(files):
    

    os.chdir(destination_path)
    files=os.listdir(files)  
    for file in files:
        print(file)  

    merged_document = Document()

    for index, file in enumerate(files):
        sub_doc = Document(file)

        # # Don't add a page break if you've reached the last file.
        if index <len(files)-1:
           sub_doc.add_page_break()

        for element in sub_doc.element.body:
            
            merged_document.element.body.append(element)

    merged_document.save(r'merge.docx')
    
    os.system(r'merge.docx')


source_path=os.environ['UserProfile']+'//desktop'                
destination_path=os.environ['UserProfile']+'//desktop//Merage'

move_file(source_path,destination_path)

combine_word_documents(destination_path) 

# for root,folder,file in os.walk(destination_path):
#     print(file)  
# print(os.listdir(destination_path)) 
# path=os.environ['UserProfile']+'//download//Merage.docx' 
