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
    print("Metadata inside pytest_configure")
    config.addinivalue_line("markers", "integration: mark test as integration test")
    config.option.metadata = {
        'Project Name': 'nop Commerce',
        'Module Name': 'Customers',
        'Tester': 'Kushal Kadam'
    }
    print(config.option.metadata)


###It is a hook for delete/modify Environment info to html report
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    print("Metadata inside pytest_metadata")
    print(metadata)





# ########
# from selenium import webdriver
# import pytest
#
# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         print("Launching Chrome browser.....")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#         print("Launching Firefox browser.....")
#     else:
#         driver = webdriver.Ie()
#         return driver
#
# def pytest_addopton(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
