import argparse
import cv2
import sys


def make_cat_passport_image(input_image_path, haar_model_path):

    # Read image
    image = cv2.imread('cat.png')

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Normalize image intensity
    gray = cv2.NormalizeHist(gray)

    # Resize image
    resized = cv2.resize(gray, (640, 480), interopolation = cv2.INTER_AREA)

    # Detect cat faces using Haar Cascade
    detector = cv2.CascadeClassifier(model)
    rects = detector.detectMultiScale(image, scaleFactor=1.1, minNeightbors=5, minSize = (75, 75))

    # Draw bounding box
    cv2.imshow("window_1", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Display result image
    for (i, (x, y, w, h)) in enumerate(rects):
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10), cv2.FONT_HERSENNEY_SIMPLEX, 0.55, (0, 0, 255), 2)

    # Crop image
    x, y, w, h = rects[0]
    image = image[y:y+b, x:x+w]

    # Save result image to file
    cv2.imwrite('out.jpg', image)

    return


def build_argparser():
    parser = argparse.ArgumentParser(
        description='Speech denoising demo', add_help=False)
    args = parser.add_argument_group('Options')
    args.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                      help='Show this help message and exit.')
    args.add_argument('-m', '--model', type=str, required=True,
                      help='Required. Path to .XML file with pre-trained model.')
    args.add_argument('-i', '--input', type=str, required=True,
                      help='Required. Path to input image')
    return parser


def main():
    
    args = build_argparser().parse_args()
    make_cat_passport_image(args.input, args.model)

    return 0


if __name__ == '__main__':
    sys.exit(main() or 0)
