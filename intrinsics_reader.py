from __future__ import annotations

from pathlib import Path
from typing import Tuple

import yaml
from pydantic import BaseModel


BASE_PATH = Path(__file__).parent
INTRINSICS_FILE_PATH = BASE_PATH / "intrinsics.yaml"


class CameraModel(BaseModel):
    xi: float
    alpha: float
    fu: float
    fv: float
    pu: float
    pv: float
    resolution: Tuple[int, int]

    @staticmethod
    def from_yaml(yaml_path: Path) -> CameraModel:
        with yaml_path.open() as yaml_stream:
            parsed_yaml = yaml.safe_load(yaml_stream)

            xi, alpha, fu, fv, pu, pv = parsed_yaml["cam0"]["intrinsics"]
            resolution = parsed_yaml["cam0"]["resolution"]

            return CameraModel(
                xi=xi,
                alpha=alpha,
                fu=fu,
                fv=fv,
                pu=pu,
                pv=pv,
                resolution=resolution
            )
    

camera_model = CameraModel.from_yaml(INTRINSICS_FILE_PATH)
print(camera_model)
