pipeline {
    agent any

    environment {
        // Set up environment variables, if any
        VIRTUAL_ENV = 'venv'
    }

    stages {
        // Stage to set up the environment
        stage('Set up Python Environment') {
            steps {
                script {
                    // Install Python and dependencies
                    echo "Setting up Python environment..."
                    sh 'python3 -m venv ${VIRTUAL_ENV}'
                    sh '. ${VIRTUAL_ENV}/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        // Stage to run unit tests
        stage('Run Unit Tests') {
            steps {
                script {
                    echo "Running unit tests..."
                    sh '. ${VIRTUAL_ENV}/bin/activate && python -m unittest test_app.py'
                }
            }
        }

        // Stage to run code coverage tests
        stage('Run Code Coverage') {
            steps {
                script {
                    echo "Running code coverage..."
                    sh '. ${VIRTUAL_ENV}/bin/activate && coverage run -m unittest test_app.py'
                    sh '. ${VIRTUAL_ENV}/bin/activate && coverage report'
                    sh '. ${VIRTUAL_ENV}/bin/activate && coverage html' // For HTML report
                }
            }
        }

        // Stage to archive the code coverage reports
        stage('Archive Coverage Reports') {
            steps {
                script {
                    echo "Archiving coverage reports..."
                    // Archive the code coverage HTML report
                    archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
                }
            }
        }

        // Stage to clean up after the build
        stage('Clean Up') {
            steps {
                script {
                    echo "Cleaning up environment..."
                    // Clean up virtual environment
                    sh 'rm -rf ${VIRTUAL_ENV}'
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace after the build
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
