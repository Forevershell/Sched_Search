import urllib.request
import urllib.parse
import re
import bs4
import time

DESC_URL = "https://enr-apps.as.cmu.edu/open/SOC/SOCServlet/courseDetails"

def get_page(url):
    try:
        response = urllib.request.urlopen(url)
    except (urllib.request.URLError, ValueError):
        return None

    return bs4.BeautifulSoup(response.read(), 'html.parser')

def parse_lect_sess(soup, num, semester):
    # Result set
    result = dict()
    # Regex used to find Lecture
    lec_reg = re.compile("Lec.*")
    # Using find params to determine where the section table is and find it
    find_params   = {'data-subtitle': semester, 'data-maintitle' : re.compile(num + "\w*")}
    section_table = soup.find(attrs = find_params).table
    # Retrieve header from section table
    raw_head      = section_table.thead.find_all('th')
    # Encode each header with its index
    encoded_head  = dict()
    for i in range(len(raw_head)):
        encoded_head[raw_head[i].string] = i

    lec_name = ''
    for row in section_table.tbody.find_all('tr'):
        row_extract  = row.find_all('td')
        section_name = row_extract[encoded_head['Section']].string
        if section_name:
            if lec_reg.match(section_name):
                lec_name = section_name
            else:
                result[lec_name] = result.get(lec_name, [])
                result[lec_name].append(section_name)
    print(result)
    return result


def get_lect_sess(num, semester):
    # Profiling
    time_0 = time.time()
    params = {
        'COURSE': num,
        'SEMESTER': semester.split(' ')[0][0] + semester.split(' ')[1][2:]
    }
    url = DESC_URL + '?' + urllib.parse.urlencode(params)
    # Profiling get_page
    soup = get_page(url)
    time_1 = time.time()
    # print("Phase 1", time_1 - time_0)
    # Profiling parse_lect_sess
    return parse_lect_sess(soup, num, semester)
    # time_2 = time.time()
    # print("Phase 2", time_2 - time_1)
    # # Final Profile
    # print("Phase 3", time.time() - time_0)


get_lect_sess("15112", "Spring 2021")