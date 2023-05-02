def main():
    file = open("Solution_data.csv", "r")
    lines = file.readlines()
    file.close()
    new_lines = []
    for line in lines:
        new_lines.append(line.replace(' ', ','))
    file = open("Formatted_solution_data.csv", "w")
    for line in new_lines:
        file.write(line)


if __name__ == "__main__":
    main()