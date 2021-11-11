# Testing 

The following sections are the results of the testing throughout the software development lifecycle for MSP-4. This information has been included in a separate document in order to keep the README document uncluttered.


## Testing Plan

Testing will be conducted regularly alongside development of this project. Each User Story will include Unit testing of the code being developed and a manual exploratory test session.

During the manual exploratory test sessions:
- test cases will be identified for test automation
- site functionality will be verified
- cross browser/device compatibiliy will be confirmed
- general usibility will be assessed

Test automation will be conducted at regular intervals and with the implementation of major functionality.

Upon initial deployment the following testing will be conducted: 
- All unit tests
- The automation suite
- Manual shakedown of all functionality
- Performance testing of site loading
- Device and cross browser compatibility
- WAVE web accessibility tests
- WAI color contrast assessments (of the final colours and patterns)

## Testing Plan

The following list of tools have been utilised during the testing of this project:
- [screen to gif](https://www.screentogif.com/)
  - Used for Evidence collection
  
- [unittest - Django built in unit test application](https://docs.djangoproject.com/en/3.2/topics/testing/overview/)
  - Used for python unit testing
  
- [placeholder]()
  - Used for Functional automation testing

- [placeholder]()
  - Used for Functional automation testing

- [placeholder]()
  - Used for Functional automation testing


## Sprint 1 - 26th September - 3rd October 2021

### User Stories Closed
- As a Developer I want to see the generic base app created in Django
- As a Developer I want to see the generic base templates in place
- As a User I want to be able to view practise exam details before starting

### Unit Tests conducted
<p float="left">
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/unit_tests/01.10.21_1.png" width="300" height="200" />
</p>

### Exploratory Test Session Goals
- I want to confirm that the base templates load as expected
- I want to confirm the exam list basic page load with modal
- I want to confirm that all User Stories are done to my satisfaction
- I want to identify any edge cases
- I want to identify any potential test cases for automation


## Sprint 2 - 4th October - 10th October 2021

### User Stories Closed
- As a Developer I will need the following Exam App Database scheme in place
- As a User I want to clearly understand the sites landing/home
- BUG: 500 Error appearing in relation to all DB interactions
- As a User I want to access the "Badges" page within the Resource Section of the site
- As a User I want to be able to access the Resources main page
- As a User I want to access the "IDE" Page of the Resource Section of the site
- As a User I want to access the "Frameworks" page of the Resource section of the site

### Unit Tests conducted
<p float="left">
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/unit_tests/10.10.21_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/unit_tests/10.10.21_2.png" width="300" height="200" />
</p>

### Exploratory Test Session Goals
- I want to confirm that exams can be added/amended/delete via the Django admin portal
- I want to confirm that questions can be added/amended/delete via the Django admin portal
- I want to confirm that answers can be added/amended/delete via the Django admin portal
- I want to confirm that the frameworks subpage of the resources section loads and contains required data
- I want to confirm that the IDE subpage of the resources section loads and contains required data
- I want to confirm that the Badges subpage of the resources section loads and contains required data
- I want to confirm that all text is clearly visible for the user
- I want to confirm that all User Stories are done to my satisfaction
- I want to identify any edge cases
- I want to identify any potential test cases for automation


## Sprint 3 - 11th October - 17th October 2021

### User Stories Closed
- As a User I want to access the "Learnings" page within the Resource Section of the site

### Unit Tests conducted
<p float="left">
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/unit_tests/16.10.21_1.png" width="300" height="200" />
</p>

### Exploratory Test Session Goals
- I want to confirm that the Learnings subpage of the resources section loads and contains required data
- I want to confirm that all text is clearly visible for the user
- I want to confirm that all User Stories are done to my satisfaction
- I want to identify any edge cases
- I want to identify any potential test cases for automation


## Sprint 4 - 18th October - 24th October 2021

### User Stories Closed
- As a User I want to be able to move between resource sub pages directly
- As a Developer I will need the following Providers Database scheme in place
- BUG: Second Instance - 500 error appearing in relation to all DB interactions
- As a User I want to access the "Media" page within the Resource Section of the site
- As a User I want to access the "Tools" page within the Resource Section of the site
- As an Admin User I want to be able to Add a provider to the site
- As a User I want to view a list of Certification Providers

### Unit Tests conducted
<p float="left">
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/unit_tests/21.10.21_1.png" width="600" height="400" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/unit_tests/21.10.21_2.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/unit_tests/23.10.21_1.png" width="300" height="200" />
</p>

### Exploratory Test Session Goals
- I want to confirm that a user can navigate between the resources subpages
- I want to confirm that a provider can be added to the site via a specific page
- I want to confirm that the Media subpage of the resources section loads and contains required data
- I want to confirm that the Tools subpage of the resources section loads and contains required data
- I want to confirm that a User can view a list of the existing Providers listed on the site
- I want to confirm that all text is clearly visible for the user
- I want to confirm that all User Stories are done to my satisfaction
- I want to identify any edge cases
- I want to identify any potential test cases for automation

### Issues found/faced
- GITPOD workspace was down for a day, but the ability to interact with the database within GITPOD was down for 2 days


## Sprint 5 - 25th October - 31st October 2021

### User Stories Closed
- As a Developer I will need the following Users App Database scheme in place
- As an Admin User I want to delete an existing provider from the site
- As a User I want to be able to become a member
- As a User I want to be able to log into the site

### Unit Tests conducted
<p float="left">
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/unit_tests/28.10.21_1.png" width="600" height="400" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/unit_tests/28.10.21_2.png" width="600" height="400" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/unit_tests/28.10.21_3.png" width="600" height="400" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/unit_tests/30.10.21_1.png" width="600" height="400" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/unit_tests/30.10.21_2.png" width="600" height="400" />
</p>

### Exploratory Test Session Goals
- I want to confirm that a user can navigate between the resources subpages
- I want to confirm that a provider can be added to the site via a specific page
- I want to confirm that the Media subpage of the resources section loads and contains required data
- I want to confirm that the Tools subpage of the resources section loads and contains required data
- I want to confirm that a User can view a list of the existing Providers listed on the site
- I want to confirm that all text is clearly visible for the user
- I want to confirm that all User Stories are done to my satisfaction
- I want to identify any edge cases
- I want to identify any potential test cases for automation

### Issues found/faced
- Log in page restrictions broke most of the Unit tests - restrictions have been temporarily removed until further development has been completed. Additional user stories have been created.

### Initial User Testing (Alpha)
A session was held with an end user. During this session the following occurred:
- Demo of Sites purpose and available functions
- Exlainations of development setup
- Free time given to the User to "play" with the site

The feedback obtained from the User included:
- All bars on the site, ie top, middle and footer were each different shades of grey
- The images displayed on the exam list page (within the cards) were not uniform and some appeared stretched
- Go back button on the exam page does not work (page doesn't exist)
- Having the pattern in the background is fine, but if it is to be removed then the card background will need to be lighter
- On the login/register pages, the blue link to the opposite page is not very visible
- Name when I am signed in is not very big, or properly aligned
- The Providers new page, it would look better if the fields aligned
- In the Providers amend page, it would be better if the current logo was displayed as an image
- In the delete providers page, it would be good to confirm all the details, not just the title


## Sprint 6 - 1st November - 7th November 2021

### User Stories Closed
- As a User I want to be able to view all available Practise exams (caveat: pending JS UnitTests)
- As a User I want to be able to partake in the chosen exam (caveat: pending JS UnitTests)
- As a User I want to have my Submitted exam answers(results) Validated (caveat: pending JS UnitTests)

### Unit Tests conducted
No specific Unit Tests were created during this sprint.


### Exploratory Test Session Goals
- I want to confirm that a user can view all available exams
- I want to confirm that a user can view exam specifics when take exam button is selected, via a modal
- I want to confirm that a user can view questions and applicable answers for a chosen exam
- I want to confirm that a user can select a single answer for each question
- I want to confirm that a user can submit chosen answers for grading
- I want to confirm that a user will receive the correct response for each answer given (correct, incorrect, no answer)
- I want to confirm that a user will receive the correct overall score for an exam (pass, fail)
- I want to confirm a user can re-take the chosen exam
- I want to confirm a user can choose to return to the exam list after completing an exam
- I want to confirm a user can choose to return to the exam list instead of submitting exam answers
- I want to confirm that all text is clearly visible for the user
- I want to confirm that all User Stories are done to my satisfaction
- I want to identify any edge cases
- I want to identify any potential test cases for automation

<p float="left">
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/exploratory/resources_list.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/exploratory/resources_audio.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/exploratory/resource_landing_page.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/exploratory/exam_list.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/exploratory/exam_modal.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/exploratory/exam_questions.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/exploratory/exam_questions2.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/exploratory/exam_results.png" width="300" height="200" />
</p>

### Issues found/faced
- Once an exam has been submitted, the django url shortcut is not working to return the user to the exam list view
- Bug raised for Unit Tests which will be broken as a result of user authentification implementation

## Sprint 7 - 8th November - 15th November 2021

### User Stories Closed
-
-
-

### Issues fixed
- Once an exam has been submitted, the django url shortcut is not working to return the user to the exam list view
- Bug raised for Unit Tests which will be broken as a result of user authentification implementation

### Unit Tests conducted
<p float="left">
<img src="" width="300" height="200" />
<img src="" width="300" height="200" />
<img src="" width="300" height="200" />
</p>

### Code Validation Testing

#### Python (PEP8) Validation - Base studyWorld App
<p float="left">
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/studyworld_testspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/studyworld_testspy_pep8_2.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/studyworld_urlspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/studyworld_urlspy_pep8_2.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/studyworld_viewspy_pep8.png" width="300" height="200" />
</p>

#### Python (PEP8) Validation - Providers App
<p float="left">
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/providersformspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/providersmodelsspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/providersmodelsspy_pep8_2.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/providerstestspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/providerstestspy_pep8_2.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/providersurlspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/providersviewspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/providersviewspy_pep8_2.png" width="300" height="200" />
</p>

#### Python (PEP8) Validation - Members App
<p float="left">
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/membersformspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/memberstestspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/memberstestspy_pep8_2.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/membersurlspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/membersviewspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/membersviewspy_pep8_2.png" width="300" height="200" />
</p>

#### Python (PEP8) Validation - Exams App
<p float="left">
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/examsadminpy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/examsmodelspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/examstestpy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/examstestpy_pep8_2.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/examsurlspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/examsviewspy_pep8_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/examsviewspy_pep8_2.png" width="300" height="200" />
</p>

#### CSS Code Validation
<p float="left">
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/examcss_test_7.11.21.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/maincss_test_7.11.21.png" width="300" height="200" />
</p>

#### JavaScript Code Validation
<p float="left">
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/display.js_test_7.11.21_1.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/display.js_test_7.11.21_2.png" width="300" height="200" />
<img src="https://github.com/Sphere42/MSP-4/blob/master/static/images/testing/code_validation/examlist.js_test_7.11.21_1.png" width="300" height="200" />
</p>


### Exploratory Testing



### Initial User Testing on full MVP (Alpha)
A session was held with an end user. During this session the following occurred:
- Demo of Sites purpose and available functions
- Exlainations of development setup
- Free time given to the User to "play" with the site

_Note: User is different to the previous User conducting Alpha UAT_

The feedback obtained from the User included:
1. Providers List Page
    1. Change the delete buttons to Red
    1. Change the amend buttons to Orange/yellow
    1. Increase the header and description text size
    1. Center the description text
    1. Increase the icon size
    1. Change the color of the page buttons
    1. Change the colour of the visit site button
1. Add Providers Page
    1. Increase the description field size, can the text be wrapped?
    1. Correct the jumbotro text/buttons
1. Amend Providers Page
    1. Refactor the description field. 
    1. Show the existing logo as an image, not a link 
1. Delete Providers Page
    1. Change the buttons size and colours
    1. Change provider name to bold
    1. Move the fotter to the base of the page
1. Exam List Page
    1. Change the colour of the "take exam" button
    1. Center the text
    1. Increase size for larger devices
1. Take exam / display page
    1. Increase text size for larger screens
    1. soften the colour of the answer boxes
    1. Thicken the border between questions
    1. The timer acts straingely on smaller devices
1. Exam Results page
    1. Got to list page button broken
    1. Increase the text sixe for larger screens
    1. The total results section overhangs the width of the page
1. Resources List page
    1. Tweek the icons, not all display nicely on a dark background
1. Resources - Media page
    1. Make backgrounds "smaller" as they dont load straight away on first page visit for the tabs
    1. Remove the empty block at the base of each tab
    1. Increase the intro paragraph size on bigger screens
1. Resources - IDE/Tools?frameworks etc
    1. Center the pictures
    1. Change the link button colors 
    1. Increase the intro paragraph size on bigger screens








## Final Compatability testing:

The following Gifs are evidence collected from the compatability testing of the MSP-4 project

__iphone6/7/8 plus:__
Device width: 414px

<p float="left">
<img src=""/>
</p>

__samsung galaxy s5:__
Device width 360px

<p float="left">
<img src=""/>
</p>

__Moto G4:__

Device width 360px

<p float="left">
<img src=""/>
</p>

__Pixel 2:__

Device width 411px

<p float="left">
<img src=""/>
</p>

__iPad:__

Device width 1024px

<p float="left">
<img src=""/>
</p>

__Desktop Chrome:__

<p float="left">
<img src="" width="600" height="400" />
</p>

__Desktop Firefox:__

<p float="left">
<img src="" width="600" height="400" />
</p>

__Desktop Edge:__

<p float="left">
<img src="" width="600" height="400" />
</p>


## User Acceptance Testing:

Due to the size and timelines of this project, there will not be a structured Alpha/Beta stage of UAT. Instead, a selection of volunteers will conduct a time boxed exploratory session. After which feedback will be collated and transformed into bugs, improvements or new features.

The following is the feedback provided from the end users from their exploratory test session:


## Performance Testing:
The following evidence are the results from the performance speed test conducted on the deployed site:
<p float="left">
<img src="" />
</p>

## WAI Luminosity Colour Contrast Ratio Assessment

The following are the results of the Luminosity Colour Contract Ratio Analysis. This analysis determines the readability of the site based of background to foreground ratios as specified by the WAI. (https://www.w3.org/WAI/tips/designing/)

### Haze Background
<p float="left">
<img src="" />
</p>

### Fog Background
<p float="left">
<img src="https://" />
</p>

### Default Background
<p float="left">
<img src="" />
</p>


## Production Shakedown Pre Submission

Note to Assessor: Due to GitPods behaviour surrounding links, (and unexpected CORBS errors) there are numerous commit messages directly after the deployment that are very similar. This is due to the need to push all changes to production to verify if the implemented fixes were successful.

Once the web application had been deployed the HTML code was passed through an  for the HTML portions:

![w3cvalidator]()

Once the web application had been deployed the CSS code was passed through the official Jigsaw validator for the CSS portions:

![jigsawvalidator]()

Once the web application had been deployed the JavaScript code was passed through the official Jshint validator for the JavaScript portions:

![jshintvalidator]()

All elements have been visually inspected to ensure all information has been correctly populated and loaded.

All visual elements have been validated by the WAI approved Luminosity Colour Contrast Ratio Analysis checker. These results are located within the testing document.

Once the web application has been deployed the site loading/performance will be tested to ensure there are no undue delays for the User

### Unfixed bugs

