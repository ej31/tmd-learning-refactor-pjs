class WordModel:
    def __init__(self):
        self.last_cha = ""
        self.word_list = [""]  # 입력한 단어를 모으는 리스트, 이전에 나왔던 단언인지 확인하기 위함이다.
        self.korean_alphabet = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㅐㅒㅔㅖㅘㅙㅚㅝㅞㅟㅢ"

    def setting_up_next_phase(self, word):
        """
        올바른 단어를 입력했으므로 다음 차례를 준비함
        :param word: 사용자가 입력한 단어
        """
        self.word_list.append(word)
        self.last_cha = word[-1]

    def word_checker(self, word):
        if not self.compare_end_first(word):
            print(f"잘못된 단어를 입력하셨습니다. 전 순서의 끝말과 현재 순서의 첫말이 다릅니다. (현재 마지막 글자 {word[-1]}) 다시 입력해주세요!")
            return 100
        elif not self.came_out_before(word):
            print(f"이미 나온 단어를 입력하셨습니다. (현재까지 나온 단어 리스트 마지막 글자 목록입니다.")
            print(f"{self.word_list}")
            return 200
        elif not self.determine_korean(word):
            return 300
        elif not self.is_under_10(word):
            return 400
        elif self.invalid_word(word) is True:
            return 500

    def determine_korean(self, word):
        """
        1. isalpha()를 통해 한글, 영어만 남고 특수문자, 숫자, 띄어쓰기는 걸러진다.
        2. 한글과 영어만 남아있는 상황에서 isascii()가 False인 경우이므로 영어도 걸러진다.
        1과 2의 과정을 거치면 한글만 남게 된다.
        """
        if (word.isalpha() is True) and (word.isascii() is False):
            return True
        else:
            return False

    def is_under_10(self, word):
        # 글자수를 10 이하로 설정하는 코드
        if len(word) <= 10:
            return True
        else:
            return False

    def came_out_before(self, word):
        """
        나왔던 단어들은 word_list에 append해서
        게임에서 순서가 넘어갈때마다 확인할 예정
        """
        if word not in self.word_list:
            return True
        else:
            return False

    def compare_end_first(self, word):
        # 전 순서의 끝말과 현재 순서의 첫말이 같은지를 판단하는 코드
        if self.last_cha == word[0]:
            return True
        else:
            return False

    def invalid_word(self, word):
        """
        소ㄴ기", "역ㅏ동" 같이 글자에 자음만 혹은 모음만 있은 경우를 걸러내기 위한 조건
        """
        for i in range(len(word)):
            if word[i] in self.korean_alphabet:
                return False

    def first_condition(self, word):
        """
        self.num = 1 일 때의 if문에 쓰이는 조건.
        첫 번째 순서이기 때문에 끝말과 첫글자가 일치해야 하는 조건과
        이전에 나왔던 단어인지를 확인하는 조건은 포함되지 않는다.
        """
        return (self.determine_korean(word)) and (self.is_under_10(word)) and (self.invalid_word(word) != False)

    def word_validator(self, word):
        """
        self.num이 1보다 클 때 if문에 쓰이는 조건.
        전 단어의 끝말과 입력 단어의 첫 말이 같은지,
        이전에 나왔던 단어인지,
        한국어만 허용되는지,
        글자수가 10보다 작은지,
        유효하지 않은 단어인지
        위의 조건들을 판단하여 규정에 옳은 단어일때만 True를 반환한다.
        """
        return (self.compare_end_first(word)) and (self.came_out_before(word)) and (self.determine_korean(word)) and (
            self.is_under_10(word)) and (self.invalid_word(word) is False)
