from typing import Text

def infer_shapes(b: bytes, check_type: bool) -> bytes: ...

def infer_shapes_path(model_path: Text, output_path: Text, check_type: bool) -> None: ...
