from enum import Enum, IntEnum

# enum for payment target
class PaymentTargetEnum(str, Enum):
    event = "event"
    game = "game"
    microitem = "microitem"