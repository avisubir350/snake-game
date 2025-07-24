pipeline {
    agent {
        label "avi"
    }

    environment {
        DOCKER_HUB_CRED = credentials('dockerHubcred')
    }

    stages {
        stage("Code clone") {
            steps {
                echo "This is code cloning"
                git url: "https://github.com/avisubir350/snake-game.git", branch: "master"
                echo "code clone success"
            }
        }
        
        stage("Build") {
            steps {
                echo "This is building stage"
                sh "docker build -t snake-game:v1 ."
            }
        }
        
        stage("Push") {
            steps {
                echo "This is pushing stage"
                sh "docker login -u ${DOCKER_HUB_CRED_USR} -p ${DOCKER_HUB_CRED_PSW}"
                sh "docker image tag snake-game:v1 ${DOCKER_HUB_CRED_USR}/snake-game:v1"
                sh "docker push ${DOCKER_HUB_CRED_USR}/snake-game:v1"
            }
        }
    }
}