from pathlib import Path
from render_ortho_camera_path import RenderOrthoCameraPath

config_path = Path("../outputs/poster/nerfacto/2024-10-07_162639/config.yml")
camera_path_filename = Path("../data/nerfstudio/poster/camera_paths/cut_1.json")


ren = RenderOrthoCameraPath(
	load_config=config_path,
	camera_path_filename=camera_path_filename,
	output_format="video"
)

ren.main()
