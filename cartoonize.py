import cv2

print('Please enter the name of image you want to cartoonize \n')
image_name = input("")

image = cv2.imread(image_name)
cv2.imshow("Original image", image)

print('Enter 1: for low cartoonization and \n2: for high cartoonization')
cartoon_style = input("")
if (cartoon_style == '1'):
    cartoon = cv2.stylization(image, sigma_s=50, sigma_r=0.5)
    cv2.imshow('Low', cartoon)
elif (cartoon_style == '2'):
    cartoon = cv2.stylization(image, sigma_s=250, sigma_r=0.25)
    cv2.imshow('High', cartoon)
else:
    print("Invalid style selection")

print("Do you want to save the image (y/n):")
answer = input("")
if answer == 'y':
    img_name = input("Enter a name for the image: ")
    cv2.imwrite(f'cartoons/{img_name}.jpeg', cartoon)
elif answer == 'no':
    pass
else:
    print("Invalid answer!")

cv2.waitKey()
cv2.destroyAllWindows()