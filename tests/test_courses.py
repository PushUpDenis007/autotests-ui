from playwright.sync_api import expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text') 
    expect(courses_title).to_have_text("Courses")

    no_results_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text') 
    expect(no_results_block).to_have_text("There is no results")

    empty_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon') 
    expect(empty_icon).to_be_visible()

    description_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text') 
    expect(description_block).to_have_text("Results from the load test pipeline will be displayed here")