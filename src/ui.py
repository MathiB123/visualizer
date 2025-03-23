# import pygame

# # pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True


# while running:
#     clock.tick(120)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # fill the screen with a color to wipe away anything from last frame
#     screen.fill("black")

#     n = 1280
#     height = 600
#     for i in range(n):
#         rect = pygame.Rect(0+i, 720-height, 1, height)
#         pygame.draw.rect(screen, 'white', rect)

#     font = pygame.font.SysFont("Arial" , 18 , bold = True)
#     fps = str(int(clock.get_fps()))
#     fps_t = font.render(fps , 1, pygame.Color("white"))
#     screen.blit(fps_t,(0,0))


#     # flip() the display to put your work on screen
#     pygame.display.flip()


# pygame.quit()




#Passer en argument le temps de l'ordi?

# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import numpy as np

# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = ax.plot([], [], 'ro')

# def init():
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     return ln,

# def update(frame):
#     xdata.append(frame)
#     ydata.append(np.sin(frame))
#     ln.set_data(xdata, ydata)
#     return ln,

# ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 128),
#                     init_func=init, blit=True, interval=0)
# plt.show()


# def create_video(n):
#     global X
#     X = np.random.binomial(1, 0.3, size = (n, n))

#     fig = plt.figure()
#     im = plt.imshow(X, cmap = plt.cm.gray)

#     def animate(t):
#         global X
#         X = np.roll(X, +1, axis = 0)
#         im.set_array(X)
#         return im, 

#     anim = FuncAnimation(
#         fig,
#         animate,
#         frames = 100,
#         interval = 1000/30,
#         blit = True
#     )

#     plt.show()

#     return anim

# anim = create_video(10)






