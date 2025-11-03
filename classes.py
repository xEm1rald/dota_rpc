from dataclasses import dataclass, asdict


@dataclass
class ConfigGSIData:
    buildings: int = 0
    provider: int = 0
    map: int = 0
    player: int = 0
    hero: int = 0
    abilities: int = 0
    items: int = 0
    draft: int = 0
    wearables: int = 0

    def to_dict(self) -> dict:
        return {k: str(v) for k, v in asdict(self).items() if v == 1}


@dataclass
class ConfigGSI:
    uri: str
    data: ConfigGSIData
    timeout: float = 5.0
    buffer: float = 0.1
    throttle: float = 0.1
    heartbeat: float = 30.0

    def to_dict(self) -> dict:
        return {
            'uri': str(self.uri),
            'timeout': str(self.timeout),
            'buffer': str(self.buffer),
            'throttle': str(self.throttle),
            'heartbeat': str(self.heartbeat),
            'data': self.data.to_dict()
        }