import re,os
import string

x = 0;
y = 0;

def files_name(path):
    filesname_list = []
    for i in range(len(path)):
        (filepath, tempfilename) = os.path.split(path[i])
        (filesname, extension) = os.path.splitext(tempfilename)
        filesname_list.append(filesname)
    return filesname_list

# 遍历文件夹，获取当前文件夹下文件所有路径的列表
def dir_name(path):
    file_list = os.listdir(path)
    file_name_list = []
    for i in range(len(file_list)):
        file_name = path + '/' + file_list[i]
        file_name_list.append(file_name)
    return file_name_list

# 该角色的音频文件夹
file_path = dir_name('D:\移植\Eden\sio')

ogg_list = files_name(file_path)

# 提取文本正则
re_str  = r' シオン 「(.*)」';

# 多个台本所在的文件夹
files_path = 'D:\迅雷下载\e\台本';

files = os.listdir(files_path);
for file in files:
    f = open(files_path+"\\"+files[y],'r',encoding='shift-jis')
    f_read = f.read();
    
    for ogg in ogg_list:
        pattern = ogg+re_str;
        re_jp = re.findall(pattern,f_read);
        
         # list文本规定的格式
        re_prefix = "wavs/" + ogg +".wav"+"|";
       
        # 检查文本是否出错
        if len(re_jp) ==0:
            pass;
        else:
            # 写入文件
            write_file = open ("list.txt", 'a',encoding='utf-8')
            write_file.write(re_prefix+str(re_jp)+"\n");
            print(re_jp)
    y+=1;














