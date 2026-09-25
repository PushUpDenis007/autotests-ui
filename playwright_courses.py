from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Переходим на страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill("username")

    # Заполняем поле пароль
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

    # Нажимаем на кнопку Login
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()
    context.storage_state(path="browser-state.json")

    dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard).to_be_visible()

    new_context = browser.new_context(storage_state="browser-state.json")
    new_page = new_context.new_page()
    new_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = new_page.get_by_test_id('courses-list-toolbar-title-text') 
    expect(courses_title).to_have_text("Courses")

    no_results_block = new_page.get_by_test_id('courses-list-empty-view-title-text') 
    expect(no_results_block).to_have_text("There is no results")

    empty_icon = new_page.get_by_test_id('courses-list-empty-view-icon') 
    expect(empty_icon).to_be_visible()

    description_block = new_page.get_by_test_id('courses-list-empty-view-description-text') 
    expect(description_block).to_have_text("Results from the load test pipeline will be displayed here")

