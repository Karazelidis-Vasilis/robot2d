from math import sin,cos,radians
import matplotlib.pyplot as plt
class Robot2D :
    def __init__(self,x,y,th):
        self.x = x
        self.y = y
        self.th = th
        self.path=[(self.x , self.y)]

    def rotate(self,dth):
        self.th += dth
        while self.th>360 or self.th<-360:
            if self.th>360:
                self.th-=360
            elif self.th<-360:
                self.th+=360
        if self.th>180:
            self.th-=360
        elif self.th<-180:
            self.th+=360


    def move(self, dx): 
            
        self.x += dx*cos(radians(self.th))
        self.y += dx*sin(radians(self.th))
        self.path.append((self.x,self.y))

    def pose_history(self):
        print("##############")
        print("#Robot Status#")
        print("##############")

        for index,point in enumerate(self.path):
            print(f"\nPoint {index}: ({point[0]:.2f}, {point[1]:.2f})\n")
        print("______________________") 
    def current_pose(self):
        print(f"\nCurrent possition X:{self.x:.2f} Y:{self.y:.2f}")
        print(f"Current angle {self.th}\n") 

    def plot(self):
        #Total_points=[(0,0)]
        x_points=[]
        y_points=[]
        for points in self.path:
            dx=points[0]
            dy=points[1]
        
            x_points.append(dx)
            y_points.append(dy)

            
        plt.plot(x_points,y_points,marker='o',color='green')
            
        plt.grid(True)
        plt.title('Robot path')
        plt.axis('equal')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.show()
     
def main():
    running=True
    print("\n Welcome to Robot2D")
    my_robot=Robot2D(0.0,0.0,0.0)
    while running:
        question=input("\n  Robot2D Menu\n"\
                    "m for declare distance\n"\
                    "r for declare rotation\n"\
                    "s for show current pose\n"\
                    "h for show point history\n"\
                    "p for plot the path\n"\
                    "f for write a file whitc contains commands\n"\
                    "q for exit\n"\
                    "Choose what you want : ")
        if question.lower() =="m":
            move=input("Input distance :")
            try:
                my_robot.move(float(move))            
            except ValueError:
                print("\nInvalid input\n")
        elif question.lower()=="r":
            rotation=input("Input rotation in degree:")
            try:
                my_robot.rotate(float(rotation))
            except ValueError:
                print("\nInvalid input\n")
        elif question.lower()=="s":
            my_robot.current_pose()                        
        elif question.lower()== "h":
            my_robot.pose_history()
        elif question.lower()=="p":
            my_robot.plot()
        elif question.lower()=="f":
            read_file=input("Write txt file location :")
            try:
                with open(read_file,"r") as file:
                    rd=file.read()  
                    commands=rd.split("\n")
                    print("##################")
                    print("#Robot2D commands#")
                    print("##################")

                    for index,command in enumerate(commands):
                        parts=command.split()
                        if not parts:
                            continue
                        elif len(parts) == 2:
                            mv=parts[0].lower()
                            num=parts[1]
                            try:
                                if mv=="move":
                                    my_robot.move(float(num))
                                    print(f" {mv} {num}")
                                elif mv=="rotate":
                                    
                                    my_robot.rotate(float(num))
                                    print(f" {mv} {num}")
                            except ValueError:
                                    print(f"\nInvalid input in line {index}, {num} is not \n")
                        elif len(parts)!=2:
                            print(f"\nYou have {len(parts)} arguments in line {index}, instead of 2 :\n {parts} \n")
            except FileNotFoundError:
                print("\nThat file is not exist\n")  

        elif question.lower() =="q":
            print("Exit from Menu.")
            print("Good bye !")
            running=False   
        else:
            print("Invalid input.Try again")
        
if __name__=="__main__":
    main()
