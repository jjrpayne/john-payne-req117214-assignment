# john-payne-req117214-assignment
Written assignment for BCPS competition REQ117214

## Purpose
This is a simple business rules engine that determines a client's eligibility for the Winter Supplement, and calculates the eligible supplement amount for each client.

### Eligibility Calculation
This rules engine determines the supplement amount based on the following criteria:

- **Family Unit In Pay For December**: If the client is not in pay for December, they are not eligible and all amounts are 0.

- **Family Composition**: Single people recieve a base amount of $60 and couples get a base amount of $120.

- **Number of Children**: Clients recieve $20 per child in adddition to the base amount.

## Prerequisites
This project requires Python 3 and the virtualenv module (recommended).

## Setup
First, clone the project to your local machine and navigate to the root directory.

Create a virtual environment:
```python3 -m venv venv```

Activate the virtual environment.

On Linux / MacOS:
```source venv/bin/activate```

On Windows:
```venv\Scripts\activate```

Install the requirements:
```pip3 install -r requirements.txt```

In order to use this application you need to set a topic ID. To set it as an environment variable, create a file named ".env" with the contents:
```TOPIC_ID=[insert topic ID]```

The topic ID can be provided by the [Winter Supplement Calculator](https://winter-supplement-app-d690e5-tools.apps.silver.devops.gov.bc.ca/) web app, or simply any string if you are not using the web app.

e.g:
```TOPIC_ID=d8114d3a-4984-4ff4-ac36-27ca0baa74fa```

Now, you can run the app in the terminal window with the virtual environment activated:
```python3 bre.py```