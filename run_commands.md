# Reference for running the simulation

## Run the image render requests

```sh
roslaunch flightrender drone_hil.launch quad_name:=camera_0 other_quad:=actor_0
```

## Show the images from the camera drone

### Remember to choose the correct topic - `camera_0/onboard_view/compressed`

```sh
rqt_image_view
```

## Run actor drone on rendering server

```sh
roslaunch agiros agisim.launch quad_name:=actor_0 simulation_config:=offboard_simulation.yaml is_server:=False
```

## Run camera drone on rendering server

```sh
roslaunch agiros agisim.launch quad_name:=camera_0 simulation_config:=kolibri_simulation.yaml is_server:=False
```