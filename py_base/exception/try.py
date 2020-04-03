##try:
##    int('ab')
##except ValueError as reason:
##    print(reason)
##else:
##    print('无异常，else执行....')
##print('异常已经被处理，此处可以被执行....')

try:
    with open('data.txt','w') as f:
        for line in f:
            print(line)
except OSError as reason:
    print(str(reason))
