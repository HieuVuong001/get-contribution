import subprocess

def get_log(filename='gitlog.txt'):
    with open(filename, 'w') as f:
        try:
            subprocess.run(['git', 'log'], stdout=f, check=True)
        except Exception:
            print("Cannot get git to run. Are you in a git repository? Did you forget to install git?")