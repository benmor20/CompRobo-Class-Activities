
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped


class SendMessageNode(Node):
    def __init__(self):
        super().__init__('send_message')
        self.create_timer(0.1, self.run_loop)
        self.pub = self.create_publisher(PointStamped, 'point', 10)

    def run_loop(self):
        msg = PointStamped()
        msg.point.x = 1.0
        msg.point.y = 2.0
        msg.header.frame_id = 'odom'
        msg.header.stamp = self.get_clock().now().to_msg()
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = SendMessageNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
