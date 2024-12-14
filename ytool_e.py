#ytool_e.py模块
#一个包含了多个实用功能的函数，其目标是用尽可能少的代码做尽可能多的事。
import random,base64
import os,signal
from urllib.parse import quote
import urllib.parse
import socket,requests
import sys
import platform,datetime
from shutil import move
import warnings;warnings.simplefilter("always", ImportWarning)

try:
    from isos import getos
    import isos
except:
    warnings.warn("isos模块没有被导入！", ImportWarning)
    def getos():
        if "android" in platform.platform().lower():# and "linux" in platform.platform().lower():
            system = "Android"
            ch = os.getcwd()
            try:
                os.chdir("/data/data/com.termux/files/home")
                if 'termux' in os.getcwd():
                    os.chdir(ch)
                    return "Termux"
            except:
                pass
        else:
            system = platform.system().replace("Darwin", "macOS")
        return system
try:
    import win32api
    import win32con
    import win32console
except:
    pass

#import this
"""
import PyPDF2
from reportlab.pdfgen import canvas
"""

FILE = os.path.basename(__file__)

modul = os.path.splitext(FILE)[0]

E = 2.7182818284590452353602874713

PI = 3.1415926535897932384626433832

ysystem = getos()


dns_ip = (
    "1.2.4.8",
    "8.8.8.8",
    "8.8.4.4",
    "208.67.222.222",
    "180.76.76.200",
    "208.67.220.220",
    "1.1.1.1",
    "1.0.0.1",
    "180.76.76.76",
    "223.5.5.5",
    "223.6.6.6",
    "119.29.29.29",
    "114.114.114.114",
    "114.114.115.115",
    "9.9.9.9",
    "219.141.136.10",
    "219.141.140.10",
    "117.50.11.11",
    "52.80.66.66",
    "117.50.10.10",
    "52.80.52.52",
    "117.50.60.30",
    "52.80.60.30",
    "101.226.4.6",
    "218.30.118.6",
    "123.125.81.6",
    "140.207.198.6",
    "1.1.8.8",
    "223.5.5.5",
    "223.6.6.6",
    "37.235.1.174",
    "37.235.1.177",
    "216.146.35.35",
    "216.146.36.36",
    "8.26.56.26",
    "8.20.247.20",
    "64.6.64.6",
    "64.6.65.6",
    "77.88.8.8",
    "77.88.8.1",
    "101.226.4.6",
    "218.30.118.6",
    "4.2.2.1",
    "4.2.2.2",
    "122.112.208.1",
    "139.9.23.90",
    "114.115.192.11",
    "116.205.5.1",
    "116.205.5.30",
    "122.112.208.175",
    "139.159.208.206",
    "180.184.1.1",
    "180.184.2.2",
    "168.95.192.1",
    "168.95.1.1",
    "203.80.96.10",
    "203.80.96.9",
    "199.85.126.10",
    "199.85.127.10",
    "216.146.35.35",
    "216.146.36.36",
    "64.6.64.6",
    "64.6.65.6",
    "221.131.143.69",
    "112.4.0.55",
    "221.130.13.133",
    "211.103.55.50",
    "221.130.56.241",
    "211.103.13.101",
    "211.138.200.69",
    "116.199.0.200",
    "116.116.116.116",
    "61.235.70.252",
    "211.98.4.1"
)


# 用户字符串
user_agents = (
    "Dalvik/2.1.0 (Linux; U; Android 12; PFUM10 Build/SKQ1.211209.001)",
    "Mozilla/5.0 (Linux; Android 12; PFUM10 Build/SKQ1.211209.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 T7/13.56 SP-engine/2.95.0 baiduboxapp/13.56.5.10 (Baidu; P1 12) NABar/1.0",
    "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 5 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 12; PFUM10 Build/SKQ1.211209.001) 7.78.0 os/android model/PFUM10 mobi_app/android build/7780300 channel/oppo innerVer/7780310 osVer/12 network/2",
    "Mozilla/5.0 (Linux; U; Android 12; zh-cn; PFUM10 Build/SKQ1.211209.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36 EdgA/124.0.0.0",
    "Mozilla/5.0 (Linux; U; Android 12; zh-cn; Unknown Build/SKQ1.211209.001) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 12; zh-CN; PFUM10 Build/SKQ1.211209.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Quark/6.12.5.560 Mobile Safari/537.36",
    "com.dragon.read/62532 (Linux; U; Android 12; zh_CN; PFUM10; Build/SKQ1.211209.001; Cronet/TTNetVersion:d4b582b8 2024-03-11 QuicVersion:1886aac1 2023-11-17)",
    "Mozilla/5.0 (Linux; Android 12; PFUM10 Build/SKQ1.211209.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046281 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; PFUM10 Build/SKQ1.211209.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160175 MMWEBSDK/20240404 MMWEBID/9666 MicroMessenger/8.0.49.2600(0x2800313F) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.2478.87",
    "Android 12; zh_CN; PFUM10 Build/SKQ1.211209.0011121991229169M-8033763061504916416",
    "com.zuoyebang.airclass/1242 (Linux; U; Android 12; zh_CN; PFUM10; Build/SKQ1.211209.001; Cronet/88.0.4324.181)",
    "Mozilla/5.0 (Linux; Android 12; PFUM10 Build/SKQ1.211209.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 Html5Plus/1.0"
)

# 预定义的MIME类型字典
mime_types = {
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'gif': 'image/gif',
    'svg': 'image/svg+xml',
    'tif': 'image/tiff',
    'tiff': 'image/tiff',
    'webp': 'image/webp',
    'mp4': 'video/mp4',
    'mpeg': 'video/mpeg',
    'mpg': 'video/mpeg',
    'mov': 'video/quicktime',
    'webm': 'video/webm',
    'ogv': 'video/ogg',
    'mp3': 'audio/mpeg',
    'ogg': 'audio/ogg',
    'weba': 'audio/webm',
    'pdf': 'application/pdf',
    'doc': 'application/msword',
    'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'xls': 'application/vnd.ms-excel',
    'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'zip': 'application/zip',
    'rar': 'application/x-rar-compressed',
    '7z': 'application/x-7z-compressed',
    'txt': 'text/plain',
    'html': 'text/html',
    'htm': 'text/html',
    'css': 'text/css',
    'js': 'text/javascript',
    'ttf': 'font/ttf',
    'woff': 'font/woff',
    'woff2': 'font/woff2'
}

def get_mime_type(filename):
    """
    猜测文件的MIME类型
    """
    # 从文件名中提取扩展名
    ext = filename.split('.')[-1].lower()
    # 返回对应的MIME类型，如果找不到则返回None
    if mime_types.get(ext):
        return mime_types.get(ext)
    else:
        return 'text/plain'



def replace_html_with_htm(requested_path):
    if not os.path.exists(requested_path):
        # 检查Python版本是否大于3.10
        if sys.version_info >= (3, 10):
            match requested_path.lower():
                case s if s.endswith('.html'):
                    return s[:-5] + '.htm'
                case s if s.endswith('.htm'):
                    return s[:-4] + '.html'
                case _:
                    return requested_path
        else:
            if requested_path.lower().endswith('.html'):
                new_filename = requested_path[:-5] + '.htm'
            elif requested_path.lower().endswith('.htm'):
                new_filename = requested_path[:-4] + '.html'
            else:
                return requested_path
            return new_filename
    return requested_path

def getlip():
    '''尝试通过创建套接字来获取本机的IP地址。
    
    如果操作失败（例如，无网络连接），则返回127.0.0.1。
    
    返回:
    - str: 本机的IP地址，或者在失败时返回127.0.0.1。
    '''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('1.2.4.8', 53))
        ip = s.getsockname()[0]
    except Exception as e:
        print(f"无法获取IP地址: {e}")
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def printlog(file, e, con=""):
    """con: 额外加入的错误信息"""
    try:
        with open(file, "a+") as a:
            a.write(f"{con}{e}\n")
        try:
            import tkinter
            tkinter.messagebox.show_error(f"{con}{e}")
        except:
            print(f"{con}{e}")
    except Exception as aa:
        print(f"Error: {aa}")


def get_system_info():
    system_info = {}
    bits, linkage = platform.architecture()
    bits = bits.replace("bit", "位")
    system_info["架构"] = bits
    if linkage:
        system_info["链接"] = linkage

    if FILE.endswith('.py'):
        system_info["Python 版本"] = platform.python_version()

    release = platform.release()
    if "android" in release.lower():
        system = "Android"
    else:
        system = platform.system()
    system_info["操作系统"] = system
    system_info["系统详细信息"] = release

    system_info["系统构建版本"] = platform.version()

    system_info["计算机网络名"] = platform.uname().node
    system_info["处理器架构"] = platform.uname().machine
    if platform.uname().processor:
        system_info["处理器具体型号"] = platform.uname().processor

    if system == "Windows":
        system_info["Windows 版本信息"] = platform.win32_ver()
    elif system == "Darwin":
        system_info["macOS 版本信息"] = platform.mac_ver()
    elif system == "Linux":
        libc_ver_info = platform.libc_ver()
        if libc_ver_info[0]:
            if libc_ver_info[1] == "":
                system_info["Libc 版本信息"] = "无法获取Libc 版本信息"
            else:
                system_info["Libc 版本信息"] = libc_ver_info[1]

    return system_info



def reget(url, params=None, headers=None, cookies=None, files=None, data=None, json=None, auth=None, timeout=3.0, allow_redirects=True, proxies=None, verify=True, stream=False, cert=None, hooks=None, raise_status=True, session=False):
    """
    封装requests.get方法，包含所有参数并设置默认值。

    :param url: 要请求的URL地址。
    :param params: 一个字典或字节序列，将会被编码为查询字符串格式附加到URL上。
    :param headers: 一个字典，包含了HTTP请求的头部。
    :param cookies: 一个字典或CookieJar对象，包含了要发送的cookies。
    :param files: 一个字典，包含了要上传的文件。
    :param data: 一个字典或字节序列，将会被发送在请求的body中。
    :param json: 一个字典，将会被编码为JSON格式并发送在请求的body中。
    :param auth: 一个元组，包含了HTTP认证的用户名和密码。
    :param timeout: 一个浮点数或元组，指定了请求的超时时间。
    :param allow_redirects: 一个布尔值，默认为False，表示是否允许重定向。
    :param proxies: 一个字典，包含了代理服务器的地址。
    :param verify: 一个布尔值或字符串，指定是否验证SSL证书。
    :param stream: 一个布尔值，默认为True，表示是否要立即下载响应内容。
    :param cert: 一个字符串或元组，包含了SSL证书的路径。
    :param trust_env: 一个布尔值，默认为True，表示是否从环境变量中获取代理设置。
    :param hooks: 一个字典，包含了事件挂钩函数。
    :param raise_status: 一个布尔值，默认为True，表示是否在HTTP请求返回不成功的状态码时抛出异常。
    :param session: 一个Session对象，用于持久化参数。
    :return: requests.Response对象。
    """
    response = requests.get(
        url=url,
        params=params,
        headers=headers,
        cookies=cookies,
        files=files,
        data=data,
        json=json,
        auth=auth,
        timeout=timeout,
        allow_redirects=allow_redirects,
        proxies=proxies,
        verify=verify,
        stream=stream,
        cert=cert,
        hooks=hooks,
        raise_status=raise_status,
        session=session
    )
    return response

def get_file_size(file_path):
    """
    获取文件的大小，单位自动转换为KB, MB, GB, TB, PB, EB, 或 ZB。
    
    :param file_path: 文件路径
    :return: 文件大小的可读字符串表示
    """
    try:
        # 获取文件大小（字节）
        size_bytes = os.path.getsize(file_path)
        
        # 单位
        units = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB")
        
        # 如果文件大小小于1KB，直接返回字节
        if size_bytes < 1024:
            return f"{size_bytes} {units[0]}"
        
        # 计算合适的单位
        size = size_bytes
        unit_index = 0
        while size >= 1024 and unit_index < len(units) - 1:
            size /= 1024
            unit_index += 1
        
        # 返回格式化的字符串
        return f"{size:.2f} {units[unit_index]}"
    except Exception as e:
        return None

def get_dir_size(directory_path):
    """
    获取目录的大小，单位自动转换为KB, MB, GB, TB, PB, EB, 或 ZB。
    
    :param directory_path: 目录路径
    :return: 目录大小的可读字符串表示
    """
    try:
        # 初始化总大小
        total_size = 0
        
        # 遍历目录及其子目录
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                # 获取文件的完整路径
                file_path = os.path.join(root, file)
                # 累加文件大小
                total_size += os.path.getsize(file_path)
        
        # 单位
        units = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB")
        
        # 如果目录大小小于1KB，直接返回字节
        if total_size < 1024:
            return f"{total_size} {units[0]}"
        
        # 计算合适的单位
        size = total_size
        unit_index = 0
        while size >= 1024 and unit_index < len(units) - 1:
            size /= 1024
            unit_index += 1
        
        # 返回格式化的字符串
        return f"{size:.2f} {units[unit_index]}"
    except Exception as e:
        return None

def getlipv6(dns='2001:4860:4860::8888', port=53):
    """
    尝试通过连接到Google的公共DNS服务器来获取本机的IPv6地址。
    
    如果操作失败（例如，无网络连接），则返回None。
    
    返回:
    - str: 本机的IPv6地址，或者在失败时返回None。
    """
    try:
        with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
            s.connect((dns, port))
            return s.getsockname()[0]
    except socket.error as e:
        warnings.warn(f"IPv6获取出现问题: {e}")
        return '::1'

def nowtime(gs="%Y-%m-%d %H:%M:%S"):
    '''获取当前日期和时间'''
    return datetime.datetime.now().strftime(gs)

def time():
    '''获取当前日期和时间'''
    current_datetime = datetime.datetime.now()
    # 将日期和时间转换为字符串
    str_datetime = str(current_datetime)
    str_second = str_datetime[0:19]
    return str_second

def nowdir():
    return os.getcwd()

def nowfiledir():
    return os.path.dirname(os.path.abspath(__file__))

def yexit(n=0):
    """
    提示用户按回车键退出程序。
    """
    input("按回车键退出")
    sys.exit(n)

def y_exit(n=0):
    print("此程序将立即退出")
    os._exit(status=n)

def yerrexit():
    print("程序遇到严重错误，为减少损失，即将退出")
    os.abort()

def check_elements_in_string(lst, target_string):
    """
    检查列表中的所有元素是否都存在于目标字符串中。

    使用列表推导式和all()函数来验证列表中的每个元素是否为字符串的子串。
    如果列表中的所有元素都在目标字符串中找到，则返回True，否则返回False。

    参数:
    lst (list): 要检查的元素列表。
    target_string (str): 目标字符串，用于检查列表中的元素是否存在。

    返回:
    bool: 如果列表中的所有元素都在目标字符串中找到，则返回True，否则返回False。

    示例:
    >>> check_elements_in_string(['hello', 'world'], 'helloworld')
    True
    >>> check_elements_in_string(['hello', 'moon'], 'helloworld')
    False

    注意:
    - 函数对大小写敏感。
    - 如果目标字符串或列表中的元素包含特殊字符，可能会影响匹配结果。
    - 函数假设输入的lst是列表类型，target_string是字符串类型。
    """
    return all(element in target_string for element in lst)

def check_elements_in_string_lower(lst, target_string):
    """
    检查列表中的所有元素（不区分大小写）是否都存在于目标字符串中。

    使用列表推导式和all()函数来验证列表中的每个元素（转换为小写）是否为字符串的子串（也转换为小写）。
    如果列表中的所有元素都在目标字符串中找到，则返回True，否则返回False。

    参数:
    lst (list): 要检查的元素列表。
    target_string (str): 目标字符串，用于检查列表中的元素是否存在。

    返回:
    bool: 如果列表中的所有元素都在目标字符串中找到，则返回True，否则返回False。

    例子:
    >>> check_elements_in_string_case_insensitive(['Hello', 'world'], 'helloworld')
    True
    >>> check_elements_in_string_case_insensitive(['Hello', 'moon'], 'helloworld')
    False

    注意:
    - 函数将目标字符串和列表中的元素都转换为小写，以实现大小写不敏感的匹配。
    - 如果目标字符串或列表中的元素包含特殊字符，可能会影响匹配结果。
    - 函数假设输入的lst是列表类型，target_string是字符串类型。
    """
    return all(element.lower() in target_string.lower() for element in lst)


def find_replace(file_path, search_text, replace_text):
    with open(file_path, 'r') as f:
        text = f.read()
        modified_text = text.replace(search_text, replace_text)

    with open(file_path, 'w') as f:
        f.write(modified_text)

def count_words(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        word_count = len(text.split())
    return word_count

def sort_files(directory_path):
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            file_extension = filename.split('.')[-1]
            destination_directory = os.path.join(directory_path, file_extension)

            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)

            move(os.path.join(directory_path, filename), os.path.join(destination_directory, filename))

'''
def read_pdf(file_path):
    """读取PDF文件并返回一个PdfFileReader对象"""
    with open(file_path, 'rb') as file:
        return PyPDF2.PdfFileReader(file)

def extract_text_from_page(pdf_reader, page_number):
    """从指定页面提取文本"""
    page = pdf_reader.getPage(page_number)
    return page.extractText()

def merge_pdfs(pdf_paths, output_path):
    """合并PDF文件"""
    writer = PyPDF2.PdfFileWriter()
    for path in pdf_paths:
        with open(path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            for i in range(reader.numPages):
                writer.addPage(reader.getPage(i))
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

def split_pdf(pdf_reader, output_path, start_page, end_page):
    """分割PDF文件"""
    writer = PyPDF2.PdfFileWriter()
    for i in range(start_page, end_page + 1):
        writer.addPage(pdf_reader.getPage(i))
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

def rotate_page(pdf_reader, page_number, output_path):
    """旋转PDF页面"""
    page = pdf_reader.getPage(page_number)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

def add_watermark(pdf_path, watermark_text, output_path):
    """给PDF添加水印"""
    watermark = canvas.Canvas("watermark.pdf")
    textobject = watermark.beginText(72, 720)
    textobject.setTextOrigin(72, 720)
    textobject.setFont("Helvetica", 60)
    textobject.setFillColor("grey")
    textobject.textLines(watermark_text)
    watermark.drawText(textobject)
    watermark.save()

    reader = read_pdf(pdf_path)
    watermark_reader = read_pdf("watermark.pdf")
    for i in range(watermark_reader.numPages):
        page = watermark_reader.getPage(i)
        for j in range(reader.numPages):
            reader.getPage(j).mergePage(page)
    with open(output_path, 'wb') as output_file:
        reader.write(output_file)
'''
"""
# 使用示例
if __name__ == "__main__":
    pdf_reader = read_pdf('example.pdf')
    print(extract_text_from_page(pdf_reader, 0))

    merge_pdfs(['file1.pdf', 'file2.pdf'], 'merged.pdf')

    split_pdf(pdf_reader, 'splitted.pdf', 0, 1)

    rotate_page(pdf_reader, 0, 'rotated_page.pdf')

    add_watermark('example.pdf', 'CONFIDENTIAL', 'watermarked.pdf')
"""

import urllib.parse

def url_encode(input_string):
    """对字符串进行URL编码"""
    # safe参数设置为空字符串，表示所有字符都需要编码
    return urllib.parse.quote(input_string, safe='')
"""
# 示例使用
utf8_string = '你好，世界！'
url_encoded_string = utf8_to_url_encoded(utf8_string)
print(url_encoded_string)  # 输出: %E4%BD%A0%E5%A5%BD%EF%BC%8C%E4%B8%96%E7%95%8C%EF%BC%81
"""
def url_decode(input_string):
    """对字符串进行URL解码"""
    return urllib.parse.unquote(input_string)
"""
# 示例使用
url_encoded_string = '%E4%BD%A0%E5%A5%BD%EF%BC%8C%E4%B8%96%E7%95%8C%EF%BC%81'
utf8_string = url_encoded_to_utf8(url_encoded_string)
print(utf8_string)  # 输出: 你好，世界！
"""

def generate_html_directory_listing(directory_path='.'):
    # 获取目录列表
    files_and_dirs = os.listdir(directory_path)
    
    # 开始构建HTML内容
    html_content = f"""
<!DOCTYPE HTML><html><head><meta charset="utf-8">
<title>Directory listing for {directory_path}</title></head><body>
<h1>Directory listing for {directory_path}</h1><hr><ul>
"""
    # 遍历文件和目录，添加到HTML内容中
    for item in files_and_dirs:
        # 对文件名进行URL编码
        encoded_item = quote(item)
        # 添加列表项到HTML
        html_content += f'<li><a href="{encoded_item}">{item}</a></li>\n'
    
    # 结束HTML内容
    html_content += "</ul><hr></body></html>"
    return html_content

import base64

def reverse_string(s):
    """反转字符串"""
    return s[::-1]

def url_encode(s):
    """URL编码"""
    return urllib.parse.quote_plus(s)

def url_decode(s):
    """URL解码"""
    return urllib.parse.unquote(s)

def contains_digit(s):
    """检查是否包含数字"""
    return any(char.isdigit() for char in s)

def contains_letter(s):
    """检查是否包含字母"""
    return any(char.isalpha() for char in s)

def word_count(s):
    """单词计数"""
    words = s.split()
    return {word: words.count(word) for word in words}

def base64_encode(s):
    """Base64编码"""
    return base64.b64encode(s.encode()).decode()

def base64_decode(s):
    """Base64解码"""
    return base64.b64decode(s.encode()).decode()

def caesar_cipher(s, shift):
    """凯撒密码处理"""
    encrypted_text = ""
    for char in s:
        if char.isalpha():  # 检查字符是否为字母
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                encrypted_text += chr((ord(char) - start + shift_amount) % 26 + start)
            else:
                start = ord('A')
                encrypted_text += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            encrypted_text += char  # 非字母字符不变
    return encrypted_text


def get_all_drives():
    '''生成存在的驱动器列表'''
    return [f'{letter}:' for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f'{letter}:')]

def nowdriver():
    '''获取当前工作目录的驱动器部分'''
    current_path = os.getcwd()
    if current_path.startswith("/"):
        return
    current_drive = current_path[0] + ':'
    return current_drive

try:
    def simulate_keyboard_interrupt(ctrl_event=win32con.CTRL_C_EVENT, process_group_id=0):
        """
        模拟键盘中断信号。
        
        :param ctrl_event: 要发送的控制事件，可以是win32con.CTRL_C_EVENT或win32con.CTRL_BREAK_EVENT。
        :param process_group_id: 进程组ID，0表示当前进程。
        """
        if ysystem == 'Windows':
            win32console.GenerateConsoleCtrlEvent(ctrl_event, process_group_id)
        else:
            os.kill(pid, sig=signal.SIGTERM)
except:
    pass

def make_list(filename, ignore_prefixes=(), encoding='utf-8'):
    """
    逐行读取整个文本文件，并组成一个列表
    可以根据需要忽略以特定字符开头的行
    """
    with open(filename, 'r', encoding=encoding) as file:
        lines = [line.strip() for line in file if line.strip() and not any(line.startswith(prefix) for prefix in ignore_prefixes)]
    return lines

def get_random_line(filename='/storage/emulated/0/yunfeiy/励志名言.txt'):
    lines = make_list(filename, ('#',))
    if lines:  # 确保列表不为空
        return random.choice(lines)  # 随机选择一行
    else:
        return


def c_substr(main_string, substrings):
    """
    计算主字符串中每个子字符串出现的次数。

    参数:
    main_string (str): 要搜索的主字符串。
    substrings (list): 要计数的子字符串列表。

    返回值:
    dict: 一个字典，其键为子字符串，值为它们在主字符串中出现的次数。
    """
    count_dict = {}
    for substring in substrings:
        count = main_string.count(substring)
        count_dict[substring] = count
    return count_dict

# 使用示例
#main_string = "hello world, hello moon"
#substrings = ["hello", "world", "moon", " "]
#result = c_substr(main_string, substrings)
#print(result)

def c_a_substr(main_string, substrings):
    """
    计算所有子字符串在主字符串中的总出现次数。

    参数:
    main_string (str): 要搜索的主字符串。
    substrings (list): 要计数的子字符串列表。

    返回值:
    int: 所有子字符串在主字符串中的总出现次数。
    """
    total_count = 0
    for substring in substrings:
        total_count += main_string.count(substring)
    return total_count

# 示例使用
#main_string = "hello world, hello moonshot"
#substrings = ["hello", "world", "moon", " "]
#total_count = c_a_substr(main_string, substrings)
#print(f"所有子字符串的总出现次数是: {total_count}")


def read_file(file_path):
    """
    读取文件并返回文件内容的列表，每个元素是一行。
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        quotes = file.readlines()
    return [quote.strip() for quote in quotes]

def write_file(file_path, quotes):
    """
    将清洗后的行列表写入文件。
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        for quote in quotes:
            file.write(quote + '\n')

def remove_duplicates(quotes):
    """
    去除重复的行，保持原有顺序。
    """
    seen = {}
    unique_quotes = []
    for quote in quotes:
        quote_text = quote
        if quote_text not in seen:
            seen[quote_text] = True
            unique_quotes.append(quote)
    return unique_quotes

def txtmain(file_path):
    """
    主函数，读取文件，去除重复的行，并将结果写回文件。
    """
    quotes = read_file(file_path)
    unique_quotes = remove_duplicates(quotes)
    write_file(file_path, unique_quotes)
    print(f"去重完成，共保留了 {len(unique_quotes)} 条唯一的行。")

def yrun(iterations, main_func, *hooks):  #数字为附加函数的个数
    """
    在循环中交替调用主函数和附加函数。

    :param iterations: 循环次数
    :param main_func: 主函数，每次循环都会调用
    :param hooks: 可选的附加函数，按照顺序在主函数后调用
    """
    hooks_length = len(hooks)
    
    for i in range(iterations):
        # 先调用主函数
        main_func()

        # 调用附加函数（如果有）
        if hooks_length > 0:
            hook_index = i % hooks_length
            hooks[hook_index]()


# 定义常见服务器的默认端口和备用端口列表
SERVER_PORTS = {
    'http': [80, 8080, 8008, 8000, 8888],
    'https': [443, 8443, 8844, 8081, 8444],
    'ftp': [21, 2121, 1021, 990, 2021],
    'smtp': [25, 2525, 587, 465],  # 简单邮件传输协议
    'pop3': [110, 995],  # 邮局协议版本3
    'imap': [143, 993],  # 互联网消息访问协议
    'ssh': [22, 2222],  # 安全外壳协议
    'telnet': [23, 8023],  # 远程登录服务
    'dns': [53, 5353],  # 域名系统
    'snmp': [161, 162],  # 简单网络管理协议
    'mysql': [3306, 3307],  # MySQL数据库
    'postgresql': [5432, 5433],  # PostgreSQL数据库
    'mongodb': [27017, 27018],  # MongoDB数据库
    'redis': [6379, 6380],  # Redis数据库
    'rdp': [3389, 3390],  # 远程桌面协议
    'nfs': [2049, 4045],  # 网络文件系统
    'smb': [139, 445],  # 服务器消息块
    'rpc': [111, 32771, 1111],  # 远程过程调用
    'nntp': [119, 8888],  # 网络新闻传输协议
    'ntp': [123, 1234],  # 网络时间协议
    'ldap': [389, 636],  # 轻量级目录访问协议
    'sip': [5060, 5061],  # 会话初始协议
    'rsync': [873, 8730],  # 文件同步协议
    "unknown": []
}

def is_port_available(port):
    """
    检查指定端口是否可用。
    
    :param port: int, 要检查的端口号
    :return: bool, 如果端口可用则返回True，否则返回False
    """
    if not isinstance(port, int) or not (0 <= port <= 65535):
        raise ValueError("端口号必须是一个0到65535之间的整数")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind(('localhost', port))
            return True
        except Exception as e:
            return False


#接下来的这个函数和端口字典应一起使用
def find_free_port(server_type="unknown"):
    """
    根据服务器类型自动选择可用的端口。
    
    :param server_type: str, 服务器类型（如'http', 'https', 'ftp'）
    :return: int, 可用的端口号
    :raises ValueError: 如果server_type不在预定义的SERVER_PORTS中
    """
    server_type = server_type.lower()  # 将server_type转换为小写
    if server_type not in SERVER_PORTS:
        raise ValueError(f"Unsupported server type: {server_type}")
    
    ports = SERVER_PORTS[server_type]
    attempted_ports = set()  # 用于记录尝试过的端口
    
    for port in ports:
        if is_port_available(port):
            return port
        attempted_ports.add(port)
    
    # 如果没有在已知端口列表中找到合适端口，则开始随机生成端口尝试
    for _ in range(10):  # 最多尝试10次随机端口
        random_port = random.randint(1024, 65535)  # 生成1024到65535之间的随机端口（通常的可用范围）
        if random_port not in attempted_ports and is_port_available(random_port):
            return random_port
        attempted_ports.add(random_port)

    #如果随机之后没有结果
    for _ in range(64511):  # 端口
        random_port = 1024
        if random_port not in attempted_ports and is_port_available(random_port):
            return random_port
        random_port += 1
        attempted_ports.add(random_port)
        
    # 如果没有找到可用的端口，抛出运行时异常
    raise RuntimeError(f"没有找到可用的端口")



def help():
    """
    显示模块帮助信息，包括函数和类的帮助信息。
    """
    print(f"{modul}模块帮助信息:")
    print("-" * 50)
    
    import sys
    import inspect
    
    current_module = sys.modules[__name__]
    for name, obj in inspect.getmembers(current_module):
        if (inspect.isfunction(obj) or inspect.isclass(obj)) and not name.startswith('_'):
            docstring = obj.__doc__ if obj.__doc__ else "暂无文档"
            print(f"{name}: {docstring}")
            
    print("-" * 50)
    print(f"{modul}模块旨在提供一个实用的工具集，以便于快速完成常见的编程任务。\n二级教授编写")
    yexit()  # 等待用户输入


def help_write():
    """
    将模块帮助信息写入到文件中，而不是显示，方便阅读查看。
    """
    with open(f"{modul}_help.txt", "w+") as f:
        f.write(f"{modul}模块帮助信息:\n")
        f.write("-" * 50 + "\n")
        
        import sys
        import inspect
        
        current_module = sys.modules[__name__]
        for name, obj in inspect.getmembers(current_module):
            if (inspect.isfunction(obj) or inspect.isclass(obj)) and not name.startswith('_'):
                docstring = obj.__doc__ if obj.__doc__ else "暂无文档"
                f.write(f"{name}: {docstring}\n")
                
        f.write("-" * 50 + "\n")
        f.write(f"{modul}模块旨在提供一个实用的工具集，以便于快速完成常见的编程任务。\n\n二级教授编写\n")
    print("已写入，",end="")
    yexit()  # 等待用户输入
'''
# 示例使用
if __name__ == "__main__":
    try:
        http_port = find_free_port('http')
        print(f"HTTP server can use port: {http_port}")
        
        https_port = find_free_port('https')
        print(f"HTTPS server can use port: {https_port}")
        
        ftp_port = find_free_port('FTP')
        print(f"FTP server can use port: {ftp_port}")
        
        port = find_free_port()
        print(f"server can use port: {port}")
        
        help()
        
    except Exception as e:
        print(f"Error: {e}")
'''
import importlib
def run_function(module_name, function_name, *args, **kwargs):
    try:
        # 动态导入模块
        directory, filename = os.path.split(module_name)
        if directory:
            os.chdir(directory)
        filename = os.path.splitext(filename)[0]
        module = importlib.import_module(filename)
        # 获取函数
        func = getattr(module, function_name)
        # 执行函数
        result = func(*args, **kwargs)
        return result
    except ModuleNotFoundError:
        print(f"错误: 要导入的模块 {filename} 不存在")
    except AttributeError:
        print(f"错误: 模块 '{filename}' 没有叫 '{function_name}' 的函数")
    except Exception as e:
        print(f"发生了一个错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {FILE} <function_name> [args]")
        print(f"""\
Help: {modul}模块命令行模式，通过传入模块名和要调用的函数以及此函数的参数来直接运行模块中的函数。
需传入的参数标准格式: <function_name> [args]
其中function_name是模块中的函数，[args]是函数的参数，没有则不传入
你可以用python {FILE} help来获取 {modul} 的帮助""")
    else:
        module_name = f'{modul}'
        function_name = sys.argv[1]
        args = sys.argv[2:]
        result = run_function(modul, function_name, *args)
        if result is not None:
            print(f"{result}")

