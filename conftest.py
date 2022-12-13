import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def br_set():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1020

