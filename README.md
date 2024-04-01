# Customizing Insurance Product Based on Customer Profile Leveraging Data Analytics

## Overview
This project develops a web-based application aimed at recommending life insurance products to users with high accuracy. By leveraging a refined ensemble of Random Forest and XGBoost machine learning algorithms, the system achieves an 80% accuracy rate in customizing product recommendations. Hosted on Heroku, the application provides a scalable and accessible platform for users to find life insurance products that best fit their needs.

## Features
Ensemble Machine Learning Model: Combines Random Forest and XGBoost algorithms to analyze user data and preferences, offering highly accurate recommendations.
* User-Friendly Interface: Developed using HTML5 and CSS, ensuring a seamless and engaging user experience.
* Cloud-Based Deployment: Utilizes Heroku for hosting, ensuring easy access and scalability.
* Research-Backed: Underpinned by extensive research on machine learning techniques, including Neural Networks and K-Means Clustering, with findings published in IEEE Xplore and presented at the 4th ICAECC-2022.

## Technologies Used
* Machine Learning: Random Forest, XGBoost
* Web Development: HTML5, CSS
* Deployment: Docker, Heroku

## Getting Started
To run this project locally, ensure you have Docker installed and follow these steps:

Clone the repository to your local machine.
Navigate to the project directory and build the Docker container:
```
docker build -t life-insurance-recommender
```
Run the container:
```
docker run -p 8000:8000 life-insurance-recommender
```
Access the application in your web browser at http://localhost:8000.


## Research and Publications
The methodology and findings of this project have been documented and published in IEEE Xplore and were presented at the 4th International Conference on Advances in Electronics, Computers and Communications (ICAECC) in 2022. For more detailed insights into the research behind this application, refer to the published papers linked in the docs directory.

