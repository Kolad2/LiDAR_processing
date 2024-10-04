from pathlib import Path
import json


from nerfstudio.utils.eval_utils import eval_setup
from nerfstudio.scripts import render
from nerfstudio.utils import colormaps, install_checks

from utils import get_path_from_json


class RenderOrthoCameraPath(render.RenderCameraPath):
	def main(self):
		_, pipeline, _, _ = eval_setup(
			self.load_config,
			eval_num_rays_per_chunk=self.eval_num_rays_per_chunk,
			test_mode="inference",
		)
		install_checks.check_ffmpeg_installed()
		with open(self.camera_path_filename, "r", encoding="utf-8") as f:
			camera_path = json.load(f)

		seconds = camera_path["seconds"]
		crop_data = render.get_crop_from_json(camera_path)
		camera_path = get_path_from_json(camera_path)

		if self.output_format == "video" and str(self.output_path.suffix) == "":
			self.output_path = self.output_path.with_suffix(".mp4")

		if self.camera_idx is not None:
			camera_path.metadata = {"cam_idx": self.camera_idx}

		render._render_trajectory_video(
			pipeline,
			camera_path,
			output_filename=self.output_path,
			rendered_output_names=self.rendered_output_names,
			rendered_resolution_scaling_factor=1.0 / self.downscale_factor,
			crop_data=crop_data,
			seconds=seconds,
			output_format=self.output_format,
			image_format=self.image_format,
			jpeg_quality=self.jpeg_quality,
			depth_near_plane=self.depth_near_plane,
			depth_far_plane=self.depth_far_plane,
			colormap_options=self.colormap_options,
			render_nearest_camera=self.render_nearest_camera,
			check_occlusions=self.check_occlusions,
		)