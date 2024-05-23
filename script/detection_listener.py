#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from ultralytics_ros.msg import YoloDetections


class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener_node')
        self.subscription = self.create_subscription(
            YoloDetections,
            'yolo_result',
            self.listener_callback,
            10)
        self.subscription  

    def listener_callback(self, msg):
        self.get_logger().info('\n\n Received detections on the last image:')
        for detection in msg.detections:
            self.get_logger().info(f'Class: {detection.class_name}, '
                                   f'Position: (x: {detection.x}, y: {detection.y}), '
                                   f'Size: (width: {detection.width}, height: {detection.height}) \n')

def main(args=None):
    rclpy.init(args=args)
    node = ListenerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
