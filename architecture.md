# 🏗️ Architecture — GitHub Profile View Simulator

> ⚠️ **Educational reference only.** See [README.md](./README.md) for full
> legal disclaimer before implementing or adapting anything in this document.

---

## High-Level Flow

```
┌─────────────────────────────────────────────────────────┐
│                        main()                           │
│                                                         │
│  1. Detect Chrome version                               │
│  2. Initialize UserAgent generator                      │
│  3. Loop MAX_ITERATIONS times                           │
│     ├── Create fresh browser instance                   │
│     ├── Visit target URL                                │
│     ├── Close browser                                   │
│     └── Wait random delay                               │
└─────────────────────────────────────────────────────────┘
```

---

## Component Breakdown

```
GitHub-Profile-View-Simulator/
│
├── viewer.py                  ← Main script (not published)
│   │
│   ├── get_chrome_major_version()
│   │     └── Calls system: google-chrome --version
│   │         Parses → returns integer (e.g. 124)
│   │
│   ├── create_driver()
│   │     ├── Input:  UserAgent string, Chrome major version
│   │     ├── Config: headless, no-sandbox, disable-gpu,
│   │     │           window-size, user-agent, no-automation-flag
│   │     └── Output: uc.Chrome driver instance
│   │
│   ├── visit_url()
│   │     ├── Input:  driver instance, iteration number
│   │     ├── Action: driver.get(URL)
│   │     │           WebDriverWait → body present (20s timeout)
│   │     └── Output: logs title + success/failure
│   │
│   └── main()
│         ├── Orchestrates the full loop
│         ├── Handles exceptions per iteration
│         └── Ensures driver.quit() in finally block
│
├── requirements.txt           ← Python dependencies
├── .gitignore                 ← Excludes caches, env, binaries
├── LICENSE                    ← Apache 2.0
├── README.md                  ← Full disclaimer + documentation
├── pseudocode.md              ← Logic in plain English (this repo)
└── architecture.md            ← This file
```

---

## Dependency Graph

```
viewer.py
  │
  ├── undetected-chromedriver   (uc)
  │     └── patches ChromeDriver to bypass automation detection
  │
  ├── selenium
  │     ├── webdriver           → controls Chrome
  │     ├── By                  → element locator strategy
  │     ├── WebDriverWait       → explicit wait conditions
  │     └── expected_conditions → wait until body is present
  │
  ├── fake-useragent            (UserAgent)
  │     └── generates random browser UA strings per iteration
  │
  └── stdlib
        ├── subprocess          → reads Chrome version from shell
        ├── time                → sleep between iterations
        └── random              → randomizes delay duration
```

---

## Execution Timeline (Single Iteration)

```
 main() starts
     │
     ▼
 get_chrome_major_version()
     │  shell: google-chrome --version
     │  parse: "Google Chrome 124.0.0.0" → 124
     ▼
 UserAgent() initialized
     │
     ▼
 ┌── ITERATION i ──────────────────────────────────┐
 │                                                  │
 │  create_driver()                                 │
 │    └── uc.Chrome(options, version=124)           │
 │          └── headless Chrome process starts      │
 │                                                  │
 │  visit_url()                                     │
 │    ├── driver.get(URL)        ← page request     │
 │    ├── WebDriverWait(20s)     ← wait for body    │
 │    └── log title + result                        │
 │                                                  │
 │  driver.quit()                ← always runs      │
 │    └── Chrome process killed                     │
 │                                                  │
 │  time.sleep(random 3–7s)      ← rate limit       │
 └──────────────────────────────────────────────────┘
     │
     ▼
 next iteration OR done
```

---

## Why Each Library Was Chosen

| Library | Why Not a Simpler Alternative |
|---|---|
| `undetected-chromedriver` | Regular Selenium is trivially detected by sites via `navigator.webdriver` flag |
| `fake-useragent` | Hardcoded UA strings are easy to fingerprint and blocklist |
| `WebDriverWait` | `time.sleep()` is unreliable — explicit waits respond to actual page state |
| Per-iteration driver | Reusing one driver leaks session cookies/state across visits |

---

> ⚠️ **Note:** The actual `viewer.py` script is intentionally not included
> in this repository. This architecture document exists to explain the design
> for educational purposes. Implementing this against services you do not own
> may violate their Terms of Service and applicable law.
