import json
import copy
import parser

class Scheduler:
    def __init__(self, outfile):
        with open(outfile, 'r') as file:
            self.cache = json.load(file)

    def findClasses(self, inputs, outfile):
        class_list = []
        for cl in self.cache['schedules']:
            if cl['num'] in inputs:
                class_list.append(cl)
        return class_list

    def findSchedules(self, class_list):
        schedules = []
        self.__recurseFind(schedules, [], copy.copy(class_list))
        return schedules

    def __recurseFind(self, schedules, section_list, class_list):
        # finding which class to add all the stuff in
        if len(class_list) == 0:
            schedules.append(section_list)
        else:
            cl = class_list[0]
            for section in cl['lectures']:
                if not __checkConflict(section_list, section):
                    # if there are no time conflicts
                    section_list.append(section)
                    class_temp = copy(class_list)
                    class_temp.pop(0)
                    result = __recurseFind(schedules, section_list, class_temp)
            return

    def __checkConflict(self, section_list, section):
        for section in section_list:
            for time in time_list:
                return False
        return True
        

        
# findClasses([], 'out.json')