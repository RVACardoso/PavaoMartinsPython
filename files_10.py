
# # A10.1
# def join(file_lst, out_file):
#     out = ''
#     for file in file_lst:
#         f = open(file, 'r')
#         out += f.read()
#         f.close()
#
#     f = open(out_file, 'w')
#     write_out = f.write(out)
#     f.close()
#     return write_out != 0

# # A10.2
# def ordered_file(file_name):
#     f1 = open(file_name, 'r')
#     lines = f1.readlines()
#     for idx in range(len(lines)-1):
#         if len(lines[idx+1]) <= len(lines[idx]):
#             f1.close()
#             return False
#     f1.close()
#     return True

# # A10.3
# def write_backwards(file1, file2):
#     f1 = open(file1, 'r')
#     lines = f1.readlines()
#     lines[len(lines)-1] += '\n'
#     print(lines)
#     f1.close()
#
#     f2 = open(file2, 'w')
#     for line in lines[::-1]:
#         f2.write(line)
#     f2.close()
#
# # A10.4
# def count_vowels(file):
#     f1 = open(file, 'r')
#     content = f1.read()
#     dict1 = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
#     for letter in content:
#         if letter in dict1:
#             dict1[letter] += 1
#     f1.close()
#     return dict1

# A10.9
