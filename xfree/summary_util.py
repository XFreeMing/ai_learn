import re
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

# def load_vtt(vtt_file):
#     captions = []
#     for caption in webvtt.read(vtt_file):
#         formatted_start = format_time(caption.start)
#         formatted_end = format_time(caption.end)
#         captions.append({
#             'start': caption.start,
#             'end': caption.end,
#             'formatted_start': formatted_start,
#             'formatted_end': formatted_end,
#             'text': caption.text
#         })
#     return captions
def load_srt(srt_file):
    captions = []
    with open(srt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    current_text = ""
    current_start_time = ""
    current_end_time = ""
    sequence_number = 1
    skip_header = True
    for i in range(len(lines)):
        line = lines[i].strip()
        if skip_header:
            if line == "WEBVTT":
                continue
            elif line == "":
                skip_header = False
                continue
            else:
                skip_header = False
        timecode_match = re.match(r'^(\d{2}:\d{2}:\d{2}\,\d{3}) --> (\d{2}:\d{2}:\d{2}\,\d{3})$', line)
        if timecode_match:
            if not current_start_time:
                current_start_time = timecode_match.group(1)
            current_end_time = timecode_match.group(2)
        elif line.isdigit():
            continue
        elif line:
            if current_text:
                current_text += " " + line
            else:
                current_text = line
            if current_text.endswith('.'):
                captions.append({
                    'sequence_number': sequence_number,
                    'start': current_start_time,
                    'end': current_end_time,
                    'text': current_text
                })
                sequence_number += 1
                current_text = ""
                current_start_time = ""
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if re.match(r'^(\d{2}:\d{2}:\d{2}\,\d{3}) --> (\d{2}:\d{2}:\d{2}\,\d{3})$', next_line):
                current_end_time = timecode_match.group(2)
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

def generate_summary_stream(path,output_path):
    video_name = os.path.basename(path)
    
    
    captions = load_srt(path)
    prompt = f"""
    ## Goal
    根据视频标题信息和字幕信息用中文总结视频作者所有的观点
    标题：'{video_name[:-13]}'
    视频字幕:
    --- 
    {captions}
    ---  
    ## 要求:  
    1. 观点要有逻辑，不要出现无意义的观点。
    2. 所有观点 要附加来源要包含实在 视频什么时间说的 
    3. markdown格式。
    """
     
    
    if os.path.exists(output_path):
        return f"{video_name}:已存在"

    llm_res = llm_kimi_stream(prompt)
    show_data = ""
    with open(output_path, 'w',encoding='utf-8') as file:
        for chunk in llm_res:
            data = chunk.choices[0].delta.content or "" if chunk.choices else ""
            show_data+=data
            file.write(data)
    return show_data

if __name__ == "__main__":
 
    from pathlib import Path
    path = Path(__file__).resolve().parent / "mls/downloaded_videos/"
    files = path.rglob("*_sentence.srt")
    for file in files:
        generate_summary_stream(file,file.with_name(f"{file.stem[:-9]}_summary.md"))
        print(f"{file}处理完成")



