import pytest
from pyi18n_new import I18N

from pathlib import Path


BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / "locales"


@pytest.fixture()
def i18n():
    return I18N(path=LOCALES_DIR, default="ru")


@pytest.fixture()
def _():
    return I18N(path=LOCALES_DIR, default="ru", fallback="en").translate


@pytest.fixture()
def __():
    return I18N(path=LOCALES_DIR, default="ru", fallback="en")


@pytest.fixture()
def __en():
    return I18N(path=LOCALES_DIR, default="en")
