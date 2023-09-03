from examon_core.in_memory_db import InMemoryDB
from examon_pcep_package.questions import *


class TestInputParameterQuestion:
    def test_repo(self):
        assert len(InMemoryDB.load()) == 43
