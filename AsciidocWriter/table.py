import pandas as pd

class Table():
    def __init__(self, name):
        self.name = name
        self.table = []

    def set_width(self, width="[%autowidth.stretch]"):
        return width

    def from_df(self, df:pd.DataFrame):

        self.table.append(f".{self.name}")              # Table Title
        self.table.append(self.set_width())             # Table Width
        self.table.append("|===")                       # Table Start

        self.table.append(f"|*{'*|*'.join(df.columns.values.tolist())}*")  # Table Columns
        for item in df.values.tolist():
            self.table.append(f"|{'|'.join(str(v) for v in item)}")

        self.table.append("|===")  # Table End


    def from_groupby(self, groupby, columns=None):

        self.table.append(f".{self.name}")              # Table Title
        self.table.append(self.set_width())             # Table Width
        self.table.append("|===")                       # Table Start

        keys = groupby.grouper.names
        for value, df in groupby:
            groups = dict(zip(keys, value))

            groupby_str = [f"*{k.upper()}* {groups[k]}" for k in groups]
            if columns:
                self.table.append(f"|*{'*|*'.join(columns)}*")                      # Table Columns
                self.table.append(f"{len(columns)}+| {' -- '.join(groupby_str)}")   # GroupBy Header
                for item in df[columns].values.tolist():
                    self.table.append(f"|{'|'.join(str(v) for v in item)}")         # GroupBy Row
            else:
                self.table.append(f"|*{'*|*'.join(df.columns.values.tolist())}*")   # Table Columns
                self.table.append(f"{len(df.columns.values.tolist())-len(keys)}+| {' -- '.join(groupby_str)}")  # GroupBy Header
                for item in df.values.tolist():
                    self.table.append(f"|{'|'.join(str(v) for v in item)}")         # GroupBy Row

        self.table.append("|===")  # Table End
