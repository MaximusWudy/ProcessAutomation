import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class") # class level fixture
def setup(request): # when you define a fixture you'll have a request as an instance
    global driver # use the global variable 'driver', without creating new local object
    browser_name = request.config.getoption("--browser_name") # retrieve the value from request object from runtime
    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe')

    elif browser_name != 'chrome':
        # firefox invocation: in cmd, run 'py.test --browser_name firefox
        raise "currently only chrome driver is supported, pls change to chrome instead"

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver # 'driver' instance will be sent to class object 'driver' in test_e2e.py, which invoked this setup()
    yield
    driver.close()

'''
Whenever a test fails, the html report will save a screenshot of the website
the below code is to modify the html-report code which is out of the course scope
'''
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)