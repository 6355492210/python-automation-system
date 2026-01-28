import os #files handle
import shutil #files move

def organize_files():
    print("File automation started")

    source_folder = "Downloads"

    if not os.path.exists(source_folder): #folder exit kre che k ny
        print("Downloads folder not found")
        return

    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name) #full file banavase

        if os.path.isfile(file_path): #file che k ny check krse
            # Images
            if file_name.lower().endswith((".jpg", ".png", ".jpeg")): # img file check
                os.makedirs("Images", exist_ok=True) #img folder create, hse to skip
                shutil.move(file_path, os.path.join("Images", file_name)) #file ne move krse
                print(f"Moved image: {file_name}")

            # Documents
            elif file_name.lower().endswith(".pdf"): #.pdf file check
                os.makedirs("Documents", exist_ok=True)
                shutil.move(file_path, os.path.join("Documents", file_name)) #pdf move
                print(f"Moved document: {file_name}")

    print("File automation completed")
0
if __name__ == "__main__":
    organize_files()