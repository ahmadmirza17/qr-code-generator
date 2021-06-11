import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hello Lukesh you fat fuck!", image_factory=factory)
svg_img.save("mygr.svg")
