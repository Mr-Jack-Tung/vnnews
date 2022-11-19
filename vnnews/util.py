import os
import requests

# Working with file systems
def lmt_detect():
    """Detect the running OS and return file path delimiter"""
    if os.name == 'nt':
        lmt = '\\'
    else:
        lmt = '/'
    return lmt

ROOT_DIR = os.path.abspath(os.curdir)
LMT = lmt_detect()

def file_ls(directory=ROOT_DIR):
    """List all file in the root directory"""
    data = []
    for entry in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, entry)):
            data.append(entry)
    return data

def subdir_ls(basepath=ROOT_DIR):
    """List all subdirectories in the root folder"""
    data = []
    for entry in os.listdir(basepath):
        if os.path.isdir(os.path.join(basepath, entry)):
            data.append(entry)
    return data

# Data loading
def read_txt(path_to_file):
    """Read a plain text file"""
    with open(path_to_file) as f:
        content = f.read()
    return content


def api_request(url, payload={}, method='GET'):
  headers = {
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-platform': '"macOS"',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-api-source': 'pc',
    'x-requested-with': 'XMLHttpRequest',
    'x-shopee-language': 'vi'
  }
  response = requests.request(f"{method}", url, headers=headers, data=payload)
  return response.json()
