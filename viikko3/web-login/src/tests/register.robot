*** Settings ***
Library  SeleniumLibrary
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  heksaani
    Set Password  salasana123
    Set Password Confirmation  salasana123
#Register With Too Short Username And Valid Password
# ...

#Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
# ...

#Register With Nonmatching Password And Password Confirmation
# ...

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}