def call() {
    stage("Code clone") {
        echo "This is code cloning"
        git url: "https://github.com/avisubir350/snake-game.git", branch: "master"
        echo "code clone success"
    }
    return this
}