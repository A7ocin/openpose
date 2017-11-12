from gflags import *
from glog import *
from google.apputils import app
import sys
import cv2 as cv
import time

sys.path.insert(0, 'windows/1_user_asynchronous_output')

import UserClasses as UserClasses
import PyOPUAO as PyOP

DEFINE_integer('logging_level', 3, "The logging level. Integer in the range [0, 255]. 0 will output any log() message, while"
	" 255 will not output any. Current OpenPose library messages are in the range 0-4: 1 for"
	" low priority messages and 4 for important ones.");
# Producer
DEFINE_integer('camera', -1, "The camera index for cv::VideoCapture. Integer in the range [0, 9]. Select a negative"
	" number (by default), to auto-detect and open the first available camera.");
DEFINE_string('camera_resolution', "1280x720", "Size of the camera frames to ask for.");
DEFINE_float('camera_fps', 30.0, "Frame rate for the webcam (only used when saving video from webcam). Set this value to the"
	" minimum value between the OpenPose displayed speed and the webcam real frame rate.");
DEFINE_string('video', "", "Use a video file instead of the camera. Use `examples/media/video.avi` for our default"
	" example video.");
DEFINE_string('image_dir', "", "Process a directory of images. Use `examples/media/` for our default example folder with 20"
	" images. Read all standard formats (jpg, png, bmp, etc.).");
DEFINE_string('ip_camera', "", "String with the IP camera URL. It supports protocols like RTSP and HTTP.");
DEFINE_integer('frame_first', 0, "Start on desired frame number. Indexes are 0-based, i.e. the first frame has index 0.");
DEFINE_integer('frame_last', -1, "Finish on desired frame number. Select -1 to disable. Indexes are 0-based, e.g. if set to"
	" 10, it will process 11 frames (0-10).");
DEFINE_bool('frame_flip', False, "Flip/mirror each frame (e.g. for real time webcam demonstrations).");
DEFINE_integer('frame_rotate', 0, "Rotate each frame, 4 possible values: 0, 90, 180, 270.");
DEFINE_bool('frames_repeat', False, "Repeat frames when finished.");
DEFINE_bool('process_real_time', False, "Enable to keep the original source frame rate (e.g. for video). If the processing time is"
	" too long, it will skip frames. If it is too fast, it will slow it down.");
# OpenPose
DEFINE_string('model_folder', "models/", "Folder path (absolute or relative) where the models (pose, face, ...) are located.");
DEFINE_string('output_resolution', "-1x-1", "The image resolution (display and output). Use \"-1x-1\" to force the program to use the"
	" input image resolution.");
DEFINE_integer('num_gpu', -1, "The number of GPU devices to use. If negative, it will use all the available GPUs in your"
	" machine.");
DEFINE_integer('num_gpu_start', 0, "GPU device start number.");
DEFINE_integer('keypoint_scale', 0, "Scaling of the (x,y) coordinates of the final pose data array, i.e. the scale of the (x,y)"
	" coordinates that will be saved with the `write_keypoint` & `write_keypoint_json` flags."
	" Select `0` to scale it to the original source resolution, `1`to scale it to the net output"
	" size (set with `net_resolution`), `2` to scale it to the final output size (set with"
	" `resolution`), `3` to scale it in the range [0,1], and 4 for range [-1,1]. Non related"
	" with `scale_number` and `scale_gap`.");
# OpenPose Body Pose
DEFINE_bool('body_disable', False, "Disable body keypoint detection. Option only possible for faster (but less accurate) face"
	" keypoint detection.");
DEFINE_string('model_pose', "COCO", "Model to be used. E.g. `COCO` (18 keypoints), `MPI` (15 keypoints, ~10% faster), "
	"`MPI_4_layers` (15 keypoints, even faster but less accurate).");
DEFINE_string('net_resolution', "656x368", "Multiples of 16. If it is increased, the accuracy potentially increases. If it is"
	" decreased, the speed increases. For maximum speed-accuracy balance, it should keep the"
	" closest aspect ratio possible to the images or videos to be processed. Using `-1` in"
	" any of the dimensions, OP will choose the optimal aspect ratio depending on the user's"
	" input value. E.g. the default `-1x368` is equivalent to `656x368` in 16:9 resolutions,"
	" e.g. full HD (1980x1080) and HD (1280x720) resolutions.");
DEFINE_integer('scale_number', 1, "Number of scales to average.");
DEFINE_float('scale_gap', 0.3, "Scale gap between scales. No effect unless scale_number > 1. Initial scale is always 1."
	" If you want to change the initial scale, you actually want to multiply the"
	" `net_resolution` by your desired initial scale.");
DEFINE_bool('heatmaps_add_parts', False, "If true, it will add the body part heatmaps to the final op::Datum::poseHeatMaps array,"
	" and analogously face & hand heatmaps to op::Datum::faceHeatMaps & op::Datum::handHeatMaps"
	" (program speed will decrease). Not required for our library, enable it only if you intend"
	" to process this information later. If more than one `add_heatmaps_X` flag is enabled, it"
	" will place then in sequential memory order: body parts + bkg + PAFs. It will follow the"
	" order on POSE_BODY_PART_MAPPING in `include/openpose/pose/poseParameters.hpp`.");
DEFINE_bool('heatmaps_add_bkg', False, "Same functionality as `add_heatmaps_parts`, but adding the heatmap corresponding to"
	" background.");
DEFINE_bool('heatmaps_add_PAFs', False, "Same functionality as `add_heatmaps_parts`, but adding the PAFs.");
DEFINE_integer('heatmaps_scale', 2, "Set 0 to scale op::Datum::poseHeatMaps in the range [0,1], 1 for [-1,1]; and 2 for integer"
	" rounded [0,255].");
# OpenPose Face
DEFINE_bool('face', False, "Enables face keypoint detection. It will share some parameters from the body pose, e.g."
	" `model_folder`. Note that this will considerable slow down the performance and increse"
	" the required GPU memory. In addition, the greater number of people on the image, the"
	" slower OpenPose will be.");
DEFINE_string('face_net_resolution', "368x368", "Multiples of 16 and squared. Analogous to `net_resolution` but applied to the face keypoint"
	" detector. 320x320 usually works fine while giving a substantial speed up when multiple"
	" faces on the image.");
# OpenPose Hand
DEFINE_bool('hand', False, "Enables hand keypoint detection. It will share some parameters from the body pose, e.g."
	" `model_folder`. Analogously to `--face`, it will also slow down the performance, increase"
	" the required GPU memory and its speed depends on the number of people.");
DEFINE_string('hand_net_resolution', "368x368", "Multiples of 16 and squared. Analogous to `net_resolution` but applied to the hand keypoint"
	" detector.");
DEFINE_integer('hand_scale_number', 1, "Analogous to `scale_number` but applied to the hand keypoint detector. Our best results"
	" were found with `hand_scale_number` = 6 and `hand_scale_range` = 0.4");
DEFINE_float('hand_scale_range', 0.4, "Analogous purpose than `scale_gap` but applied to the hand keypoint detector. Total range"
	" between smallest and biggest scale. The scales will be centered in ratio 1. E.g. if"
	" scaleRange = 0.4 and scalesNumber = 2, then there will be 2 scales, 0.8 and 1.2.");

DEFINE_bool('hand_tracking', False, "Adding hand tracking might improve hand keypoints detection for webcam (if the frame rate"
	" is high enough, i.e. >7 FPS per GPU) and video. This is not person ID tracking, it"
	" simply looks for hands in positions at which hands were located in previous frames, but"
	" it does not guarantee the same person ID among frames");
# OpenPose Rendering
DEFINE_integer('part_to_show', 0, "Prediction channel to visualize (default: 0). 0 for all the body parts, 1-18 for each body"
	" part heat map, 19 for the background heat map, 20 for all the body part heat maps"
	" together, 21 for all the PAFs, 22-40 for each body part pair PAF");
DEFINE_bool('disable_blending', False, "If enabled, it will render the results (keypoint skeletons or heatmaps) on a black"
	" background, instead of being rendered into the original image. Related: `part_to_show`,"
	" `alpha_pose`, and `alpha_pose`.");
# OpenPose Rendering Pose
DEFINE_float('render_threshold', 0.05, "Only estimated keypoints whose score confidences are higher than this threshold will be"
	" rendered. Generally, a high threshold (> 0.5) will only render very clear body parts;"
	" while small thresholds (~0.1) will also output guessed and occluded keypoints, but also"
	" more false positives (i.e. wrong detections).");
DEFINE_integer('render_pose', 2, "Set to 0 for no rendering, 1 for CPU rendering (slightly faster), and 2 for GPU rendering"
	" (slower but greater functionality, e.g. `alpha_X` flags). If rendering is enabled, it will"
	" render both `outputData` and `cvOutputData` with the original image and desired body part"
	" to be shown (i.e. keypoints, heat maps or PAFs).");
DEFINE_float('alpha_pose', 0.6, "Blending factor (range 0-1) for the body part rendering. 1 will show it completely, 0 will"
	" hide it. Only valid for GPU rendering.");
DEFINE_float('alpha_heatmap', 0.7, "Blending factor (range 0-1) between heatmap and original frame. 1 will only show the"
	" heatmap, 0 will only show the frame. Only valid for GPU rendering.");
# OpenPose Rendering Face
DEFINE_float('face_render_threshold', 0.4, "Analogous to `render_threshold`, but applied to the face keypoints.");
DEFINE_integer('face_render', -1, "Analogous to `render_pose` but applied to the face. Extra option: -1 to use the same"
	" configuration that `render_pose` is using.");
DEFINE_float('face_alpha_pose', 0.6, "Analogous to `alpha_pose` but applied to face.");
DEFINE_float('face_alpha_heatmap', 0.7, "Analogous to `alpha_heatmap` but applied to face.");
# OpenPose Rendering Hand
DEFINE_float('hand_render_threshold', 0.2, "Analogous to `render_threshold`, but applied to the hand keypoints.");
DEFINE_integer('hand_render', -1, "Analogous to `render_pose` but applied to the hand. Extra option: -1 to use the same"
	" configuration that `render_pose` is using.");
DEFINE_float('hand_alpha_pose', 0.6, "Analogous to `alpha_pose` but applied to hand.");
DEFINE_float('hand_alpha_heatmap', 0.7, "Analogous to `alpha_heatmap` but applied to hand.");
# Result Saving
DEFINE_string('write_images', "", "Directory to write rendered frames in `write_images_format` image format.");
DEFINE_string('write_images_format', "png", "File extension and format for `write_images`, e.g. png, jpg or bmp. Check the OpenCV"
	" function cv::imwrite for all compatible extensions.");
DEFINE_string('write_video', "", "Full file path to write rendered frames in motion JPEG video format. It might fail if the"
	" final path does not finish in `.avi`. It internally uses cv::VideoWriter.");
DEFINE_string('write_keypoint', "", "Directory to write the people body pose keypoint data. Set format with `write_keypoint_format`.");
DEFINE_string('write_keypoint_format', "yml", "File extension and format for `write_keypoint`: json, xml, yaml & yml. Json not available"
	" for OpenCV < 3.0, use `write_keypoint_json` instead.");
DEFINE_string('write_keypoint_json', "", "Directory to write people pose data in *.json format, compatible with any OpenCV version.");
DEFINE_string('write_coco_json', "", "Full file path to write people pose data with *.json COCO validation format.");
DEFINE_string('write_heatmaps', "", "Directory to write body pose heatmaps in *.png format. At least 1 `add_heatmaps_X` flag"
	" must be enabled.");
DEFINE_string('write_heatmaps_format', "png", "File extension and format for `write_heatmaps`, analogous to `write_images_format`."
	" Recommended `png` or any compressed and lossless format.");

def main(argv):
    print("Starting pose estimation demo.")

    PyOP.initialize(int(FLAGS.logging_level), FLAGS.output_resolution, FLAGS.net_resolution, FLAGS.face_net_resolution, FLAGS.hand_net_resolution, FLAGS.image_dir, FLAGS.video, FLAGS.ip_camera, int(FLAGS.camera), FLAGS.camera_resolution, int(FLAGS.camera_fps), FLAGS.model_pose, int(FLAGS.keypoint_scale), bool(FLAGS.heatmaps_add_parts), bool(FLAGS.heatmaps_add_bkg), bool(FLAGS.heatmaps_add_PAFs), bool(FLAGS.heatmaps_scale))
    
    start = time.time()

    while(PyOP.PyOP()):
        print("-----------------------------------------------------------------------------------")

        print("\nKeypoints:")
		#Accesing each element of the keypoints
        poseKeypoints = PyOP.getDatum().poseKeypoints

        # FROM THE NEXT INSTRUCTION ON, IT DOESN'T WORK
        # The problem is that PyOP.getDatum().poseKeypoints returns a SwigPyObject, instead of an array
        # I can't find a way to figure out how to access to the raw data of it

        #print("Person pose keypoints: " + str((PyOP.getDatum().poseKeypoints)))
        #for person in xrange(0, poseKeypoints.getSize(0)):
        #    print("Person " + str(person) + " (x, y, score):")
        #    for bodyPart in xrange(0, poseKeypoints.getSize(1)):
        #        for xyscore in xrange(0, poseKeypoints.getSize(2)):
        #            valueToPrint += str(poseKeypoints[{person, bodyPart, xyscore}]) + " "
        #            print(valueToPrint)
        print("-----------------------------------------------------------------------------------")
        
    PyOP.stop()
    end = time.time()
    print("Real-time pose estimation demo successfully finished. Total time: " + str(end - start) + " seconds.")
    
if __name__ == '__main__':
    app.run()
