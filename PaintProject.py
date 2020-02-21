#PaintProject.py
#Jack Li, Computer Science Macanovik Period 8
from pygame import * 
from random import *
from tkinter import *
from math import *
root=Tk()
root.withdraw()
import pygame
pygame.mixer.init()#start pygame mixer
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()#start engine
font.init()


RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
GREY=(222,222,222)

size=(1200,800)#screen resolution
screen=display.set_mode(size)
myClock=time.Clock

display.set_caption("Mass Effect Paint")#Program caption/name
##############################################################
#colour pallette
palRect=Rect(340,35,300,66)#Palette(drawn underneath image since can't take colour from an image directly)
#easter egg
ppapRect=Rect(1000,790,2,2)#Small easter egg     for fun(not really part of program)
#Music
skipRect=Rect(285,100,30,30)
pauseRect=Rect(250,100,30,30)
backRect=Rect(215,100,30,30)
#tools rectangles (self explanatory)
pencilRect=Rect(40,170,40,40)
eraserRect=Rect(100,170,40,40)
openRect=Rect(40,250,40,40)
saveRect=Rect(100,250,40,40)
brushRect=Rect(40,330,40,40)
sprayRect=Rect(100,330,40,40)
lineRect=Rect(40,410,40,40)
rectRect=Rect(100,410,40,40)
emptyrectRect=Rect(40,490,40,40)
ellipseRect=Rect(100,490,40,40)
emptyellipseRect=Rect(40,570,40,40)
undoRect=Rect(100,570,40,40)
redoRect=Rect(40,650,40,40)
fillRect=Rect(100,650,40,40)
eyedropperRect=Rect(40,730,40,40)
#stamp rectangles (self explanatory)
stamp1Rect=Rect(220,695,145,70)
stamp2Rect=Rect(220,610,145,70)
stamp3Rect=Rect(375,610,135,135)
stamp4Rect=Rect(520,610,80,135)
stamp5Rect=Rect(620,610,80,135)
stamp6Rect=Rect(720,610,80,135)
stamp7Rect=Rect(820,610,80,135)
stamp8Rect=Rect(920,610,80,135)
#canvas rectangle
canvasRect=Rect(200,150,950,450)
#border rectangle
borderRect=Rect(195,145,960,460)
###############################################################
#LOAD music+MAKE playlist
index=0#set index to zero
#define all songs
file1="audio/The Galaxy.mp3"
file2="audio/Leaving Earth.mp3"
file3="audio/Mars.mp3"
file4="audio/The Krogan.mp3"
file5="audio/An End.mp3"
file6="audio/Proud of You.mp3"
#make empty list for playlist
#then add songs to the playlist
playlist=[]
playlist.append(file1)
playlist.append(file2)
playlist.append(file3)
playlist.append(file4)
playlist.append(file5)
playlist.append(file6)
#shuffle playlist to "randomise" songs each time program runs for the first time
shuffle(playlist)
#set song to the first song in the playlist
song=playlist[index]
#load song from earlier
pygame.mixer.music.load(song)
#play song
pygame.mixer.music.play()
#define event when music ends
END_MUSIC_EVENT=pygame.USEREVENT+0
pygame.mixer.music.set_endevent(END_MUSIC_EVENT)
###############################################################
#LOAD images (self explanatory)
background=image.load("images/ME3 background2.jpg")
easteregg=image.load("stamps/easteregg.jpg")
logo=image.load("images/MElogo.png")
colour=image.load("images/colour.png")
pencil=image.load("images/pencil.png")
eraser=image.load("images/eraser.png")
save=image.load("images/save.png")
brush=image.load("images/brush.png")
spraypaint=image.load("images/spraypaint.jpg")
undo=image.load("images/undo.ico")
redo=image.load("images/redo.png")
fill=image.load("images/fill.jpg")
pause=image.load("images/pause.png")
marker=image.load("images/marker.png")
fastforward=image.load("images/fastforward.png")
load=image.load("images/load.png")
eyedropper=image.load("images/eyedropper.png")
###############################################################
#LOAD stamp images (seperated from other images for organization)
stamp1=image.load("stamps/mass relay.png")
stamp2=image.load("stamps/normandy.png")
stamp3=image.load("stamps/male shepard.png")
stamp4=image.load("stamps/female shepard.png")
stamp5=image.load("stamps/garrus.png")
stamp6=image.load("stamps/liara.png")
stamp7=image.load("stamps/javik.png")
stamp8=image.load("stamps/tali.png")
###############################################################
#SCALE images (self explanatory)
pencil=transform.scale(pencil,(37,37))
eraser=transform.scale(eraser,(35,35))
brush=transform.scale(brush,(37,37))
logo=transform.scale(logo,(400,75))
save=transform.scale(save,(35,35))
colour=transform.scale(colour,(300,100))
spraypaint=transform.scale(spraypaint,(37,37))
background=transform.scale(background,(1200,800))
easteregg=transform.scale(easteregg,(100,100))
undo=transform.scale(undo,(35,35))
redo=transform.scale(redo,(35,35))
fill=transform.scale(fill,(35,35))
pause=transform.scale(pause,(27,27))
marker=transform.scale(marker,(35,35))
fastforward=transform.scale(fastforward,(27,27))
back=transform.rotate(fastforward,180)
load=transform.scale(load,(35,35))
eyedropper=transform.scale(eyedropper,(35,35))
###############################################################
#SCALE stamp box labels
stamp1label=transform.scale(stamp1,(120,60))
stamp2label=transform.scale(stamp2,(120,60))
stamp3label=transform.scale(stamp3,(120,120))
stamp4label=transform.scale(stamp4,(60,120))
stamp5label=transform.scale(stamp5,(60,120))
stamp6label=transform.scale(stamp6,(60,120))
stamp7label=transform.scale(stamp7,(60,120))
stamp8label=transform.scale(stamp8,(60,120))
###############################################################
#SCALE stamp images
stamp1=transform.scale(stamp1,(200,100))
stamp2=transform.scale(stamp2,(200,100))
stamp3=transform.scale(stamp3,(140,140))
stamp4=transform.scale(stamp4,(100,200))
stamp5=transform.scale(stamp5,(100,200))
stamp6=transform.scale(stamp6,(100,200))
stamp7=transform.scale(stamp7,(100,200))
stamp8=transform.scale(stamp8,(100,200))
###############################################################

running=True #boolean variable
tool="No Tool"#start without tool chosen
col=BLACK#default colour
#radius is used to determine size/thickness of things in my program
#i.e. thickness of brush tool
#variable can be changed by scrolling up or down
radius=5#default is 5

#create "basic" program before start
screen.blit(background,(0,0))#blit back ground image to cover whole program
screen.blit(logo,(700,50))#blit logo on upper right side
draw.rect(screen,(0,0,0),(17,12,306,126))#draw border of label rectangle
draw.rect(screen,(0,0,0),(337,12,306,92))#draw border for palrect
draw.rect(screen,BLACK,borderRect)#draw rectangle slightly larger than canvas for border
draw.rect(screen,WHITE,canvasRect)#draw canvas on top of border rectangle
omx,omy=0,0 #will be used for the pencil tool
undolist=[screen.copy()]#empty list for undo
redolist=[]#empty list for redo
pixelList=[]#empty list for fill tool
paused=False

while running:
    lclick=False#variable for left click
    rclick=False#variable for right click
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            if lclick:
                prestamp=screen.copy()#copy screen for stamps every time a click occurs
            if evt.button==4:#if scroll up
                if radius<100:#set max thickness to 100
                    radius+=1#increase thickness by 1
            if evt.button==5:#if scroll down
                if radius>1:#don't allow negatives
                    radius-=1#decrese thickness by 1
            if evt.button==1:
                lclick=True#if left click, lclick is true
            if evt.button==3:
                rclick=True#if right click, rclick is true
        if evt.type==MOUSEBUTTONUP:
            if canvasRect.collidepoint(mx,my):
                undoscreen=screen.copy()#take copy of screen (for undo/redo function)
                undolist.append(undoscreen)#add screen to list

        
        if evt.type==END_MUSIC_EVENT and evt.code==0:#if a song ends
            index+=1#add one to list
            if index==len(playlist):#if index out of list
                index=0#set index to 0 (restart)
            song=playlist[index]#set "song" to new song
            pygame.mixer.music.load(song)#load new song
            pygame.mixer.music.play()#play
            

    mx,my=mouse.get_pos()#set mx,my to mouse position
    mb=mouse.get_pressed()#set mb to when mouse is pressed
    draw.rect(screen,(222,222,222),palRect)#draw pal rect underneath colour box
    screen.blit(colour,(340,15))#blit colour box on top of pal rect
    ##############################################################
    #song Names
    if song=="audio/The Galaxy.mp3":
        songName="Saving the Galaxy"
    if song=="audio/Leaving Earth.mp3":
        songName="Leaving Earth"
    if song=="audio/Mars.mp3":
        songName="Mars"
    if song=="audio/The Krogan.mp3":
        songName="Future of Krogan"
    if song=="audio/An End.mp3":
        songName="An End"
    if song=="audio/Proud of You.mp3":
        songName="Proud of You"
    ##############################################################
    #Text
    comicFont=font.SysFont("comic sans ms",15)#set font(comic sans)
    ThicknessText=comicFont.render("Current Thickness %s" %(radius),True,BLACK)#render text to display tool thickness
    ColourText=comicFont.render("Current Colour",True,col)#render text to display current colour
    ToolText=comicFont.render("Current Tool/Stamp is: ",True,BLACK)#render text telling current tool
    ToolText2=comicFont.render("%s" %(tool),True,RED)#render text telling current tool
    MusicText=comicFont.render("Current Song is: ",True,BLACK)#render text telling current song
    MusicText2=comicFont.render("%s" %(songName),True,BLACK)#render text telling current song
    draw.rect(screen,WHITE,(20,15,300,120))#draw rect containing text
    draw.rect(screen,GREEN,skipRect,2)#draw rect for skipping songs
    draw.rect(screen,GREEN,pauseRect,2)#draw rect for pausing/playing songs
    draw.rect(screen,GREEN,backRect,2)#draw rect for previous songs
    screen.blit(ThicknessText,(24,15))#blit thickness text
    screen.blit(ColourText,(24,35))#blit colour text
    screen.blit(ToolText,(24,55))#blit tool text
    screen.blit(ToolText2,(24,75))#blit tool text
    screen.blit(MusicText,(24,95))#blit music text
    screen.blit(MusicText2,(24,115))#blit music text
    ##############################################################
    if pauseRect.collidepoint(mx,my):#if hovering over pause/play
        if lclick:#if click pause/play
            if paused==True:#if song is paused
                pygame.mixer.music.unpause()
                paused=False
            elif paused==False:#if song is unpaused
                pygame.mixer.music.pause()
                paused=True
        draw.rect(screen,RED,pauseRect,2)
    if skipRect.collidepoint(mx,my):#if hovering over skip
        if lclick:#if click on skip rect
            index+=1#add one to the list index
            if index==len(playlist):#if index is outside of list
                index=0#restart playlist
            song=playlist[index]#set song equal to new song
            pygame.mixer.music.load(song)#load new song
            pygame.mixer.music.play()#play new song
        draw.rect(screen,RED,skipRect,2)
    if backRect.collidepoint(mx,my):#if hovering over back rect
        if lclick:
            index-=1#subtract 1 from index
            if index==0-len(playlist):#if index outside of list set index to 0
                index=0
            song=playlist[index]#set song to current song
            pygame.mixer.music.load(song)#load current song
            pygame.mixer.music.play()#play song
        draw.rect(screen,RED,backRect,2)
            
    ##############################################################
    #backgrounds for toolboxes (self explanatory)
    draw.rect(screen,GREY,pencilRect)
    draw.rect(screen,GREY,eraserRect)
    draw.rect(screen,GREY,openRect)
    draw.rect(screen,GREY,saveRect)
    draw.rect(screen,GREY,brushRect)
    draw.rect(screen,GREY,sprayRect)
    draw.rect(screen,GREY,lineRect)
    draw.rect(screen,GREY,rectRect)
    draw.rect(screen,GREY,emptyrectRect)
    draw.rect(screen,GREY,ellipseRect)
    draw.rect(screen,GREY,emptyellipseRect)
    draw.rect(screen,GREY,undoRect)
    draw.rect(screen,GREY,redoRect)
    draw.rect(screen,GREY,fillRect)
    draw.rect(screen,GREY,eyedropperRect)
    draw.rect(screen,GREY,stamp1Rect)
    draw.rect(screen,GREY,stamp2Rect)
    draw.rect(screen,GREY,stamp3Rect)
    draw.rect(screen,GREY,stamp4Rect)
    draw.rect(screen,GREY,stamp5Rect)
    draw.rect(screen,GREY,stamp6Rect)
    draw.rect(screen,GREY,stamp7Rect)
    draw.rect(screen,GREY,stamp8Rect)
    ###############################################################
    #Draw tool boxes (self explanatory)
    draw.rect(screen,GREEN,pencilRect,2)
    draw.rect(screen,GREEN,eraserRect,2)
    draw.rect(screen,GREEN,openRect,2)
    draw.rect(screen,GREEN,saveRect,2)
    draw.rect(screen,GREEN,brushRect,2)
    draw.rect(screen,GREEN,sprayRect,2)
    draw.rect(screen,GREEN,lineRect,2)
    draw.rect(screen,GREEN,rectRect,2)
    draw.rect(screen,GREEN,emptyrectRect,2)
    draw.rect(screen,GREEN,ellipseRect,2)
    draw.rect(screen,GREEN,emptyellipseRect,2)
    draw.rect(screen,GREEN,undoRect,2)
    draw.rect(screen,GREEN,redoRect,2)
    draw.rect(screen,GREEN,fillRect,2)
    draw.rect(screen,GREEN,eyedropperRect,2)
    ###############################################################
    #draw stampboxes (self explanatory)
    draw.rect(screen,GREEN,stamp1Rect,2)
    draw.rect(screen,GREEN,stamp2Rect,2)
    draw.rect(screen,GREEN,stamp3Rect,2)
    draw.rect(screen,GREEN,stamp4Rect,2)
    draw.rect(screen,GREEN,stamp5Rect,2)
    draw.rect(screen,GREEN,stamp6Rect,2)
    draw.rect(screen,GREEN,stamp7Rect,2)
    draw.rect(screen,GREEN,stamp8Rect,2)
    ###############################################################
    #Toolbox labels (self explanatory)
    screen.blit(pencil,(42,172))
    screen.blit(eraser,(102,172))
    screen.blit(load,(42,252))
    screen.blit(save,(102,252))
    screen.blit(brush,(42,332))
    screen.blit(spraypaint,(102,332))
    draw.line(screen,col,(45,415),(75,445))
    draw.rect(screen,col,(105,415,30,30))
    draw.rect(screen,col,(45,495,30,30),2)
    draw.ellipse(screen,col,(105,495,30,30))
    draw.ellipse(screen,col,(45,575,30,30),2)
    screen.blit(undo,(102,572))
    screen.blit(redo,(42,652))
    screen.blit(fill,(102,652))
    screen.blit(pause,(252,102))
    screen.blit(fastforward,(286,102))
    screen.blit(back,(218,102))
    screen.blit(eyedropper,(42,732))
    ###############################################################
    #stampbox labels (self explanatory)
    screen.blit(stamp1label,(233,698))
    screen.blit(stamp2label,(233,613))
    screen.blit(stamp3label,(383,613))
    screen.blit(stamp4label,(533,613))
    screen.blit(stamp5label,(633,613))
    screen.blit(stamp6label,(733,613))
    screen.blit(stamp7label,(833,613))
    screen.blit(stamp8label,(933,613))
    ###############################################################
    #selecting the tool
    if pencilRect.collidepoint(mx,my):
        if lclick: tool="Pencil"#if left click on rect set tool to pencil
        draw.rect(screen,RED,pencilRect,2)
    if eraserRect.collidepoint(mx,my):
        if lclick: tool="Eraser"#if left click on rect set tool to eraser
        draw.rect(screen,RED,eraserRect,2)
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,RED,saveRect,2)
    if openRect.collidepoint(mx,my) :
        draw.rect(screen,RED,openRect,2)
    if brushRect.collidepoint(mx,my):
        if lclick: tool="Brush"#if left click on rect set tool to brush
        draw.rect(screen,RED,brushRect,2)
    if sprayRect.collidepoint(mx,my):
        if lclick: tool="Spray"#if left click on rect set tool to spray
        draw.rect(screen,RED,sprayRect,2)
    if rectRect.collidepoint(mx,my):
        if lclick: tool="Full Rect"#if left click on rect set tool to filled rect
        draw.rect(screen,RED,rectRect,2)
    if emptyrectRect.collidepoint(mx,my):
        if lclick: tool="Empty Rect"#if left click on rect set tool to unfilled rect
        draw.rect(screen,RED,emptyrectRect,2)
    if lineRect.collidepoint(mx,my):
        if lclick: tool="Line"#if left click on rect set tool to line
        draw.rect(screen,RED,lineRect,2)
    if ellipseRect.collidepoint(mx,my):
        if lclick: tool="Ellipse"#if left click on rect set tool to filled ellipse
        draw.rect(screen,RED,ellipseRect,2)
    if emptyellipseRect.collidepoint(mx,my):
        if lclick: tool="Empty Ellipse"#if left click on rect set tool to unfilled ellipse
        draw.rect(screen,RED,emptyellipseRect,2)
    if undoRect.collidepoint(mx,my):
        if lclick:
            tool="Undo"#if left click set tool to undo
            if len(undolist)>1:
                redolist.append(undolist[-1])#append last item from undolist to redolist
                undolist.pop()#pop last item from undolist
                screen.blit(undolist[-1],(0,0))#blit item that is now last in undolist
        draw.rect(screen,RED,undoRect,2)
    if redoRect.collidepoint(mx,my):
        if lclick:
            tool="Redo"#if left click set tool to redo
            if 0!=len(redolist):#if len redolist isn't 0
                undolist.append(redolist.pop())#append last item from redolist
                screen.blit(undolist[-1],(0,0))#blit last item from undolist
        draw.rect(screen,RED,redoRect,2)
    if fillRect.collidepoint(mx,my):
        if lclick: tool="Fill"#if left click on rect set tool to fill
        draw.rect(screen,RED,fillRect,2)
    if eyedropperRect.collidepoint(mx,my):
        if lclick: tool="Eyedropper"#if left click on rect set tool to eyedropper
        draw.rect(screen,RED,eyedropperRect,2)
    ###############################################################
    #selecting stamp
    if stamp1Rect.collidepoint(mx,my):#if hovering over stamp1 rect
        if lclick: tool="Mass Relay"#if left click set tool to mass relay
        draw.rect(screen,RED,stamp1Rect,2)
    if stamp2Rect.collidepoint(mx,my):#if hovering over stamp2 rect
        if lclick: tool="Normandy"#if left click set tool to normandy
        draw.rect(screen,RED,stamp2Rect,2)
    if stamp3Rect.collidepoint(mx,my):#if hovering over stamp3 rect
        if lclick: tool="Male Shepard"#if left click set tool to male shepard
        draw.rect(screen,RED,stamp3Rect,2)
    if stamp4Rect.collidepoint(mx,my):#if hovering over stamp4 rect
        if lclick: tool="Female Shepard"#if left click set tool to female shepard
        draw.rect(screen,RED,stamp4Rect,2)
    if stamp5Rect.collidepoint(mx,my):#if hovering over stamp5 rect
        if lclick: tool="Garrus"#if left click set tool to garrus
        draw.rect(screen,RED,stamp5Rect,2)
    if stamp6Rect.collidepoint(mx,my):#if hovering over stamp6 rect
        if lclick: tool="Liara"#if left click set tool to liara
        draw.rect(screen,RED,stamp6Rect,2)
    if stamp7Rect.collidepoint(mx,my):#if hovering over stamp7 rect
        if lclick: tool="Javik"#if left click set tool to javik
        draw.rect(screen,RED,stamp7Rect,2)
    if stamp8Rect.collidepoint(mx,my):#if hovering over stamp8 rect
        if lclick: tool="Tali"#if left click set tool to tali
        draw.rect(screen,RED,stamp8Rect,2)
    ###############################################################
    #using the tool
    dx,dy=0,0#define dx and dy(for brush tool)
    if canvasRect.collidepoint(mx,my) and mb[0]==1:
        screen.set_clip(canvasRect)
        #only allows the canvas to be modified
        if tool=="Pencil":
            draw.line(screen,col,(omx,omy),(mx,my))#draw line from old x and y to current x and y
        if tool=="Eraser":
            draw.circle(screen,WHITE,(omx,omy),radius)#draw circle with center at old x and y
            draw.circle(screen,WHITE,(mx,my),radius)#draw circle with center at current x and y
            draw.line(screen,WHITE,(omx,omy),(mx,my),radius*2)#draw thick line(rectangle) connecting 2 circles
        if tool=="Brush":
            dx=mx-omx#set dx to distance between old and current x
            dy=my-omy#set dx to distance between old and current y
            dist=int(sqrt(dx**2+dy**2))#use distance formula
            for i in range(1,dist+1):
                dotX=int(omx+i*dx/dist) #(change in y)
                dotY=int(omy+i*dy/dist) #(change in x)
                draw.circle(screen,col,(dotX,dotY),radius)#draw circles with centers depending on change in x and change in y
        if tool=="Spray":
            for i in range(radius):#change speed of dots
                x=randint(-radius,radius)#set x to random integer depending on tool thickness
                y=randint(-radius,radius)#set y to random integer depending on tool thickness
                if hypot(x,y)<=radius:#if the coordinates of the point are within the radius of the circle:
                    screen.set_at((x+mx,y+my),col)#set the colour of the point to whatever colour user has selected
        if tool=="Line":
            if lclick:
                startline=mx,my#set start line to current location
                preline=screen.copy()#take copy of screen
            screen.blit(preline,(0,0))#continuously blit copy of screen
            draw.line(screen,col,(startline),(mx,my))#draw line from original start point to current location of mouse
        if tool=="Full Rect":
            if lclick:
                startx=mx#set startx to original x coordinate of mouse
                starty=my#set starty to original y coordinate of mouse
                prerect=screen.copy()#take copy of screen
            screen.blit(prerect,(0,0))#continuously blit copy of screen
            draw.rect(screen,col,(startx,starty,mx-startx,my-starty))#draw rect with startx and starty as top left point
        if tool=="Empty Rect":#same as previous tool except with rect not filled
            if lclick:
                startx=mx
                starty=my
                prerect=screen.copy()
            screen.blit(prerect,(0,0))
            draw.rect(screen,col,(startx,starty,mx-startx,my-starty),1)#same as Full Rect tool except with thickness of 1
        if tool=="Ellipse":
            if lclick:
                startx=mx#set start x to original x coordinate of mouse
                starty=my#set start y to original y coordinate of mouse
                preellipse=screen.copy()#take copy of screen
            elliRect=Rect(startx,starty,mx-startx,my-starty)#draw rect using same way as full rect tool
            elliRect.normalize()#normalize ellirect
            screen.blit(preellipse,(0,0))#continuously blit copy of screen
            try: draw.ellipse(screen,col,elliRect)#try to draw ellipse with elliRect dimensions
            except ValueError:#if value error occurs pass
                pass
        if tool=="Empty Ellipse":#same as previous tool except not filled
            if lclick:
                startx=mx
                starty=my
                preellipse=screen.copy()
            elliRect=Rect(startx,starty,mx-startx,my-starty)
            elliRect.normalize()
            screen.blit(preellipse,(0,0))
            try: draw.ellipse(screen,col,elliRect,2)#draw ellipse with elliRect but thickness is 2
            except:
                pass
        if tool=="Fill":
            if lclick:
                Colour=screen.get_at((mx,my))#set Colour to whatever colour the pixel user clicks on is
                pixelList=[(mx,my)]#create list with original pixel as first item in list
                usedPixelSet=set()#create a set
                while len(pixelList)>0:#while pixelList has an item inside it
                    pixel=pixelList.pop()#set pixel to pixelList.pop()
                    if Colour==screen.get_at(pixel) and pixel not in usedPixelSet:#if pixel is the same colour as original pixel and hasn't been checked yet
                        screen.set_at(pixel,col)#set colour of pixel to col
                        pixelList.append((pixel[0]+1,pixel[1]))#add pixel to the right
                        pixelList.append((pixel[0]-1,pixel[1]))#add pixel to the left
                        pixelList.append((pixel[0],pixel[1]+1))#add pixel one down
                        pixelList.append((pixel[0],pixel[1]-1))#add pixel one up
                    usedPixelSet.add(pixel)#add checked pixels to set
        if tool=="Eyedropper":
            if lclick:
                col=screen.get_at((mx,my))#set col to the colour of whatever pixel was clicked

    ###############################################################
    #using stamps
        if tool=="Mass Relay":
            if lclick:
                prestamp=screen.copy()#take copy of screen
            screen.blit(prestamp,(0,0))#continuously blit copy of screen
            screen.blit(stamp1,(mx-100,my-50))#blit stamp(with cursor in the middle of stamp)
        if tool=="Normandy":
            if lclick:
                prestamp=screen.copy()#take copy of screen
            screen.blit(prestamp,(0,0))#continuously blit copy of screen
            screen.blit(stamp2,(mx-100,my-50))#blit stamp(with cursor in the middle of stamp)
        if tool=="Male Shepard":
            if lclick:
                prestamp=screen.copy()#take copy of screen
            screen.blit(prestamp,(0,0))#continuously blit copy of screen   
            screen.blit(stamp3,(mx-70,my-70))#blit stamp(with cursor in the middle of stamp)
        if tool=="Female Shepard":
            if lclick:
                prestamp=screen.copy()#take copy of screen
            screen.blit(prestamp,(0,0))#continuously blit copy of screen
            screen.blit(stamp4,(mx-50,my-100))#blit stamp(with cursor in the middle of stamp)
        if tool=="Garrus":
            if lclick:
                prestamp=screen.copy()#take copy of screen
            screen.blit(prestamp,(0,0))#continuously blit copy of screen
            screen.blit(stamp5,(mx-50,my-100))#blit stamp(with cursor in the middle of stamp)
        if tool=="Liara":
            if lclick:
                prestamp=screen.copy()#take copy of screen
            screen.blit(prestamp,(0,0))#continuously blit copy of screen
            screen.blit(stamp6,(mx-50,my-100))#blit stamp(with cursor in the middle of stamp)
        if tool=="Javik":
            if lclick:
                prestamp=screen.copy()#take copy of screen
            screen.blit(prestamp,(0,0))#continuously blit copy of screen
            screen.blit(stamp7,(mx-50,my-100))#blit stamp(with cursor in the middle of stamp)
        if tool=="Tali":
            if lclick:
                prestamp=screen.copy()#take copy of screen
            screen.blit(prestamp,(0,0))#continuously blit copy of screen
            screen.blit(stamp8,(mx-50,my-100))#blit stamp(with cursor in the middle of stamp)

        screen.set_clip(None)#modify entire screen
    ###############################################################
    #changing the colour
    if palRect.collidepoint(mx,my) and lclick==True:#if click on palrect
            col=screen.get_at((mx,my))#set col to colour of clicked on pixel
    ###############################################################
    #saving picture (canvas)
    if saveRect.collidepoint(mx,my) and lclick==True:#if click on save rect
        try:
            fname=filedialog.asksaveasfilename(defaultextension=".png")
            #asks the user to input the file name they would like to save as
            image.save(screen.subsurface(canvasRect),fname)#save canvas as fname
        except:#if error
            pass#pass
    ###############################################################
    #opening a picture (loading)
    if openRect.collidepoint(mx,my) and lclick==True:
        try:
            fname=filedialog.askopenfilename(filetypes=[("images","*.png;*.jpg;*.bmp")])#ask user to open an image
            screen.set_clip(canvasRect)
            screen.blit(image.load(fname),(200,150))
            #load the picture and blit on canvas
            screen.set_clip(None)
        except:#if error
            pass#pass
  
    omx,omy=mx,my#set omx,omy equal to current position of mouse
    display.flip()


            
quit() #closing the pygame window
