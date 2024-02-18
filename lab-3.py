if __name__ == "__main__":
    num_list = [int(x) for x in input("Enter a list of numbers separated by space:").split()]
    total_sum = sum(num_list)
    print("Sum of numbers in the list:", total_sum)