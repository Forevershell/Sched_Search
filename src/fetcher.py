import json
import cmu_course_api
from cmu_course_api.parse_schedules import parse_schedules

def fetch(semester, outfile):
    print('Fetching...')
    data = parse_schedules(semester)

    with open(outfile, 'w') as file:
        json.dump(data, file)
    print('Cache fetch complete')
    return

def fetch_complete(semester, outfile):
    print('Fetching...')
    data = cmu_course_api.get_course_data(semester)
    with open(outfile, 'w') as file:
        json.dump(data, file)
    print('Cache fetch complete')
    return