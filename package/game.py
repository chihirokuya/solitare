from package.windows import main
from PyQt6.QtWidgets import *
from package.windows.dialog_package.dialog_open import open_dialog


class Game:
    left = "LEFT"
    right = "RIGHT"
    up = "UP"
    down = "DOWN"

    def __init__(self, ui: main.Ui_MainWindow):
        self.ui = ui

        self.field = [
            None, None, ui.pushButton_49, ui.pushButton_50, ui.pushButton_51, None, None,
            None, None, ui.pushButton_39, ui.pushButton_38, ui.pushButton_37, None, None,
            ui.pushButton_68, ui.pushButton_67, ui.pushButton_52, ui.pushButton_53, ui.pushButton_54, ui.pushButton_76, ui.pushButton_75,
            ui.pushButton_72, ui.pushButton_71, ui.pushButton_55, ui.pushButton_56, ui.pushButton_57, ui.pushButton_74, ui.pushButton_73,
            ui.pushButton_70, ui.pushButton_69, ui.pushButton_58, ui.pushButton_59, ui.pushButton_60, ui.pushButton_77, ui.pushButton_78,
            None, None, ui.pushButton_64, ui.pushButton_65, ui.pushButton_66, None, None,
            None, None, ui.pushButton_62, ui.pushButton_63, ui.pushButton_61, None, None
        ]

        base_style_sheet = """
        background-color: white;
        border-radius:20px;
        """

        self.filled = base_style_sheet + """
        background-color: rgb(120, 255, 125);
        """

        self.empty = base_style_sheet + """
        background-color:white;
        """

        self.empty_movable = self.empty + """
        background-color: rgba(215, 251, 255, 215);
        """

        self.focused = self.filled + """
        border: 2px solid  rgb(255, 161, 0);
        """

        self.is_focused = False

        for i in range(len(self.field)):
            if self.field[i]:
                self.field[i].clicked.connect(lambda checked, index=i: self.button_clicked(index))

        self.reset()

        ui.reset_button.clicked.connect(self.reset)

    @staticmethod
    def two_to_one(i, j):
        return i * 7 + j

    @staticmethod
    def one_to_two(m):
        i = m // 7

        j = m - i * 7

        return [i, j]

    def reset(self):
        for b in self.field:
            if b:
                b.setStyleSheet(self.filled)

        # 真ん中のみ白に
        self.field[self.two_to_one(3, 3)].setStyleSheet(self.empty)

    def get_movable_direction(self, index):
        [i, j] = self.one_to_two(index)
        res = []

        # 上
        if i - 2 > -1:
            if self.field[self.two_to_one(i - 1, j)] and self.field[self.two_to_one(i - 1, j)].styleSheet() == self.filled and \
                    self.field[self.two_to_one(i - 2, j)] and self.is_empty(self.two_to_one(i - 2, j)):
                res.append(self.up)

        # 下
        if i + 2 < 6:
            if self.field[self.two_to_one(i + 1, j)] and self.field[self.two_to_one(i + 1, j)].styleSheet() == self.filled and \
                    self.field[self.two_to_one(i + 2, j)] and self.is_empty(self.two_to_one(i + 2, j)):
                res.append(self.down)

        # 右
        if j + 2 < 6:
            if self.field[self.two_to_one(i, j + 1)] and self.field[self.two_to_one(i, j + 1)].styleSheet() == self.filled and \
                    self.field[self.two_to_one(i, j + 2)] and self.is_empty(self.two_to_one(i, j + 2)):
                res.append(self.right)

        # 左
        if j - 2 > -1:
            if self.field[self.two_to_one(i, j - 1)] and self.field[self.two_to_one(i, j - 1)].styleSheet() == self.filled and \
                    self.field[self.two_to_one(i, j - 2)] and self.is_empty(self.two_to_one(i, j - 2)):
                res.append(self.left)

        return res

    def is_empty(self, index):
        return self.field[index] and (self.field[index].styleSheet() == self.empty or self.field[index].styleSheet() == self.empty_movable)

    def is_focusable(self, index):
        """
        隣の隣が空いていればTrueを返す。
        :param index:
        :return: True if is checkable else False
        """
        # assert is not an empty circle
        if self.is_empty(index):
            return False

        return self.get_movable_direction(index)

    def set_focused(self, index):
        self.is_focused = True

        # 色が塗ってあるものをセット
        for i in range(len(self.field)):
            if i == index:
                self.field[i].setStyleSheet(self.focused)
                continue

            if self.field[i] and self.is_empty(index):
                self.field[i].setStyleSheet(self.filled)

        # 移動できるマスをマークアップ
        directions = self.get_movable_direction(index)
        [i, j] = self.one_to_two(index)

        for direction in directions:
            if direction == self.right:
                self.field[self.two_to_one(i, j + 2)].setStyleSheet(self.empty_movable)
            elif direction == self.left:
                self.field[self.two_to_one(i, j - 2)].setStyleSheet(self.empty_movable)
            elif direction == self.up:
                self.field[self.two_to_one(i - 2, j)].setStyleSheet(self.empty_movable)
            else:
                self.field[self.two_to_one(i + 2, j)].setStyleSheet(self.empty_movable)

    def set_unfocused(self):
        self.is_focused = False

        for i in range(len(self.field)):
            if not self.field[i]:
                continue

            if not self.is_empty(i):
                self.field[i].setStyleSheet(self.filled)
            elif self.field[i].styleSheet() == self.empty_movable:
                self.field[i].setStyleSheet(self.empty)

    def move(self, empty_index):
        if self.field[empty_index].styleSheet() != self.empty_movable:
            return

        focused_index = 0

        # search focused index
        for i in range(len(self.field)):
            if self.field[i] and self.field[i].styleSheet() == self.focused:
                focused_index = i
                break

        [f_i, f_j] = self.one_to_two(focused_index)
        [e_i, e_j] = self.one_to_two(empty_index)

        self.field[
            self.two_to_one(f_i, f_j - 1) if f_i == e_i and f_j > e_j else \
            self.two_to_one(f_i, f_j + 1) if f_i == e_i and f_j < e_j else \
            self.two_to_one(f_i - 1, f_j) if f_j == e_j and f_i > e_i else \
            self.two_to_one(f_i + 1, f_j)
        ].setStyleSheet(self.empty)
        self.field[empty_index].setStyleSheet(self.filled)
        self.field[focused_index].setStyleSheet(self.empty)

    def is_finished(self):
        filled_ind = 0
        for button in self.field:
            if button and button.styleSheet() == self.filled:
                if filled_ind == 1:
                    return False
                else:
                    filled_ind += 1

        return True

    def is_continuable(self):
        for i in range(len(self.field)):
            if self.field[i] and not self.is_empty(i) and self.is_focusable(i):
                return True

        return False

    def button_clicked(self, index):
        if self.is_focusable(index):
            self.set_unfocused()
            self.set_focused(index)
        else:
            if self.is_focused:
                self.move(index)

            self.set_unfocused()

            if self.is_finished():
                open_dialog('やったね！')
            elif not self.is_continuable():
                open_dialog('ざんねーーーん')
