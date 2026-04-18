# ============================================================
# ⚠️  WARNING — PLEASE READ BEFORE RUNNING
# ============================================================
#
# 1. EDUCATIONAL USE ONLY
#    This script is intended solely for learning browser
#    automation with Selenium. It is not designed or endorsed
#    for any abusive or deceptive purpose.
#
# 2. ONLY TEST YOUR OWN WEBSITES
#    Never run automated scripts against websites you do not
#    own or have explicit written permission to test.
#    Doing so may violate Terms of Service and applicable law.
#
# 3. LEGAL NOTICE
#    Unauthorized automated access to third-party platforms
#    may violate the Computer Fraud and Abuse Act (CFAA),
#    the Computer Misuse Act (UK), or equivalent laws in
#    your jurisdiction. Violations can result in civil or
#    criminal liability.
#
# 4. NO WARRANTY
#    This code is provided as-is with no guarantees.
#    The author accepts no responsibility for misuse.
#
# 5. RESPECT ROBOTS.TXT
#    Always check a website's robots.txt and Terms of Service
#    before running any automated scripts against it.
#
# 6. LEGAL DISCLAIMER
#    The author of this script accepts no responsibility
#    for any legal action, account bans, or consequences
#    arising from misuse of this code. Use at your own risk.
# ============================================================
# --- INSTALLATION FOR COLAB ---
!apt-get update
!apt-get install -y wget
!wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
!dpkg -i google-chrome-stable_current_amd64.deb
!apt --fix-broken install -y
!wget https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
!unzip chromedriver_linux64.zip
!mv chromedriver /usr/bin/chromedriver
!chown root:root /usr/bin/chromedriver
!chmod +x /usr/bin/chromedriver
!pip install undetected-chromedriver selenium fake-useragent

# --- IMPORTS ---
import subprocess
import undetected_chromedriver as uc
from fake_useragent import UserAgent
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIGURATION ---
URL = "only use for educational puropose "
MAX_ITERATIONS = 5
DELAY_RANGE = (1,2)
# --- END CONFIGURATION ---

def get_chrome_major_version() -> int:
    try:
        out = subprocess.check_output(['/usr/bin/google-chrome', '--version']).decode().strip()
        major = int(out.split()[-1].split('.')[0])
        print(f"Chrome major version: {major}")
        return major
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error checking Chrome version: {e}")
        print("Ensure Google Chrome is installed and in your PATH.")
        raise

def create_driver(ua: UserAgent, chrome_major: int) -> uc.Chrome:
    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(f"--user-agent={ua.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.binary_location = "/usr/bin/google-chrome"

    driver = uc.Chrome(
        options=options,
        version_main=chrome_major,
        use_subprocess=True,
    )
    return driver

def visit_url(driver: uc.Chrome, iteration: int) -> None:
    print(f"  → Loading page...")
    driver.get(URL)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    print(f"  → Title: {driver.title}")
    print(f"  ✓ Iteration {iteration} done.")

def main():
    chrome_major = get_chrome_major_version()
    ua = UserAgent()
    print(f"\nStarting {MAX_ITERATIONS} iterations on:\n{URL}\n")

    for i in range(1, MAX_ITERATIONS + 1):
        driver = None
        try:
            print(f"[{i}/{MAX_ITERATIONS}] Opening browser...")
            driver = create_driver(ua, chrome_major)
            visit_url(driver, i)
        except Exception as e:
            print(f"  ✗ Iteration {i} failed: {e}")
        finally:
            if driver:
                driver.quit()
                print(f"  → Browser closed.")

        if i < MAX_ITERATIONS:
            delay = random.uniform(*DELAY_RANGE)
            print(f"  → Waiting {delay:.1f}s...\n")
            time.sleep(delay)

    print("\nAll iterations complete.")

if __name__ == "__main__":
    main()




# ============================================================
# ⚠️  REMINDER — AFTER RUNNING
# ============================================================
#
# 1. REFLECT ON YOUR USE
#    If you used this script on a site you do not own,
#    stop immediately and review the platform's ToS.
#
# 2. DO NOT MODIFY FOR MISUSE
#    Do not add user-agent rotation, multiple iterations,
#    or bot-detection evasion to this script. Doing so
#    crosses the line from education into abuse.
#
# 3. ETHICAL RESPONSIBILITY
#    As a developer, you are responsible for how your
#    code is used. Build tools that help, not harm.
#
# 4. REPORT MISUSE
#    If you see this script being misused, report it
#    to the platform being targeted.
#
# 4. LEGAL DISCLAIMER
#    The author of this script accepts no responsibility
#    for any legal action, account bans, or consequences
#    arising from misuse of this code. Use at your own risk.
