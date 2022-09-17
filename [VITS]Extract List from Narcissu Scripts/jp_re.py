import re,os
import string

x = 0;

ogg_path = "D:/移植/水仙的移植/ATIS/w";
ogg_list = os.listdir(ogg_path);

# 载入并读取游戏脚本
file = open("D:/steam/steamapps/common/narcissu2/0.utf",'r',encoding='utf-8');
f_read = file.read();
# 设置正则表达式

#脚本内第一部和第二部使用的文本展示格式不一样，所以写了两个正则，第一步只需要这一个正则提取
# re_str  = r'"\s;\S(.*)' ---
re_str  = r'.\s\n;「(.*)」';
# 对search提取出来的文本再次进行一次正则提取
re_search = r'「.*」';

# for循环获取ogg目录下的所有文件名 ,并且对每个段语音都进行一个正则提取出其对应的台本

print("提取台本中\n请稍等......");
for key in ogg_list:
    key  = ogg_list[x];                 
    pattern = key+re_str;

    re_prefix = "wavs/" +key +"|";
    re_jp = re.search(pattern,f_read);
    # 按指定格式写入台本写入台本
    write_file = open ("list.txt", 'a',encoding='utf-8')

    # 对指定的文本再次进行筛选
    re_search_jp = re.findall(re_search,str(re_jp));
    # 写入筛选后的台本
    write_file.write(re_prefix+str(re_search_jp)+"\n");

    x+=1;
print("已完成");




