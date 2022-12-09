pipeline {
    agent any
    stages {
        stage('begin') {
            steps {
                echo 'Hello 123'
            }
        }
    }
    post {
        always {
            echo 'goodbay'
        }
    }
}