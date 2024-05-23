class JujeobRepository:
    def __init__(self, name):
        self._name = name

    @property
    def ONE(self):
        return f'''{self._name}아 그거 알아? 사람이 너무 예쁜걸 보면 단기 기억상실증에 걸린대..\n
{self._name}아 그거 알아? 사람이 너무 예쁜걸 보면 단기 기억상실증에 걸린대..\n
{self._name}아 그거 알아?'''

    @property
    def TWO(self):
            return f'''{self._name}이 너무 귀여워서 벽 치다가 우리집 원룸 됐다
못 참겠어서 계속 치니까 옆집 벽도 무너져서 옆집 사람들이랑 인사함ㅠ'''

    @property
    def THREE(self):
        return f'''{self._name}왜 매일 미모 기록을 경신하지? 매일 목표가 과거의 나를 이기기 뭐 그런거야?
너의 미모는 왜 근로기준 주 52시간을 지키지 않고 일 하는거냔 말야
월화수목금토일 아침 점심 저녁으로 항상 예쁘면 어떡해...?'''

    @property
    def FOUR(self):
        return f'''{self._name}은(는) 린스 안써도 되겠다 나만의 프린스니까...'''

    @property
    def FIVE(self):
        return f'''{self._name}아(가) 너 혹시 MBTI가 CUTE니?'''