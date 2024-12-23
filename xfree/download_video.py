import json
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
import os
from selenium.webdriver.edge.options import Options

edge_options = Options()

edge_options.add_argument("--inprivate")  # 这里省略此行即表示非无痕模式
driver = webdriver.Edge(options=edge_options)

base_path = os.path.dirname(os.path.abspath(__file__))
course_id = "146130217~T7hf5jWeEeuGCBL8_hyTUQ"
# 在当前脚本运行目录的基础上追加指定文件夹
download_path = os.path.join(base_path, "mls\\downloaded_videos")
if not os.path.exists(download_path):
    os.makedirs(download_path)
def web_get_weeks(id):
    url = f"https://www.coursera.org/api/guidedCourseSessionProgresses.v1?ids={id}&fields=id,startedAt,endedAt,weeks,courseProgressState"
    cookie_str = 'FPID=FPID2.2.uEZOqacaduO7iHlACYWWa6LlA%2FiNIW0lKl6VtMWPjyk%3D.1705412360; _fbuy_buckets=%7B%22ekW-q5K%22%3A%5B79328%2C1705455958902%5D%7D; drift_aid=158714e5-5cd5-4b62-9186-20a489f965ac; driftt_aid=158714e5-5cd5-4b62-9186-20a489f965ac; __204u=1300027967-1718076627117; usprivacy=1---; OneTrustWPCCPAGoogleOptOut=false; _ga=GA1.1.198624248.1718588413; IR_PI=19309497-b4d2-11ee-b208-677e5350c626%7C1718953999691; __stripe_mid=1fcc3010-853b-42b3-97b0-70c2a6cf133aff986e; G_ENABLED_IDPS=google; CAUTH=XnQDQOv3EN5fdzdh7RWbXlzV8ltR9p9xp03ovvh4xU6cD7UpB8rXJHbmm830EGYHBuwAlbqBqIK8Lg9oPzvJGA.Y8X57pFAlvJMKV0di_mbNA.pw0YA-bk52EAydVlo-SwqJpO4wJPjx-8djgJ-rW4nB-q8CcDfLzd9azNv9XDMLB-hDiv7L0kCvdHXD0HecWwjqVTOW1Gsnf9LlvLpPhBJVeKO0vNUmY1j8jiPpBqgwqZQuEQBlmXrwRNdlzMdrwwmzLiY6OTa534mYq7_w76lSprCJ3P2ddk3Po5gc84WAvxWCRlx5SXA-_9IwGU1BNSJd8jcdWkdiT4cohwMnAX7MFFeVYgOWJBA2S6WJlxuyucT0AMNfCMgIngsxFCbVPo4iLbcvnOhSNATsFjz42Mi7EJQP7CAbj4QEcwq_glqeCvMOmGYnrZFwfN3TK9ZRR3fbpuq_Z3Y24Mna8rVVLnZx0shFzwLWA9KfOcWAi4lJFW60eQe1LpYV7Yme4e7YnkGNSYLAvQDZuJLGG6KRhj3hlgxDF-RcAMjMd4IU6mYZ-6ZlANkI5gH_DHhJ_O3Z82nQ; _gcl_au=1.1.261099981.1728518200; CSRF3-Token=1730640104.OKPpT9xwozbJ3d2D; aws-waf-token=c400feb2-b53e-4bb8-8dea-5be425ca7996:AQoAdgheG3dzAAAA:tJ1VYm3I4s44ihNNfz6Xug23QKdlqTAFNkcXlcA+VRU6WPe3oNpjKMa4keYyumJNU6nPAiAET2FRCe/bUP25XIHI8iS4vfXHHPWnDCJqTY2PwKNEHKOWLheJ6Ng8JX0mFTUh7AxYpTbvfJBm18wSE4JUibyTR2vOKpqFGb8FutE6gKsZaCJpzArWaqt85Ug=; FPLC=tYh4csEBf68b2U38DSQak5QvKHadjLWOusQCSLW3bAW2EzG8EACubitsWa%2BatbpWcrYgqtM36x7vq36qqUIs%2FZ5d1BOnFCY682NfVQNe7W72TJomGQ2fV%2Fmmu6gVHw%3D%3D; __400v=b9613601-6e24-40f4-9bbb-762f7e2df8de; _rdt_uuid=1718588414113.df1e6058-7e3e-435f-848b-54dfc07183dd; _tq_id.TV-63455409-1.39ed=3e8b7cd6506980d2.1718588415.0.1729834951..; IR_gbd=coursera.org; IR_14726=1729834950768%7C0%7C1729834950768%7C%7C; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+25+2024+13%3A42%3A31+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202408.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d8fdcf3a-addf-421d-9a0c-5fcfbc23adca&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=CN%3BTJ&isAnonUser=1; OptanonAlertBoxClosed=2024-10-25T05:42:31.060Z; _uetsid=b364fc80920b11efbebfc918b41ac901|2c9iio|2|fqb|0|1758; ab.storage.sessionId.6b512fd4-04b5-4fd4-8b44-3f482bc8dcf9=g%3A7f0792a9-e07e-486a-f4c8-90d7871fc4bc%7Ce%3A1729836753817%7Cc%3A1729834953818%7Cl%3A1729834953818; ab.storage.deviceId.6b512fd4-04b5-4fd4-8b44-3f482bc8dcf9=g%3A720b86ea-3f7c-1c43-cafe-1b0f760d9d07%7Ce%3Aundefined%7Cc%3A1722954692448%7Cl%3A1729834953819; ab.storage.userId.6b512fd4-04b5-4fd4-8b44-3f482bc8dcf9=g%3A146130217%7Ce%3Aundefined%7Cc%3A1722954692445%7Cl%3A1729834953821; _uetvid=493f27704b8511ee86eea13eda58b5db|1gmxqm7|1729834957931|1|1|bat.bing.com/p/insights/c/e; _ga_ZCE2Q9YZ3F=GS1.1.1729834950.30.0.1729834963.47.0.0; _ga_7GZ59JSFWQ=GS1.1.1729834950.32.0.1729834963.0.0.1506446169; __400vt=1729834969571'

    # Split the cookie string and create a list of dictionaries
    cookies = [{'name': c.split('=')[0], 'value': c.split('=')[1]} for c in cookie_str.split('; ')]

   

    
    driver.get(url)
    #  # Add each cookie to the driver
    # for cookie in cookies:
    #     driver.add_cookie(cookie)
    # driver.get(url)
    # 找到包含 JSON 数据的 script 标签
    # 找到包含 JSON 数据的 div 标签
    page_source = driver.page_source
    # 使用正则表达式找到包含 JSON 数据的 div 标签
    match = re.search(r'<div hidden="true">(.*?)</div>', page_source, re.DOTALL)
    if match:
        json_text = match.group(1)
        # 解析 JSON 数据
        parsed_json = json.loads(json_text)
        for item in parsed_json["elements"][0]["weeks"]:
            week_name = item["modules"][0]["name"].replace(":"," ").replace(" ","_")
            week_path = os.path.join(download_path, week_name)
            if not os.path.exists(week_path):
                os.makedirs(week_path)
            videos = []
            for one in item["modules"][0]["items"]:
                resource_path =  one["resourcePath"]
                item_id = one["id"]
                folder_name = resource_path.split("/")[-1]
                folder_path = os.path.join(week_path, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                
                type_name = one["contentSummary"]["typeName"]
                if type_name == "lecture":
                    video_id = id.split("~")[-1]+"~"+item_id
                    get_video_info(video_id,folder_name,folder_path)
        print(parsed_json)
    else:
        print("未找到匹配的 div 标签")
def get_video_info(id,file_name,folder_path):
    url = f"https://www.coursera.org/api/onDemandLectureVideos.v1/{id}?includes=video&fields=onDemandVideos.v1(sources%2Csubtitles%2CsubtitlesVtt%2CsubtitlesTxt%2CsubtitlesAssetTags)%2CdisableSkippingForward"
    # # 启用性能日志，以便拦截网络请求
    # capabilities = DesiredCapabilities.EDGE  # noqa: F821
    # capabilities['ms:loggingPrefs'] = {'performance': 'ALL'}

    # 启动 Edge 浏览器
    # driver = webdriver.Edge(desired_capabilities=capabilities)
        # 启动浏览器
    

   

   
  

    # 再次请求目标页面，确保 Cookie 生效
    driver.get(url)
    # 找到包含 JSON 数据的 script 标签
    # 找到包含 JSON 数据的 div 标签
    page_source = driver.page_source
    # 使用正则表达式找到包含 JSON 数据的 div 标签
    match = re.search(r'<div hidden="true">(.*?)</div>', page_source, re.DOTALL)
    if match:
        json_text = match.group(1)
        # 解析 JSON 数据
        parsed_json = json.loads(json_text)
        print(parsed_json)
    else:
        print("未找到匹配的 div 标签")

    # 解析 JSON 数据
    parsed_json = json.loads(json_text)
    for item in parsed_json["linked"]["onDemandVideos.v1"]:
        srt_url = 'https://www.coursera.org'+ item["subtitles"]["en"].replace("amp;","")
        vtt_url = 'https://www.coursera.org'+ item["subtitlesVtt"]["en"].replace("amp;","")

        video_url = item["sources"]["byResolution"]["720p"]["mp4VideoUrl"].replace("amp;","")
        
        srt_save_path = os.path.join(folder_path, f"{file_name}.srt")
        vtt_save_path = os.path.join(folder_path, f"{file_name}.vtt")
        video_save_path = os.path.join(folder_path, f"{file_name}.mp4")
 
        if not os.path.exists(vtt_url):
            download_srt(vtt_url, vtt_save_path)
        if not os.path.exists(srt_save_path):
            download_srt(srt_url, srt_save_path)
        if not os.path.exists(video_save_path):
            download_video(video_url, video_save_path)
        
    print(parsed_json)

def download_srt(url, save_path):
    try:
        driver.get(url)
        page_source = driver.page_source
        # <pre style="word-wrap: break-word; white-space: pre-wrap;"></pre>
        match = re.search(r'<pre style="word-wrap: break-word; white-space: pre-wrap;">(.*?)</pre>', page_source, re.DOTALL)
        if match:
            page_source = match.group(1).encode('utf-8')
        else:
            print("未找到匹配的 pre 标签")
            
        # Open a file to write the SRT content
        with open(save_path, 'wb') as file:
            file.write(page_source)
        print(f"SRT downloaded successfully and saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading SRT: {e}")


def download_video(url, save_path):
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check if the request was successful

        # Open a file to write the video content
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # Filter out keep-alive new chunks
                    file.write(chunk)
        print(f"Video downloaded successfully and saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading video: {e}")

web_get_weeks(course_id)
