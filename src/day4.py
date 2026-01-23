#!/usr/bin/env python3

def main() -> None:
    forklift = open("/input/input_day4.txt").read().strip()
    forklift_list_2d = [list(x) for x in forklift.split("\n")]
    forklift_list_2d_updated = [row.copy() for row in forklift_list_2d]
    num_removed = 0
    while True:
        for i in range(len(forklift_list_2d)):
            for j in range(len(forklift_list_2d[i])):
                if forklift_list_2d[i][j] != "@":
                    continue
                num_neighbors = 0
                if j - 1 >= 0 and forklift_list_2d[i][j - 1] == "@":
                    num_neighbors += 1
                if j + 1 < len(forklift_list_2d[i]) and forklift_list_2d[i][j + 1] == "@":
                    num_neighbors += 1
                if i - 1 >= 0 and forklift_list_2d[i - 1][j] == "@":
                    num_neighbors += 1
                if i + 1 < len(forklift_list_2d) and forklift_list_2d[i + 1][j] == "@":
                    num_neighbors += 1
                if i - 1 >= 0 and j - 1 >= 0 and forklift_list_2d[i - 1][j - 1] == "@":
                    num_neighbors += 1
                if i - 1 >= 0 and j + 1 < len(forklift_list_2d[i]) and forklift_list_2d[i - 1][j + 1] == "@":
                    num_neighbors += 1
                if i + 1 < len(forklift_list_2d) and j - 1 >= 0 and forklift_list_2d[i + 1][j - 1] == "@":
                    num_neighbors += 1
                if i + 1 < len(forklift_list_2d) and j + 1 < len(forklift_list_2d[i]) and forklift_list_2d[i + 1][j + 1] == "@":
                    num_neighbors += 1                
                if num_neighbors < 4:
                    forklift_list_2d_updated[i][j] = "x"
                    num_removed += 1
        if forklift_list_2d == forklift_list_2d_updated:
            break
        forklift_list_2d = [row.copy() for row in forklift_list_2d_updated]
    print(num_removed)


if __name__ == "__main__":
    main()