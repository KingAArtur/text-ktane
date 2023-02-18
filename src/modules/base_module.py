class BombModule:
    disarmed: bool = False

    def disarm(self):
        self.disarmed = True

    @classmethod
    def create(cls, *args) -> 'BombModule':
        pass

    def show(self) -> str:
        pass

    def guess(self, s: str) -> bool:
        pass
