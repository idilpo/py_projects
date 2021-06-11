while True:
    try:
        x = int(input("Enter: "))
        break
    except ValueError:
        x = int(input("Enter a valid input: "))
    finally:
        print("always runs")