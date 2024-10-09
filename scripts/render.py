from pathlib import Path
from render_ortho_camera_path import RenderOrthoCameraPath
from nerfstudio.utils import colormaps
from dataclasses import dataclass, field
from nerfstudio.scripts.render import RenderCameraPath

config_path = Path("outputs/poster/nerfacto/2024-10-07_162639/config.yml")
camera_path_filename = Path("data/nerfstudio/poster/camera_paths/cut_2.json")

colormap = colormaps.ColormapOptions(
	colormap="gray",
	colormap_min=0,
	colormap_max=1,
	normalize=True
)

RenderOrthoCameraPath(
	load_config=config_path,
	camera_path_filename=camera_path_filename,
	output_format="images", #"video"
	rendered_output_names=["rgb", "depth"],
	colormap_options=colormap,
	output_path=Path("renders/output_ortho.mp4"),
	depth_far_plane=100,
	depth_near_plane=0
).main()

RenderCameraPath(
	load_config=config_path,
	camera_path_filename=camera_path_filename,
	output_format="images", #"video"
	rendered_output_names=["rgb", "depth"],
	colormap_options=colormap,
	output_path=Path("renders/output_perspective.mp4"),
	depth_far_plane=100,
	depth_near_plane=0
).main()

#
#rendered_output_names=field(default_factory=lambda: ["depth"])