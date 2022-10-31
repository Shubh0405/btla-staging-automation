Feature: Login Screen

  Scenario: Verify that after launching the app, login screen should open in Portrait mode.
    Given The minimum Android OS version supporting BTLA OS 5 and above
    When Launch the app
    Then Verify that after launching the app, login screen should open in Portrait mode.

  Scenario: Verify the elements in Login screen
    Given The minimum Android OS version supporting BTLA OS 5 and above
    And Launch the app online
    When Navigate to the Login screen
    Then Verify the Login screen icon
    And Verify the "Enter Mobile Number" text
    And Verify the Mobile Number field with auto-filled country code
    And Verify the Send OTP button
    And Verify the 'Privacy Policy and T&C' link

  Scenario Outline: Verify that User should be able to select the Country Code and respective Country name from the bottom sheet
    Examples:
      |CountryCode|
      |+93|
      |+244|
      |+213|

    Given The minimum Android OS version supporting BTLA OS 5 and above
    And Launch the app online
    And Navigate to the Login screen
    When User taps on Country Code menu
    And select any from the bottom sheet <CountryCode>
    Then Verify selected <CountryCode> should be shown in country code field

  Scenario: Verify that tapping on the Cancel button in the country code bottom sheet dialog, the bottom sheet should dismiss from the screen
    Given The minimum Android OS version supporting BTLA OS 5 and above
    And Launch the app online
    And Navigate to the Login screen
    When User taps on Country Code menu
    And User is in Country code bottom sheet dialog screen
    And user taps on Cancel button
    Then Verify that tapping on the Cancel button in the country code bottom sheet dialog, the bottom sheet should  dismiss from the screen i.e tapping outside the bottom sheet.

  Scenario Outline: Verify that when users enter mobile number below 7 digits in Mobile Number field should show a error message 'Please enter valid mobile number'
    Examples:
    |Digits|
    |123456|

    Given The minimum Android OS version supporting BTLA OS 5 and above
    And Launch the app online
    And Navigate to the Login screen
    When Enters less than 7 digit Mobile Number <Digits>
    Then Verify error message "Please enter valid mobile number" is displayed below mobile number field

  Scenario Outline: Verify that when user enter mobile number above 15 digits for all Countries including India, mobile Number field should be validated with error message 'Please enter valid mobile number'
    Examples:
    |Digits|
    |1234567891234567|

    Given The minimum Android OS version supporting BTLA OS 5 and above
    And Launch the app online
    And Navigate to the Login screen
    When Enter <Digits> above 15 in Mobile Number field with any
    Then Verify error message "Please enter valid mobile number" is displayed below mobile number field

  Scenario: Verify that tapping on Send OTP button after entering the valid Mobile number should navigate the user to OTP verification Screen
    Given The minimum Android OS version supporting BTLA OS 5 and above
    And Launch the app online
    And Navigate to the Login screen
    When User enter a valid mobile number
    And User taps on Send OTP
    Then Verify that user is navigated to OTP Verification screen

  Scenario: Verify that tapping on Privacy policy link in the login screen should navigate the user to the Privacy Policy screen
    Given The minimum Android OS version supporting BTLA OS 5 and above
    And Launch the app online
    And Navigate to the Login screen
    When User tap on the 'Privacy Policy' link
    Then Verify that tapping on Privacy policy link in the login screen should navigate the user to the Privacy Policy screen

    Scenario: Verify that tapping on App back button in Privacy policy screen should redirect back the user to login screen
      Given The minimum Android OS version supporting BTLA OS 5 and above
      And Launch the app online
      And User is in Login screen
      When User tap on the 'Privacy Policy' link
      And Verify the Privacy policy screen
      And User taps on the app back arrow
      Then Verify that user should be redirected back to the Login screen

    Scenario: Verify that tapping on T&C link in the login screen should navigate the user to the Terms & Conditions screen.
      Given The minimum Android OS version supporting BTLA OS 5 and above
      And Launch the app online
      And User is in Login screen
      When User tap on the 'T & C' link
      Then Verify that User should navigate to the Terms & Conditions screen
