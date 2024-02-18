if __name__ == "__main__":
    num_list = [int(x) for x in input("Enter a list of intergers separated by space:").split()]
    shorted_list = sorted(num_list)
    print("Sorted list:", shorted_list)