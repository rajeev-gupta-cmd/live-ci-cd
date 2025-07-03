def write_to_file(filename,content):
    f = open(filename,"w")
    f.write(content)

if __name__ == "__main__":
    write_to_file('output.txt', "hello from python script")

    print("file created and ran successfully")
