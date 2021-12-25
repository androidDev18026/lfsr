'''
Random Numbers w/ Linear Feedback Shift Register (LFSR)

Inspired by computerphile video 

URL : https://www.youtube.com/watch?v=Ks1pw1X22y4
=================================================
Arguments
=========
number : int, initial number (binary representation)
iterations : int, random bits
log level : INFO, WARN, ERROR

'''
import argparse
import logging


def repr(bits, size):
    return f"{bits:0{size}b}"


def last_bit(bit):
    return bit & 1


def shift_bits(bits, size):
    return ((bits >> 1 ^ bits) & 1) << size - 1 | bits >> 1


def permutations(bits, iters):
    orig_bits = bits

    for idx, _ in enumerate(range(iters)):
        logging.info(
            f"Permutation {idx+1} => {repr(bits, orig_bits.bit_length())}")
        logging.info(f"Random bit generated {last_bit(bits)}")

        # print(last_bit(bits), end='')

        bits = shift_bits(bits, orig_bits.bit_length())
        if orig_bits == bits:
            logging.warning(f"Got the same sequence after {idx+1} iterations")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Linear Shift State Register",
                                     description="Generate random numbers", add_help=True, allow_abbrev=True,
                                     exit_on_error=True)

    parser.add_argument("-n", "--bits", action="store", type=int, metavar="N",
                        help="initial number", required=True)

    parser.add_argument("-i", "--iterations", action="store", type=int, metavar="I",
                        help="number of random bits to generate", required=True)

    parser.add_argument("--log-level", action="store", type=str,
                        help="set log level", required=False, choices=["info", "warn", "error"],
                        default="info")

    try:
        args = parser.parse_args()
        logging.basicConfig(
            format="[%(levelname)-7s]- %(asctime)15s : %(msg)s", datefmt="%H:%M:%S %d/%m/%Y",
            level=str(args.log_level).upper(), encoding="utf-8")

        permutations(args.bits, args.iterations)
    except argparse.ArgumentError:
        print("Invalid argument")
