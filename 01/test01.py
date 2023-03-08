# 文字列の基礎
print("python-izum");
print('python-izum');

test_str =  """
test_1
test_2
"""
print(test_str);

# 文字列の連結
test_str='python'
test_str = test_str + '_'
test_str = test_str + 'izm'
print(test_str);

test_str = '012'
test_str += '345'
test_str += '678'
test_str += '9'
print(test_str);

test_str = '0123' * 3
print(test_str);

# 文字列の変換
test_str = 100
print(str(test_str) + '円');

# 文字列の置換
test_str='python-ism'
print(test_str.replace('ism','izm'))

# 文字列の分割
test_str = 'python-izm'
print(test_str.split('-'))

# 文字列の桁揃え
test_str = '123'
print(test_str.rjust(10,'0'))
print(test_str.rjust(10,'!'))
print(test_str.zfill(10))
print(test_str.zfill(3))

# 文字列の検索
test_str = 'python-izm'
print(test_str.startswith('python'))
print(test_str.startswith('izm'))

print('z' in test_str)
print('s' in test_str)

# 大文字・小文字変換
test_str = 'Python-Izm.Com'
print(test_str.upper())
print(test_str.lower())