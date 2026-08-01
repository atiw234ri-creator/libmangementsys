pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                // Add your command here
                // Example:
                // sh 'npm install'
                // sh 'pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
                // Example:
                // sh 'npm run build'
                // sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Example:
                // sh 'npm test'
                // sh 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}