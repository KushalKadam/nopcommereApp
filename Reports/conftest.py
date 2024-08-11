# Tomorrow even if we add new test cases, in those test cases, wee are creating driver in every test methd
# So instead of rier creation multiple times I have just created conftest.py


from selenium import webdriver
import pytest


@pytest.fixture()  # instead of creating
def setup():
    driver = webdriver.Chrome()
    return driver


##It is a hook for adding environment
def pytest_configure(config):
    print("Kushal")
    config._metadata = {'Project Name': 'nop Commerce', 'Module Name': 'Customers', 'Tester': 'Kushal Kadam'}



###It is a hook for delete/modify Environment info to html report
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
