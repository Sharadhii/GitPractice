import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chrome_driver_path = "C:/Users/sharadhi/PycharmProjects/pythonProject/chromedriver.exe"
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        # Assuming you have the geckodriver executable in your path
        driver = webdriver.Firefox()

    elif browser_name == "IE":
        # Assuming you have the IEDriverServer executable in your path
        driver = webdriver.Ie()

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get("https://routesgroup.com/")
    driver.maximize_window()

    # Store the driver instance in the request.cls for access in the test class
    request.cls.driver = driver

    yield driver

    # Teardown: Close the browser after the tests
    driver.quit()
