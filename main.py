import subprocess
import time

counter = 0

while True:
    counter += 1

    with open("counter.txt", "w") as f:
        f.write(str(counter))

    subprocess.run(["git", "add", "counter.txt"], check=True)
    subprocess.run(
        ["git", "commit", "-m", f"Auto commit #{counter}"],
        check=True
    )

    # subprocess.run(["git", "push"], check=True)

    time.sleep(10)