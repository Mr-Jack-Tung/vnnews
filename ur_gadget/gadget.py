import os
import subprocess
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

# run cmd commands
def env_setup(command_ls):
    """Run the cmd command. Use the pipe `|` to separate each command"""
    os.system(command_ls)

def runcmd(cmd, verbose = False, *args, **kwargs):
    """Run cmd commands"""
    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

# Data loading
def read_txt(path_to_file):
    """Read a plain text file"""
    with open(path_to_file) as f:
        content = f.read()
    return content


# Memory cleaning
def memory_cleaner():
    """Free up memory from large model data"""
    import gc
    import torch
    gc.collect()
    torch.cuda.empty_cache()


# API Request
def api_request(url, payload={}, method='GET'):
    """Request any API endpoints with a default User-Agent"""
    headers = {
        'accept-language': 'en-US,en;q=0.9',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-platform': '"macOS"',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
    response = requests.request(f"{method}", url, headers=headers, data=payload)
    return response.json()
