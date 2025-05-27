***Settings ***
Library    SeleniumLibrary
Resource  ../../Resources/Arlo_Resource.robot

***Variables ***

***Test Cases ***
Login goldendev
    [Documentation]  Arlo Test
    [Tags]  regression

    Open and maximize Browser
    Click Button  ${Home_Login}
    Wait Until Element Is Visible  ${Acct_Login}
    Input login info
    Sleep    5s

After login
    [Documentation]  Arlo Test
    [Tags]  regression
    Wait Until Element Is Visible    id=automation_action_nav_feed
    Click Element  id=automation_action_nav_feed
    Sleep    5s
    Execute JavaScript
    ...  var evt = new MouseEvent("click", {bubbles:true});
    ...  document.elementFromPoint(500, 100).dispatchEvent(evt);
    Sleep    3s

    Wait Until Element Is Visible    id=automation_action_nav_emergency_response
    Click Element  id=automation_action_nav_emergency_response
    Sleep    5s

    Wait Until Element Is Visible    id=automation_action_nav_cameras_new
    Click Element  id=automation_action_nav_cameras_new
    Sleep    5s
    Execute JavaScript
    ...  var evt = new MouseEvent("click", {bubbles:true});
    ...  document.elementFromPoint(500, 100).dispatchEvent(evt);

    Wait Until Element Is Visible    id=automation_action_nav_routines.modes
    Click Element  id=automation_action_nav_routines.modes
    Sleep    5s
    Execute JavaScript
    ...  var evt = new MouseEvent("click", {bubbles:true});
    ...  document.elementFromPoint(500, 100).dispatchEvent(evt);

    Wait Until Element Is Visible    id=automation_action_nav_settings
    Click Element  id=automation_action_nav_settings
    Sleep    5s
    Execute JavaScript
    ...  var evt = new MouseEvent("click", {bubbles:true});
    ...  document.elementFromPoint(500, 100).dispatchEvent(evt);

    Wait Until Element Is Visible    id=automation_action_nav_dashboard
    Click Element  id=automation_action_nav_dashboard
    Sleep    5s

***Keywords ***




