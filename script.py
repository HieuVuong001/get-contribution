import subprocess

test = subprocess.run(['git', 'log'], capture_output=True)

print(test.stdout.decode('UTF-8'))