import json
from os import path
import sys
import fetcher
from scheduler import Scheduler

# SOURCES = os.path.join(os.path.commonpath, "/something")
SOURCES = path

def main():
    outfile = 'out.json'
    if not SOURCES.exists(outfile):
        print("Refetching cache")
        fetcher.fetch('S', outfile)

    inputs = set()
    total_courses = 0
    while True:
        course_no = input()
        if not course_no:
            break
        elif course_no.isnumeric():
            inputs.add(course_no)
            total_courses += 1
        else:
            print("Input has to be a course number")

    print(inputs)
    print(total_courses)
    sched = Scheduler(outfile)
    classes = sched.findClasses(inputs, outfile)
    print(classes)
    schedule = sched.findSchedules(classes)
    print(schedule)
    
    # return findCombinations(inputs)
    

if __name__ == "__main__":
    main()