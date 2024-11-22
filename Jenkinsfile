pipeline {
    agent any
    tools {
        python "Python3"
    }

    environment {
        registryCredential = 'ecr:us-east-1:awscreds' # Replace by the proper values
        appRegistry = "654654369899.dkr.ecr.us-east-1.amazonaws.com/flask-webapp" # Replace by the proper values
        Registryurl = "https://54654369899.dkr.ecr.us-east-1.amazonaws.com/" # Replace by the proper values
        cluster = "ECS-cluster"
        service = "ECS-service"
    }
    stages {
        stage('Fetch code') {
            steps {
                git branch: 'main', url: '<your-project-git-repo>' # Replace by the proper values
            }
        }

        stage('Build App Image') {
            steps {
                script {
                    dockerImage = docker.build(appRegistry + ":$BUILD_NUMBER", ".") # change the "." to the correct path to your dockerfile in case it doesn't reside in the root of the repo
                }
            }
        }

        stage('Upload App Image') {
            steps {
                script {
                    docker.withRegistry(Registryurl, registryCredential) {
                        dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }
}