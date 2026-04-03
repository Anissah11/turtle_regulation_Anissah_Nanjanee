import rclpy
from rclpy.node import Node
from turtle_interfaces.srv import SetWayPoint as SetWayPointSrv
from std_msgs.msg import Bool

class WaypointClient(Node):
    def __init__(self):
        super().__init__('waypoint_client')

        self.client = self.create_client(SetWayPointSrv, 'set_waypoint_service')

        self.is_moving = True
        self.sent = False

        self.sub = self.create_subscription(
            Bool, 'is_moving', self.is_moving_callback, 10)

        # 3 waypoints à envoyer
        self.waypoints = [
            (3.0, 3.0),
            (7.0, 3.0),
            (5.0, 8.0),
        ]
        self.index = 0

        # Attendre que le service soit disponible
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

        # Envoyer le premier waypoint
        self.send_next_waypoint()

    def is_moving_callback(self, msg):
        # Envoyer le prochain waypoint seulement quand la tortue est arrêtée
        if not msg.data and not self.sent:
            self.sent = True
            self.send_next_waypoint()
        elif msg.data:
            self.sent = False

    def send_next_waypoint(self):
        if self.index >= len(self.waypoints):
            self.get_logger().info('Tous les waypoints sont faits! 🎉')
            return

        x, y = self.waypoints[self.index]
        self.index += 1

        request = SetWayPointSrv.Request()
        request.x = x
        request.y = y

        self.get_logger().info(f'Envoi waypoint #{self.index}: ({x}, {y})')
        self.client.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    node = WaypointClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
