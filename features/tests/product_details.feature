# Created by shaha at 9/20/2022
Feature: Product preview images test cases


  Scenario:user can shuffle through product images using image slider
    Given Open Gittop page
    When click on laptop category
    When Click on the first product of laptop category
    Then user can shuffle through product images using image slider

  Scenario: user can see thumbnail images in product page
    Given Open Gittop page
    When click on laptop category
    When Click on the first product of laptop category
    Then user can see thumbnail images by clicking on it

  Scenario: user can share product details via facebook, twitter, pintrest, email, tumblr
    Given Open Gittop page
    When click on laptop category
    When Click on the first product of laptop category
    When Store original window
    When click on facebook link
    And Switch to the newly opened window
    Then Verify facebook is opened
    And User can closed the window
    And User can come back to original window
