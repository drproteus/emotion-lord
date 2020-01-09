# emotion-lord
Emotion Lord Automated Mood Tracker with Reporting

## The Goal
Allow users to schedule intervals in which the app will notify them to report a mood via SMS. This is an attempt to create a reliable but ideally non-invasive running record of an individual's mood. 
Submissions can also be done at any given moment (perhaps in times of particular distress, or following an event) via SMS or, in the future, a web interface or app.
Twilio is used for SMS.

## What's working(ish)
* Basic auth and registration.
* Users and profile's for the users that have numbers associated. This is how the SMS webhook finds the correct user. Currently no validation exists and duplications are possible. <- TODO: FIX
* Can send SMS with a mood level of 0 to 10. There is some validation of the input, and relevant response is sent to the user. 
* Basic API for the MoodRecord models using DRF.
