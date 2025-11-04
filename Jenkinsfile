pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jayaram0241/python-ci-cd-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -v'
            }
        }

        stage('Package App') {
            steps {
                sh 'zip -r app.zip app.py'
            }
        }

        stage('Deploy (Simulated)') {
            steps {
                sh '''
                mkdir -p deploy
                mv app.zip deploy/
                echo "App deployed to $(pwd)/deploy/"
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build and Deployment Successful!'
        }
        failure {
            echo '❌ Build Failed!'
        }
    }
}

