Feature: Product preview images test cases


Scenario:user can see product images using image slider in mobile mode
    Given Open Gittop page
    When click on hamburger menu
    When click on laptop category from the hamburger menu
    When Click on the first product of laptop category of hamburger menu
    Then user can see through product images using image slider in mobile mode


Scenario: user can see thumbnail images in product page from mobile
    Given Open Gittop page
    When  click on hamburger menu
    When click on laptop category from the hamburger menu
    When Click on the first product of laptop category of hamburger menu
    Then user can see thumbnail images by clicking on it from mobile preview
