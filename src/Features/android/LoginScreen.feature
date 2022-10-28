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