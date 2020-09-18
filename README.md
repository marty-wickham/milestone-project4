# Fourth Milestone Project / PEWN
____
The live site: (https://eshop-project4.herokuapp.com/)

Pewn is an ecommerce site built using Django, to showcase my skills in a Full Stack website. The purpose of the website is to allow a user 
to access the sites to purchase video games. If the user wishes to buy the video games they  will have to register with the site and make an
account. Once the user has made an account the site will automatically generate a very basic profile for the user. Here they can change the details
of their profile such as there email adress and profile picture. A default profile picture is supplied if the user does not wish to change this themselves.

In addition to purchasing games, users may use the website to leave their own reviews on a game. These reviews can be found in the details page of each game.
This is also where the form to leave reviews can be found. Each review requires a rating and the average of the total ratings is displayed for each game.
A user may only leave one review per game.

When the users access's the site they will land on the home page. The home page is designed to allow for the owner to post information about the site and
provide some basic information about how to use the site as well as any upcoming news or sales events. These posts are provided in carousel format, and may
only be provided by the site administrator through the backend administration page.


## UX Design:

### Strategy

#### Who is this for?
This website serves as a fictional ecommerce shop for anyone who wishes to sell products online such as video games, in this case.

#### What type of content will be relevant? 
The content on the site will be made up of a collection of some of my favourite games. Each game has a details page where you can view more information about 
each game such as genre, release date, multiplayer options etc.

Media content – The games are displayed in a tile format in a library. Each tile has a title image for the game. Each tile itself is a clickable link to a page 
                for more information about that game. To avoid gathering large amounts of media for the site, each game model only requires two images, a large
                background title image for the games detail page and a a small title image for the game tiles. To substitute for the lack of imagery each game-details
                page has a trailer which is displayed in a video modal. Each of the trailers is taken from Youtube.


### Scope

#### What does the client need?
* A brand name to help make the site more recognisable and create a sense of familiarity.
* A mobile first website approach
* A "Home"/ landing page which contains some information about the site itself.
* A "Store" page displaying all of the games, including an image, name and price for each game tile.
* A "Game details" page providing more information about each game.
* A review form, to allow users to post their own review for each game.
* A registration page for a user to create an account.
* A login page to allow the user to login
* A basic profile page for each user, with a profile image, username and email address.
* A "cart" page to allow users to view the items they are interested in.
* A "checkout" page to confirm purchase order and handle payment.

#### User scenarios
**Scenario:**
A user would like to view the site ---  
**Requirement:**
The ability to click on a link and be directed to the home page.

**Scenario**
A user wishes to learn more information about the site. ---
**Requirement:**
Obvious information on the Home page explaining what the site is and how to use it. Information about the site and any relevant news 
should be available as a post on the website provided by the site administrator through Djano's built in admin page.

**Scenario:**
A user wants to view what games are for sale ---  
**Requirement:**
A "Store" link should be available in the navbar to access the sites collection of products. This page will access all of the products models
from the site database. Pagination will be used to spread out the collection of products on to more than one page to allow for easier naviagtion.

**Scenario:**
A user wants to check if a specififc product is sold by the site ---  
**Requirement:**  
A search bar should be contained in the navbar to allow a user search if that specific product is available on the site. This will require a search
filter to filter out databse results using the users query.

**Scenario:**
A user wants to view more information about a product available in the store  ---  
**Requirement:**  
Each product tile should serve as a link allowing the user to easily and intuitvely access that prodcuts detals and information. In the HTML each tile
div will be wrapped in an an anchor link. 

**Scenario:**
An anonymous user/ registered user would like to browse the sites products and add items to a cart ---  
**Requirement:**  
The site will need a "Cart" page which will allow the user to edit their choices before commiting to a purchase. To achieve this a cart context will
need to be created so that the cart's contents are available anywhere on the site. Cart views will also need to be created which allow
the user to add and remove items from the cart.

**Scenario:**
A user would like to purchase a product ---  
**Requirement:**  
In order to purchase a product an anonymouse user will need to register to the site and make an account. Once they have done this, a checkout page and
some form of payment processing api will then be require to allow the user to purchase the items. The checout page will require two forms. One form will
be used to create an order item in the site's database. The second form will be used to handle the user's payment information.

**Scenario:**
A user would like make an account on the site ---  
**Requirement:**  
The site will require a registration page. Here they will register a username, email address and confirm a password choice. This will
require the use of Django's built in authorization and authentication models to create users in the database.

**Scenario:**
A user would like login to their account  ---  
**Requirement:**  
The site will require a login page. Here they will login with their login credentials created at registration. This will require a login view and a login form.

**Scenario:**
A user would like to edit their account information  ---  
**Requirement:**  
A basic profile will be created automaically by the site when the user makes an account. Here the use will be able to change the information they registered
with, as well as the default profile picture.

**Scenario:**
A user would like to leave a review on a product ---  
**Requirement:**  
On each game details page there will be a form to leave a review. In order to leave a review the user will need to be logged in. If they are not logged in,
they will be redirected to the login page, or, if they do not have an account, the registration page. Once the user logins they will be redirected to the
review form. To make this do this a review model and review form will be created. The form will allow the user to intreract with a star rating. This will
require the use of some Javascript and jQuery.


### Structure

#### Information Architecture
For this project I will be using a standard tree structure. To achieve this, the header of each page will 
consist of a navigation bar that contains the logo of the business and the main navigational links for each page in the website. 


## Features

### Existing Features
* Feature 1 - A "store" page that displays all of the games in the database in the form of tiles. Each tile displays a title image for the game,
                the game title, a price and an add to cart button. 

* Feature 2 - A registration page containing a form that allows the user to create an account.

* Feature 3 - A login page containing a form that allows the user to log in to their account.

* Feature 4 - A "Game details" page that shows more information about each game.

* Feature 5 - Each "Game details" page contains a video modal that plays a trailer for each game. 

* Feature 6 - An "Add review" button. This will toggle the display value for the review form. If the user is not authenticated then a message will redirect 
                them to a login or registration page. This avoids needlessly writing a review that cannot be submitted if the user is not logged in.

* Feature 7 - An "Cart" page that allows the user to view all of the items in their cart and add or remove items. 

* Feature 8 - A "Checkout" page that allows the user to review their order. The forms here create an order object in the database and the second Stripe form handles 
                payment.
 

## Technology's Used:
Information Architecture

For this project I will be using a standard tree structure. To achieve this, the header of each page will 
consist of a navigation bar that contains the logo of the business and the main navigational links for each page in the website. 
* [HTML5](https://www.w3schools.com/html/html5_intro.asp) - A markup language used to create the structure of the webpage.
* [CSS3](https://www.w3schools.com/css/) - Used to style the HTML code. 
* [Bootstrap4](https://getbootstrap.com/) - A front-end component library used to build responsive mobile-first desifn for this webpage.
* [Font Awesome](https://fontawesome.com/) - An icon library and toolkit used to implement various icons and social logos on this webpage.
* [JavaSccript](https://www.javascript.com/) - A high-level, interpreted programming language used to mange the interactivity of the site by
                                                controlling the behaviour of elemetns on the page when a user interacts with them.
* [jQuery](https://jquery.com/) - jQuery is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling.
* [Gitpod](https://github.com/gitpod-io/gitpod) - The is the IDE used to write and test the code for this project.
* [Git](https://git-scm.com/) - Git is a tool that is used to track and store changes to your codes as you work. It stores your code in a local repository.
* [Github](https://github.com/) - Github is a remote repository used to store all of the code for this project.
* [Python 3](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language. In this project it was
                                        used to manage the back end development of the project.
* [Django](https://www.djangoproject.com/) - Django is a free opensource, high level Python framework. It handles a lot of the work of building a fullstack website.
* [Stripe](https://stripe.com/en-ie) - Stripe is a software as a service. The stripe API is used to handle payment processing for this project.
* [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform as a service. Heroku is used to deploy this project.
* [S3 Buckets](https://www.mongodb.com/cloud/atlas) - An Amazon web service, S3 (Simple Storage Solution) is a storage service used to host all of the media and the
                                                        static files for this project.


## Testing

### Manual Testing 
In order to ensure the website functioned as expected, most of the testing for this project was done using the browser web developer tools. This was a very 
important tool for me through the creative process as it helped me to isolate where the problems were in my code. The issues that this helped me resolve 
include:

* Navigation bar and page links:
1. Click each link and check to that each page is rendered.

* Media settings:
1. Create a super user via the CLI.
2. Log in to the super user account through the login form.
3. Head to the "profile" page and check to see the default image is displaying.

* Registration form - empty/partially filled form:
1. Fill out the form leaving the first field empty.
2. Try to submit a partially filled form and check for the required field messages.
3. Repeat for each field.

* Registration form - password confirm:
1. Fill out the form.
2. Deliberatley mismatch passwords.
3. Submit form and check for error message.

* Registration form - login message and redirect:
1. Fill out the fom create a new "TestUser".
2. Submit the form.
3. Check to see that the user is redirected to the login page and the "succesful account creation" message is displayed.

* Registration form - user model:
1. Log in to the admin page with the super user credentials.
2. Check to see that a new "TestUser" was created.

* Registration form - existing user:
1. Fill out the form using the same username "TestUser".
2. Try to submit the form and check for "user already exists" error message.

* Login form:
1. Login with the "TestUser" credentials.
2. Check to see redirectd to "Home" page and "successful login" message.

* Login form - error messages:
1. Login with a non-existing user.
2. Check for error message.
3. Login "TestUser" with wrong password.
4. Check for error message.

* Logout:
1. Click the logout button in the navbar.
2. Check to see redirectd to "Logout" page and "Logout succesful" message.

* Update profile form:
1. Change username to "TestUser2", email and the default picture.
2. Submit form and check for success message and updated details.
3. Check user info updated in admin site.

* Update profile form - existing username:
1. Register a new "TestUser".
1. Change username of "TestUser2" to "TestUser".
2. Submit form and check for "Username already exists" message.

* "All games" view:
1. Create some game models with and without sale discounts in the admin site of the project.
2. Go to the "Store" page and check to see that the game models have been loaded and their images are displaying.

* Cart: 
1. Add multiple items to cart.
2. As items are added check "product count" variable displayed in the navbar increases by 1 with each request.
3. Once an item has been added three times check "Max limit" error message is displayed.
4. Add games to the cart with and without sale prices to test the "total" variable.
5. On the "Cart" page, remove items from the cart and submit.
6. Check "quantity" value has changed in the forms quantiity input.
7. Change an items quantity value to 0.
8. Check that the game is completely removed from the cart.
9. Remove all games from the cart and check for the "Empty shopping cart" message.

* Cart - links:
1. Click the different "Add to cart" links throughout the site.
2. Check that the user is returned to the page they are currently viewing.

* Checkout form - empty/partially filled form:
1. Fill out the form leaving the first field empty.
2. Try to submit a partially filled form and check for the required field messages.
3. Repeat for each field.

* Review form - star rating:
1. Hover over the first star in the rating.
2. Move to the right gradually over each star and to see if it becomes highlighted.
3. At the last star, move back from left over each star checking that each star becomes unhighlighted as you move.
4. Move over a random star. Check all the stars up to that star become highlighted at the same time.
5. Click a random star to leave a rating.
6. Hover over the higher rating stars to see that they highlight, displaying the option to click choose anothe rating.

* Review form - empty/partially filled form:
1. Fill out the form leaving the first field empty.
2. Try to submit a partially filled form and check for the required field messages.
3. Repeat for each field.

* Review form - review limit per user:
1. Log in as "TestUser".
2. Fill out the form and post a review.
3. Check for "review posted" message and review.
4. Fill out the form again and try post a second review for the same game.
5. Check for "One review per user" error message.


### Autmoated Testing
For this project I used Django's built in TestCase class to test the products app. Tests were written to test the product models, forms and views.


I used a *code validator* on [W3 Markup Validation Service](https://validator.w3.org/#validate_by_input) to checks for any errors that needed to be 
fixed in my code. 

Finally, I posted my project in the peer-code-review channel on Slack and received some very helpful criticism to help me fix some mistakes that 
slipped under the rader.

### Bugs
Bugs I am aware of:
1. The star rating does not highlight completely effectively when you hover over any random star. However if you move to the left or right, the stars
    will then highlight.
2. When adding items to the cart it would be preferable that the page was not reloaded and hence, the use would remain where they are on a page.

## Features Left to implement
1. I would like to add in an order history section to the profile page of the site to allow users to view the details of past orders.
2. On the "Game details" page I think a carousel modal with images would be a nice feature and give the site more content.
3. A delete button to completely remove an item from the cart in one click.
4. An "Empty cart" button to remove all items from the cart in one click.
5. After being redirectd to sign in to leave a review, I would have liked that when the user signs in they are redirectd to the review form.
6. On the Game Detials page, the video modal does not stop playing when you click out of it. You must first click pause or else it will keep playing.
    It would be better that the video automatically stop when the user clicks out of the video.


## Deployment

### Gitpod and Github
1. The project was written and developed in the Gitpod IDE.
2. A local repository was intialized using Git. Regular changes were commited to the local repository.
3. Github was used as a remote repository, and at the end of each development session, all local commits were pushed to (https://github.com/martycistudent/milestone-project4)
4. At the start of the project configuration variables were set in and env.py file. This included the SECRET_KEY, DATABSE_URL, HOST_NAME, DEVELOPMENT variable, STRIPE keys,
    AMAZON_S3 keys. These had to be set in both the Gitpod IDE and on Heroku. The env.py file was added to the a .gitignore file so as not to be included in the Github repository.

### AWS S3 Buckets
1. S3 buckets was used to host the media and static files for this project. This was necessary for deployment as Heroku does not provide a standard file system.
2. Create a new S3 bucket. Add all of the relevant settings to allow public access and hosting for static files.
3. Create a new group, matching the group name with the bucket name.
4. Add the relevant settings and policies.
5. Add a new user to this group with programmatic access. 
6. The AWS_ACCESS keys were then added to the projects env.py file.
7. Install boto3 and django-storages in the CLI to allow Django to use S3 as a storage loaction.
8. The relevant settings were then added to to the settings.py file in the project folder.
9. I then ran a collectstatic command to upload the projects static files into the new S3 bucket.

### Heroku
1. To deploy the project on Heroku a new app was created via the CLI. The dependancy guncicorn was installed to serve the website on Heroku.
2. The project was linked to Heroku for deployment, a requirements.txt file and a Procfile were created to deploy the project on Heroku.
3. In Heroku in the project application, Heroku Postres database was added into the application. The databse URI was then added to the projects
    env.py file.
4. I then installed dj-database-url updated the settings.py file to allow the project to connect to the Postgres database URL.
5. The Github repository for the code was then linked to the Heroku aplication to enable the apllication to be updated with a single push command.
6. Finally in the Heroku dashboard all of the configuration variables from the env.py file were added to the Heroku application.
5. The Project’s source file is now published as a site on Heroku at [PEWN](https://eshop-project4.herokuapp.com/)


## Credits
### Media 
All of the images for this project were searched and found on google images. All of the game trailers for this project came from Youtube.com.

### Acknowledgements 
#### Front End Design
For the main layout of this project I took inspiration from [GOG.com](https://www.gog.com/).

#### Back End
To complete this project I relied on additional reasearch in order to get the star rating working for my review form.
* (https://codepen.io/depy/pen/vEWWdw)

During the project I had to upgrade Django to a newer version. In order to do that I watched Corey Schafer's Django series on youtube. Great guy.
* (https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1)

