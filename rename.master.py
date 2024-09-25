import os
import sys
import re

def natural_sort_key(s):
    # 导入 re 模块用于正则表达式操作。
    # 这个函数接受一个字符串参数 s。
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def rename_files(path):
    if os.name == 'nt':  # Windows 系统
        path = path.replace('\\\\', '\\').replace('\\', os.sep)

    # 获取指定路径下除了 rename.py 的所有文件
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f != 'rename.py']

    # 对文件进行排序（使用自然排序规则）
    sorted_files = sorted(files, key=natural_sort_key)

    # 打印文件列表让用户确认顺序
    print("以下是当前文件夹下的文件列表：")
    for index, file in enumerate(sorted_files):
        print(f"{index + 1}. {file}")

    # 获取用户输入的电视剧名称
    series_name = input("请输入电视剧名称（不可留空）：")

    season_number = input("请输入季数（默认：NULL）：")
    episode_number_length = int(input("请输入集数的数字位数（默认：2）：") or 2)
    custom_content = input("请输入可选的自定义内容（如果不想添加可留空）：")

    # 获取要删除的字符数量
    num_chars_to_delete_input = input("请输入要删除的文件名前的字符数量（默认：不留）：") 
    num_chars_to_delete = 0

    # 确认用户是否想要继续重命名
    confirmation = input("确认要按照上述信息重命名文件吗？（默认：n）（y/n）") or 'n'
    if confirmation.lower() == 'y':
        for index, file in enumerate(sorted_files):
            base_name, ext = os.path.splitext(file)  # 分离文件名和扩展名
            
            if num_chars_to_delete_input == '':
                print("用户未输入删除文件名字符数量，将删除所有原文件名字符！")
                num_chars_to_delete = len(base_name)
            else:
                print("将删除的文件名字符数量为：" + str(num_chars_to_delete_input))
                num_chars_to_delete = int(num_chars_to_delete_input)

            if num_chars_to_delete == 0:
                remaining_name = base_name
            elif num_chars_to_delete > 0:
                remaining_name = base_name[num_chars_to_delete:]
            else:
                remaining_name = ''

            # 根据当前文件的序号生成集数
            episode_number = str(index + 1).zfill(episode_number_length)

            new_name = series_name + ".E" + episode_number
            if remaining_name:
                new_name += "." + remaining_name
            if custom_content:
                new_name += "." + custom_content

            if season_number:
                season_number_str = str(season_number).zfill(2)
                new_name = series_name + ".S" + season_number_str + "E" + episode_number
                if remaining_name:
                    new_name += "." + remaining_name
                if custom_content:
                    new_name += "." + custom_content

            # 重新组合新的文件名和扩展名
            new_file_name = new_name + ext
            os.rename(os.path.join(path, file), os.path.join(path, new_file_name))

        print("重命名完成！")
    else:
        print("操作取消。")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '.'

    rename_files(path)
