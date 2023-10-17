# Email Sentiment Analysis Project
## Overview
This project aims to determine the sentiment of received emails and store the sentiment analysis results in a database per mail sender. The idea business goal behind it, it´s the company to be able to "track" how happy their customers are over the time and take actions through personalized mails. 
The project utilizes pre-trained language models, specifically leveraging the Hugging Face Transformers library, for sentiment analysis. The AWS cloud platform is used for model deployment and database storage. More detailed information of each step will be provided in the README of each folders. 

## Project Structure
The project is structured as follows:

src/: Contains the source code for the sentiment analysis model and API.

data/: Placeholder for storing datasets and preprocessed data.

scripts/: Scripts for data preprocessing and model training.

docs/: Documentation related to the project.

notebooks/: Jupyter notebooks for experimenting and analysis.

config/: Configuration files for the project.

## Steps to Reproduce
### Setup Environment:

Set up the required Python environment with dependencies by following the instructions in src/README.md.

### Data Preprocessing:

Preprocess the email data and prepare it for training. Refer to the scripts/preprocess.py script.

### Train the Sentiment Analysis Model:

Fine-tune a pre-trained language model for sentiment analysis using the provided training script (scripts/train_model.py).

### Model Deployment on AWS:

Launch an AWS EC2 instance and deploy the sentiment analysis model as a RESTful API.
### Database Setup on AWS:

Choose and configure an AWS database service to store the sentiment analysis results.
### Connect API with Database:

Modify the API to store sentiment analysis results in the database.
### Testing and Validation:

Test the API for sentiment analysis and database storage functionality.
### Monitoring and Maintenance:

Set up monitoring for the API and AWS services to track performance and usage.
### Contributing
Contributions to the project are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request.

### Contact
For inquiries or assistance, please contact sormando@correo.um.edu.uy

