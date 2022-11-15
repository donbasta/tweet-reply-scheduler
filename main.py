from src.services import *

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--add-quote", action="store_true")
    parser.add_argument("--see-quote", action="store_true")
    parser.add_argument("--check-tables", action="store_true")
    parser.add_argument("--quote-content")
    parser.add_argument("--quote-source")

    args = parser.parse_args()
    print(args)
    if args.add_quote:
        assert args.quote_content is not None
        add_quote(args.quote_content, args.quote_source)
    elif args.see_quote:
        see_quote()
    elif args.check_tables:
        check_tables()
    else:
        print("run()")
