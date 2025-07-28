def call() {
    stage("Push") {
        echo "This is pushing stage"
        sh "docker login -u ${DOCKER_HUB_CRED_USR} -p ${DOCKER_HUB_CRED_PSW}"
        sh "docker image tag snake-game:v1 ${DOCKER_HUB_CRED_USR}/snake-game:v1"
        sh "docker push ${DOCKER_HUB_CRED_USR}/snake-game:v1"
    }
    return this
}