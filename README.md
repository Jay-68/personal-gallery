# [Personal Gallery](https://gallery68.herokuapp.com/)
## Personal Gallery is a web based app where one can view different photos and a description  of these photos with the location they were taken.
#### By **[James Ngari](https://github.com/jay-68)**

## Description
The Personal gallery application has images displayed with their titles. Clicking a specific image displays a description and location of the image shot in a modal. A user can also filter images by location through the navigation bar.

## Live link

https://gallery68.herokuapp.com/

![Live page Image](/images/gallery.png)

## BDD

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Click Image | Click the image and a modal pops up | Shows the details of the image eg. title, description and the location |
| Click Location on navbar | Click on the location drop down | Takes the user to the page with images filtered according to location |
| Click on navbar brand | This is the home page | User is routed to the main page with all images. |

## Set-up and Installation

### Prerequsites
    - Python 3.6
    - Django

### Clone the Repo
Run the following command on the terminal:
`https://github.com/Jay-68/personal-gallery`


### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6 -venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate`

### Install dependencies
Install dependencies that will create an environment for the app to run

`pip3 install -r requirements`


### Running the app in development
In the same terminal type:
`python3 manage.py runserver`

Open the browser on `http://localhost:8000/`

## Known bugs

No known bugs. Any bugs or collaboration reach me at ngari.james.n@gmail.com


## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Animate CSS
    - Heroku
    - Django2
    - Postgresql

## Support and contact details
Contact me on ngari.james.n@gmail.com for any comments or reviews.

### License
MIT - Licence