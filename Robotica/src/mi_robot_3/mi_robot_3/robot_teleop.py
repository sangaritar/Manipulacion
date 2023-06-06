import rclpy

from geometry_msgs.msg import Twist

from std_msgs.msg import Float32

from std_msgs.msg import String

from rclpy.node import Node

from pynput import keyboard as kb

import time



class Robot_teleop(Node):

    def __init__(self):

        super().__init__('robot_teleop')

        self.pubcmd = self.create_publisher(Twist, 'robot_cmdVel', 10)

        lineal = input(" Ingrese la velocidad lineal:")

        print("El valor ingresado es:" , lineal)

        self.lineal = float(lineal)

        angular = input("Ingrese la velocidad angular:")

        print("El valor ingresado es:" , angular)

        self.angular = float(angular)

        self.tiempo_tecla = float()



    def on_press(self, key):

        twistMessage = Twist()

        

        try:

            if key == kb.KeyCode.from_char('w'):

                twistMessage.linear.x = self.lineal


            elif key == kb.KeyCode.from_char('d'):

                twistMessage.angular.z = -self.angular


            elif key == kb.KeyCode.from_char('s'):       

                twistMessage.linear.x = -self.lineal

               
            elif key == kb.KeyCode.from_char('a'):

                twistMessage.angular.z = self.angular


            self.pubcmd.publish(twistMessage)


        except:

            print("No sirve esa tecla")



            

    def on_release(self, key):

        twistMessage = Twist()

        self.pubcmd.publish(twistMessage)

def main():

    rclpy.init()

    robot_teleop = Robot_teleop()

    with kb.Listener(robot_teleop.on_press, robot_teleop.on_release) as escuchador:

        escuchador.join()

    rclpy.spin(robot_teleop)

    robot_teleop.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':

    main()



     