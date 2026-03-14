class BaseTool:
    def __init__(self, name: str) -> None:
        self.name = name

    def execute(self, input_data):
        raise NotImplementedError

