***Settings ***
Library    SeleniumLibrary

***Variables ***
${URL}  http://mygoldendev.arlo.com
${BROWSER}  chrome
${Acct}  arlodevregister+1710987637835hbxi+us@gmail.com
${PWD}  Netgear1
${Home_Login}  xpath=/html/body/ui-view/ng-component/div/div/div/div[2]/button
${Acct_Login}  xpath=//*[@id="loginForm"]/div[3]/button
${Forgot_PW}   xpath=/html/body/ui-view/app-login/div/div/div/div[2]/a
${Forgot_Submit}   xpath=/html/body/ui-view/app-forgot-password/div/div/div/form/div/button
${Create Acct}   xpath=/html/body/ui-view/ng-component/div/div/div/div[3]/button

*** Keywords ***
Open and maximize Browser
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window

Input login info
    Input Text  xpath=//*[@id="loginEmail"]  ${Acct}
    Input Text  xpath=//*[@id="loginPassword"]  ${PWD}
    Click Button  ${Acct_Login}

Open Browser, maximize and go to "Forgot Password" page
    Open Browser   ${URL}  ${BROWSER}
    Maximize Browser Window
    Click Button   ${Home_Login}
    Click Link     ${Forgot_PW}
    Sleep    2s
In "Forgot page", input email to get reset password link
    Input Text     id=email  ${Acct}
    Sleep    2s
    Click Button   ${Forgot_Submit}
    Sleep    5s
    #Close Browser

