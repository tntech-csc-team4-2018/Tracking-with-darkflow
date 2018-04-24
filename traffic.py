import sys
def main():
    count = 0
    people = {}
    for line in sys.stdin:
        if "demo" in line:
            break
    for line in sys.stdin:
        if "Killed" in line or "exit" in line:
            break
        elif line != "\n":
            values = line.strip('[]\n').split(',')
            x = (int(values[2]) + int(values[4])+int(values[2])) / 2
            person = values[1]
            if person in people:
                if people[person] < 2048:
                    vel = x - people[person]
                else:
                    vel = 0
            else:
                vel = 0
            if x > 450 and vel > 0:
                count += 1
                x = 2048
            if person not in people:
                people[person] = x
                continue
            if people[person] < 2048:
                people[person] = x

    print str(count) + " visitors detected while running."

if __name__ == '__main__':
    main()
