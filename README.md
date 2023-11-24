# Recipe

## Description

HomeChef, a web platform crafted with Django using Python, JavaScript, CSS/Bootstrap, and HTML, is a celebration of heart warming home-cooked meals.
Tailored for home cooks around the globe, this website provides a virtual haven for users passionate about sharing their culinary creations. Whether you're a seasoned home chef or an enthusiastic cook, HomeChef empowers you to create and share your favorite home-cooked recipes.
HomeChef  was created as the fourth project for the Code Institute Diploma in Software Development. The site features include user authentication and full CRUD functionality.
Users are given the ability to elevate their dishes with appealing photos, share their cooking through visual elements, and gives the option to like and comment on the recipes.
Link to the live site - [HomeChef](https://recipeblog-e0d016298fa8.herokuapp.com/)

## Design

#### Wireframe mock-ups

[Balsamiq](https://balsamiq.com/) was used to design the wireframes for my website.
![Home Page Wireframe](assets/balsamiq/balsamiq1.png)
![Recipe Page when login Wireframe](assets/balsamiq/balsamiqlogin.png)
![Recipe Page Wireframe not login](assets/balsamiq/balsamiqnotlogin.png)
![Register Wireframe](assets/balsamiq/balsamiqregister.png)
![Login Wireframe](assets/balsamiq/loginbalsamiq.png)
![Add new recipe Wireframe](assets/balsamiq/addnewrecipebalsamiq.png)
![MyProfile Wireframe](assets/balsamiq/myprofilebalsamiq.png)

#### Database Schema
![Database Schema Diagram](assets/databaseschema.png)
The database schemas were designed using [Lucid App](https://lucid.app/) These schemas were pivotal in planning the database models and defining their respective fields. They also facilitated visualizing the relationships between the models and their interactions. Recipe comprises four models: Recipe, Profile, User and Comment.

## Agile Development

The project applied Agile Methodology on GitHub for planning and execution. User Stories were established as GitHub issues, outlining their purposes distinctly. Each story contained specific acceptance criteria and tasks, categorized using colored labels such as 'must-have', 'should-have', 'could-have', or 'won't-have' to manage tasks during iterations.

Additionally, 4 Epics were initiated and expanded into 20 User Stories. Each of these stories was also assigned story points based on their complexity.

### Epics

1. User Authentication and Profiles [#1](https://github.com/users/nataliatesarova/projects/6/views/1?pane=issue&itemId=39537085)
2. Recipe management#21 [#2](https://github.com/users/nataliatesarova/projects/6/views/1?pane=issue&itemId=39569106)
3. Interaction with recipes [#3](https://github.com/users/nataliatesarova/projects/6/views/1?pane=issue&itemId=39571127)
4. Admin panel and content management [#4](https://github.com/users/nataliatesarova/projects/6/views/1?pane=issue&itemId=39536019)

![Django User Stories](assets/django_user_stories.png)

A full list of user stories can be found in the [HomeChef] (https://github.com/users/nataliatesarova/projects/6/views/1).

## Future features
Allow the user to save a draft version of a recipe to edit and complete at a later time.
Bio to be available for all registered users to view
Recipe Search and Filters: Allow users to search for recipes using keywords, ingredients, cuisine, and dietary preferences (e.g. gluten free, vegan)
Recipe Categories: Categorize recipes into sections such as breakfast, lunch, dinner, desserts.
Add difficulty level, serving size, nutritional and calorific information.
Newsletter Subscription: Provide a subscription option for users to receive regular updates on new recipes, cooking tips, and the latest blog updates.
Enable sharing of recipes directly via social media.
