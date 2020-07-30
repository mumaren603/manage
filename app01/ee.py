import os
cmd1 = 'java -version'
# tt = os.popen(cmd1)
# f = tt.read()
# print(f)

cmd2 = 'ipconfig'
with os.popen('python --version') as f:
    text = f.read()
    print("text:",text)
    print("长度为:",len(text))