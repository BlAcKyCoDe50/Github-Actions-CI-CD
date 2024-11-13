# CI/CD Pipeline with Github-Actions, Ansible, and Docker

This project sets up a Continuous Integration/Continuous Deployment (CI/CD) pipeline using Github-Actions, Ansible, and Docker to automate the build, test, and deployment of code. The goal is to ensure reliable and efficient code delivery.

## Project Overview

### Components
- **Github-Actions**: Orchestrates the CI/CD pipeline, triggering the build, test, and deployment stages.
- **Docker**: Containerizes the application, providing consistent environments across different stages of the pipeline.
- **Ansible**: Manages configuration and deployment, deploying Docker containers to the production server.

### Pipeline Flow

1. **Code Push**: Developers push code changes to the GitHub repository.
2. **Code update**: A GitHub-Actions will triggered automatically notifies  to start the pipeline.
   
   #### Build Stage:
   - Github-Actions checks for the changes in the code.
   - Docker builds a new image based on the latest code using the `Dockerfile`.
   - The image is tagged with a unique identifier (e.g., commit SHA or build number) for versioning.

   #### Test Stage:
   - Github-Actions runs tests on the Docker container to validate the code.
   - If tests pass, the pipeline continues; otherwise, Github-Actions marks the build as failed.

   #### Deployment Stage:
   - Github-Actions uses Ansible to deploy the Docker container to the production server.
   - Ansible connects to the production server, pulls the latest Docker image, and starts the container.

   #### Production:
   - The application runs in a Docker container on the production server.
   - Monitoring can be configured to track the health of the application.

  ## Pipeline flow images

  ![image](https://github.com/user-attachments/assets/46a13f7c-a7f4-4266-8944-f29b3bbb96e3)

  
  ![image](https://github.com/user-attachments/assets/c4ec991c-ae87-4b70-9fd5-b9a38ec4bca9)

  # CI/CD pipeline executed successfully and deployed the updates to the website
  ![image](https://github.com/user-attachments/assets/0f7632dc-3cba-4f48-a715-c72df69f53c6)


  ## You can also check by click on Actions -> click on any workflow 
  ![image](https://github.com/user-attachments/assets/b2fe2916-684e-4e40-9c00-9d4661f46b7d)




## File Details

- **Dockerfile**: Specifies the environment and dependencies for the application, creating a consistent containerized build.
- **.workflowfile**: Defines the workflow of Github-Actions  stages (Build, Test, Deploy).
- **playbook.yml**: Ansible playbook that automates the deployment by pulling the latest Docker image and running it on the production server.

## Setup Instructions

### Prerequisites

- Docker installed on AWS EC2 server.
- Must have knowledge of Github-actions with access to the GitHub repository and Docker.
- Ansible installed on AWS EC2 instance  for deployment to production.

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BlAcKyCoDe50/Github-Actions-CI-CD


