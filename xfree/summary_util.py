import webvtt
from dotenv import load_dotenv
import os
load_dotenv()
from collections import defaultdict


from openai import OpenAI

client = OpenAI(
        api_key=os.getenv("OPEN_AI_KEY"),
        base_url="https://api.moonshot.cn/v1",
)

def format_time(vtt_time):
    parts = vtt_time.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = float(parts[2])
    
    # Format minutes and seconds, removing milliseconds
    formatted_seconds = int(seconds)
    formatted_time = f'{minutes:02}:{formatted_seconds:02}'
    
    if hours > 0:
        formatted_time = f'{hours}:{formatted_time}'
        
    return formatted_time

def load_vtt(vtt_file):
    captions = []
    for caption in webvtt.read(vtt_file):
        formatted_start = format_time(caption.start)
        formatted_end = format_time(caption.end)
        captions.append({
            'start': caption.start,
            'end': caption.end,
            'formatted_start': formatted_start,
            'formatted_end': formatted_end,
            'text': caption.text
        })
    return captions


def get_model(content):
    model="moonshot-v1-128k"
    if len(content)>20000:
        model = "moonshot-v1-128k"
    return model

def llm_kimi_stream(content):   
    response = client.chat.completions.create(
        model=get_model(content),
        messages=[
            {"role": "user", "content": content}
        ],
        temperature=0.3,
        stream=True
    )
    return response

def generate_summary_stream(path):
    path_str = str(path)
    video_name = os.path.basename(path)
    
    
    captions = load_vtt(f'{path_str[:-4]}.vtt')
    prompt = f"""
    ## Goal
    根据视频标题信息和字幕信息总结视频作者所有的观点'{video_name[:-4]}'
    视频字幕:
    --- 
    {captions}
    ---  
    ## 要求:  
    1. 观点要有逻辑，不要出现无意义的观点。
    2. 所有观点 要附加来源要包含实在 视频什么时间说的 
    3. markdown格式。
    """
     
    summary_path = f'{path_str[:-4]}.md'
    if os.path.exists(summary_path):
        return "已存在"

    llm_res = llm_kimi_stream(prompt)
    show_data = ""
    with open(summary_path, 'w') as file:
        for chunk in llm_res:
            data = chunk.choices[0].delta.content or "" if chunk.choices else ""
            show_data+=data
            file.write(data)
    return show_data

if __name__ == "__main__":
    # 获取指定目录下的所有mp4文件
    from pathlib import Path
    path = Path("/home/ai_demo/workspace/ai_learn/xfree/机器学习/Supervised Machine Learning-Regression And Classification/W1-Introduction to Machine Learning")
    files = path.glob("*.mp4")
    for file in files:
        print(generate_summary_stream(file))

