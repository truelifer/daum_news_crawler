pipeline {
    agent { dockerfile true }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    def customImage = docker.build("test:0.01")
                }
            }
        }
    }
}