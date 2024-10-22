import re
from pathlib import Path


def merge_vtt_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    result = []
    current_text = ""
    current_start_time = ""
    current_end_time = ""
    sequence_number = 1

    skip_header = True
    for i in range(len(lines)):
        line = lines[i].strip()

        # Skip the "WEBVTT" header
        if skip_header:
            if line == "WEBVTT":
                continue
            elif line == "":
                skip_header = False
                continue
            else:
                skip_header = False
        
        # Match timecodes, e.g., "00:00:01.130 --> 00:00:03.899"
        timecode_match = re.match(r'^(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})$', line)
        
        if timecode_match:
            if not current_start_time:
                current_start_time = timecode_match.group(1)
            current_end_time = timecode_match.group(2)
        elif line.isdigit():
            # Skip sequence numbers
            continue
        elif line:
            # Add the text to the current segment
            if current_text:
                current_text += " " + line
            else:
                current_text = line

            # Check if the current text ends with a period
            if current_text.endswith('.'):                
                result.append(f"{sequence_number}\n{current_start_time} --> {current_end_time}\n{current_text}\n\n")
                sequence_number += 1
                current_text = ""
                current_start_time = ""
        
        # Update end time if the next line is a timecode or EOF
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if re.match(r'^(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})$', next_line):
                current_end_time = timecode_match.group(2)
    
    # Write the output to the file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("WEBVTT\n\n")
        for item in result:
            outfile.write(item)
    


# # 获取当前脚本的目录
# current_dir = Path(__file__).resolve().parent

# # 使用示例
# input_file = current_dir / 'W1_3.4_Cost_Function_Intuition.vtt'
# output_file = current_dir / 'output.vtt'



# merge_vtt_lines(input_file, output_file)


if __name__ == "__main__":
    # 获取指定目录下的所有vtt文件
    from pathlib import Path
    path = Path("/home/xiaolt1/workspace/ai_learn/xfree/mls/Supervised_Machine_Learning_Regression_And_Classification/W1_Introduction_to_Machine_Learning/video/")
    files = path.glob("*.vtt")
    for file in files:
        merge_vtt_lines(file, f"{str(path)}/{file.stem}_output.vtt")