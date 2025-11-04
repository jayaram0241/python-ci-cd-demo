pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'   // name of virtual environment folder
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jayaram0241/python-ci-cd-demo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                # Create virtual environment if it doesn't exist
                if [ ! -d "$VENV_DIR" ]; then
                    python3 -m venv $VENV_DIR
                fi

                # Upgrade pip inside the virtual environment
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                pytest -v
                '''
            }
        }

        stage('Package App') {
            steps {
                sh '''
                zip -r app.zip app.py
                '''
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

