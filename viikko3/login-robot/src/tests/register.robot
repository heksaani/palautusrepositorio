*** Settings ***
Resource  resource.robot
#when the new input is given the app is starting to create registration
Test Setup  Input New Command And Register
 
*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kallensalasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  matti  matinsalasana123
    Output Should Contain  User with username matti already exists


Register With Too Short Username And Valid Password
    Input Credentials  ma  matinsalasana123
    Output Should Contain  Username must be at least 3 characters long 

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  123  matinsalasana123
    Output Should Contain  Username must only contain letters

Register With Valid Username And Too Short Password
    Input Credentials  matti  matin
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  matti  matinsalasana
    Output Should Contain  Password cannot only contain letters
*** Keywords ***
Input New Command And Register
    Create User  matti  matinsalasana123
    Input New Command
# User story --> A new user account can be created if a proper unused username and a proper password are given 
