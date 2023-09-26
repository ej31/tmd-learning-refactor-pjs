from src.game_status import GameStatusEnum
from src.menu_view import MenuView
from src.word_model import WordModel


class WordController:

    def __init__(self):
        self.word_model = WordModel()

    @staticmethod
    def game_status(word):
        if word == GameStatusEnum.GAME_EXIT.value:
            MenuView.print_exit()
            return GameStatusEnum.GAME_EXIT

    @staticmethod
    def get_word_v2(word):
        return str(input(f"이전 키워드는 {word} 입니다. '{word[-1]}'로 시작되는 단어를 입력해주세요"))

    @staticmethod
    def get_user_a():
        return str(input("첫 번째 플레이어 이름을 입력해주세요"))

    @staticmethod
    def get_user_b():
        return str(input("두 번째 플레이어 이름을 입력해주세요"))

    @staticmethod
    def get_word():
        return str(input("단어를 입력하세요: "))

    def word_checker(self, word):
        return self.word_model.word_checker(word=word)

    def setting_up_next_phase(self, word):
        return self.word_model.setting_up_next_phase(word)

    def add_score(self, player_name, player_score):
        return self.word_model.add_score(player_name, player_score)
