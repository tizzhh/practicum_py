import hashlib


class MarsURLEncoder:
    def __init__(self):
        self.__links: dict[str, str] = {}

    def encode(self, long_url: str):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        short_url = (
            'https://ma.rs/'
            + hashlib.sha256(
                long_url.removeprefix('https://').encode('utf-8')
            ).hexdigest()
        )
        self.__links[short_url] = long_url
        return short_url

    def decode(self, short_url: str):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.__links[short_url]


test = MarsURLEncoder()
test.encode('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html')
print(test.__dict__)
