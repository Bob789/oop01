from datetime import datetime

class Timer:

    def __init__(self, name: str, duration: int):
        print('new instance created',__class__)
        self._name = name
        self._duration = duration
        self._started_at = datetime.now()

    def __str__(self) -> str:
        return f"Timer '{self._name}' set for {self._duration} minutes (started at: {self._started_at.strftime('%H:%M:%S')})"

    def __repr__(self):
        return f"Timer('{self._name}', {self._duration})"

    def __del__(self):
        print(self._name,' ', float((datetime.now() - self._started_at).total_seconds()))
        print(f"Goodbye {self._name}")

