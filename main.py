from pygame import *
from random import *
from colours import *

class Doodle():
 init()
size = width, height = 1000, 700
screen = display.set_mode(size)

LeftToolBarY = []
RightToolBarY = []
SizeMenuBarY = []
tool = "Pencil"
oldx = oldy = 0
mhold = "up"
loadbox = Rect(10, 10, 100, 45)
savebox = Rect(120, 10, 100, 45)


colour = black
colourswitch = 0
colour1 = black
colour2 = gray77

saveloadfont = font.SysFont("Arial", 30, True, True)
saveboxfont = font.SysFont("Arial", 18, True, True)
loadboxfont = font.SysFont("Arial", 16, True, True)
filenamefont = font.SysFont("Arial", 22, True, True)
loadtextpic = saveloadfont.render("Load", False, (0, 0, 0))
savetextpic = saveloadfont.render("Save", False, (0, 0, 0))
clearfont = font.SysFont("Arial", 30, True, True)
cleartextpic = clearfont.render("Clear", False, (0, 0, 0))
saveinstruction = saveboxfont.render("Enter the file name to save: ", False, (0, 0, 0))
loadinstruction = loadboxfont.render("Enter the file name to load /w: ", False, (0, 0, 0))

optionswitch = 0
OSactive = 0
optionsrect1 = Rect(150, 30, 100, 45)
optionsrect2 = Rect(150, 84, 100, 45)
optionsrect3 = Rect(150, 138, 100, 45)

pencilSize = 1
brushSize = 8
spraySize = 12
eraserSize = 10
rectFill = 0

backgroundpic = image.load("backgrounddjpg.jpg")
colourgrid = image.load("colourgrid.bmp")
pencilpic = image.load("pencil.png")
eraserpic = image.load("eraser.png")
paintbrushpic = image.load("paintbrush.png")
paintbucketpic = image.load("paintbucket.png")
spraypaintpic = image.load("spraypaint.png")
eyedropperpic = image.load("eyedropper.png")
spraypaints1pic = image.load("spraypaints1.png")
spraypaints2pic = image.load("spraypaints2.png")
spraypaints3pic = image.load("spraypaints3.png")
recttoolpic = image.load("recttool.png")
ovaltoolpic = image.load("ovaltool.png")
linetoolpic = image.load("linetool.png")


screen.blit(backgroundpic, (0, 0))
optionsbackrect = screen.subsurface(Rect(143, 22, 114,168)).copy()
canvas = [8, 60, 720, 620]
Rectcanvas = Rect(canvas)
draw.rect(screen, black, Rect(canvas[0] - 3, canvas[1] - 3, canvas[2] + 5, canvas[3] + 5), 4)
draw.rect(screen, white, canvas)

ccrect = Rect(975, 30, 20, 495)
ccrect1 = Rect(975, 30, 20, 247)
ccrect2 = Rect(975, 277, 20, 248)
draw.rect(screen, colour1, ccrect1)
draw.rect(screen, colour2, ccrect2)
draw.rect(screen, green, ccrect1, 975)
draw.rect(screen, white, Rect(973, 28, 24, 499), 3)

colourrect = Rect(750, 540, 244, 150)
screen.blit(colourgrid, colourrect)
draw.rect(screen, black, Rect(747, 537, 249, 155),4)

draw.rect(screen, gray90, loadbox)
screen.blit(loadtextpic, Rect(30, 10, 80, 45))
draw.rect(screen, black, Rect(8, 10, 104, 45), 3)
draw.rect(screen, gray90, savebox)
screen.blit(savetextpic, Rect(140, 10, 80, 45))
draw.rect(screen, black, Rect(118, 10, 104, 45), 3)

draw.rect(screen, gray90, Rect(230, 10, 100, 45))
draw.rect(screen, black, Rect(230, 10, 100, 45), 3)
screen.blit(cleartextpic, (250, 10))

for y in range(30, 520, 85):
        draw.rect(screen, gray90, Rect(750, y, 100, 70))
        LeftToolBarY.append(y)
        draw.rect(screen, black, Rect(747, y - 2, 104, 74), 3)

for y in range(200, 520, 85):
        draw.rect(screen, gray90, Rect(865, y, 100, 70))
        RightToolBarY.append(y)
        draw.rect(screen, black, Rect(863, y - 2, 104, 74), 3)

for y in range(30, 139, 54):
        draw.rect(screen, gray90, Rect(865, y, 100, 45))
        SizeMenuBarY.append(y)

def Pencil(screen, colour, Rectcanvas, mx, my, pencilsize):
        screen.set_clip(Rectcanvas)
        global screenCopy
        global oldx, oldy
        mx, my = mouse.get_pos()
        if mb == 1:
            draw.line(screen, colour, (oldx, oldy), (mx, my), pencilsize)
            screenCopy = screen.copy()
        oldx, oldy = mx, my

def Eraser(screen, Rectcanvas, mx, my, erasersize):
        screen.set_clip(Rectcanvas)
        global screenCopy
        global oldx, oldy
        screen.blit(screenCopy, (0, 0))
        if mb == 1:
            draw.rect(screen, white, (mx - (erasersize / 2), my - (erasersize / 2), erasersize, erasersize))
            draw.line(screen, white, (oldx, oldy), (mx, my), erasersize)
            screenCopy = screen.copy()
        draw.rect(screen, black, (mx - (erasersize / 2), my - (erasersize / 2), erasersize, erasersize),
                  2)
        oldx, oldy = mx, my

def Paintbrush(screen, colour, Rectcanvas, mx, my, brushsize):
        screen.set_clip(Rectcanvas)
        global screenCopy
        global oldx, oldy
        mx, my = mouse.get_pos()
        if mb == 1:
            draw.circle(screen, colour, (mx, my), brushsize)
            draw.line(screen, colour, (oldx, oldy), (mx, my), brushsize + 12)
            screenCopy = screen.copy()
        oldx, oldy = mx, my

def Paintbucket(screen, colour, Rectcanvas, mx, my):
        screen.set_clip(Rectcanvas)
        global screenCopy
        if mb == 1:
            draw.rect(screen, colour, Rectcanvas)
            screenCopy = screen.copy()

def Spraypaint(screen, colour, Rectcanvas, mx, my, spraysize):
        screen.set_clip(Rectcanvas)
        global screenCopy
        if mb == 1:
            for i in range(220):
                dotx, doty = randint(mx - spraysize, mx + spraysize), randint(my - spraysize,
                                                                              my + spraysize)  #
                if (mx - dotx) ** 2 + (
                        my - doty) ** 2 <= spraysize ** 2:
                    screen.set_at((dotx, doty), colour)
                    display.update((dotx - 1, doty - 1, 2, 2))
            screenCopy = screen.copy()

def Eyedropper(screen, mx, my, colourswitch):
        global screenCopy
        global colour, colour1, colour2
        if mb == 1:
            if colourswitch == 0:
                colour1 = Pickcolour(screen, mx, my)
                CIrect(screen, colour1, colour2, 0)
                colour = colour1
            if colourswitch == 1:
                colour2 = Pickcolour(screen, mx, my)
                CIrect(screen, colour1, colour2, 1)
                colour = colour2
            draw.rect(screen, colour, Rect(3, 537, 249, 155),
                      4)
            screenCopy = screen.copy()

def Linetool(screen, colour, Rectcanvas, oldx, oldy, mx, my, mhold, pencilsize):
        global screenCopy
        screen.set_clip(Rectcanvas)
        if mhold == "up":
            screenCopy = screen.copy()
        if mhold == "down":
            screen.blit(screenCopy, (0, 0))
            draw.line(screen, colour, (oldx, oldy), (mx, my), pencilsize)

def Recttool(screen, colour, Rectcanvas, oldx, oldy, mx, my, mhold, rectfill):
        global screenCopy
        screen.set_clip(Rectcanvas)
        if mhold == "up":
            screenCopy = screen.copy()
        if mhold == "down":
            screen.blit(screenCopy, (0, 0))
            draw.rect(screen, colour, Rect(oldx, oldy, mx - oldx, my - oldy), rectfill)

def Ovaltool(screen, colour, Rectcanvas, oldx, oldy, mx, my, mhold, rectfill):
        global screenCopy
        screen.set_clip(Rectcanvas)
        if mhold == "up":
            screenCopy = screen.copy()
        if mhold == "down":
            screen.blit(screenCopy, (0, 0))
            width = abs(mx - oldx)
            height = abs(my - oldy)
            x = min(mx, oldx)
            y = min(my, oldy)
            if rectfill != 5 and width > 4 and height > 4:
                draw.ellipse(screen, colour, Rect(x, y, width, height), rectfill)
            if rectfill == 5 and width > 9 and height > 9:
                draw.ellipse(screen, colour, Rect(x, y, width, height), rectfill)

def getmouse():
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()[0]
        return (mx, my, mb)

def checkmhold():
        global screenCopy
        global mhold
        global oldx, oldy
        if mhold == "up" and mouse.get_pressed()[
            0] == 1:
            oldx, oldy = mouse.get_pos()
            mhold = "down"
        if mhold == "down" and mouse.get_pressed()[
            0] == 0:
            mhold = "up"

def Pickcolour(screen, mx, my):
        colour = screen.get_at((mx, my))
        return colour

def checkcolour(colourswitch):
        global screenCopy
        global colour
        global colour1
        global colour2
        checkcolourswitch(screen, mb, ccrect1, ccrect2, colour1, colour2)
        if colourrect.collidepoint(mx, my) and mb == 1:
            if colourswitch == 0:
                colour1 = Pickcolour(screen, mx, my)
                CIrect(screen, colour1, colour2, 0)
                colour = colour1
            if colourswitch == 1:
                colour2 = Pickcolour(screen, mx, my)
                CIrect(screen, colour1, colour2, 1)
                colour = colour2
            draw.rect(screen, colour, Rect(747, 537, 249, 155),
                      4)
            screenCopy = screen.copy()

def selectcolour1(ccrect1, ccrect2):
        draw.rect(screen, colour2, ccrect2)
        draw.rect(screen, green, ccrect1, 5)
        draw.rect(screen, white, Rect(973, 28, 24, 499), 3)
        draw.rect(screen, colour, Rect(747, 537, 249, 155),
                  4)

def selectcolour2(ccrect1, ccrect2):
        draw.rect(screen, colour1, ccrect1)
        draw.rect(screen, green, ccrect2, 5)
        draw.rect(screen, white, Rect(973, 28, 24, 499), 3)
        draw.rect(screen, colour, Rect(747, 537, 249, 155),
                  4)

def checkcolourswitch(screen, mb, ccrect1, ccrect2, colour1,colour2):
        global colourswitch
        global colour
        global screenCopy
        if ccrect1.collidepoint(mx, my) and mb == 1:
            colourswitch = 0
            colour = colour1
            selectcolour1(ccrect1, ccrect2)
            screenCopy = screen.copy()
        elif ccrect2.collidepoint(mx, my) and mb == 1:
            colourswitch = 1
            colour = colour2
            selectcolour2(ccrect1, ccrect2)
            screenCopy = screen.copy()

def CIrect(screen, colour1, colour2, colourswitch):
        if colourswitch == 0:
            draw.rect(screen, colour1, ccrect1)
            draw.rect(screen, green, ccrect1, 5)
        elif colourswitch == 1:
            draw.rect(screen, colour2, ccrect2)
            draw.rect(screen, green, ccrect2, 5)
        draw.rect(screen, white, Rect(973, 28, 24, 499), 3)

def defaultsize():
        global pencilsize
        global brushsize
        global spraysize
        global erasersize
        global rectfill
        pencilsize = 1
        brushsize = 8
        spraysize = 12
        erasersize = 15
        rectfill = 0

def nooptions(screen):
        screen.blit(optionsbackrect, (860, 22, 114, 168))
        screenCopy = screen.copy()

def options(screen, tool, SizeMenuBarY):
        defaultsize()
        for i in SizeMenuBarY:
            draw.rect(screen, gray90, Rect(865, i, 100, 45))
        if tool == "Pencil" or tool == "Linetool":
            draw.line(screen, black, (880, 52), (950, 52), 1)
            draw.line(screen, black, (880, 106), (950, 106), 3)
            draw.line(screen, black, (880, 160), (950, 160), 6)
        elif tool == "Eraser":
            draw.rect(screen, white, (915 - (15 / 2), 52 - (15 / 2), 15, 15))
            draw.rect(screen, black, (915 - (15 / 2), 52 - (15 / 2), 15, 15), 2)
            draw.rect(screen, white, (915 - (23 / 2), 105 - (23 / 2), 23, 23))
            draw.rect(screen, black, (915 - (23 / 2), 105 - (23 / 2), 23, 23), 2)
            draw.rect(screen, white, (915 - (30 / 2), 160 - (30 / 2), 30, 30))
            draw.rect(screen, black, (915 - (30 / 2), 160 - (30 / 2), 30, 30), 2)
        elif tool == "Paintbrush":
            draw.line(screen, black, (880, 52), (950, 52), 10)
            draw.line(screen, black, (880, 106), (950, 106), 15)
            draw.line(screen, black, (880, 160), (950, 160), 18)
        elif tool == "Spraypaint":
            screen.blit(spraypaints1pic, Rect(875, 32, 90, 40))
            screen.blit(spraypaints2pic, Rect(875, 86, 90, 40))
            screen.blit(spraypaints3pic, Rect(875, 140, 90, 40))
        elif tool == "Recttool":
            draw.rect(screen, red3, (880, 40, 60, 25))
            draw.rect(screen, red3, (880, 94, 60, 25), 2)
            draw.rect(screen, red3, (880, 148, 60, 25), 5)
        elif tool == "Ovaltool":
            draw.ellipse(screen, (120, 176, 230), (880, 35, 70, 35))
            draw.ellipse(screen, (120, 176, 230), (880, 89, 70, 35), 2)
            draw.ellipse(screen, (120, 176, 230), (880, 143, 70, 35), 5)

def HighlightOptions(screen, optionsrect):
        optionsrect1 = Rect(865, 30, 100, 45)
        optionsrect2 = Rect(865, 84, 100, 45)
        optionsrect3 = Rect(865, 138, 100, 45)
        options(screen, tool, SizeMenuBarY)
        draw.rect(screen, white, Rect(860, 24, 110, 164), 5)
        draw.rect(screen, black, Rect(863, 28, 104, 157), 3)
        draw.line(screen, black, (862, 75 + 4), (967, 75 + 4), 3)
        draw.line(screen, black, (862, 129 + 4), (967, 129 + 4), 3)
        if optionsrect == optionsrect1:
            draw.rect(screen, green, Rect(866, 31, 98, 43), 3)
        if optionsrect == optionsrect2:
            draw.rect(screen, green, Rect(866, 85, 98, 43), 3)
        if optionsrect == optionsrect3:
            draw.rect(screen, green, Rect(866, 139, 98, 43), 3)

def checkoptions():
        global pencilsize, brushsize, spraysize, erasersize, rectfill, screenCopy, OSactivate, optionswitch
        optionsrect1 = Rect(865, 30, 100, 45)
        optionsrect2 = Rect(865, 84, 100, 45)
        optionsrect3 = Rect(865, 138, 100, 45)
        if optionsrect1.collidepoint(mx,
                                     my) and mb == 1 or OSactivate == 1 and optionswitch == 0:
            HighlightOptions(screen, optionsrect1)
            defaultsize()  # makes all the sizes the default sizes (smallest size)
        elif optionsrect2.collidepoint(mx,
                                       my) and mb == 1 or OSactivate == 1 and optionswitch == 1:
            HighlightOptions(screen, optionsrect2)
            pencilsize = 3  # second set of sizes
            brushsize = 13
            spraysize = 18
            erasersize = 30
            rectfill = 2
        elif optionsrect3.collidepoint(mx,
                                       my) and mb == 1 or OSactivate == 1 and optionswitch == 2:
            HighlightOptions(screen, optionsrect3)
            pencilsize = 6
            brushsize = 16
            spraysize = 22
            erasersize = 50
            rectfill = 5
        screenCopy = screen.copy()

def checkoptionswitch():
        global optionswitch, OSactivate
        if key.get_pressed()[K_LSHIFT] == 1:
            screen.blit(screenCopy, (0, 0))
            OSactivate = 1
            if optionswitch == 2:
                optionswitch = 0
            else:
                optionswitch += 1
            checkoptions()
            time.wait(200)

def drawtoolpics():
        screen.blit(pencilpic, Rect(760, 32, 65, 65))
        screen.blit(eraserpic, Rect(760, 117, 65, 65))
        screen.blit(paintbrushpic, Rect(760, 202, 65, 65))
        screen.blit(paintbucketpic, Rect(760, 287, 65, 65))
        screen.blit(spraypaintpic, Rect(760, 372, 65, 65))
        screen.blit(eyedropperpic, Rect(760, 457, 65, 65))
        screen.blit(recttoolpic, Rect(880, 290, 100, 70))
        screen.blit(ovaltoolpic, Rect(880, 375, 100, 70))
        screen.blit(linetoolpic, Rect(880, 205, 100, 70))

def checkrtoolbar(RightToolBarY):
        global toolnumber
        global tool
        global screenCopy
        for i in range(len(RightToolBarY)):
            RToolbox = Rect(865, RightToolBarY[i], 100, 70)
            if RToolbox.collidepoint(mx, my) and mb == 1:
                toolnumber = i + 6
                tool = Picktool(tool, toolnumber)
                screenCopy = screen.copy()

def checkltoolbar(LeftToolBarY):
        global toolnumber
        global tool
        global screenCopy
        for i in range(len(LeftToolBarY)):
            LToolbox = Rect(750, LeftToolBarY[i], 100, 70)
            if LToolbox.collidepoint(mx, my) and mb == 1:
                toolnumber = i
                tool = Picktool(tool, toolnumber)
                screenCopy = screen.copy()

def Highlighttoolbox(screen, toolnumber):
        if toolnumber <= 5:
            drawltoolbar(screen, LeftToolBarY)
            drawrtoolbar(screen, RightToolBarY)
            drawtoolpics()
            draw.rect(screen, green, Rect(750, LeftToolBarY[toolnumber] + 1, 98, 68), 3)
        if toolnumber >= 6:
            drawltoolbar(screen, LeftToolBarY)
            drawrtoolbar(screen, RightToolBarY)
            drawtoolpics()
            toolnumber -= 6
            draw.rect(screen, green, Rect(866, RightToolBarY[toolnumber] + 1, 98, 68), 3)
        display.flip()

def Picktool(tool, toolnumber):
        global screenCopy
        Highlighttoolbox(screen, toolnumber)
        if toolnumber == 0:
            options(screen, tool, SizeMenuBarY)
            HighlightOptions(screen, optionsrect1)
            tool = "Pencil"
        elif toolnumber == 1:
            options(screen, tool, SizeMenuBarY)
            HighlightOptions(screen, optionsrect1)
            tool = "Eraser"
        elif toolnumber == 2:
            options(screen, tool, SizeMenuBarY)
            HighlightOptions(screen, optionsrect1)
            tool = "Paintbrush"
        elif toolnumber == 3:
            nooptions(screen)
            tool = "Paintbucket"
        elif toolnumber == 4:
            options(screen, tool, SizeMenuBarY)
            HighlightOptions(screen, optionsrect1)
            tool = "Spraypaint"
        elif toolnumber == 5:
            nooptions(screen)
            tool = "Eyedropper"
        elif toolnumber == 6:
            options(screen, "Pencil", SizeMenuBarY)
            HighlightOptions(screen, optionsrect1)
            tool = "Linetool"
        elif toolnumber == 7:
            HighlightOptions(screen, optionsrect1)
            tool = "Recttool"
        elif toolnumber == 8:
            HighlightOptions(screen, optionsrect1)
            tool = "Ovaltool"

        return tool

def usetool():
        global mhold
        global oldx, oldy
        checkmhold()
        if tool == "Pencil":
            Pencil(screen, colour, Rectcanvas, mx, my, pencilsize)
        elif tool == "Eraser":
            mouse.set_visible(False)
            Eraser(screen, Rectcanvas, mx, my, erasersize)
        elif tool == "Paintbrush":
            Paintbrush(screen, colour, Rectcanvas, mx, my, brushsize)
        elif tool == "Paintbucket":
            Paintbucket(screen, colour, Rectcanvas, mx, my)
        elif tool == "Spraypaint":
            Spraypaint(screen, colour, Rectcanvas, mx, my, spraysize)
        elif tool == "Eyedropper":
            Eyedropper(screen, mx, my, colourswitch)
        elif tool == "Linetool":
            Linetool(screen, colour, Rectcanvas, oldx, oldy, mx, my, mhold, pencilsize)
        elif tool == "Recttool":
            Recttool(screen, colour, Rectcanvas, oldx, oldy, mx, my, mhold, rectfill)
        elif tool == "Ovaltool":
            Ovaltool(screen, colour, Rectcanvas, oldx, oldy, mx, my, mhold, rectfill)


def drawltoolbar(screen, LeftToolBarY):
        for y in LeftToolBarY:
            draw.rect(screen, gray90, (750, y, 100, 70))

def drawrtoolbar(screen, RightToolBarY):
        for y in RightToolBarY:
            draw.rect(screen, gray90, (865, y, 100, 70))

def defaultsaveloadbox(savebox, loadbox):
        global screenCopy
        draw.rect(screen, gray90, loadbox)
        screen.blit(loadtextpic, Rect(30, 10, 80, 45))
        draw.rect(screen, black, Rect(8, 10, 104, 45), 3)
        draw.rect(screen, gray90, savebox)
        screen.blit(savetextpic, Rect(140, 10, 80, 45))
        draw.rect(screen, black, Rect(118, 10, 104, 45), 3)
        screenCopy = screen.copy()

def checksave(screen, Rectcanvas, savebox, loadtextpic):
        if savebox.collidepoint(mx, my) and mb == 1:
            draw.rect(screen, green, savebox)
            screen.blit(savetextpic, Rect(140, 10, 80, 45))
            draw.rect(screen, black, Rect(118, 10, 104, 45), 3)
            display.flip()
            saveimage(screen, Rectcanvas)
            defaultsaveloadbox(savebox, loadbox)

def checkload(screen, Rectcanvas, loadbox, savetextpic):
        if loadbox.collidepoint(mx, my) and mb == 1:
            draw.rect(screen, green, loadbox)
            screen.blit(loadtextpic, Rect(30, 10, 80, 45))
            draw.rect(screen, black, Rect(8, 10, 104, 49), 3)
            display.flip()
            loadimage(screen, Rectcanvas)
            defaultsaveloadbox(savebox, loadbox)

def drawfilenametext(screen, filenamefont, filename):
        draw.rect(screen, white, Rect(350, 34, 380, 20))
        filenametextpic = filenamefont.render(filename, False, (0, 0, 0))
        screen.blit(filenametextpic, (350, 33))
        display.flip()

def saveimage(screen, Rectcanvas):
        global Stamparea
        global running
        global screenCopy
        filename = ""
        shift = "off"
        badcharacters = """ \/:*?"<>\ """
        Stamparea = screen.subsurface(
            Rect(335, 3, 406, 66)).copy()
        canvassave = screen.subsurface(Rectcanvas).copy()
        draw.rect(screen, yellow1, Rect(340, 8, 400, 50))
        draw.rect(screen, black, Rect(340, 8, 400, 50), 3)
        draw.rect(screen, white, Rect(350, 11, 380, 20))
        screen.blit(saveinstruction, (360, 10))
        display.flip()
        saveloop = True
        while saveloop:
            for evnt in event.get():
                if key.get_pressed()[K_LSHIFT] == 1:
                    if shift == "off":
                        shift = "on"
                    elif shift == "on":
                        shift = "off"
                elif key.get_pressed()[K_ESCAPE] == 1:
                    screen.blit(Stamparea, (265, 585))
                    screenCopy = screen.copy()
                    saveloop = False

                elif evnt.type == QUIT:
                    saveloop = False
                    running = False

                elif key.get_pressed()[K_RETURN] == 1:
                    image.save(canvassave, filename + ".bmp")
                    print
                    "Image saved as", "'", filename + ".bmp'"
                    print
                    ""
                    screen.blit(Stamparea, (265, 585))
                    saveloop = False

                elif key.get_pressed()[K_SPACE] == 1 and len(
                        filename) != 50:
                    filename += " "
                    drawfilenametext(screen, filenamefont, filename)

                elif key.get_pressed()[K_BACKSPACE] == 1 and len(filename) != 0:
                    filename = filename[0:len(filename) - 1]
                    drawfilenametext(screen, filenamefont, filename)

                elif evnt.type == KEYDOWN and key.get_pressed()[K_BACKSPACE] != 1 and len(
                        filename) != 50:
                    character = chr(evnt.key)
                    if character not in badcharacters and shift == "on":
                        filename += character.upper()
                    if character not in badcharacters and shift == "off":
                        filename += character
                    drawfilenametext(screen, filenamefont, filename)

def loadimage(screen, Rectcanvas):
        global Stamparea
        global running
        global screenCopy
        filename = ""
        shift = "off"
        badcharacters = """ \/:*?"<>\ """
        Stamparea = screen.subsurface(
            Rect(335, 3, 406, 66)).copy()
        draw.rect(screen, yellow, Rect(340, 8, 400, 50))
        draw.rect(screen, black, Rect(340, 8, 400, 50), 3)
        draw.rect(screen, white, Rect(350, 11, 380, 20))
        screen.blit(loadinstruction, (360, 10))
        display.flip()
        saveloop = True
        while saveloop:
            for evnt in event.get():
                if key.get_pressed()[K_LSHIFT] == 1:
                    if shift == "off":
                        shift = "on"
                    elif shift == "on":
                        shift = "off"
                elif key.get_pressed()[K_ESCAPE] == 1:
                    screen.blit(Stamparea, (265, 585))
                    screenCopy = screen.copy()
                    saveloop = False

                elif evnt.type == QUIT:
                    saveloop = False
                    running = False

                elif key.get_pressed()[K_RETURN] == 1:
                    screen.set_clip(Rectcanvas)
                    newimage = image.load(filename)
                    screen.blit(newimage, (canvas[0], canvas[1]))
                    print
                    "Loaded image", "'", filename, "'"
                    print
                    ""
                    screen.set_clip(Rect(0, 0, 1000, 700))
                    screen.blit(Stamparea, (265, 585))
                    saveloop = False

                elif key.get_pressed()[K_SPACE] == 1 and len(
                        filename) != 50:
                    filename += " "
                    drawfilenametext(screen, filenamefont, filename)

                elif key.get_pressed()[K_BACKSPACE] == 1 and len(filename) != 0:
                    filename = filename[0:len(filename) - 1]
                    drawfilenametext(screen, filenamefont, filename)

                elif evnt.type == KEYDOWN and key.get_pressed()[K_BACKSPACE] != 1 and len(
                        filename) != 50:
                    character = chr(evnt.key)
                    if character not in badcharacters and shift == "on":
                        filename += character.upper()
                    if character not in badcharacters and shift == "off":
                        filename += character
                    drawfilenametext(screen, filenamefont, filename)

def drawScene(screen, Rectcanvas, mx, my, mb):
        global tool
        global colour
        global screenCopy
        global mhold
        global OSactivate

        screen.set_clip(Rect(0, 0, 1000, 700))

        if tool == "Pencil" or tool == "Eraser" or tool == "Paintbrush" or tool == "Spraypaint" or tool == "Linetool" or tool == "Recttool" or tool == "Ovaltool":
            checkoptionswitch()
            OSactivate = 0

        if not Rectcanvas.collidepoint(mx,
                                       my):
            screen.blit(screenCopy, (0, 0))
            if mhold == "down" and mouse.get_pressed()[
                0] == 0:
                mhold = "up"

            if mhold == "up":
                checkcolour(colourswitch)
                checkltoolbar(LeftToolBarY)
                checkrtoolbar(RightToolBarY)
                if Rect(250, 10, 100, 35).collidepoint(mx, my) and mb == 1:
                    draw.rect(screen, white, Rectcanvas)
                    screenCopy = screen.copy()

                if tool == "Pencil" or tool == "Eraser" or tool == "Paintbrush" or tool == "Spraypaint" or tool == "Linetool" or tool == "Recttool" or tool == "Ovaltool":
                    checkoptions()
                checksave(screen, Rectcanvas, savebox, loadtextpic)
                checkload(screen, Rectcanvas, loadbox, savetextpic)
            mouse.set_visible(True)

        if Rectcanvas.collidepoint(mx, my):
            usetool()
display.flip()

Picktool(tool, 0)
Highlighttoolbox(screen, 0)
options(screen, tool, SizeMenuBarY)
HighlightOptions(screen, optionsrect1)
screenCopy = screen.copy()

running = True
myClock = time.Clock()
while running:
        for evnt in event.get():
            if evnt.type == QUIT or key.get_pressed()[
                K_F5] == 1:
                running = False
        mx, my, mb = getmouse()
        drawScene(screen, Rectcanvas, mx, my, mb)

myClock.tick(60)
quit()


