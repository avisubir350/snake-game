@Library('shared-library') _

pipeline {
    agent {
        label "avi"
    }

    environment {
        DOCKER_HUB_CRED = credentials('dockerHubcred')
    }

    stages {
        stage('Clone') {
            steps {
                script {
                    clone()
                }
            }
        }
        
        stage('Build') {
            steps {
                script {
                    build()
                }
            }
        }
        
        stage('Push') {
            steps {
                script {
                    push()
                }
            }
        }
    }
}