from pathlib import Path
from render_ortho_camera_path import RenderOrthoCameraPath

config_path = Path("outputs/poster/nerfacto/2024-10-03_195556/config.yml")
camera_path_filename = Path("data/nerfstudio/poster/camera_paths/cut_poster.json")


ren = RenderOrthoCameraPath(
	load_config=config_path,
	camera_path_filename=camera_path_filename,
	output_format="images"
)

ren.main()
