pipeline {

       agent {
        label 'vinode'
    }


    parameters {

        string(
            name: 'IMAGE_NAME',
            defaultValue: 'your-dockerhub-username/library-management',
            description: 'Docker Hub image name'
        )


        string(
            name: 'IMAGE_TAG',
            defaultValue: 'latest',
            description: 'Docker image tag'
        )

    }



    environment {

        DOCKER_CREDENTIALS_ID = 'dockerhub-creds'

        CONTAINER_NAME = 'library-management-app'

    }



    stages {



        stage('Checkout Code') {

            steps {

                echo "Checking out source code..."

                checkout scm

            }

        }




        stage('Install Security Tools') {

            steps {

                echo "Installing security tools..."

                sh '''

                pip install bandit

                '''

            }

        }





        stage('Python Security Scan - Bandit') {

            steps {

                echo "Running Bandit scan..."

                sh '''

                bandit -r . \
                -f json \
                -o bandit-report.json || true

                '''

            }

        }





        stage('Dependency Vulnerability Scan - Trivy') {

            steps {

                echo "Running Trivy filesystem scan..."

                sh '''

                trivy fs \
                --severity HIGH,CRITICAL \
                --exit-code 0 .

                '''

            }

        }





        stage('Create Docker Image') {

            steps {

                echo "Creating Docker image..."


                sh """

                docker build \
                -t ${params.IMAGE_NAME}:${params.IMAGE_TAG} .

                """

            }

        }





        stage('Verify Docker Image') {

            steps {

                echo "Docker image created:"

                sh """

                docker images \
                ${params.IMAGE_NAME}

                """

            }

        }





        stage('Docker Image Security Scan') {

            steps {

                echo "Scanning Docker image..."

                sh """

                trivy image \
                --severity HIGH,CRITICAL \
                --exit-code 0 \
                ${params.IMAGE_NAME}:${params.IMAGE_TAG}

                """

            }

        }





        stage('Docker Hub Login') {

            steps {


                echo "Login into Docker Hub..."


                withCredentials([usernamePassword(

                    credentialsId: "${DOCKER_CREDENTIALS_ID}",

                    usernameVariable: 'DOCKER_USERNAME',

                    passwordVariable: 'DOCKER_PASSWORD'

                )]) {


                    sh '''

                    echo "$DOCKER_PASSWORD" | docker login \
                    -u "$DOCKER_USERNAME" \
                    --password-stdin


                    '''

                }


            }

        }





        stage('Push Docker Image') {

            steps {

                echo "Pushing image to Docker Hub..."


                sh """

                docker push \
                ${params.IMAGE_NAME}:${params.IMAGE_TAG}

                """

            }

        }





        stage('Deploy Container') {

            steps {


                echo "Deploying application..."


                sh """

                docker stop ${CONTAINER_NAME} || true

                docker rm ${CONTAINER_NAME} || true


                docker run -d \
                --name ${CONTAINER_NAME} \
                -p 5000:5000 \
                ${params.IMAGE_NAME}:${params.IMAGE_TAG}


                """

            }

        }



    }



    post {



        success {

            echo """
            ====================================
             Pipeline Completed Successfully
             Docker Image Created
             Security Scan Completed
             Image Pushed to Docker Hub
             Application Deployed
            ====================================
            """

        }



        failure {

            echo "Pipeline Failed"

        }



        always {

            sh "docker logout || true"

            cleanWs()

        }


    }

}