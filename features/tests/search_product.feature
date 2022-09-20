# Created by shaha at 9/19/2022
Feature: Search functionality test cases


  Scenario: Presence of UI elements of search functionality
    Given Open Gittop page
    When Hover over a search icon
    Then user can sees all UI elements related to search


  Scenario: User can search for product from search input field
   Given Open Gittop page
    When Hover over a search icon
    When Enter TABLET in search input field
    Then User can see TABLET search result


   Scenario: An error message appear for an irrelevant product search
     Given Open Gittop page
     When Hover over a search icon
     When  Enter coffee in search input field
     Then User can see an error message for irrelevant search
