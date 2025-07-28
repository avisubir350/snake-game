def call() {
    stage("Build") {
        echo "This is building stage"
        sh "docker build -t snake-game:v1 ."
    }
    return this
}