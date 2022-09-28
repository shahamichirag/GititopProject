from behave import given, when, then


@given('Open Gittop page')
def open_gittop_page(context):
    context.app.header.open_gittop_page()


@when('Hover over a search icon')
def hover_search_icon_in_header(context):
    context.app.header.hover_search_icon_in_header()


@when('Enter {product} in search input field')
def enter_product_search_field(context, product):
    context.app.header.enter_product_search_field(product)


@when('click on laptop category')
def click_laptop_category(context):
    context.app.header.click_laptop_category()


@then('user can click on category links on the header and see relevant result')
def click_category_link(context):
    context.app.header.click_category_link()


@then('user can sees all UI elements related to search')
def verify_search_ui_elements(context):
    context.app.header.verify_search_ui_elements()


