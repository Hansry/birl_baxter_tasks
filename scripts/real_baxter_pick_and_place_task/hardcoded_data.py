from geometry_msgs.msg import (
    Pose,
    Quaternion,
)

import copy


starting_joint_angles = {
    'right_w0': -0.6699952259595108,
    'right_w1': 1.030009435085784,
    'right_w2': 0.4999997247485215,
    'right_e0': -0.189968899785275,
    'right_e1': 1.9400238130755056,
    'right_s0': 0.08000397926829805,
    'right_s1': -0.9999781166910306
}

pick_object_pose = Pose()
pick_object_pose.position.x = 0.783433342576
pick_object_pose.position.y = -0.281027705287
pick_object_pose.position.z = -0.0395903973417
pick_object_pose.orientation = Quaternion(
    x= -0.0634582357249,
    y= 0.997906913323,
    z= 0.0122551630271,
    w= -0.00215769313191
)

place_object_pose = copy.deepcopy(pick_object_pose)
place_object_pose.position.y += 0.3


hover_distance = 0.15

hover_pick_object_pose = copy.deepcopy(pick_object_pose)
hover_pick_object_pose.position.z += hover_distance


hover_place_object_pose = copy.deepcopy(place_object_pose)
hover_place_object_pose.position.z += hover_distance

