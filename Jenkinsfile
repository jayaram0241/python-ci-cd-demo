pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
        PYTHON = "python3"
    }

    stages {
        stage('Setup Python') {
            steps {
                // Ensure python3-venv is installed (optional: only works if Jenkins has sudo)
                sh '''
                if ! python3 -m venv --help > /dev/null 2>&1; then
                    echo "python3-venv not found. Please install it: sudo apt install python3-venv"
                    exit 1
                fi
                '''

                // Create virtual environment if it doesn't exist
                sh '''
                if [ ! -d "$VENV_DIR" ]; then
                    $PYTHON -m venv $VENV_DIR
                    echo "Virtual environment created."
                else
                    echo "Virtual environment already exists."
                fi
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                #!/bin/bash
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
                # Replace with your test command, e.g. pytest
                if [ -f "test_sample.py" ]; then
                    pytest
                else
                    echo "No tests found, skipping."
                fi
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                # Replace with your app entry point, e.g. python app.py
                echo "Build successful. You can run your Python scripts here."
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
        success {
            echo "Pipeline succeeded."
        }
        failure {
            echo "Pipeline failed."
        }
    }
}
