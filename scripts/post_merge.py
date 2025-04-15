import subprocess
from os.path import join

def handle_post_merge():
  # Read current version from VERSION file
  with open(join('QAPPBuilder', 'VERSION'), 'r') as f:
    version = f.read().strip()

  # Tag the current version and push the tags to GitHub
  subprocess.run(["git", "tag", version])
  subprocess.run(["git", "push", "origin", "--tags"])


if __name__ == "__main__":
  handle_post_merge()
