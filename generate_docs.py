import subprocess

subprocess.run(["pdoc", "./src/visual", "-d", "google", "-o", "./dist"])
