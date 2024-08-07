from datetime import datetime
from openpyxl import load_workbook, cell
# from .const import Part, SHEET_NAME
from const import Part, Span, Skills, SHEET_NAME, COLUMN_M


class Prompt:
    def __init__(self, file_path):
        self.sheet = (load_workbook(file_path))[SHEET_NAME]

    def get_info(self):
        read_range = self.sheet['B1': 'B144']
        return read_range

    def find_index(self, read_range):
        file_index = {
            Part.CERTIFICATION.value: [],
            Part.INTRODUCTION.value: [],
            Part.PROJECT.value: [],
            Part.SKILL.value: [],
        }
        index_name = list([name for name in list(file_index.keys())])
        start, end = 0, 0

        for idx, row in enumerate(read_range, 1):
            val = row[0].value
            if (val in index_name) or (idx == len(read_range)):
                if start != 0:
                    end = idx - 1
                    file_index[bf_val] = [start, end]
                start = idx
                bf_val = val
        return file_index

    def get_range_content(self, part, range):
        start, end = range
        range_content = self.sheet[f"B{start}": f"BY{end}"]
        if part == Part.CERTIFICATION.value:
            return self.read_certification(range_content)
        if part == Part.INTRODUCTION.value:
            return self.read_introduction(range_content)
        if part == Part.PROJECT.value:
            return self.read_project(range_content)
        if part == Part.SKILL.value:
            return self.read_skill(range_content)
    
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
    
    def read_introduction(self, range_content):
        ret = []

        for row in range_content:
            for col in row:
                if col.value == "\n": continue
                if col.value == Part.INTRODUCTION.value: continue
                if col.value is not None:
                    ret.append(col.value)

        ret = ret[0].split("\n")
        return ret
    
    def read_project(self, range_content):
        per_project_range = {} # {No.(num): [start, end]}
        experiences = {} # {title: [span], [project_contents]}
        num = 1
        start = None
        year, month  = None, None
        title = None

        # 欲しい情報: 期間, タイトル, 内容
        # eg. ret = {ttl: [span, contents]}
        # noで１案件の記述の長さを測る

        # 各プロジェクトの範囲取得
        for idx, row in enumerate(range_content):
            if idx == 0: continue
            if not isinstance(row[0], cell.Cell): continue
            if start is not None:
                end = idx
                if (end - start) > 1:
                    per_project_range[f"No.{num}"] = [start, end]
                    num += 1
                start = None
            start = idx

        # タイトル取得
        for item in list(per_project_range.values()):
            start, end = item
            title = (range_content[start:(end+1)][0][COLUMN_M]).value
            experiences[title] = [[], []]

        # 期間取得
        for key, item in zip(list(experiences.keys()), list(per_project_range.values())):
            start, end = item
            pass

        # 内容取得

        return experiences
    
    def read_skill(self, range_content):
        ret = {}
        ttl = None

        for row in range_content:
            for col in row:
                val = col.value
                bg_color = col.fill.fgColor.value

                if isinstance(col, cell.Cell):
                    if val is None: ttl = None
                if val is None: continue
                if bg_color != "00000000": continue

                if ttl is not None:
                    ret[ttl] = val
                    ttl = None
                else:
                    ttl = val
        return ret