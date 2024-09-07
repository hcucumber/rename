import os
import sys
# 导入 os 模块用于与操作系统进行交互，导入 sys 模块用于获取命令行参数等。

def natural_sort_key(s):
    import re
    # 导入 re 模块用于正则表达式操作。
    # 这个函数接受一个字符串参数 s。
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]
    # 使用正则表达式 re.split(r'(\d+)', s) 将输入的字符串 s 按照数字和非数字进行分割。
    # 然后遍历分割后的结果，对于是数字的部分转换为整数，非数字部分转换为小写字母。
    # 最后返回处理后的结果列表，这个列表将用于对文件名进行自然排序。

def rename_files(path):
    # 定义一个函数 rename_files，接受一个路径参数 path。
    if os.name == 'nt':  # Windows 系统
        # 判断当前操作系统是否为 Windows 系统。
        path = path.replace('\\\\', '\\').replace('\\', os.sep)
        # 如果是 Windows 系统，处理路径中的反斜杠问题，确保路径格式正确。
    # 获取指定路径下除了 rename.py 的所有文件
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f!= 'rename.py']
    # 使用列表推导式遍历指定路径下的所有文件，筛选出文件（os.path.isfile 判断）且文件名不为 'rename.py' 的文件，将这些文件的文件名放入列表 files 中。
    # 对文件进行排序（使用自然排序规则）
    sorted_files = sorted(files, key=natural_sort_key)
    # 使用内置函数 sorted 对 files 列表进行排序，排序依据是 natural_sort_key 函数返回的结果，实现自然排序。
    # 打印文件列表让用户确认顺序
    print("以下是当前文件夹下的文件列表：")
    for index, file in enumerate(sorted_files):
        print(f"{index + 1}. {file}")
    # 使用 enumerate 函数遍历 sorted_files 列表，输出文件的序号和文件名，让用户确认文件顺序。
    # 获取用户输入的电视剧名称
    series_name = input("请输入电视剧名称（不可留空）：")
    # 获取用户输入的电视剧名称，存储在 series_name 变量中。
    season_number = input("请输入季数（默认：NULL）：")
    # 获取用户输入的季数，存储在 season_number 变量中。
    episode_number_lenth = int(input("请输入集数的数字位数（默认：2）：") or 2)
    # 获取用户输入的集数数字位数，如果用户未输入则默认为 2，将输入转换为整数存储在 episode_number_lenth 变量中。
    custom_content = input("请输入可选的自定义内容（如果不想添加可留空）：")
    # 获取用户输入的自定义内容，存储在 custom_content 变量中。
    # 获取要删除的字符数量
    num_chars_to_delete = int(input("请输入要删除的文件名前的字符数量（默认：0）：") or 0)
    # 获取用户输入的要删除的文件名前的字符数量，将输入转换为整数存储在 num_chars_to_delete 变量中。
    # 确认用户是否想要继续重命名
    confirmation = input(("确认要按照上述信息重命名文件吗？（默认：n）（y/n）") or n)
    # 获取用户输入的确认信息，存储在 confirmation 变量中。
    if confirmation.lower() == 'y':
        # 如果用户确认进行重命名。
        for index, file in enumerate(sorted_files):
            if num_chars_to_delete > 0:
                remaining_name = file[num_chars_to_delete:]
            else:
                remaining_name = file
            # 根据用户输入的要删除的字符数量决定是否删除文件名的前若干字符，得到剩余的文件名存储在 remaining_name 变量中。
            episode_number = str(index + 1).zfill(episode_number_lenth)
            # 根据当前文件的序号生成集数，集数的数字位数由用户输入决定，使用 zfill 方法填充数字位数。
            new_name = series_name + ".E" + episode_number
            if remaining_name:
                new_name += "." + remaining_name
            if custom_content:
                new_name += "." + custom_content
            # 根据用户输入的信息和处理后的文件名生成新的文件名 new_name。
            if season_number:
                season_number_str = str(season_number).zfill(2)
                new_name = series_name + ".S" + season_number_str + "E" + episode_number
                if remaining_name:
                    new_name += "." + remaining_name
                if custom_content:
                    new_name += "." + custom_content
            # 如果用户输入了季数，生成包含季数的新文件名。
            os.rename(os.path.join(path, file), os.path.join(path, new_name))
            # 使用 os.rename 方法将旧文件名重命名为新文件名。
        print("重命名完成！")
    else:
        print("操作取消。")
    # 如果用户未确认重命名，则输出操作取消的信息。

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '.'
    # 如果命令行参数中提供了路径，则使用该路径，否则使用当前路径。
    rename_files(path)
    # 调用 rename_files 函数进行文件重命名操作。
