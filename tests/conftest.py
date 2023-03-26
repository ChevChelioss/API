import os
import pytest
from dotenv import load_dotenv
from utils.base_session import BaseSession

load_dotenv()


@pytest.fixture(scope='session')
def reqres():
    return BaseSession(os.getenv("URL"))
