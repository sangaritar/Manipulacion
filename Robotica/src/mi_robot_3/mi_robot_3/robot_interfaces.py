import serial,time
import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class Robot_interfaces(Node):

    def __init__(self):

        super().__init__('robot_interface')

        

        self.subscription_velocity = self.create_subscription(Twist, 'robot_cmdVel', self.listener_callback_velocity, 10)  

        self.subscription_velocity

        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

    
    def listener_callback_velocity(self, msg):

        self.get_logger().info(str(msg.linear.x))

        self.get_logger().info(str(msg.angular.z))

        

        vellineal = msg.linear.x

        velangular = msg.angular.z

        #Delante
        if vellineal > 0:
            self.ser.write([119])

        #Atras
        if vellineal < 0:
            self.ser.write([115])

        #Derecha

        if velangular > 0:
            self.ser.write([100])

        #Izquierda

        if velangular < 0:
            self.ser.write([97])
        
        if velangular == 0 and vellineal == 0:
            self.ser.write([113])



def main(args=None):

        rclpy.init(args=args)

        robot_interfaces = Robot_interfaces()
        rclpy.spin(robot_interfaces)
        rclpy.shutdown()
       

if __name__ == '__main__':

        main()

