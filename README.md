# 👁️ GitHub Profile View Simulator

> **A browser automation tool for simulating page visits using rotating user agents.**  
> Built with Python, Selenium, and `undetected-chromedriver`.

---

## ⚠️ Legal Disclaimer & Terms of Use

> **READ CAREFULLY BEFORE USING THIS SOFTWARE.**

This software is published strictly for **educational and research purposes**, including but not limited to:

- Understanding browser automation techniques
- Learning about user-agent rotation and anti-bot fingerprinting
- Studying headless browser behavior and web scraping fundamentals
- Academic research on web traffic simulation

### 🚫 What This Tool Must NOT Be Used For

By downloading, cloning, forking, or running this software, you explicitly agree **not** to use it for:

| Prohibited Use | Reason |
|---|---|
| Inflating view/traffic counters on GitHub or any platform | Violates platform Terms of Service |
| Manipulating analytics, metrics, or engagement statistics | May constitute fraud |
| Circumventing rate limits or access controls of third-party services | Potentially illegal under CFAA / similar laws |
| Automating access to services in a manner that degrades performance | Constitutes a denial-of-service-adjacent abuse |
| Any commercial deception or misleading representations | Unethical and potentially illegal |

### ⚖️ Platform Terms of Service

This tool, **if misused**, may violate the Terms of Service of platforms including but not limited to:

- **GitHub** — [Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies): prohibits automated abuse, disruption of services, and artificial manipulation of metrics.
- **Any web service** — Most platforms explicitly prohibit automated bots that simulate human behavior without authorization.

**The author takes NO responsibility for account suspensions, bans, legal action, or any other consequences resulting from misuse of this software.**

---

## 📜 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 [Your Name / GitHub Handle]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

> **In plain language:** You are free to use, copy, modify, and distribute this code for any purpose — including commercially — as long as you keep the copyright notice. The author provides no warranty and accepts no liability for how the software is used.

---

## 🔍 What This Script Does

This script automates a headless Chromium browser to visit a specified URL a configurable number of times, with:

- **Randomized user-agent strings** — each visit mimics a different browser/device fingerprint
- **Randomized delays** — human-like pauses between visits to avoid detection
- **Undetected ChromeDriver** — bypasses basic bot-detection mechanisms
- **Auto-detection of local Chrome version** — no manual version matching needed
- **Per-iteration browser instances** — each visit opens and closes a fresh browser session

### Architecture Overview

```
main()
 ├── get_chrome_major_version()   # Detects installed Chrome version
 └── loop (MAX_ITERATIONS)
      ├── create_driver()          # Spins up headless Chrome with random UA
      ├── visit_url()              # Loads the target URL, waits for <body>
      └── driver.quit()            # Closes browser cleanly
```

---

## 🛠️ Requirements

| Dependency | Purpose |
|---|---|
| Python 3.8+ | Runtime |
| `undetected-chromedriver` | Headless Chrome with anti-detection |
| `fake-useragent` | Randomized browser fingerprints |
| `selenium` | WebDriver interface |
| Google Chrome (installed) | Browser engine |
| ChromeDriver (matching version) | WebDriver binary |

### Install dependencies

```bash
pip install undetected-chromedriver fake-useragent selenium
```

---

## ⚙️ Configuration

Edit the `--- CONFIGURATION ---` block at the top of the script:

```python
URL            = "https://example.com"   # Target URL
MAX_ITERATIONS = 5                        # Number of visits
DELAY_RANGE    = (3, 7)                   # Seconds between visits (random range)
```

---

## ▶️ Usage

```bash
python viewer.py
```

**Example output:**

```
Chrome major version: 124

Starting 5 iterations on:
https://example.com

[1/5] Opening browser...
  → Loading page...
  → Title: Example Domain
  ✓ Iteration 1 done.
  → Browser closed.
  → Waiting 4.3s...

...

All iterations complete.
```

---

## 🧪 Intended Use Cases

✅ **Legitimate uses this tool is designed for:**

- Testing your own website's server behavior under repeated automated visits
- Practicing Selenium and headless browser automation in a local/dev environment
- Learning how user-agent rotation works
- Academic coursework on web scraping or automation

❌ **This tool is NOT designed or endorsed for:**

- Gaming any platform's view/analytics counters
- Creating artificial social proof or engagement
- Any use that violates a third party's Terms of Service

---

## 🤝 Contributing

Pull requests are welcome for improvements to the automation logic, documentation, or test coverage. Please ensure all contributions maintain the educational focus of this project.

---

## 📬 Contact

For questions about legitimate use cases, open an [issue](../../issues) or reach out via GitHub.

---

*This README was written to ensure full transparency about what this tool does and the legal boundaries of its use. If you are unsure whether your use case is permitted, consult the Terms of Service of the platform you are targeting and, if necessary, seek legal advice.*
