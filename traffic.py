import sys
import MySQLdb
import time
def main():
    ENTRANCE = 100
    EXIT = 500
    incount = 0
    outcount = 0
    lastquery = 0
    people = {}
    connection = MySQLdb.connect(
        host="visitorinfo.cor4qvbqsu7p.us-east-2.rds.amazonaws.com",
        user="atdao42",
        passwd="X5ujNkX8DG",
        db="visitor_info")
    cursor=connection.cursor()
    for line in sys.stdin:
        if "demo" in line:
            break
    for line in sys.stdin:
        if "Killed" in line or "exit" in line:
            break
        elif line != "\n":
            values = line.strip('[]\n').split(',')
            if len(values) < 5: 
                break
            x = (int(values[2]) + int(values[4])+int(values[2])) / 2
            person = values[1]
            if person in people:
                if people[person] < 2048:
                    vel = x - people[person]
                else:
                    vel = 0
            else:
                people[person] = x
                continue
            if x > EXIT and vel > 0:
                outcount += 1
                x = 2048
            elif x < ENTRANCE and vel < 0:
                incount += 1
                x = 2048
            if people[person] < 2048:
                people[person] = x
            if time.localtime().tm_min == 0 and last_query != time.localtime().tm_hour:
                now = time.localtime()
                date = "{0}-{1}-{2}".format(now.tm_year,now.tm_mon,now.tm_mday)
                hour = now.tm_hour - 1
                query = "INSERT INTO GuestsPerHour VALUES({0}, {1}, {2}, {3})".format(date,hour,incount,outcount)
                cursor.execute(query)
                db.commit()
                incount = 0
                outcount = 0
                people = {}
                last_query = now.tm_hour
                if now.tm_hour == 18:
                    break
    connection.close()
    #print str(incount) + " visitors detected while running."
    #print str(outcount) + " leaving visitors detected."

if __name__ == '__main__':
    main()
