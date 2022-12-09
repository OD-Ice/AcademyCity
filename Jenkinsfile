pipeline {
    agent any
    stages {
        stage('begin') {
            steps {
                echo 'Hello'
            }
        }
    }
    post {
        always {
            echo 'goodbay'
        }
    }
}