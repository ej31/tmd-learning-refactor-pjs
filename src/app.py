from src.game_status import GameStatusEnum
from word_ctrl import WordController


class Application:
    # 유저 이름 받고 단어 받고 검증하고 점수 계산하고
    def __init__(self):
        self.word_ctrl = WordController()
        self.player_1_score = 0  # 플레이어1의 누적점수
        self.player_2_score = 0  # 플레이어2의 누적점수
        self.player_number = 3  # play 메소드에서 플레이어1,2의 누적점수를 넣을때 순서를 구분하기 위해 쓸 변수

    def execute(self):
        # 유저에게 입력을 받는 부분
        user_a = self.word_ctrl.get_user_a()
        user_b = self.word_ctrl.get_user_b()
        user_list = [user_a, user_b]

        while True:
            word = self.word_ctrl.get_word()
            if self.word_ctrl.game_status(word) == GameStatusEnum.GAME_EXIT:
                # "종료" 입력받은 경우 프로그램 종료
                break

            if self.player_number % 2 == 1:  # 첫 번째 플레이어
                print(f"[게임진행] 플레이어 {user_list[self.player_number % 2]} 차례 입니다.")
                _tmp_word = self.word_ctrl.get_word_v2(word)
                _score = self.word_ctrl.word_checker(_tmp_word)
                if _score is not None:
                    self.player_1_score -= _score
                    continue
                self.word_ctrl.setting_up_next_phase(word)
                self.player_1_score += 50
                self.player_number += 1

            elif self.player_number % 2 == 0:  # 두 번째 플레이어 (홀수)
                print("[게임진행] 두 번째 플레이어 차례 입니다.")
                _tmp_word = self.word_ctrl.get_word_v2(word)
                _score = self.word_ctrl.word_checker(_tmp_word)
                if _score is not None:
                    self.player_2_score -= _score
                    continue
                self.word_ctrl.setting_up_next_phase(word)
                self.player_2_score += 50
                self.player_number += 1

                print(f"현재단어: {word}")
                print(f"플레이어1 점수: {self.player_1_score}")
                print(f"플레이어2 점수: {self.player_2_score}")


if __name__ == '__main__':
    Application().execute()
