from empire_config import empire_config
from rebel_config import rebel_config
from republic_config import republic_config
from separatist_config import separatist_config
from mercenary_config import mercenary_config
from constants import PROBABILITY_UNIT, UNLIMITED_TOKENS

unit_config = {
    **empire_config,
    **rebel_config,
    **republic_config,
    **separatist_config,
    **mercenary_config
}
