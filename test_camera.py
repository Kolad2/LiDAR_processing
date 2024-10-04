"""
Test the camera classes.
"""

import dataclasses
from itertools import product

import torch

from nerfstudio.cameras.cameras import Cameras, CameraType
from nerfstudio.cameras.rays import RayBundle



def test_orthophoto_camera():
    """Test that the orthographic camera model works."""
    c2w = torch.eye(4)[None, :3, :]
    # apply R and T.
    R = torch.Tensor(
        [
            [0.5, -0.14644661, 0.85355339],
            [0.5, 0.85355339, -0.14644661],
            [-0.70710678, 0.5, 0.5],
        ]
    ).unsqueeze(0)
    T = torch.Tensor([[0.5, 0, -0.5]])
    c2w[..., :3, :3] = R
    c2w[..., :3, 3] = T

    ortho_cam = Cameras(cx=1.5, cy=1.5, fx=1.0, fy=1.0, camera_to_worlds=c2w, camera_type=CameraType.ORTHOPHOTO)
    ortho_rays = ortho_cam.generate_rays(camera_indices=0)
    # campare with `PERSPECTIVE` to validate `ORTHOPHOTO`.
    pinhole_cam = Cameras(cx=1.5, cy=1.5, fx=1.0, fy=1.0, camera_to_worlds=c2w, camera_type=CameraType.PERSPECTIVE)
    pinhole_rays = pinhole_cam.generate_rays(camera_indices=0)

    assert ortho_rays.shape == pinhole_rays.shape
    # `ortho_rays.directions` should equal to the center ray of `pinhole_rays.directions`.
    assert torch.allclose(
        ortho_rays.directions, pinhole_rays.directions[1, 1].broadcast_to(ortho_rays.directions.shape)
    )
    # `ortho_rays.origins` should be grid points with a mean value of `pinhole_rays.origins`.
    assert torch.allclose(ortho_rays.origins.mean(dim=(0, 1)), pinhole_rays.origins[1, 1])



test_orthophoto_camera()