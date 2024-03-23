import os;
import shutil;
import subprocess;

if __name__ == "__main__":
    # copy over any html files
    for root, dir, files in os.walk("./dev/html"):
        for f in files:
            if os.path.splitext(root + f)[1] == ".html":
                shutil.copy(os.path.join(root, f), "./build")
    
    subprocess.run("tsc")