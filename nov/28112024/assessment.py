import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# URL of the Table Search Demo page
URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"


def setup_browser():
    """Initialize the WebDriver and navigate to the page."""
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    return driver


@pytest.fixture
def driver():
    """Pytest fixture to set up and tear down the WebDriver."""
    driver = setup_browser()
    yield driver
    driver.quit()


def test_search_functionality(driver):
    """Test to validate the search functionality for 'New York' entries."""
    search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys("New York")
    time.sleep(2)  # Allow time for filtering

    # Get the filtered row count
    rows = driver.find_elements(By.XPATH, "//table[@id='example']//tbody/tr")
    visible_rows = [row for row in rows if row.is_displayed()]

    # Assertion to check that 5 entries are displayed
    assert len(visible_rows) == 5, f"Expected 5 results, but got {len(visible_rows)}"

    # Validate that each row contains 'New York'
    for row in visible_rows:
        assert "New York" in row.text, f"Row does not contain 'New York': {row.text}"

    print("Test Passed: Search functionality works as expected!")