import sqlite3

# Connect to database
conn = sqlite3.connect("youtube_video.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
""")
conn.commit()


def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("No videos found.")
    for row in rows:
        print(row)


def add_videos(name, time):
    cursor.execute(
        "INSERT INTO videos (name, time) VALUES (?, ?)",
        (name, time)
    )
    conn.commit()
    print("Video added successfully!")


def update_videos(video_id, name, time):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (name, time, video_id)
    )
    conn.commit()
    print("Video updated successfully!")


def delete_video(video_id):
    cursor.execute(
        "DELETE FROM videos WHERE id = ?",
        (video_id,)
    )
    conn.commit()
    print("Video deleted successfully!")


def main():
    while True:
        print("\nYouTube Manager App")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_videos(name, time)

        elif choice == "3":
            video_id = int(input("Enter video ID to update: "))
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            update_videos(video_id, name, time)

        elif choice == "4":
            video_id = int(input("Enter video ID to delete: "))
            delete_video(video_id)

        elif choice == "5":
            print("Exiting app...")
            break

        else:
            print("Invalid choice!")

    conn.close()


if __name__ == "__main__":
    main()
