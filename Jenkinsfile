pipeline {
    agent any

    environment {
        IMAGE_NAME = "library-management"
        CONTAINER_NAME = "library-management-app"

        MYSQL_HOST = "mysql"
        MYSQL_USER = "root"
        MYSQL_PASSWORD = "root123"
        MYSQL_DATABASE = "lms"

        NETWORK = "library-network"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d \
                  --name $CONTAINER_NAME \
                  --network $NETWORK \
                  -p 5000:5000 \
                  -e MYSQL_HOST=$MYSQL_HOST \
                  -e MYSQL_USER=$MYSQL_USER \
                  -e MYSQL_PASSWORD=$MYSQL_PASSWORD \
                  -e MYSQL_DATABASE=$MYSQL_DATABASE \
                  $IMAGE_NAME
                '''
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo "Deployment Successful"
        }

        failure {
            echo "Pipeline Failed"
        }
    }
}