import os
from webdriver_manager.chrome import ChromeDriverManager


def pytest_configure(config):
    driver_path = ChromeDriverManager().install()
    driver_dir = os.path.dirname(driver_path)
    os.environ["PATH"] = driver_dir + os.pathsep + os.environ.get("PATH", "")
