# This automatically takes a picture every 10 seconds and uploads to Dropbox
import cv2
import time
import random
import dropbox

start_time = time.time()
def take_picture():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "image" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time()
        result = False

    return img_name
    print("Picture taken!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_image(img_name):
    access_token = 'sl.BGTbr13diEbEsAZbw0iVBKYWWywFwI82pp7yNn-TP24l0_Xf3EvHd3wWpWQpH1QrqK_-LJ-fI_Kz0ygIsxhm0ZnCPoXuQ2dlWEezMSqFQBbtIya7jnNgyt79RqRY6jGay46wyj4'
    file = img_name
    file_from = file
    file_to = "/pictureFolder/" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print(file_amount)
        print("File uploaded!")

def main():
    while(True):
        if((time.time() - start_time) >= 10):
            name = take_picture()
            upload_image(name)

main()