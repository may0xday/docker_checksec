import re
import argparse

def main():
    with open(args.file, 'r') as f:
        filedecs = f.read()
        from_checker(filedecs)
        user_checker(filedecs)
        secret_env_checker(filedecs)
        f.close()

def from_checker(filename):
    pattern = r'^FROM+(.+?):((?!latest).+)'
    if re.findall(pattern, filename):
        print('[SECURE] Dockerfile FROM uses version tag')
    else:
        print('[WARN] [UNSECURE] Dockerfile dont use version tag or uses "latest". Please specify particular version tag.')
        
def user_checker(filename):

    flag_rootexec = 0
    flag_addgroup = 0
    flag_useradd = 0
    
    pattern_useradd = r'RUN+\s+useradd'
    if re.findall(pattern_useradd, filename):
        flag_useradd = 1
        
    pattern_groupadd = r'RUN+\s+addgroup'
    if re.findall(pattern_groupadd, filename):
        flag_addgroup = 1
    
    pattern_root = r'USER+\s+root'
    if re.findall(pattern_root, filename):
        flag_rootexec = 1
    
    if flag_useradd != 0 or flag_addgroup != 0:
        print ('[SECURE] Dockerfile contains useradd and addgroup to create a user for a container')
    else: 
        print('[FATAL] [UNSECURE] CIS-DI-0001 - Create a user for the container. It is a good practice to run the container as a non-root user, if possible.')
    
    if flag_rootexec != 0:
        print('[WARN] [UNSECURE] Detected USER root in the dockerfile. Dont forget to change to another non-root user after.')
    
def secret_env_checker(filename):
    pattern_useradd = r'[a-zA-Z0-9]{16,128}'
    secret_list = re.findall(pattern_useradd, filename)
    if len(secret_list) != 0:
        print('[WARN] [UNSECURE] CIS-DI-0010 - Detected some weird 16-128 length strings, possibility of API key exposing. Do not store secrets in Dockerfiles')
        for i in secret_list:
            print('[!] Probable secret found: ', i)
    else:
        print('[SECURE] Dockerfile is safe for API secrets')



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dockerfile checksec python script')
    parser.add_argument('--file', type=str, help='Dockerfile')
    args = parser.parse_args()
    
    main()