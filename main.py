import pygame as py
import random



py.init()
py.font.init()


class Enemy():
    en_x = 250 - 50/2 +100
    en_y =  -50

    def __init__(self, en_x, en_y):
        self.en_x = en_x
        self.en_y = en_y




def main():
    wn_x  = 500
    wn_y = 500
    face_x = 250 - 50/2
    face_y = 422 - 50/2
   

    score = 0
   


    enemies = []


    for i in range(5):
        enemies.append(Enemy(random.randint(0, 500 - 50), random.randint(-480, -50)))



    
    iml = py.image.load 
    wn = py.display.set_mode((wn_x, wn_y))
    clock = py.time.Clock()
    
    face = iml('data/gfx/face.png')
    bg_tex = iml('data/gfx/bg.png')
    em_tex = iml('data/gfx/enemie.png')
    
    cs_font = py.font.SysFont('comicsans', 32)
    
    py.display.set_caption("Dodger")
    wn.blit(bg_tex, (0,0))
    wn.blit(face, (face_x, face_y))
    py.display.update()
    
    running = True
    
    # game loop
    while running:


        clock.tick(60)
        
        keys = py.key.get_pressed()
        if keys[py.K_RIGHT]:
            face_x = face_x + 2
        if keys[py.K_LEFT]:
            face_x = face_x - 2
        if keys[py.K_d]:
            face_x = face_x + 2
        if keys[py.K_a]:
            face_x = face_x - 2
            
            
        for enemy in enemies:
            enemy.en_y = enemy.en_y + 2



            if enemy.en_y > 500:
                enemy.en_y = -32
                enemy.en_x = random.randint(0, 500 - 50)
                score = score + 1







            if face_x + 50 > enemy.en_x and face_x < enemy.en_x + 50 and face_y + 50 > enemy.en_y and face_y < enemy.en_y + 50:  
             face_x = 250 - 50/2
             face_y = 422 - 50/2
             score = 0
             
             
             enemies = []


             for i in range(5):
                 enemies.append(Enemy(random.randint(0, 500 - 50), random.randint(-480, -50)))
                 

            
        
        
        
            
            
            
            
        for event in py.event.get():
            
            # Check for QUIT event      
            if event.type == py.QUIT:
                    
                    running = False


        wn.blit(bg_tex, (0,0))
        wn.blit(face, (face_x, face_y))

        for enemy in enemies:
            wn.blit(em_tex, (enemy.en_x, enemy.en_y))

        
        startMessage = cs_font.render("SCORE: " + str(score), True, (0, 0, 0))
        wn.blit(startMessage, (0, 0))
                    
        py.display.update()


    


main()




