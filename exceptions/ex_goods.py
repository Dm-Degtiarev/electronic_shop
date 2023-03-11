class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else f'Файл поврежден'

    def __str__(self):
        return self.message