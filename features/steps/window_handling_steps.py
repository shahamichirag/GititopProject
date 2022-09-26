from behave import given, when, then


@then('Verify facebook is opened')
def facebook_page_opened(context):
    context.app.new_window_page.facebook_page_opened()


@then('User can closed the window')
def close_window(context):
    context.app.new_window_page.close_window()