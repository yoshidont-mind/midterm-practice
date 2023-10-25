def enqueue(queue, candidate, pop):
    queue.append(candidate)
    queue.sort()
    if pop:
        return queue.pop(0)
    else:
        return queue[0]

def main():
    waiting_in_line = []
    print(enqueue(waiting_in_line, "Juan", False))
    print(enqueue(waiting_in_line, "Jack", True))
    print(enqueue(waiting_in_line, "Joe", True))
    print(enqueue(waiting_in_line, "Jesper", False))
    print(enqueue(waiting_in_line, "Jerry", True))
    print(enqueue(waiting_in_line, "Josh", True))


if __name__ == "__main__":
    main()
