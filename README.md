# Email Sentiment Analysis Project

## Overview

This project aims to determine the sentiment of received emails and store the sentiment analysis results in a database per mail sender. The idea business goal behind it, it´s the company to be able to "track" how happy their customers are over the time and take actions through personalized mails. The project utilizes pre-trained language models, specifically leveraging the Hugging Face Transformers library, for sentiment analysis. The AWS cloud platform is used for model deployment and database storage. More detailed information of each step will be provided in the README of each folders.

## Project Structure

The project is structured as follows:

src/: Contains the information of the tokenizer and best model.

data/: Placeholder for storing the dataset. Information about the dataset can be found in the readme of the data folder.

scripts/: Scripts for model training, EDA and some tests with emails.

static/, templates/ : For editing the webpage.

## Steps to Reproduce

### Clone the repository

``` bash
https://github.com/santiagoorar/email-sentiment
```

### Setup Environment:

Set up the required Python environment with dependencies:

``` bash
pip install -r requirements.txt
```

### Open the app

``` bash
python app.py
```

### The webpage

For this, fast api was used. After adding an email, automatically it will give its sentiment.

At first, the webpage was set by default:

![Default Webpage](Images/Webpage.jpeg)

Then, the webpage was modified using html code:

![Modified Webpage](Images/Webpage_modified.jpeg)

## Deployment

After having the optimal paremeters of the model and the dockerfile, the following steps were carried on for the deployment on AWS:

-   An IAM user was created.
-   Inside the user, in security credentials, a new access key was created in the CLI format.
-   An ECR (Elastic Container Registry) was created to save the docker image.
-   An EC2 machine was created. Just a CPU machine for cost reasons.
-   Docker was installed in the EC2 machine.
-   GitHub action was configured with the EC2 machine (Also the GitHub secret keys were added in the code).

#### Remarks: In the project only the predict pipeline was deployed, that of course in a real project also the train and test pipelines must be deployed as well, but to avoid computational costs of AWS it was done in this format.

## What to do next?

A database will be generated, with the aim of storing not only the sentiment of the email, but also the email address of the sender. With this, the companies will be able to "track" the email sentiments per sender over time. 



For deployment part I learnt the steps from the following repository:
https://github.com/krishnaik06/Text-Summarization-NLP-Project




