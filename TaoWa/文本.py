# -*- coding: utf-8 -*-
import re,random,json




def 文本_JSON转字典(内容: str) -> dict:
    """
    将JSON格式的字符串转换为Python字典。

    :param 内容: JSON格式的字符串。
    :return: 对应的Python字典。
    """
    return json.loads(内容)


def 文本_对象转文本(对象) -> str:
    """
    将任何Python对象转换为其文本表示形式。

    :param 对象: 任何Python对象。
    :return: 对象的文本表示形式。
    """
    return repr(对象)


def 文本_取左边(原文本: str, 要取出的数量: int) -> str:
    """
    从原文本中取出指定数量的字符，从左边开始。

    :param 原文本: 要进行操作的字符串。
    :param 要取出的数量: 从左边开始要取出的字符数量。
    :return: 取出的字符串。
    """
    return 原文本[:要取出的数量]


def 文本_取右边(原文本: str, 要取出的数量: int) -> str:
    """
    从原文本中取出指定数量的字符，从右边开始。

    :param 原文本: 要进行操作的字符串。
    :param 要取出的数量: 从右边开始要取出的字符数量。
    :return: 取出的字符串。
    """
    return 原文本[-要取出的数量:]


def 文本_取文本左边(原文本: str, 指定的文本: str) -> str:
    """
    从原文本中找到指定文本的位置，并返回其左边的部分。

    :param 原文本: 要进行操作的字符串。
    :param 指定的文本: 需要定位的字符串。
    :return: 指定文本左边的部分。如果未找到指定文本，则返回空字符串。
    """
    索引 = 原文本.find(指定的文本)
    return 原文本[:索引] if 索引 != -1 else ''


def 文本_取文本右边(原文本: str, 指定的文本: str) -> str:
    """
    从原文本中找到指定文本的最后出现位置，并返回其右边的部分。

    :param 原文本: 要进行操作的字符串。
    :param 指定的文本: 需要定位的字符串。
    :return: 指定文本右边的部分。如果未找到指定文本，则返回空字符串。
    """
    索引 = 原文本.rfind(指定的文本)
    return 原文本[索引 + len(指定的文本):] if 索引 != -1 else ''


import json

def 文本_JSON解析(内容, 中文解码: bool = False) -> str:
    """
    将给定的内容转换为 JSON 字符串。如果启用中文解码，汉字不会被转换为 Unicode 编码。

    :param 内容: 要转换为 JSON 字符串的内容。
    :param 中文解码: 指定是否使用中文解码，默认为 False。
    :return: JSON 格式的字符串。
    """
    return json.dumps(内容, ensure_ascii=not 中文解码)


def 文本_寻找文本(原文本: str, 寻找的文本: str, 开始的位置: int = 0, 结束的位置: int = 0) -> int:
    """
    在原文本中寻找指定的文本，返回其位置（从 0 开始）。如果未找到，返回 -1。

    :param 原文本: 要搜索的字符串。
    :param 寻找的文本: 需要查找的字符串。
    :param 开始的位置: 搜索的起始位置，默认为 0。
    :param 结束的位置: 搜索的结束位置，默认为 0，表示搜索到字符串的末尾。
    :return: 寻找的文本在原文本中的位置，如果未找到则返回 -1。
    """
    return 原文本.find(寻找的文本, 开始的位置, 结束的位置 or None)


def 文本_倒找文本(原文本: str, 寻找的文本: str, 开始的位置: int = 0, 结束的位置: int = 0) -> int:
    """
    类似于 find() 方法，但从原文本的右边开始查找指定的文本。

    :param 原文本: 要搜索的字符串。
    :param 寻找的文本: 需要查找的字符串。
    :param 开始的位置: 搜索的起始位置，默认为 0。
    :param 结束的位置: 搜索的结束位置，默认为 0，表示搜索到字符串的末尾。
    :return: 寻找的文本在原文本中的位置，如果未找到则返回 -1。
    """
    return 原文本.rfind(寻找的文本, 开始的位置, 结束的位置 or None)


def 文本_取出中间文本(原文本: str, 前面的文本: str, 后面的文本: str, 开始的位置: int = 0) -> str:
    """
    在原文本中查找并返回前面的文本和后面的文本之间的部分。

    :param 原文本: 要搜索的字符串。
    :param 前面的文本: 定位起始位置的字符串。
    :param 后面的文本: 定位结束位置的字符串。
    :param 开始的位置: 搜索的起始位置，默认为 0。
    :return: 位于前面的文本和后面的文本之间的字符串。如果未找到，则返回空字符串。
    """
    位置_前 = 原文本.find(前面的文本, 开始的位置)
    位置_后 = 原文本.find(后面的文本, 位置_前 + len(前面的文本))
    if 位置_前 != -1 and 位置_后 != -1:
        return 原文本[位置_前 + len(前面的文本):位置_后]
    else:
        return ''


def 文本_倒取出中间文本(原文本: str, 右边的文本: str, 左边的文本: str, 开始的位置: int = -1) -> str:
    """
    从原文本的右边开始，查找并返回左边的文本和右边的文本之间的部分。

    :param 原文本: 要搜索的字符串。
    :param 右边的文本: 定位结束位置的字符串。
    :param 左边的文本: 定位起始位置的字符串。
    :param 开始的位置: 搜索的起始位置，默认为 -1，表示从字符串末尾开始。
    :return: 位于左边的文本和右边的文本之间的字符串。如果未找到，则返回空字符串。
    """
    位置_右 = 原文本[:开始的位置].rfind(右边的文本)
    位置_左 = 原文本[:位置_右].rfind(左边的文本)
    if 位置_右 != -1 and 位置_左 != -1:
        return 原文本[位置_左 + len(左边的文本):位置_右]
    else:
        return ''

def 文本_倒取中间_批量(原文本: str, 文本A: str, 文本B: str) -> list:
    """
    从原文本中倒序查找文本A和文本B，提取它们之间的内容。

    :param 原文本: 原始的字符串。
    :param 文本A: 倒序查找的起始文本。
    :param 文本B: 倒序查找的结束文本。
    :return: 所有找到的匹配项列表。

    示例调用：
    - print(文本_倒取中间_批量('1231456789123456', '45', '2'))
    预期输出：
    - ['3', '31']
    """
    # 使用正则表达式进行倒序匹配
    正则表达式 = f"{文本B}(.*?){文本A}"
    匹配结果 = re.findall(正则表达式, 原文本)
    匹配结果.reverse()
    return 匹配结果

def 文本_取中间_批量(原文本: str, 文本A: str, 文本B: str) -> list:
    """
    从原文本中正序查找文本A和文本B，提取它们之间的内容。

    :param 原文本: 原始的字符串。
    :param 文本A: 正序查找的起始文本。
    :param 文本B: 正序查找的结束文本。
    :return: 所有找到的匹配项列表。
    """
    # 使用正则表达式进行正序匹配
    正则表达式 = f"{文本A}(.*?){文本B}"
    匹配结果 = re.findall(正则表达式, 原文本)
    return 匹配结果


def 文本_子文本替换(原文本: str, 要替换的文本: str, 用作替换的文本: str, 替换的次数: int = -1) -> str:
    """
    在原文本中替换指定的子文本。

    :param 原文本: 要进行替换操作的字符串。
    :param 要替换的文本: 需要被替换的子文本。
    :param 用作替换的文本: 用于替换的子文本。
    :param 替换的次数: 指定替换操作的次数，默认为 -1，表示替换所有匹配项。
    :return: 替换后的字符串。
    """
    return 原文本.replace(要替换的文本, 用作替换的文本, 替换的次数)


def 文本_删除空行(原文本: str) -> str:
    """
    删除文本中的所有空行。

    :param 原文本: 原始的字符串。
    :return: 删除空行后的字符串。
    """
    # 按行分割文本，去除空行或只包含空白字符的行
    处理后的行 = [行 for 行 in 原文本.split('\n') if 行.strip()]
    # 将非空行重新组合成字符串
    处理后的文本 = '\n'.join(处理后的行)
    return 处理后的文本

def 文本_只取字母(原文本: str) -> str:
    """
    从文本中提取所有的字母。

    :param 原文本: 原始文本字符串。
    :return: 所有字母组成的字符串。
    """
    return ''.join(re.findall(r'[A-Za-z]', 原文本))

def 文本_只取数字(原文本: str) -> str:
    """
    从文本中提取所有的数字。

    :param 原文本: 原始文本字符串。
    :return: 所有数字组成的字符串。
    """
    return ''.join(re.findall(r'\d', 原文本))

def 文本_只取符号(原文本: str) -> str:
    """
    从文本中提取所有的符号（排除字母、数字和汉字）。

    :param 原文本: 原始文本字符串。
    :return: 所有符号组成的字符串。
    """
    # 排除字母、数字、汉字以及空白字符
    return ''.join(re.findall(r'[^\w\s\u4e00-\u9fff]', 原文本))

def 文本_只取大写字母(原文本: str) -> str:
    """
    从文本中提取所有的大写字母。

    :param 原文本: 原始文本字符串。
    :return: 所有大写字母组成的字符串。
    """
    return ''.join(re.findall(r'[A-Z]', 原文本))

def 文本_只取小写字母(原文本: str) -> str:
    """
    从文本中提取所有的小写字母。

    :param 原文本: 原始文本字符串。
    :return: 所有小写字母组成的字符串。
    """
    return ''.join(re.findall(r'[a-z]', 原文本))

def 文本_只取汉字(原文本: str) -> str:
    """
    从文本中提取所有汉字。

    :param 原文本: 原始文本字符串。
    :return: 所有汉字组成的字符串。
    """
    # 使用正则表达式匹配所有汉字
    汉字列表 = re.findall(r'[\u4e00-\u9fff]+', 原文本)
    return ''.join(汉字列表)

def 文本_去重复文本(原文本: str) -> str:
    """
    去除文本中所有重复出现的字符。

    :param 原文本: 原始文本字符串。
    :return: 去重后的文本字符串。
    """
    已出现字符集合 = set()
    去重文本 = []

    for 字符 in 原文本:
        if 字符 not in 已出现字符集合:
            去重文本.append(字符)
            已出现字符集合.add(字符)

    return ''.join(去重文本)

def 文本_分割文本(原文本: str, 分割标识: str, 分割次数: int = -1) -> list:
    """
    使用指定的分割标识来分割原文本。如果指定了分割次数，返回分割次数加一的列表。

    :param 原文本: 要分割的字符串。
    :param 分割标识: 用于分割的标识。
    :param 分割次数: 分割操作的次数，默认为 -1，表示分割所有可能的部分。
    :return: 分割后的字符串列表。
    """
    return 原文本.split(分割标识, 分割次数)


def 文本_换行分割(原文本: str, 保留换行: bool = False) -> list:
    """
    以换行符（\r, \n, \r\n）分割原文本。可以选择是否保留换行符。

    :param 原文本: 要分割的字符串。
    :param 保留换行: 是否保留换行符，默认为 False。
    :return: 分割后的字符串列表。
    """
    return 原文本.splitlines(保留换行)


def 文本_到小写(原文本: str) -> str:
    """
    将原文本转换为小写。

    :param 原文本: 要转换的字符串。
    :return: 转换为小写的字符串。
    """
    return 原文本.casefold()


def 文本_到大写(原文本: str) -> str:
    """
    将原文本转换为大写。

    :param 原文本: 要转换的字符串。
    :return: 转换为大写的字符串。
    """
    return 原文本.upper()


import re

def 文本_首字母转大写(原文本: str) -> str:
    """
    将原文本的首字母转换为大写。

    :param 原文本: 要转换的字符串。
    :return: 首字母转为大写后的字符串。
    """
    return 原文本.capitalize()


def 文本_字符转小写(原文本: str) -> str:
    """
    将原文本中的所有字符转换为小写。可以处理 a-z 以外的字符转换。

    :param 原文本: 要转换的字符串。
    :return: 全部转为小写后的字符串。
    """
    return 原文本.lower()


def 文本_是否有汉字(原文本: str) -> bool:
    """
    检查原文本中是否含有汉字。

    :param 原文本: 要检查的字符串。
    :return: 如果原文本包含汉字，则返回 True；否则返回 False。
    """
    zhmodel = re.compile(u'[\u4e00-\u9fa5]')  # 检查中文
    return bool(zhmodel.search(原文本))


def 文本_是否全汉字(原文本: str) -> bool:
    """
    检查原文本中的字符是否全部是汉字。

    :param 原文本: 要检查的字符串。
    :return: 如果原文本全部由汉字组成，则返回 True；否则返回 False。
    """
    zhmodel = re.compile(u'[^\u4e00-\u9fa5]')  # 检查非中文字符
    return not bool(zhmodel.search(原文本))


def 文本_匹配数字(原文本: str) -> str:
    """
    返回原文本中的所有数字。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 原文本中所有数字的连续字符串。如果未匹配到数字，则返回空字符串。
    """
    结果 = re.findall(r'\d+', 原文本)
    return "".join(结果) if 结果 else ''


def 文本_匹配小写字母(原文本: str) -> str:
    """
    返回原文本中的所有小写字母。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 原文本中所有小写字母的连续字符串。如果未匹配到小写字母，则返回空字符串。
    """
    结果 = re.findall(r'[a-z]+', 原文本)
    return "".join(结果) if 结果 else ''


def 文本_匹配大写字母(原文本: str) -> str:
    """
    返回原文本中的所有大写字母。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 原文本中所有大写字母的连续字符串。如果未匹配到大写字母，则返回空字符串。
    """
    结果 = re.findall(r'[A-Z]+', 原文本)
    return "".join(结果) if 结果 else ''


def 文本_匹配字母(原文本: str) -> str:
    """
    返回原文本中的所有字母。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 原文本中所有字母的连续字符串。如果未匹配到字母，则返回空字符串。
    """
    结果 = re.findall(r'[a-zA-Z]+', 原文本)
    return "".join(结果) if 结果 else ''


def 文本_匹配手机号码(原文本: str) -> list:
    """
    匹配文本中的手机号码，以列表格式返回。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 匹配到的手机号码列表。如果未匹配到，则返回空列表。
    """
    结果 = re.findall(r"1[3-9]\d{9}", 原文本)
    return 结果 if 结果 else []


def 文本_匹配IP地址(原文本: str) -> list:
    """
    匹配文本中的IP地址，以列表格式返回。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 匹配到的IP地址列表。如果未匹配到，则返回空列表。
    """
    结果 = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", 原文本)
    return 结果 if 结果 else []


def 文本_匹配电话号码(原文本: str) -> list:
    """
    匹配文本中的电话号码，以列表格式返回。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 匹配到的电话号码列表。如果未匹配到，则返回空列表。
    """
    结果 = re.findall(r"\d{3,4}[\s,-]?\d{7,8}", 原文本)
    return 结果 if 结果 else []


def 文本_匹配QQ号码(原文本: str) -> list:
    """
    匹配文本中的QQ号码，以列表格式返回。最多匹配11位数QQ号。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 匹配到的QQ号码列表。如果未匹配到，则返回空列表。
    """
    结果 = re.findall(r"[1-9][0-9]{4,10}", 原文本)
    return 结果 if 结果 else []


def 文本_匹配邮政编码(原文本: str) -> list:
    """
    匹配中国邮政编码，以列表格式返回。中国邮政编码为6位数字。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 匹配到的邮政编码列表。如果未匹配到，则返回空列表。
    """
    结果 = re.findall(r"[1-9]\d{5}(?!\d)", 原文本)
    return 结果 if 结果 else []


def 文本_匹配身份证号码(原文本: str) -> list:
    """
    匹配中国的身份证号码，以列表格式返回。身份证号码为15位或18位。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 匹配到的身份证号码列表。如果未匹配到，则返回空列表。
    """
    结果 = re.findall(r"[1-9][0-9,X]{14,17}", 原文本)
    return 结果 if 结果 else []


def 文本_匹配汉字(原文本: str) -> str:
    """
    返回原文本中的所有汉字。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 原文本中所有汉字的连续字符串。如果未匹配到汉字，则返回空字符串。
    """
    结果 = re.findall(r"[\u4e00-\u9fa5]", 原文本)
    return "".join(结果)


def 文本_匹配双字节字符(原文本: str) -> str:
    """
    返回原文本中的所有双字节字符（通常包括汉字和一些全角符号）。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 原文本中所有双字节字符的连续字符串。如果未匹配到双字节字符，则返回空字符串。
    """
    结果 = re.findall(r"[^\x00-\xff]", 原文本)
    return "".join(结果)


def 文本_匹配网址(原文本: str) -> list:
    """
    匹配原文本中的网址，以列表格式返回。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 匹配到的网址列表。如果未匹配到网址，则返回空列表。
    """
    结果 = re.findall(r"[a-zA-z]+://[^\s]*", 原文本)
    return 结果 if 结果 else []


def 文本_匹配IP跟端口(原文本: str) -> list:
    """
    匹配原文本中的IP地址和端口号，以列表格式返回。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 匹配到的IP地址和端口号列表。如果未匹配到，则返回空列表。
    """
    结果 = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}", 原文本)
    return 结果 if 结果 else []


def 文本_匹配邮箱号码(原文本: str) -> list:
    """
    匹配原文本中的邮箱号码，以列表格式返回。

    :param 原文本: 要进行匹配操作的字符串。
    :return: 匹配到的邮箱号码列表。如果未匹配到邮箱号码，则返回空列表。
    """
    结果 = re.findall(r"[a-z0-9\.\-+_]{1,30}@[a-z0-9\.\-+_]{1,30}\.[a-z]{1,10}", 原文本)
    return 结果 if 结果 else []


def 文本_是否正整数(原文本: str) -> bool:
    return bool(re.match(r"^[1-9]\d*$", 原文本))


def 文本_是否负整数(原文本: str) -> bool:
    return bool(re.match(r"^-[1-9]\d*$", 原文本))


def 文本_是否整数(原文本: str) -> bool:
    return bool(re.match(r"^-?[1-9]\d*$", 原文本))


def 文本_是否非正整数(原文本: str) -> bool:
    return bool(re.match(r"^-[1-9]\d*|0$", 原文本))


def 文本_是否非负整数(原文本: str) -> bool:
    return bool(re.match(r"^[1-9]\d*|0$", 原文本))


def 文本_是否正小数(原文本: str) -> bool:
    return bool(re.match(r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$", 原文本))


def 文本_是否负小数(原文本: str) -> bool:
    return bool(re.match(r"^-([1-9]\d*\.\d*|0\.\d*[1-9]\d*)$", 原文本))


def 文本_是否小数(原文本: str) -> bool:
    return bool(re.match(r"^-?([1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0)$", 原文本))


def 文本_是否非正小数(原文本: str) -> bool:
    return bool(re.match(r"^(-([1-9]\d*\.\d*|0\.\d*[1-9]\d*))|0?\.0+|0$", 原文本))


def 文本_是否非负小数(原文本: str) -> bool:
    return bool(re.match(r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0$", 原文本))


def 文本_是否为IP地址(IP: str) -> bool:
    return bool(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", IP))


def 文本_大小写翻转(原文本: str) -> str:
    """
    对原文本中的字符进行大小写翻转。

    :param 原文本: 要进行大小写翻转的字符串。
    :return: 大小写翻转后的字符串。
    """
    return 原文本.swapcase()


def 文本_是否全大写(原文本: str) -> bool:
    """
    检查原文本中的字符是否全部为大写。

    :param 原文本: 要检查的字符串。
    :return: 如果所有字符都是大写，则返回 True；否则返回 False。
    """
    return 原文本.isupper()


def 文本_是否全小写(原文本: str) -> bool:
    """
    检查原文本中的字符是否全部为小写。

    :param 原文本: 要检查的字符串。
    :return: 如果所有字符都是小写，则返回 True；否则返回 False。
    """
    return 原文本.islower()


def 文本_是否全字母(原文本: str) -> bool:
    """
    检查原文本是否全部由字母组成。

    :param 原文本: 要检查的字符串。
    :return: 如果字符串全部由字母组成，则返回 True；否则返回 False。
    """
    return 原文本.isalpha()


def 文本_是否全数字字母(原文本: str) -> bool:
    """
    检查原文本是否全部由数字和字母组成。

    :param 原文本: 要检查的字符串。
    :return: 如果字符串全部由数字和字母组成，则返回 True；否则返回 False。
    """
    return 原文本.isalnum()


def 文本_是否全数字(原文本: str) -> bool:
    """
    检查原文本是否全部由数字组成。

    :param 原文本: 要检查的字符串。
    :return: 如果字符串全部由数字组成，则返回 True；否则返回 False。
    """
    return 原文本.isdigit()


def 文本_取出现次数(原文本: str, 欲查询的文本: str, 开始的位置: int = 0, 结束的位置: int = 0) -> int:
    """
    计算欲查询的文本在原文本中出现的次数。

    :param 原文本: 要进行查询的字符串。
    :param 欲查询的文本: 需要计算出现次数的字符串。
    :param 开始的位置: 查询的起始位置，默认为 0。
    :param 结束的位置: 查询的结束位置，默认为 0，表示查询到字符串的末尾。
    :return: 欲查询的文本在原文本中的出现次数。
    """
    结束的位置 = len(原文本) if 结束的位置 < 1 else 结束的位置
    return 原文本.count(欲查询的文本, 开始的位置, 结束的位置)


def 文本_是否标题化(原文本: str) -> bool:
    """
    检查原文本是否为标题化格式（所有单词的首字母大写，其余均为小写）。

    :param 原文本: 要检查的字符串。
    :return: 如果原文本是标题化的，则返回 True；否则返回 False。
    """
    return 原文本.istitle()


def 文本_标题化(原文本: str) -> str:
    """
    将原文本转换为标题化格式（所有单词的首字母大写，其余均为小写）。

    :param 原文本: 要转换的字符串。
    :return: 转换为标题化格式的字符串。
    """
    return 原文本.title()


def 文本_取文本长度(原文本: str) -> int:
    """
    返回原文本的长度。

    :param 原文本: 要测量长度的字符串。
    :return: 原文本的长度。
    """
    return len(原文本)


def 文本_是否全空格(原文本: str) -> bool:
    """
    检查原文本是否全部由空格组成。

    :param 原文本: 要检查的字符串。
    :return: 如果原文本全部由空格组成，则返回 True；否则返回 False。
    """
    return 原文本.isspace()

def 文本_删左边全部空格(原文本: str) -> str:
    """
    删除原文本左边的所有空格。

    :param 原文本: 要处理的字符串。
    :return: 删除左边空格后的字符串。
    """
    return 原文本.lstrip()


def 文本_删右边全部空格(原文本: str) -> str:
    """
    删除原文本右边的所有空格。

    :param 原文本: 要处理的字符串。
    :return: 删除右边空格后的字符串。
    """
    return 原文本.rstrip()


def 文本_删全部空格(原文本: str) -> str:
    """
    删除原文本中的所有空格。

    :param 原文本: 要处理的字符串。
    :return: 删除所有空格后的字符串。
    """
    return 原文本.replace(" ", "")


def 文本_删首尾指定字符(原文本: str, 欲删除的内容: str = ' ') -> str:
    """
    删除原文本首尾的指定字符。

    :param 原文本: 要处理的字符串。
    :param 欲删除的内容: 需要删除的字符，默认为空格。
    :return: 删除首尾指定字符后的字符串。
    """
    return 原文本.strip(欲删除的内容)


def 文本_填充空格_居中(原文本: str, 填充目标长度: int = 0) -> str:
    """
    将原文本用空格填充到指定长度，使原文本居中。

    :param 原文本: 要处理的字符串。
    :param 填充目标长度: 填充后的目标长度。
    :return: 填充后居中的字符串。
    """
    return 原文本.center(填充目标长度)


def 文本_填充空格_左对齐(原文本: str, 填充目标长度: int = 0) -> str:
    """
    将原文本用空格填充到指定长度，使原文本左对齐。

    :param 原文本: 要处理的字符串。
    :param 填充目标长度: 填充后的目标长度。
    :return: 填充后左对齐的字符串。
    """
    return 原文本.ljust(填充目标长度)


def 文本_填充空格_右对齐(原文本: str, 填充目标长度: int = 0) -> str:
    """
    将原文本用空格填充到指定长度，使原文本右对齐。

    :param 原文本: 要处理的字符串。
    :param 填充目标长度: 填充后的目标长度。
    :return: 填充后右对齐的字符串。
    """
    return 原文本.rjust(填充目标长度)


def 文本_填充0_右对齐(原文本: str, 填充目标长度: int = 0) -> str:
    """
    将原文本用 '0' 填充到指定长度，使原文本右对齐。

    :param 原文本: 要处理的字符串。
    :param 填充目标长度: 填充后的目标长度。
    :return: 填充后右对齐的字符串。
    """
    return 原文本.zfill(填充目标长度)


def 文本_拼接(连接符: str, 欲拼接的序列) -> str:
    """
    使用指定的连接符将序列中的元素拼接成一个字符串。

    :param 连接符: 用于拼接的连接符。
    :param 欲拼接的序列: 包含字符串元素的序列。
    :return: 拼接后的字符串。
    """
    return 连接符.join(欲拼接的序列)


def 文本_按键名转键值(按键名: str) -> int:
    """
    将给定的按键名转换为其对应的ASCII键值。

    :param 按键名: 要转换的按键名。
    :return: 对应的ASCII键值。
    """
    return ord(按键名)


def 文本_键值转按键名(键值: int) -> str:
    """
    将给定的ASCII键值转换为其对应的按键名。

    :param 键值: 要转换的ASCII键值。
    :return: 对应的按键名。
    """
    return chr(键值)


def 文本_是否指定文本结尾(原文本: str, 结尾的文本: str, 开始的位置: int = 0, 结束的位置: int = 0) -> bool:
    """
    检查原文本是否以指定的文本结尾。

    :param 原文本: 要检查的字符串。
    :param 结尾的文本: 指定的结尾文本。
    :param 开始的位置: 检查的起始位置，默认为 0。
    :param 结束的位置: 检查的结束位置，默认为 0，表示检查到字符串的末尾。
    :return: 如果原文本以指定的文本结尾，则返回 True；否则返回 False。
    """
    结束的位置 = len(原文本) if 结束的位置 < 1 else 结束的位置
    return 原文本.endswith(结尾的文本, 开始的位置, 结束的位置)


def 文本_是否指定文本开头(原文本: str, 开头的文本: str, 开始的位置: int = 0, 结束的位置: int = 0) -> bool:
    """
    检查原文本是否以指定的文本开头。

    :param 原文本: 要检查的字符串。
    :param 开头的文本: 指定的开头文本。
    :param 开始的位置: 检查的起始位置，默认为 0。
    :param 结束的位置: 检查的结束位置，默认为 0，表示检查到字符串的末尾。
    :return: 如果原文本以指定的文本开头，则返回 True；否则返回 False。
    """
    结束的位置 = len(原文本) if 结束的位置 < 1 else 结束的位置
    return 原文本.startswith(开头的文本, 开始的位置, 结束的位置)


def 文本_TAB转空格(原文本: str, 转换的数量: int = 8) -> str:
    """
    将字符串中的 tab 符号（\t）转换为指定数量的空格。

    :param 原文本: 要转换的字符串。
    :param 转换的数量: 转换为的空格数量，默认为 8。
    :return: 转换后的字符串。
    """
    return 原文本.expandtabs(tabsize=转换的数量)


def 文本_三元分割_左(原文本: str, 分割标识: str) -> tuple:
    """
    将字符串分割成三部分（分割标识前的部分，分割标识本身，分割标识后的部分）。

    :param 原文本: 要进行分割的字符串。
    :param 分割标识: 用于分割的标识。
    :return: 包含三部分的元组。
    """
    return 原文本.partition(分割标识)


def 文本_三元分割_右(原文本: str, 分割标识: str) -> tuple:
    """
    从右边开始，将字符串分割成三部分（分割标识前的部分，分割标识本身，分割标识后的部分）。

    :param 原文本: 要进行分割的字符串。
    :param 分割标识: 用于分割的标识。
    :return: 包含三部分的元组。
    """
    return 原文本.rpartition(分割标识)


def 文本_取随机邮箱() -> str:
    """
    生成随机的邮箱地址。

    :return: 随机生成的邮箱地址。
    """
    邮箱后缀 = [
        '@qq.com', '@sina.com', '@126.com', '@163.com', '@hotmail.com',
        '@139.com', '@189.com', '@sohu.com', '@21cn.com', '@189.com',
        '@tom.com', '@aol.com', '@263.com', '@aliyun.com', '@foxmail.com',
        '@yeah.net'
    ]

    def 随机字符串(长度范围, 字符集):
        return ''.join(random.choice(字符集) for _ in range(random.randint(*长度范围)))

    数字 = 随机字符串((1, 10), '123456789') + 随机字符串((0, 10), '0123456789')
    字母 = 随机字符串((5, 11), 'abcdefghijklmnopqrstuvwxyz')
    混合 = 随机字符串((1, 6), 'abcdefghijklmnopqrstuvwxyz') + 随机字符串((3, 10), '0123456789')
    字符 = 随机字符串((6, 11), '0123456789abcdefghijklmnopqrstuvwxyz')

    return random.choice([混合, 字母, 数字, 字符]) + random.choice(邮箱后缀)


def 文本_取随机手机号() -> str:
    """
    生成随机的中国大陆手机号码。

    :return: 随机生成的手机号码。
    """
    号码前缀 = [
        '130', '131', '132', '134', '135', '136', '137', '138', '139',
        '147', '150', '151', '152', '153', '155', '156', '157', '158',
        '159', '170', '171', '180', '182', '183', '185', '186', '187',
        '188', '189'
    ]
    尾号 = ''.join(str(random.randint(0, 9)) for _ in range(8))
    return random.choice(号码前缀) + 尾号


def 文本_取随机MAC地址() -> str:
    """
    生成一个随机的MAC地址。

    :return: 随机生成的MAC地址。
    """
    # MAC地址由6个16进制数表示，每个数取值范围为00到FF
    MAC片段 = [random.randint(0x00, 0xff) for _ in range(6)]
    # 将每个数转换为两位的16进制表示，然后用冒号连接
    MAC地址 = ":".join(f"{片段:02x}" for 片段 in MAC片段)
    return MAC地址


def 文本_取随机IP() -> str:
    """
    生成一个随机的IPv4地址。

    :return: 随机生成的IPv4地址。
    """
    ip = [str(random.randint(0, 255)) for _ in range(4)]
    return '.'.join(ip)


def 文本_取随机数字(取出的数量: int = 1, 是否排除0开头: bool = True) -> str:
    """
    生成指定数量的随机数字字符串。

    :param 取出的数量: 要生成的数字的数量。
    :param 是否排除0开头: 是否排除以0开头的数字。
    :return: 生成的随机数字字符串。
    """
    取出的数量 = max(1, 取出的数量)  # 确保至少生成一个数字
    文本 = str(random.randint(1, 9)) if 是否排除0开头 else str(random.randint(0, 9))
    for _ in range(取出的数量 - 1):
        文本 += str(random.randint(0, 9))
    return 文本


def 文本_取随机范围数字(最小值: int, 最大值: int, 是否返回整数: bool = False) -> int:
    """
    生成一个在指定范围内的随机数。

    :param 最小值: 随机数的最小值。
    :param 最大值: 随机数的最大值。
    :param 是否返回整数: 是否以整数形式返回。
    :return: 生成的随机数。
    """
    最小值, 最大值 = min(int(最小值), int(最大值)), max(int(最小值), int(最大值))
    return random.randint(最小值, 最大值) if 是否返回整数 else str(random.randint(最小值, 最大值))


def 文本_取随机字母(取出的数量: int = 1, 类型: int = 0) -> str:
    """
    生成指定数量的随机字母字符串。

    :param 取出的数量: 要生成的字母的数量。
    :param 类型: 字母的类型（0: 小写，1: 大写，2: 混合）。
    :return: 生成的随机字母字符串。
    """
    取出的数量 = max(1, 取出的数量)
    类型 = max(0, min(类型, 2))

    小写字母 = 'abcdefghijklmnopqrstuvwxyz'
    大写字母 = 小写字母.upper()
    字母 = 小写字母 if 类型 == 0 else 大写字母 if 类型 == 1 else 小写字母 + 大写字母

    return ''.join(random.choice(字母) for _ in range(取出的数量))


def 文本_取随机字符(取出的数量: int = 1) -> str:
    """
    生成包含数字、小写字母和大写字母的随机字符字符串。

    :param 取出的数量: 要生成的字符的数量。
    :return: 生成的随机字符字符串。
    """
    取出的数量 = max(1, 取出的数量)
    字符 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(字符) for _ in range(取出的数量))


def 文本_取随机汉字(取出的数量: int = 1) -> str:
    """
    生成指定数量的随机汉字。

    :param 取出的数量: 要生成的汉字数量。
    :return: 生成的随机汉字字符串。
    """
    取出的数量 = max(1, 取出的数量)
    return ''.join(random.choice(常量_部分汉字) for _ in range(取出的数量))


def 文本_取随机姓氏(取常见姓氏: bool = False) -> str:
    """
    随机生成一个姓氏，可以选择是否限定为常见姓氏。

    :param 取常见姓氏: 是否只从常见姓氏中选择。
    :return: 随机生成的姓氏。
    """
    if 取常见姓氏:
        return random.choice(常量_常见百家姓)
    else:
        return random.choice(常量_百家姓)


常量_百家姓 = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫柯房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊于惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭历戎祖武符刘景詹束龙叶幸司韶郜黎蓟溥印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阳郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍却璩桑桂濮牛寿通边扈燕冀浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逮盍益桓公"
常量_常见百家姓 = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛范彭郎鲁韦昌马苗凤花方俞任袁柳史唐费薛雷贺罗毕于齐萧尹姚顾孟平黄宋庞项祝董梁杜阮刘万丁石洪白田夏"
常量_部分汉字 = 常量_百家姓 + "的一是了我不人在他有这个上们来到时大地为子中你说生国年着就那和要她出也得里后自以会家可下而过天去能对小多然于心学么之都好看起发当没成只如事把还用第样道想作种开美总从无情己面最女但现前些所同日手又行意动方期它头经长儿回位分爱老因很给名法间斯知世什两次使身者被高已亲其进此话常与活正感见明问力理尔点文几定本公特做外孩相西果走将月十实向声车全信重三机工物气每并别真打太新比才便夫再书部水像眼等体却加电主界门利海受听表德少克代员许稜先口由死安写性马光白或住难望教命花结乐色更拉东神记处让母父应直字场平报友关放至张认接告入笑内英军候民岁往何度山觉路带万男边风解叫任金快原吃妈变通师立象数四失满战远格士音轻目条呢病始达深完今提求清王化空业思切怎非找片罗钱紶吗语元喜曾离飞科言干流欢约各即指合反题必该论交终林请医晚制球决窢传画保读运及则房早院量苦火布品近坐产答星精视五连司巴奇管类未朋且婚台夜青北队久乎越观落尽形影红爸百令周吧识步希亚术留市半热送兴造谈容极随演收首根讲整式取照办强石古华諣拿计您装似足双妻尼转诉米称丽客南领节衣站黑刻统断福城故历惊脸选包紧争另建维绝树系伤示愿持千史谁准联妇纪基买志静阿诗独复痛消社算义竟确酒需单治卡幸兰念举仅钟怕共毛句息功官待究跟穿室易游程号居考突皮哪费倒价图具刚脑永歌响商礼细专黄块脚味灵改据般破引食仍存众注笔甚某沉血备习校默务土微娘须试怀料调广蜖苏显赛查密议底列富梦错座参八除跑亮假印设线温虽掉京初养香停际致阳纸李纳验助激够严证帝饭忘趣支春集丈木研班普导顿睡展跳获艺六波察群皇段急庭创区奥器谢弟店否害草排背止组州朝封睛板角况曲馆育忙质河续哥呼若推境遇雨标姐充围案伦护冷警贝著雪索剧啊船险烟依斗值帮汉慢佛肯闻唱沙局伯族低玩资屋击速顾泪洲团圣旁堂兵七露园牛哭旅街劳型烈姑陈莫鱼异抱宝权鲁简态级票怪寻杀律胜份汽右洋范床舞秘午登楼贵吸责例追较职属渐左录丝牙党继托赶章智冲叶胡吉卖坚喝肉遗救修松临藏担戏善卫药悲敢靠伊村戴词森耳差短祖云规窗散迷油旧适乡架恩投弹铁博雷府压超负勒杂醒洗采毫嘴毕九冰既状乱景席珍童顶派素脱农疑练野按犯拍征坏骨余承置臓彩灯巨琴免环姆暗换技翻束增忍餐洛塞缺忆判欧层付阵玛批岛项狗休懂武革良恶恋委拥娜妙探呀营退摇弄桌熟诺宣银势奖宫忽套康供优课鸟喊降夏困刘罪亡鞋健模败伴守挥鲜财孤枪禁恐伙杰迹妹藸遍盖副坦牌江顺秋萨菜划授归浪听凡预奶雄升碃编典袋莱含盛济蒙棋端腿招释介烧误乾坤"






