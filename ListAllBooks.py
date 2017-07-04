import os
rootdir = "./"

readme_str = '# IT e-books collection \r\n ---------- \r\n'
file_tree_str = ""

for dir in os.listdir(rootdir):
    if os.path.isdir(dir) and dir != r".git":
        readme_str += "## " + dir +"\r\n"
        file_tree_str += "\r\n" + dir + "\r\n"
        for file in os.listdir(dir):
            if os.path.isfile(os.path.join(rootdir,dir,file)):
                readme_str += file + "\r\n"
                file_tree_str += "    " + file + "\r\n"

print(file_tree_str)

readme_file = open(r"readme.md", "w")
readme_file.write(readme_str)