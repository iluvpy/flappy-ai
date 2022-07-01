from FlappyBird import FlappyBird


def main():
    flappy_bird = FlappyBird()
    while flappy_bird.is_running():
        flappy_bird.update()
        flappy_bird.render()


if __name__ == "__main__":
    main()