# 📱 Appium Python Automation Framework (Android)

A **production-grade Appium automation framework** built using **Python + PyTest**, designed for **real devices and emulators**, with support for **parallel execution across devices**, **Page Object Model (POM)**, **logging**, **screenshots**, and **HTML reports**.

This framework is optimized for:
- Local execution
- Emulator + Real device parallel runs
- Maintainability and scalability

This framework is designed to be robust, readable, while remaining easy to run locally.

---

## 🚀 Key Features

- ✅ Android **Emulator & Real Device** support
- ✅ **Parallel execution across devices**
- ✅ **Same APK tested simultaneously**
- ✅ **Page Object Model (POM)**
- ✅ Retry failed tests
- ✅ Screenshot on failure
- ✅ Centralized logging
- ✅ HTML test reports
- ✅ YAML-based configuration
- ✅ Thread-safe driver creation

---

## 📂 Project Structure
````
appium_python_framework/
│
├── src/
│ ├── config/
│ │ └── config.yaml
│ │
│ ├── drivers/
│ │ └── driver_factory.py
│ │
│ ├── pages/
│ │ ├── base_page.py
│ │ ├── onboarding_page.py
│ │ ├── home_page.py
│ │ └── search_page.py
│ │
│ ├── tests/
│ │ ├── base_test.py
│ │ ├── test_smoke.py
│ │ ├── test_search.py
│ │ └── test_search_data.py
│ │
│ ├── utils/
│ │ ├── logger.py
│ │ ├── wait_utils.py
│ │ └── screenshot_utils.py
│ │
│ └── conftest.py
│
├── reports/
│ └── *.html
│
├── run_parallel.sh
├── requirements.txt
├── pytest.ini
└── README.md
````

## ⚙️ Tech Stack

- Python 3.12+
- Appium 2.x
- Appium-Python-Client (3.x – stable)
- PyTest
- pytest-xdist (parallel execution)
- pytest-html
- YAML-based configuration
- Android Emulator + Real Device

## 📦 Prerequisites

#### 1️⃣ System Requirements

- macOS / Linux
- Java 17+
- Android SDK installed
- Appium Server (2.x)
- Verify:
- adb devices


You should see something like:

- TSSOM7NJEU4XFURW    device
- emulator-5554      device

####  2️⃣ Python Virtual Environment

````
python -m venv .venv
source .venv/bin/activate
````

#### 3️⃣ Install Dependencies
````
pip install -r requirements.txt
````

#### ⚙️ Configuration (config.yaml)

````
platformName: "Android"
automationName: "UiAutomator2"

deviceType: "emulator"   # emulator | real

realDeviceUdid: "TSSOM7NJEU4XFURW"
emulatorUdid: "emulator-5554"

appPackage: "org.wikipedia"
appActivity: "org.wikipedia.main.MainActivity"
appWaitActivity: "org.wikipedia.*"

appPath: "src/app/wikipedia.apk"

appiumServerUrl: "http://127.0.0.1:4723"

noReset: false
fullReset: true
implicitWait: 10
timeout: 120
````

####🚀 Running Tests

▶️ Start Appium Server
````
appium
````
▶️ Run All Tests (Single Device)
````
python -m pytest -vv
````

To target a specific device:
````
python -m pytest --device=real
python -m pytest --device=emulator
````
#### 🔁 Retry Failed Tests

Supported via pytest-rerunfailures.
````
pytest --reruns 2
pytest --reruns 2 --reruns-delay 5
````
#### 📊 Reports & Screenshots

- HTML reports generated in /reports
- Screenshot captured automatically on failure
- Logs written via centralized logger

Example:
````
reports/
├── emulator_report.html
├── real_device_report.html
````
⚡ Parallel Execution (Emulator + Real Device)

⚠️ Parallel execution is supported across devices, not within a single device.

#### Why?

- Android allows only one foreground app per device

- Appium supports one session per device

- True parallelism = parallel devices

#### ▶️ Run Parallel Tests (Recommended)
````
chmod +x run_parallel.sh
./run_parallel.sh
````

**What this does:**

- Starts tests on emulator
- Starts tests on real device
- Same APK

Same test suite

- Two independent Appium sessions
- Two separate HTML reports

#### 🧠 Key Design Decisions

✅ Thread-safe driver creation

- Driver is function-scoped
- One driver per test
- Safe for parallel execution

✅ Page Object Model (POM)

- Clean separation of concerns
- Reusable page actions
- Maintainable locators

✅ Graceful onboarding handling

- Optional onboarding skipped safely
- No test failures if onboarding is absent

✅ Robust logging

- No print() statements
- Structured logs with timestamps

CI-friendly output

🧪 Example Test
````
class TestSearch(BaseTest):

    def test_search(self, driver):
        self.onboarding.skip_onboarding()
        self.home.click_search()
        self.search.search("India")
        assert "India" in self.search.get_first_result()
````
### 🏁 Best Practices Followed
````
✔ No hard-coded waits
✔ Explicit waits via utilities
✔ Clean driver lifecycle
✔ Device-aware execution
✔ Scalable for CI/CD
✔ Same APK across environments
````
#### 📌 Important Notes

- ❌ Parallel tests cannot run on a single device

- ✅ Parallel tests can run on emulator + real device

- Appium server must be running before execution

- Framework supports future CI/CD integration

#### 🔮 Next Enhancements (Optional)

- Auto-start Appium server
- Auto-detect connected devices
- Dynamic test splitting
- CI/CD via GitHub Actions
- Allure reporting
- Cloud device integration (BrowserStack / Sauce Labs)

#### 👤 Author

### Kunal Sharma