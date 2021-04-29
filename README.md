# MS4 - Premier League Store

[View the deployed project here.](https://premier-league-store-ms4.herokuapp.com/)
***

![Am I Responsive Image](static/readme_images/am_i_responsive.png)

For my final milestone project for the Code Institute Diploma in Software Development I created the Premier League Store. This is an app that allows fans of the Premier League to buy foootball kits and merchandise from the teams that play in the league, as well as keeping up to date with the latest news from the Premiership. 
Users are able to to filter the products by team so they can easily find the products of their favourite team and they can also leave comments on the news articles so that they can express they feeling on whats happening. 
The store owner has the ability to create, read, update and delete products and news articles enabling them to keep the store maintained and up to date. The website is fully responsive accross all devices ensuring there are no users unable to enjoy it.

## Table Of Contents

- [User Experience](#User-Experience)
    - [User Stories](#User-Stories)
    - [Project Stakeholders](#Project-Stakeholders)
    - [New users](#New-users)
    - [Returning Users](#Returning-Users)
    - [Mobile user](#Mobile-user)
- [Design Process](#Design-Process)
    - [UX Research](#UX-Research)
- [UX Design](#UX-Design)
    - [The Strategy Plane](#The-Strategy-Plane)
    - [The Scope Plane](#The-Scope-Plane)
    - [The Structure Plane](#The-Structure-Plane)
    - [The Skeleton Plane](#The-Skeleton-Plane)
    - [The Surface Plane](#The-Surface-Plane)
- [The Design Proccess](#The-Design-Proccess)
- [Features](#Features)
    - [Existing features](#Existing-features)
    - [Future releases](#Future-releases)
- [The Database Structure](#The-Database-Structure)
- [Technologies Used](#Technologies-Used)
    - [Languages](#Languages)
    - [Tools](#Tools)
- [Testing](#Testing)
- [Deployment](#Deployment)
    - [Cloning](#Cloning)
    - [Deploying to Heroku](#Deploying-to-Heroku)
- [Credits](#Credits)
    - [Content](#Content)
    - [Images](#Images)
    - [Acknowledgements](#Acknowledgements)

## User Experience
***

## Main aims of the project
***

The main aim of the Premier League Store is to provide a platform to football fans where they are able to purchase the kits and official merchandise of their favourite Premier League teams. The app is also aimed at providing it's users with up to date news regarding the Premier League whilst also giving it's registered users the chance to comment on these news articles to enable them to voice there opionion on what is happening. 

It was essential that the site was easy to use and was secure for it's users whilst they were making purchases. These matters were taken into great consideration throughout the development process to enusre that users have a good user experience.

## The Strategy Plane
***

To begin the UX process I started by creating a list of user stories that would enable me to carefully consider the design of my project to ensure that all of these potential users needs would be met.

## User Stories

### Viewing and Navigation

* As a shopper I want to be able to view a list of football shirts so that I can buy my favourite teams home shirt.

* As a shopper I want to be able to view the details of each individual product so I can see the price, description, images of the product, the sizes available and ratings.

* As a shopper I want to be able to view the contents of my shopping cart so that I can update or remove items.

* As a shopper I want to be able to view the grand total of my cart at all times so that I can avoid delivery costs.

### Registration and User Accounts

* As a user I want to be able to register for an account so that I can keep track of my order history in my profile. 

* As a user I would like to recieve a confirmation email so that I can verify my account.

* As a user I would like to be able to reset my password if I forget it, so that I can regain access to my account. 

* As a user I would like to be able to save my default delivery information so that I don't have to enter it every time I make a purchase. 

* As a user I would like to be able to view the news articles as a registered user so that I can add comments.

### Sorting and Searching

* As a shopper I want to be able to filter the products so that I can identify the best priced, best rated and by category of my choice. 

* As a shopper I want to be able to sort the products by team so that I can buy my favourite teams products.

* As a shopper I would like to be able to search by name or description so that I can buy the Arsenal Home Kit. 

### Purchasing and Checkout

* As a shopper I want to be able to see an overview of my order so that I can ensure that I have the correct items.

* As a user I want to see efficient form validation when entering my payment details so that I can be sure that my information is safe. 

* As a shopper I would like to see an overview of my order details so that I can ensure that it has been processed properly.

* As a shopper I would like to receive a confirmation email for my order so that I can keep it as proof of purchase. 

### Admin

* As the store owner I want to be able to add a product so that i can add new products to the store. 

* As the store owner I want to be able to edit and update products so that I can change the prices, images, description and ratings. 

* As the store owner I want to be able to delete products so that I can remove products that are no longer available. 

## The Scope Plane
***

By creating the user stories for my project, this enabled me to carefully consider the features that the site would need to have to meet the main aims of the project as well as the users needs.

### Products

The products page will display all of the available products to the users. From that page they will have the ability to filter the products by price, rating, category and team. Users will be able to click on each product to view the product info page where they will be given a more in depth description and be able to add the product to their cart.

### Accounts

Users will be able to register to create their own accounts. By doing so they will have their own personal profile from where they will be able to save their default delivery information and keep track of their order history. 

Store owners will have access to parts of the site that regular users will not. This will include pages to add new products and news articles and the store owners will also have the ability to edit and remove products and news articles.

### News 

The news page will feature articles of the latest news regarding the Premier League. Users will be able to add their own comments under each news article, as well as edit and delete them. 

### Shopping Cart 

The shopping cart page will provide an overview of the products that the user has added to their cart and will give them option of updating the quantity or removing products.

### Checkout 

The checkout page will feature a stripe payment system which will enable users to purchase products securely. After making a purchase users will be provided with confirmation of their order. 

## The Structure Plane
***

As I am using Django to create the site, I will structure each feature into it's own respective app. The site will contain fixed nav bar that will enable users to be able to easily navigate between the different apps.  

The apps that will collectively make up the site are as follows:
* Home
* Products (Store)
* News
* Profiles
* Cart 
* Checkout

## The Skeleton Plane

With the main features and strucutre now in place for the site, it was now time to begin designing the wireframes to really bring my ideas to life. To create the wire frames I used a programme called Figma. 

The wireframes can be seen below. 

![Am I Responsive Image](static/readme_images/wireframe_1.png)
![Am I Responsive Image](static/readme_images/wireframe_2.png)
![Am I Responsive Image](static/readme_images/wireframe_3.png)

[You can view the Figma wireframes project here](https://www.figma.com/file/opdSBty1arp4J1AOlMTdIk/Milestone-Project-4?node-id=0%3A1)

[Back to Top](#table-of-contents)

## The Surface Plane

## Features
***

### Existing Features
***

### The Products App

The products app is where users are be able to view all of the products which the store has in stock.

Users are able to filter the products by the following categories:
* Home kits
* Away Kits 
* Third Kits
* Training
* Merchandise

Users are able to filter the products by the following teams:
* Arsenal
* Chelsea
* Fulham 
* Liverpool 
* Manchester City 
* Manchester United
* Newcastle United
* Southampton
* Tottenham
* West Ham United

Users are able to filter the products by:
* All products
* By category
* By rating (low to high / high to low)
* By price (low to high / high to low)

Users are able to view a product info page which gives them a more in depth description of the product as well as enabling them to choose what size if applicable and the quantity before adding the product to their shopping cart.

### The News App

The news app is where users are able to keep up to date with what is going on in the world of the Premier League.

Registered users are able to add comments to the articles enabling them to express their opinions on the current events that are taking place. Registered users have the ability to edit or remove their comments if they wish.

### All Auth and Profiles app

The site has the functionality to allow users to register and sign up for an account. After signing up, users are sent a confirmation email for them to confirm there account. Each registered user has their own personal profile from where they are able to store their default delivery information as well as keep track of their order history. 

The store owners have the ability to add, edit and delete products and news articles enabling them to maintain the store and ensure that the News is kept up to date. 

### Shopping Cart

The shopping cart provides the users with an overview of the products they have added to their cart and gives them the opportunity to update the quantity or remove items if they wish to do so. 

### Checkout App

The checkout app allows users to enter their delivery and payment information through the stripe payment system that has been implemeneted. On the checkout page the user is also provided with an overview of the order that they are about to purchase.












