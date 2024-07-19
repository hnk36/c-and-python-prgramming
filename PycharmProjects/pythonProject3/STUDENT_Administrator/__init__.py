from database import connection

def main():
    # Connect to the postgresql database
    connect = connection
    if connect is None:
        print("Unable to connect to database")
    else:
        print("Connected to database")


if __name__ == "__main__":
    main()