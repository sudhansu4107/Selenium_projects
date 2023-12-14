import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

driver = None
service_obj = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option:Chrome,firefox,edge"
    )


@pytest.fixture(scope='class')
def Browser(request):
    print('Browser opened.')
    # option = Options()
    # option.add_argument('--headless')
    # option.add_argument('--disable-gpu')
    Browsername = request.config.getoption('browser')
    global driver
    global service_obj
    print(Browsername)
    if Browsername == 'edge':
        print('enter into edge browser')
        service_obj = Service('G:\\Selenium\\Webdrivers\\msedgedriver.exe')
        driver = webdriver.Edge(service=service_obj)
    elif Browsername == 'firefox':
        print('enter into firefox browser')
        service_obj = Service('../Webdrivers/geckodriver.exe')
        driver = webdriver.Firefox(service=service_obj)
    else:
        print('enter into chrome browser')
        service_obj = Service('../Webdrivers/chromedriver.exe')
        driver = webdriver.Chrome(service=service_obj)

    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    print(driver.title)
    request.cls.driver = driver
    yield
    driver.close()

    print('Browser closed.')


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
    Filepath = r'G:\\Selenium\\Reports\\Screenshots'
    driver.get_screenshot_as_file(Filepath + "/" + name)
