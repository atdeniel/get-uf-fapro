from pydantic import BaseSettings

class Settings(BaseSettings):

    SII_BASE_UF_YEAR_URL = 'https://www.sii.cl/valores_y_fechas/uf/uf'
    SII_BASE_UF_YEAR_URL_EXTENSION = '.htm'


    def get_sii_uf_year_url(self, year: str):
        return f'{self.SII_BASE_UF_YEAR_URL}{year}{self.SII_BASE_UF_YEAR_URL_EXTENSION}'


setting = Settings()