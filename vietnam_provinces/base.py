from enum import Enum
from typing import NamedTuple


class VietNamDivisionType(str, Enum):
    # Level 1
    TINH = 'tỉnh'
    THANH_PHO_TRUNG_UONG = 'thành phố trung ương'
    # Level 2
    HUYEN = 'huyện'
    QUAN = 'quận'
    THANH_PHO = 'thành phố'
    THI_XA = 'thị xã'
    # Level 3
    XA = 'xã'
    THI_TRAN = 'thị trấn'
    PHUONG = 'phường'


class BaseRegion(NamedTuple):
    name: str
    code: int
    division_type: VietNamDivisionType
    codename: str


class Ward(BaseRegion):
    district_code: int


class District(BaseRegion):
    province_code: int


class Province(BaseRegion):
    phone_code: int
