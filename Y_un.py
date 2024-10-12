import subprocess
import time
import os

def run_command(command, wait=True, timeout=None):
    process = subprocess.Popen(command, shell=True)
    if wait:
        start_time = time.time()
        while True:
            if process.poll() is not None:
                break
            if timeout is not None and (time.time() - start_time) > timeout:
                print(f"Процесс '{command}' превысил лимит времени и будет завершен.")
                process.terminate()
                break
            time.sleep(0.1)

def main():
    run_command("service_remote.cmd", timeout=2)
    run_command("2_any_country.cmd", timeout=2)
    run_command("0_russia_update_blacklist_file.cmd", timeout=2)
    command = "runas /user:Administrator service_install_russia_blacklist.cmd"
    run_command(command, timeout=2)

if __name__ == "__main__":
    main()
