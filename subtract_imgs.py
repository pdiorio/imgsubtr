import cv2
import sys

orig = cv2.imread("/path/to/unedited/photo.jpg")
edit = cv2.imread("/path/to/edited/photo.jpg")

# optional: convert to greyscale
#orig = cv2.cvtColor(orig,cv2.COLOR_BGR2GRAY)
#edit = cv2.cvtColor(edit,cv2.COLOR_BGR2GRAY)

# if the images are not the same size, you can force resizing; advise against this, but sometimes you have no choice
#orig = cv2.resize(orig, (960,540))
#edit = cv2.resize(edit, (960, 540))

# show the original picture; hit escape to close
cv2.imshow('image', orig)
cv2.waitKey(0)
cv2.destroyAllWindows()

# show the edited picture; hit escape to close
cv2.imshow('image', edit)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Subtract edited image from original
reveal_edits = orig - edit

# show the revealed edits; hit escape to close
cv2.imshow('image', reveal_edits)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("/path/to/revealed/edits.jpg", reveal_edits)



