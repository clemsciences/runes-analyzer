

from enum import Enum


class AutoName(Enum):
    def _generate_next_value_(name, a, b, d):
        return name
