import rclpy
from rclpy.node import Node
from turtle_interfaces.srv import SetWayPoint as SetWayPointSrv
from std_msgs.msg import Bool

class SquareClient(Node):
    def __init__(self):
        super().__init__('square_client')

        self.client = self.create_client(SetWayPointSrv, 'set_waypoint_service')

        self.sent = False

        self.sub = self.create_subscription(
            Bool, 'is_moving', self.is_moving_callback, 10)

        # Les 4 coins du carré
        self.waypoints = [
            (2.0, 2.0),
            (8.0, 2.0),
            (8.0, 8.0),
            (2.0, 8.0),
            (2.0, 2.0), 
        ]
        self.index = 0

        # Attendre que le service soit disponible
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

        # Envoyer le premier coin
        self.send_next_waypoint()

    def is_moving_callback(self, msg):
        if not msg.data and not self.sent:
            self.sent = True
            self.send_next_waypoint()
        elif msg.data:
            self.sent = False

    def send_next_waypoint(self):
        if self.index >= len(self.waypoints):
            self.get_logger().info('Carre termine! 🎉')
            return

        x, y = self.waypoints[self.index]
        self.index += 1

        request = SetWayPointSrv.Request()
        request.x = x
        request.y = y

        self.get_logger().info(f'Coin #{self.index}: ({x}, {y})')
        self.client.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    node = SquareClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
