from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    local_file_path : Path
    unzip_dir : Path