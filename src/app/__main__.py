"""Ponto de entrada: python -m app"""
import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(prog="app", description="trendsIA P0")
    parser.add_argument("--versao", action="store_true", help="mostra a versão e sai")
    args = parser.parse_args(argv)
    if args.versao:
        print("0.0.0")
        return 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
