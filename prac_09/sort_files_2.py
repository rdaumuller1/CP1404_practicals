import os


def main():
    extension_to_category = {}
    os.chdir("FilesToSort")
    extension = ''                          # help
    for file_name in os.listdir('.'):
        if os.path.isdir(file_name):
            continue

        extension = file_name.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

    for file_name in os.listdir('.'):
        os.rename(file_name, "{}/{}".format(extension_to_category[extension], file_name))


main()
