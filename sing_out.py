queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

def show_queue(queue):
    """ Print everyone currently in the queue """
    print()
    if len(queue) == 0:
        print("The queue is currently empty.")
        return
    else:
        print("Current Queue: ")
        print()
        for index, act in enumerate(queue):
            name, song = act
            print(f"{index + 1}. {name} - {song}")
        print()
        print("Options: add / next / top / remove / quit")

def prompt_for_singer():
    """ Ask for a name and a song, and return them cleaned up. """
    print()
    new_singer_name = input("Name: ")
    new_singer_song = input("Song: ")
    return new_singer_name.strip().title(), new_singer_song.strip().title()

def add_singer(queue):
    """ Ask for the singer and add them to the queue """
    singer, song = prompt_for_singer()
    if len(singer) == 0 and len(song) == 0:
        print("Oops! I need a name and a song to add someone to the queue")
        return
    queue.append((singer, song))
    # Tuple olarak eklemek için () kullanmalıyız.
    print()
    print(f"Added {singer} to the queue.")

def remove_singer(queue):
    """ Remove singer from the queue """
    if len(queue) == 0:
        print("The queue is currently empty.")
        return
    singer_name = input("Who do you want to remove? ").strip().title()
    print()
    for singer in queue:
        if singer[0] == singer_name:
            queue.remove(singer)
            print(f"Removed {singer_name} from the queue.")
            return
    print(f"There's no one named {singer_name} in the queue.")

def next_singer(queue):
    if len(queue) == 0:
        print("Oops! There's no one left to call up!")
        return
    singer, song = queue.pop(0)
    print()
    print(f"NOW UP: {singer} - {song}")
    print()

def move_to_top(queue):
    print()
    if len(queue) < 2:
        print("You need at least two singers in the queue to move someone to the top.")
        return
    try:
        position = int(input("Who do you want to move to the top? Enter a number: "))
    except ValueError:
        print("Please enter a number.")
        return
        # Burada sonlandırmamız gerekiyor.
    if position < 1 or position > len(queue):
        print(f"There's no singer at {position}")
        return
    print()
    selected_act = queue.pop(position - 1)
    # Index başlangıcı sıfır olduğu için böyle kullanmamız gerekiyor.
    queue.insert(0, selected_act)
    print(f"Moved {selected_act[0]} to the top of the queue!")
    # Burada singer, song diye açabilirdik ama direkt index ile isme eriştim.

def run_app(queue):
    print("=" * 40)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 40)

    is_running = True

    while is_running:
        show_queue(queue)
        command = input("> ")

        if command == "quit":
            is_running = False
            print("The queue is closed. Good night!")
        elif command == "add":
            add_singer(queue)
        elif command == "next":
            next_singer(queue)
        elif command == "top":
            move_to_top(queue)
        elif command == "remove":
            remove_singer(queue)
        else:
            print("Invalid command, try again.")

run_app(queue)