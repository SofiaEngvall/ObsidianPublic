import os

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)
print('basename:    ', os.path.basename(__file__))
print('dirname:     ', os.path.dirname(__file__))
print('abspath:     ', os.path.abspath(__file__))
print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))

print('[set target path 1]')
target_path_1 = os.path.join(os.path.dirname(__file__), 'token.json')

print('target_path_1: ', target_path_1)

print('read target file:')
with open(target_path_1) as f:
    print(f.read())


print('[change directory]')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print('getcwd:      ', os.getcwd())
