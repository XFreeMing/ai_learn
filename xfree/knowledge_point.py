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



def load_markdown(srt_file):
    captions = []
    with open(srt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        captions.append(lines)
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

def knowledge_point_stream():
    from pathlib import Path
   
    
    
    path = Path(__file__).resolve().parent / "mls/"
    output_path = Path(__file__).resolve().parent / "mls/knowledge_point.md"
    files = path.rglob("*_summary.md")
    for file in files:
        
        print(f"{file}获取中")
        video_name = os.path.basename(file)
        captions = load_markdown(file)
        prompt = f"""
        ## Goal
        根据视频标题信息和作者观点信息用中文提炼核心知识点
        标题：'{video_name[:-11]}'
        作者观点:
        --- 
        {captions}
        ---  
        ## 要求:
        1. 不要出现无意义的知识点，知识点要抽象。  
        2. 每个知识之间要体现逻辑关系。
        3. 每个知识点要附加刻意练习的方法。
        4. 每个知识点要附加掌握的衡量标准。
        5. markdown格式。
        """
     
    
        

        llm_res = llm_kimi_stream(prompt)
        show_data = ""
        with open(output_path, 'a',encoding='utf-8') as kfile:
            for chunk in llm_res:
                data = chunk.choices[0].delta.content or "" if chunk.choices else ""
                show_data+=data
                kfile.write(data)
                print(data)
        print(f"{file}处理完成")
       

if __name__ == "__main__":
 
   knowledge_point_stream()



