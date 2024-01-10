import cv2

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Coordinates: ({x}, {y})')

image = cv2.imread('../images/drawn_lean_canvas.png')
cv2.imshow('image', image)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()