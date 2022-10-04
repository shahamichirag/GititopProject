from behave import given, when, then

@when('click on hamburger menu')
def click_hamburger_menu(context):
    context.app.mobile_header.click_hamburger_menu()

@when('click on laptop category from the hamburger menu')
def click_laptop(context):
    context.app.mobile_header.click_laptop()


@when('Click on the first product of laptop category of hamburger menu')
def click_laptop_item(context):
    context.app.mobile_header.click_laptop_items()


@then('user can see through product images using image slider in mobile mode')
def laptop_items_slider(context):
    context.app.mobile_header.laptop_items_slider()


@then('user can see thumbnail images by clicking on it from mobile preview')
def user_can_see_thumbnail_image_from_mobile(context):
    context.app.mobile_header.user_can_see_thumbnail_image_from_mobile()