import os
from datetime import datetime
import requests
from pathlib import Path

cookie = '_ga=GA1.1.1534479515.1703739297; EudicWebSession=QYNeyJoYXNfb2xkX3Bhc3N3b3JkIjpmYWxzZSwidG9rZW4iOiIyak52YklSUVVhejAreVAyTVBTSnVBUFlEVTg9IiwiZXhwaXJlaW4iOjEzMTQwMDAsInVzZXJpZCI6IjkyZmQ5ZjIzLWIwM2ItMTFlYy1iYjMyLTAwNTA1Njg2OWFmNiIsInVzZXJuYW1lIjoi6Ieq5ZyoX1cxM1dRY1FqVlE5QyIsImNyZWF0aW9uX2RhdGUiOiIyMDIyLTAzLTMwVDA3OjEwOjUzWiIsInJvbGVzIjpudWxsLCJvcGVuaWRfdHlwZSI6bnVsbCwib3BlbmlkX2Rlc2MiOm51bGwsInByb2ZpbGUiOnsibmlja25hbWUiOiLoh6rlnKgiLCJlbWFpbCI6InhmcmVlbWluZ0BnbWFpbC5jb20iLCJnZW5kZXIiOiLlpbMiLCJwYXNzd29yZCI6bnVsbCwidm9jYWJ1bGFyaWVzIjp7ImVuIjoxMjIwfX0sImxhc3RfcGFzc3dvcmRfY2hhbmdlZF9kYXRlIjoiMTAvMTgvMjAyMiA3OjQ2OjQ3IEFNIiwicmVkaXJlY3RfdXJsIjpudWxsfQ%253d%253d; __utma=131758875.1200838336.1703738635.1705365806.1729846644.3; __utmz=131758875.1729846644.3.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _ga_6J9FB2R7F4=GS1.1.1729992904.8.1.1729992923.0.0.0'
channelmap = {
    "Week_1__Introduction_to_Machine_Learning": "913876e8-8fc9-444f-b15c-c2146e6d39e8",
    "Week_2__Regression_with_multiple_input_variables": "2d88e750-e636-424c-b387-53a04a728d7b",
    "Week_3__Classification": "1c9f0dbd-c03f-468f-8a3d-98e031f31de3"
}

def uploadprivatemedia(file_path,file_id,channelid):
    srt_file_path = file_path.with_name(file_path.stem + "_sentence.srt")
    if not srt_file_path.exists():
        raise FileNotFoundError(f"{srt_file_path} does not exist")
    
    with open(srt_file_path, 'r', encoding='utf-8') as srt_file:
        srt_content = srt_file.read()

        url = "https://my.eudic.net/ting/uploadprivatemedia"
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        form_data = {
            "id": 'null',
            "title": file_name,
            "channelId": channelid,
            "thumb": None,
            "media": file_id,
            "voice": None,
            "lrc": srt_content,
            "needProcessLrc": 'true',
            "needKeepformat": 'false',
            "reformatParagraph": 'false',
            "needMachineTranslation": 'true',
            "needAISubtitle": 'false',
            "description": None,
            "mediatype": 4,
            "intros": None,
            "istiming": 'false',
            "timing": current_time,
            "insertImage": None
        }
        form_data_encoded = "&".join(f"{key}={requests.utils.quote(str(value) if value is not None else '')}" for key, value in form_data.items())
        headers = {
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url, headers=headers, data=form_data_encoded)
        result = response.json()
        print(result)
 
def aiforx():
    path = Path(__file__).resolve().parent / "mls/downloaded_videos/"
    files = path.rglob("*.mp4")  # Use rglob to include subdirectories
    for file in files:

        file_path = file.resolve()
        url = "https://my.eudic.net/ting/UploadTingFile?type=media"
        payload={
            'name':os.path.basename(file_path),
            'type':'video/mp4',
        }
        files={
            'file': open(file_path, 'rb')
        }
       
        headers = {
        'Cookie': cookie,
        }

      
        folder_name = file_path.parents[1].name
        channelid = channelmap.get(folder_name, '')
        if folder_name == "Week_1__Introduction_to_Machine_Learning":
            continue
        if not channelid:
            raise ValueError(f"Channel ID not found for folder {folder_name}")
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        result = response.json()
        print(result)
        uploadprivatemedia(file_path, result['fileId'],channelid)
aiforx()




           
        

# upload_video()
# https://my.eudic.net/ting/UploadTingFile?type=media
# id: WU_FILE_0
# name: gradient-descent-for-linear-regression.mp4
# type: video/mp4
# lastModifiedDate: Fri Oct 25 2024 16:08:21 GMT+0800 (中国标准时间)
# size: 17178623
# file: (二进制)

# {
#     "success": true,
#     "result": "/uploads/a98392ac-0f93-4451-9824-fb6911041e64.mp4",
#     "fileId": "a98392ac-0f93-4451-9824-fb6911041e64.mp4",
#     "error": "",
#     "msg": "",
#     "keyframe": "/Uploads/dubbingkeyframes/8139ce1a-d071-448d-9114-f4e24a0f6c86_kf004.jpg",
#     "item_type": 4,
#     "filename": "gradient-descent-for-linear-regression"
# }

# # https://my.eudic.net/ting/uploadprivatemedia


# id: null
# title: gradient-descent-intuition
# channelId: 913876e8-8fc9-444f-b15c-c2146e6d39e8
# thumb: 
# media: 146047b1-e10f-42fd-8add-825a4bb9b017.mp4
# voice: 
# needProcessLrc: true
# needKeepformat: false
# reformatParagraph: false
# needMachineTranslation: true
# needAISubtitle: false
# description: 
# mediatype: 4
# intros: 
# istiming: false
# timing: 2024-10-26 17:34
# insertImage: 