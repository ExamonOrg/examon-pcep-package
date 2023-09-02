from examon_core.examon_item_registry import ExamonItemRegistry
from examon_pcep_package.questions import *


class TestInputParameterQuestion:
    def test_repo(self):
        assert len(ExamonItemRegistry.registry()) == 43
