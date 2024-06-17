import openpyxl
# from .const import Part, SHEET_NAME
from const import Part, SHEET_NAME


class Prompt:
    def __init__(self, file_path):
        self.sheet = (openpyxl.load_workbook(file_path))[SHEET_NAME]
        self.file_index = {
            Part.CERTIFICATION.value: [],
            Part.INTRODUCTION.value: [],
            Part.PROJECT.value: [],
            Part.SKILL.value: [],
        }

    def get_file_index(self):
        read_range = self.sheet['B1': 'B144']
        return read_range

    def find_dict_name(self, read_range):
        index_name = list([name for name in list(self.file_index.keys())])
        start, end = 0, 0

        for idx, row in enumerate(read_range, 1):
            val = row[0].value
            if (val in index_name) or (idx == len(read_range)):
                if start != 0:
                    end = idx - 1
                    self.file_index[bf_val] = [start, end]
                start = idx
                bf_val = val

    def get_range_content(self, part, range):
        start, end = range
        range_content = self.sheet[f"B{start}": f"BY{end}"]
        if part == Part.CERTIFICATION.value:
            return self.read_certification(range_content)
        if part == Part.INTRODUCTION.value:
            pass
        if part == Part.PROJECT.value:
            pass
        if part == Part.SKILL.value:
            pass
    
    def read_certification(self, range_content):
        ret = []
        cnt = 0

        for row in range_content:
            for idx, cell in enumerate(row):
                if idx == 0: continue
                if cell.value == None: continue
                if cnt % 5 == 0:
                    if cell.value == "年": break
                    ret.append(cell.value)
                cnt += 1
        return ret