from PyQt6.QtCore import QAbstractTableModel, Qt

class LeaderBoardModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self._data = []

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return 3  # rank, name, score

    def data(self, index, role):

        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:

            row = index.row()
            col = index.column()

            name, score = self._data[row]

            if col == 0:
                return row + 1
            elif col == 1:
                return name
            elif col == 2:
                return score

        return None

    def headerData(self, section, orientation, role):

        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:

            headers = ["Rank", "Name", "Score"]
            return headers[section]

    def update_data(self, data):

        self.beginResetModel()
        self._data = data
        self.endResetModel()