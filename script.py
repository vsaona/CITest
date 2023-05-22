import argparse as ap
from random import randint

parser = ap.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help="random string", required=True)
args = parser.parse_args()


if args.input == "pepino":
    out = open("pepino.txt", "w")
    out.write("el pepino es rico")
    out.close()
out2 = open("queso.txt", "w")
out2.write("el queso es delicioso")
out2.close()
out3 = open("zapallo.txt", "w")
out3.write("el zapallo tiene pepas")
out3.close()

if randint(0,3) > 1:
    print("listoco!")
else:
    print("listo!")
